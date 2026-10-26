"""Query graph.json within one original BlueJ project; no LLM or API required."""
import gzip
import argparse
import json
from collections import deque
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def query(project,symbol,depth=2,limit=80):
    data=json.loads(gzip.decompress((ROOT/'assets/knowledge/graph.json.gz').read_bytes()).decode('utf-8'))
    projects=sorted({p for n in data['nodes'] for p in n.get('projects',[])})
    matches=[p for p in projects if p==project or Path(p).name==project]
    if len(matches)!=1:raise ValueError('Select an exact project folder name; matches: '+str(matches))
    selected=matches[0]
    nodes={n['id']:n for n in data['nodes'] if selected in n.get('projects',[])}
    starts=[key for key,n in nodes.items() if n['label'].casefold()==symbol.casefold()]
    if not starts:raise ValueError('No exact symbol label found in selected project: '+symbol)
    edges=[e for e in data['links'] if selected in e.get('projects',[]) and e['source'] in nodes and e['target'] in nodes]
    adjacency={key:set() for key in nodes}
    for e in edges:
        adjacency[e['source']].add(e['target'])
    seen=set(starts);queue=deque((s,0) for s in starts)
    while queue:
        current,d=queue.popleft()
        if d>=depth:continue
        for target in sorted(adjacency[current]):
            if target not in seen:
                seen.add(target);queue.append((target,d+1))
    ids=sorted(seen,key=lambda key:(key not in starts,nodes[key].get('source_file',''),nodes[key].get('source_location',''),key))
    truncated=len(ids)>limit;ids=set(ids[:limit])
    output=[]
    for key in sorted(ids):
        node=dict(nodes[key])
        if node.get('source_file'):
            node['original_source']=selected+'/'+Path(node['source_file']).name
        output.append(node)
    return dict(project=selected,symbol=symbol,depth=depth,truncated=truncated,
        nodes=output,edges=[e for e in edges if e['source'] in ids and e['target'] in ids])

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('project');p.add_argument('symbol');p.add_argument('--depth',type=int,default=2)
    p.add_argument('--limit',type=int,default=80);p.add_argument('--output')
    args=p.parse_args();result=query(args.project,args.symbol,args.depth,args.limit)
    text=json.dumps(result,ensure_ascii=False,indent=2)
    if args.output:Path(args.output).write_text(text,encoding='utf-8')
    print(text)

if __name__=='__main__':main()
