"""Inspect one BlueJ Java project; optionally compile it outside the project.

No external Python packages required. Never executes the student's program.
"""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

def java_binary(name,jdk):
    suffix='.exe' if os.name=='nt' else ''
    if jdk:
        p=Path(jdk)/'bin'/(name+suffix)
        if p.is_file():return str(p)
        raise FileNotFoundError('JDK executable missing: '+str(p))
    if os.environ.get('JAVA_HOME'):return java_binary(name,os.environ['JAVA_HOME'])
    p=shutil.which(name)
    if p:return p
    for home in sorted((Path.home()/'.jdks').glob('*')):
        p=home/'bin'/(name+suffix)
        if p.is_file():return str(p)
    raise FileNotFoundError('Set JAVA_HOME or supply --jdk with a JDK directory')

def inspect(folder,compile_sources=False,jdk=None,build_root=None):
    folder=Path(folder).resolve()
    marker=folder/'package.bluej'
    if not marker.is_file():raise ValueError('Select the individual project directory containing package.bluej')
    metadata=marker.read_text(encoding='utf-8-sig',errors='replace')
    encoding=next((s.split('=',1)[1].strip() for s in metadata.splitlines() if s.startswith('project.charset=')),'UTF-8')
    sources=sorted(folder.glob('*.java'))
    stride=sorted(folder.glob('*.stride'))
    jars=sorted((folder/'+libs').rglob('*.jar')) if (folder/'+libs').exists() else []
    result=dict(project=str(folder),charset=encoding,java_files=[p.name for p in sources],
        stride_files=[p.name for p in stride],jars=[str(p.relative_to(folder)) for p in jars],
        note='A Java compile validates .java files only. It does not prove current Stride editor sources were regenerated, task completeness, GUI behavior or authorship.')
    if compile_sources:
        if not sources:raise ValueError('No Java sources found in this project directory')
        if build_root:
            build_root=Path(build_root).resolve();build_root.mkdir(parents=True,exist_ok=True)
        with tempfile.TemporaryDirectory(prefix='bluej-check-',dir=build_root) as output:
            args=[java_binary('javac',jdk),'-encoding',encoding,'-d',output]
            if jars:args+=['-classpath',os.pathsep.join(str(p) for p in jars)]
            process=subprocess.run(args+[str(p) for p in sources],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=120)
            result['compilation']=dict(passed=process.returncode==0,exit_code=process.returncode,diagnostics=process.stdout+process.stderr)
    return result

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project')
    parser.add_argument('--compile',action='store_true')
    parser.add_argument('--jdk',help='JDK root directory')
    parser.add_argument('--output',help='Optional JSON report file')
    parser.add_argument('--build-root',help='Writable parent directory for temporary compilation files')
    args=parser.parse_args()
    try:result=inspect(args.project,args.compile,args.jdk,args.build_root)
    except (ValueError,FileNotFoundError,subprocess.TimeoutExpired) as ex:
        parser.exit(2,str(ex)+'\n')
    text=json.dumps(result,ensure_ascii=False,indent=2)
    if args.output:Path(args.output).write_text(text,encoding='utf-8')
    print(text)
    if result.get('compilation',{}).get('passed') is False:raise SystemExit(1)

if __name__=='__main__':main()
