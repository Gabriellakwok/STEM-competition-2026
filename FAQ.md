# FAQ — The Questions You'll Actually Get Asked

Short, honest answers to the questions a teacher, judge, or classmate will
throw at this project. Written so anyone can follow it.

---

### Q: What's the point? Why does this matter?
AI agents are now given real control over computers — they run code, browse the
web, and call tools on their own. If an agent is tricked, jailbroken, or just
buggy, it can try to **break out of its sandbox**: reach the open internet, grab
secrets it shouldn't have, and leak them. Companies are deploying these agents
faster than they're securing them. This project answers a concrete, urgent
question: **does adding isolation layers actually stop an agent, or does it just
feel safer?**

### Q: Where's the creativity? Isn't this just a tutorial?
The creativity isn't in the code — it's in the **experiment**. Three original
design choices make it mine:
1. **A real LLM agent that decides its own escape attempts** — paired with a
   deterministic probe, so I can both *show the threat* and *measure the defense*
   cleanly. Explaining why I use both is a research decision, not a tutorial step.
2. **The ablation** — instead of changing everything at once, I test each layer
   alone (network-only, privileges-only, read-only) to measure *which one does
   the most work*. That produces an original finding and a graph.
3. **The surprise twist** — I show that a sandbox can *look* locked down and
   still leak because of one common misconfiguration, then close that hole too.

### Q: How will this help me stand out?
Most students demo one side — either an attack or a defense. I show the full
loop: I **build the escape** (penetration-tester mindset) *and* **design the
defense**, then **quantify** the result with a graph. A surprising, measured
result that a judge can see in one chart is what gets remembered.

### Q: You used AI to write the code — isn't that plagiarism?
No — and here's the honest line between cheating and legitimate tool use:
- **Plagiarism** = passing off work you don't understand and didn't disclose.
- **Legitimate tool use** = using AI like a calculator or a microscope:
  understanding what it produced, modifying it, and being upfront about it.

I protect the integrity of this project three ways:
1. **I understand every line.** Ask me what `--cap-drop ALL` does and I'll tell
   you on the spot.
2. **The thinking is mine** — the hypothesis, which escape routes to test, and
   what the results mean. AI helped with syntax; the science is my own.
3. **I disclose it** (see the note below and in the README).

> **AI-assistance disclosure:** Code scaffolding for this project was developed
> with AI assistance. The experimental design, choice of escape vectors,
> analysis, and conclusions are my own work.

### Q: Is any of this dangerous or unethical?
No. Nothing real is attacked and no real data ever leaves the laptop. The
"secret" is a fake string, and the agent only *tests whether* an outbound
connection is possible before immediately closing it. This is standard
defensive-security coursework — the whole goal is to show how to keep systems
safe.

### Q: Why a container (Docker) instead of just a Python flag?
A Python flag is something the program chooses to obey — an attacker's code can
ignore it. A container boundary is enforced by the **operating system itself**,
so even malicious code inside can't cross it. That's the difference between
"please don't" and "you can't," and it's the core idea of real sandboxing.
