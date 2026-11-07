# AI Sandbox Escape — A STEM Competition Study

## See PROPOSOL.md for more details

---

## What's in this repo
| File | What it is |
|------|-----------|
| `.gitignore`| tells git what to ignore so you don't see meaningless files|
| `Dockerfile` | Builds the sandbox image. (tells docker what to do when you run docker build|
| `FAQ.md` | Answers your questions |
| `Failures.md`| Documents our failures when creating this project|
| `Instructions.md`| Detailed instructions for demo|
| `PROPOSAL.md` | The full project proposal. |
| `README.md` | This file- tells you the stuff|
| `agent.py` | the reliable, repeatable version (option 1) |
| `agent_llm.py` | **Real local LLM agent** (via Ollama) that decides its own escape attempts. (option 2)|
| `run_demo.sh` | Runs the scripted A/B experiment. (option 1)|
| `fallback_demo.py` | backup version-useless (option 3) |


---
## Intro on options:

### Option 1 — Scripted A/B demo (most reliable)
**Included scripts and tools** : 

* `run_demo.sh`
* `agent.py`
*  docker desktop

**What it does** :

* a fixed script that follows the same steps every time
* Reliable, repeatable proof
* behaves exactly the same every time



### Option 2 — Real LLM agent 

**Included scripts and tools** : 

* `agent_llm.py`
* docker desktop
* ollama
* a downloaded model

**What it does** :
* a real AI trying to break out
* Thinks for itself, can vary run to run

### Option 3 — emergency backup

**Included scripts and tools** : 

* fallback_demo.py

**What it does** :
* a stimulation
* basically useless

## A quick start after reading this: go to the read me files, then run the demos, then read the code if u want
