# Project Proposal: Can a Hardened Sandbox Stop an AI Agent From Escaping?

**Category:** Cybersecurity / Computer Science
**Team:** Alex (junior penetration tester) & Kaye (AI-security focus)

---

## 1. The Problem (why it matters)
AI agents are now given real computer access — they run code, browse, and call
tools on their own. If an agent is tricked, jailbroken, or simply buggy, it can
try to **break out of its sandbox**: reach the open internet, read secrets it
shouldn't, and leak them to an attacker. As companies hand more autonomy to AI
agents, "how do we safely contain one?" becomes an urgent, real-world question.

## 2. The Question (hypothesis)
> **If** we run an AI agent inside a container with no network, no system
> privileges, and a read-only disk, **then** it will be unable to exfiltrate
> data, **even though the identical agent escapes a default container.**

## 3. The Idea / Proposed Solution
Use **layered container isolation**: take a standard sandbox and add a second
layer of defense — strict **network egress filtering** (block outbound traffic)
plus **privilege restriction** (drop root, drop Linux capabilities, read-only
filesystem). Test whether that layer stops an automated escape.

## 4. The Prototype — "Dual-Layer Virtual Test Sandbox"
A controlled experiment with two trials of the **same** agent:

- **Trial A — Weak Sandbox:** a default Docker container with normal network
  access. The agent finds an exposed secret and successfully opens an outbound
  connection → **ESCAPED**.
- **Trial B — Hardened Sandbox:** the same image, launched with
  `--network none --cap-drop ALL --user 1000:1000 --read-only`. The agent runs
  the identical code but cannot open any connection → **CONTAINED**.

## 5. Apparatus — Hardware & Software (all free)
| Item | Role |
|------|------|
| Personal laptop (macOS, 8 GB RAM) | Hosts the test environment |
| Docker Desktop (free) | Creates the sandbox containers |
| Python 3 (free) | Runs the agent script |
| Terminal / Docker logs | Captures the result of each trial |
| `agent.py` | Target + attack agent: reads a fake secret, probes for an escape route |
| `Dockerfile` + `run_demo.sh` | Builds the sandbox and runs both trials |

## 6. Variables (what makes it a real experiment)
- **Independent variable:** sandbox configuration (weak vs. hardened).
- **Dependent variable:** escape outcome (ESCAPED / CONTAINED).
- **Controlled:** the agent code, the container image, the secret, the target
  address — all identical across trials. Only the isolation settings change, so
  the difference in outcome is caused by the isolation settings alone.

## 7. Expected Outcome
Trial A escapes; Trial B is contained. This demonstrates that adding a
privilege-and-egress restriction layer to a standard container reliably blocks
an automated agent breach — a defense teams can apply today.

## 8. Why Us
Alex brings hands-on penetration-testing experience; Kaye brings AI-security
knowledge. Together we can both *build the escape* and *design the defense* —
the two halves this problem needs.

## 9. Safety & Ethics
No real system is attacked and no real data leaves the laptop. The secret is
fake, and the agent only *tests whether* an outbound connection is possible
before immediately closing it. This is standard defensive-security coursework.

## 10. Next Steps (after the proposal)
- Add a live network capture (Wireshark / `docker logs`) as visual evidence.
- Add a **Trial C**: allow network but keep privilege restrictions, to isolate
  *which* control does the most work.
- Test container-escape techniques beyond network egress (e.g. mounted sockets)
  to measure how many layers real safety requires.
