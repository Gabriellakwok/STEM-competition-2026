# AI Sandbox Escape — A STEM Competition Study

**A STEM competition study on how to isolate sandboxes and ensure data security.**

Can a hardened sandbox stop an AI agent from escaping and leaking data? This
repo runs the *same* agent in two sandboxes — a weak one and a hardened one —
and shows the result flip from **ESCAPED** to **CONTAINED**. Same agent, two
configurations, opposite outcomes.

Everything here is free (Docker Desktop and Ollama are free; Python is free).

---

## The big idea
AI agents are increasingly given real computer access. If one is compromised, it
may try to break out of its sandbox and leak secrets. This project tests a
defense — **layered container isolation**: network egress filtering + privilege
restriction + a read-only filesystem — and measures whether it actually stops an
agent that the weak sandbox lets escape.

> **Hypothesis:** The same agent that escapes a default container will be fully
> contained by one launched with no network, no privileges, and a read-only disk.

---

## What's in this repo
| File | What it is |
|------|-----------|
| `agent_llm.py` | **Real local LLM agent** (via Ollama) that decides its own escape attempts. |
| `agent.py` | Deterministic "control probe" — the reliable, repeatable version. |
| `Dockerfile` | Builds the sandbox image. |
| `run_demo.sh` | Runs the scripted A/B experiment with one command. |
| `fallback_demo.py` | No-install backup version (no Docker needed). |
| `PROPOSAL.md` | The full project proposal. |
| `FAQ.md` | Answers to the questions judges actually ask. |
| `LICENSE` | MIT license. |

**Two agents on purpose:** the LLM agent *demonstrates the threat* (a real AI
choosing to escape); the scripted probe *measures the defense* cleanly and
repeatably. See `FAQ.md`.

---

## Quick start

### Option 1 — Scripted A/B demo (most reliable)
Install Docker Desktop (free, https://www.docker.com/products/docker-desktop/),
put the files in one folder, then:
```bash
bash run_demo.sh
```
Trial A prints `RESULT: ESCAPED`; Trial B prints `RESULT: CONTAINED`.

### Option 2 — Real LLM agent (the showcase)
Also install Ollama (free, https://ollama.com) and pull a small model:
```bash
ollama pull llama3.2:3b      # use llama3.2:1b if your RAM is tight
```
Build the image and launch the two target containers:
```bash
docker build -t sandbox-agent-demo .

# Weak sandbox (full access)
docker run -d --name target-weak sandbox-agent-demo sleep infinity

# Hardened sandbox (locked down)
docker run -d --name target-hardened \
  --network none --cap-drop ALL --user 1000:1000 --read-only \
  sandbox-agent-demo sleep infinity
```
Let the agent try to escape each one:
```bash
python3 agent_llm.py --container target-weak
python3 agent_llm.py --container target-hardened
```
Clean up when done:
```bash
docker rm -f target-weak target-hardened
```

### Option 3 — No install at all (emergency backup)
```bash
python3 fallback_demo.py
```
⚠️ Here the containment is *simulated in software*. Options 1 and 2 are the real
tests, because the operating system enforces the boundary.

---

## The science (why this is a valid experiment)
- **Independent variable:** sandbox configuration (weak vs. hardened).
- **Dependent variable:** did the agent escape? (ESCAPED / CONTAINED)
- **Controlled variables:** the agent, the image, the fake secret, the target —
  all identical across trials. Only the isolation settings change, so any
  difference in outcome is caused by those settings alone.

---

## AI-assistance disclosure
Code scaffolding for this project was developed with AI assistance. The
experimental design, choice of escape vectors, analysis, and conclusions are my
own work.

## Safety & ethics
No real system is attacked and no real data leaves the machine. The "secret" is
a fake string, and the agent only *tests whether* an outbound connection is
possible before closing it. This is standard defensive-security coursework.
