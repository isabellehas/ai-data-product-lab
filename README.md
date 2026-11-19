# AI Data Product Lab

A ten-week learning project on making AI agents trustworthy enough to answer business questions about data. Each module pairs a lesson with a practical exercise and a decision an AI product manager could make from the evidence.

The lab builds on questions explored in [why-agent](https://github.com/Isa-Mapo-Hackathon/why-agent), a collaborative project for investigating metric changes. The examples here are independent and use synthetic or public data.

## Start here

1. Read [Lesson 1: How a language model produces an answer](lessons/01-model-behavior/README.md). It includes the original lesson, follow-up Q&A, and the context pipeline walkthrough.
2. Try [Experiment 01: What happens when a data agent loses the denominator?](experiments/01-denominator/README.md). You can copy the prompts by hand or print them with Python 3.10+; no packages or API keys are needed for the script.
3. Score the outputs using the supplied rubric. Record the model and conditions, summarize the failures, and write down what you would change in the product.

## Ten-week roadmap

| Period | AI focus | Work to do | Evidence and product decision |
| --- | --- | --- | --- |
| Weeks 1–2 | Model behavior and ML/statistics foundations | Vary model context; review sample size, selection bias, data leakage, and correlation versus causation | Small failure analysis: what can the agent say with this evidence, and when should it qualify an answer? |
| Weeks 3–4 | Retrieval | Compare exact lookup, keyword search, and vector search on questions with known relevant sources; check versions and metadata filters | Retrieval comparison: which approach serves which task, and where does it fail? |
| Weeks 5–6 | Agent versus fixed workflow | Run the same cases through a fixed workflow, a single agent, and an agent with critique when useful | Quality, latency, and cost comparison: when does dynamic investigation earn its complexity? |
| Weeks 7–8 | Evaluation | Build a reusable suite with known answers, ambiguous requests, insufficient data, and tool failures | Repeatable test set and error breakdown: what should block a release? |
| Weeks 9–10 | Operations and release judgment | Trace slow or costly runs, compare versions, and define pilot, monitoring, and rollback criteria | Launch recommendation with known limitations: what should ship, for which users, and under what conditions? |

**Status:** Lesson 1 is written and the first experiment has prompts and a rubric. Model trials are pending. The deeper statistics material and later modules are planned.

## Repo structure

| Path | Purpose | Status |
| --- | --- | --- |
| `README.md` | Project overview, roadmap, and entry points | Available |
| `lessons/` | Concept notes, worked examples, and consolidated Q&A | Lesson 1 available |
| `experiments/` | One folder per experiment: protocol, inputs or scripts, scoring rubric, and results when collected | Experiment 01 ready to run |
| `evals/` | Shared cases, graders, and instructions once multiple experiments can reuse them | Planned for weeks 7–8 |
| `decisions/` | Short write-ups for decisions spanning several experiments, such as a launch recommendation | Planned for weeks 9–10 |

Keep an experiment’s evidence and recommendation in its own folder until there is a reason to share it across modules. Give each write-up a question, baseline, setup, results, limitations, and product decision. Distinguish proposed requirements from measured findings. Record the model and conditions so readers can repeat the run. Keep credentials and nonpublic employer material outside the repo.
