## The questions you may ask:


### Q: What's the point? Why does this matter?
AI agents are given control over companies and data that is meant to be kept private. The recent OpenAI hugging face incident- [OpenAI rogue agent breach of Hugging Face - Wikipedia](https://wikipedia.org) intrigued me and Kaye deeply. We developed a project to test the security of sandboxes, starting with the question: **Does adding isolation layers actually stop an agent, or does it just feel safer?**

---

### Q: Where's the creativity?
The creativity is in the **experiment**.
1. **A real LLM agent that decides its own escape attempts** — paired with a
   deterministic probe, so we can both *show the threat* and *measure the defense*
   cleanly. 
2. **The careful procedure** — instead of changing everything at once, we test each layer
   alone (network-only, privileges-only, read-only) to measure *which one actually does
   the work*. That produces an original finding and a graph.
3. **Special twist** — We show that a sandbox can genuinely look like they are locked down and
   still leak because of one common misconfiguration (idk what that is yet), then close that hole too.(with full analysis if we need it!)

---

### Q: How will this help us stand out?
Most students demo one side — either an attack or a defense. We show the full procedure, isolated: I **build the escape** *and* Kaye **designs the defense**, then **show** the result with a graph. A surprising, measured
result that a judge can see in one chart can stand out (hopefully).

---

### Q: Is any of this dangerous or unethical?
No. Nothing real is attacked and no data leaves the laptop. The
"secret" is a fake string that means nothing, and the agent only tests if an outbound
connection is possible before closing it immediately. 

