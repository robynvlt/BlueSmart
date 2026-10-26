# BlueSmart

A reusable AI coding skill for **Java in BlueJ**, with practical guidance grounded in school project templates and the Graphics and Games framework.

BlueSmart helps an assistant understand, extend, explain, and debug BlueJ projects while preserving the conventions and interfaces already used in the classroom.

## What is included

- Guidance for Java naming, visibility, encoding, project libraries, and BlueJ workflows.
- Verified Graphics and Games method signatures and event callback distinctions.
- A catalog of the reviewed school projects and explanations of worked examples.
- Instructions for complete game foundations, keyboard input, press/release handling, and focus loss.
- A portable knowledge snapshot with **4,272 nodes and 10,892 directed relationships**, plus source provenance.
- Standard-library Python tools for checking a project and querying the bundled knowledge graph.

The analyzed material covers 63 Java exercise projects and a standalone library project. Original downloads are not bundled in this repository. The knowledge snapshot is dated **2026-10-26**.

## Invocation

The display name is **BlueSmart**; the technical skill identifier is `bluesmart`.

Example prompt:

```text
/BlueSmart Build a complete BlueJ game foundation with keyboard controls.
```

`/BlueSmart` is an explicitly documented text trigger. Native skill selection depends on the application: select the installed BlueSmart skill from the host's skill picker, or use `$bluesmart` in Codex. ChatGPT can also expose installed skills through its skill selector. A repository cannot register the same custom slash command in every application.

BlueSmart uses German by default to match the source material and classroom conventions; you can request explanations in English.

## Installation

### Skill folder

Use your host's skill installer to install **`skills/bluesmart`** from this repository. The repository URL is `https://github.com/robynvlt/BlueSmart`. For manual Codex setup, place that folder in a supported user skill directory such as `~/.agents/skills/bluesmart`. The folder must include `SKILL.md`, `agents/`, `references/`, `assets/`, and `scripts/`; do not copy only `SKILL.md`.

### Plugin package

The root `plugin.json` packages BlueSmart as a skills-only Agent Plugin. A repository marketplace is included at `.agents/plugins/marketplace.json` for compatible desktop hosts. This plugin has no MCP server, login requirement, API key, background service, or automatic network hook.

Installation and invocation details are documented by [OpenAI](https://learn.chatgpt.com/docs/build-skills) and depend on the host version and available features.

## Local tools

Python is required for the optional scripts. Compiling Java also requires a JDK; set `JAVA_HOME`, put `javac` on your PATH, or supply `--jdk`.

```powershell
python skills/bluesmart/scripts/check_project.py "path/to/your/project" --compile
python skills/bluesmart/scripts/query_knowledge.py 2_1_A01_Mondrian_Vorlage Figur --depth 2
```

The checker reads `package.bluej`, respects its declared encoding and `+libs` JARs, and compiles one project into a temporary directory. It does not run the program. If your system restricts temporary directories, add `--build-root "path/to/a/writable/folder"`.

The knowledge query needs only Python's standard library. Graphify is not required for using the included snapshot.

## Validation and limits

The development process included separate compilation of the 63 Java exercise projects, four repaired or completed working examples, logic tests, real Swing rendering, and an independent skill application to a fresh traffic-light template. These are development checks, not a guarantee for every future task.

This package does not contain the original conversation, every original school project, or the full textbook assignments. The assistant must inspect your actual project and ask for missing requirements when necessary. A successful compile does not establish complete task correctness. Continuous held-key control requires compatible press/release handling; BlueSmart must not invent callbacks missing from a library.

Performance depends on the model, supplied files, and available test tools. Installing the skill transfers its instructions and bundled evidence; it does not give every environment the same local files, tools, or execution permissions.

## Sources and attribution

The analysis is based on the public [Year 10 Java-BlueJ materials from Informatik Schulbuch](https://informatikschulbuch.de/jahrgangsstufe-10/objektorientierte-modellierung-und-programmierungjgst10/). Source URLs and file checksums are included under `skills/bluesmart/assets/knowledge/`. Original authors retain their attribution and rights. No affiliation or endorsement is claimed. See [NOTICE.md](NOTICE.md).

## Cost

Hosting and sharing this repository works with GitHub Free. BlueSmart itself requires no paid service or API key. Your chosen AI application or model may have its own subscription or usage costs. Optional paid GitHub products are not required.

---

<sub>This project was created with AI.</sub>
