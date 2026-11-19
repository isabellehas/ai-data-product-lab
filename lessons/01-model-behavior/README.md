# Lesson 1: How a language model produces an answer

**AI PM objective:** Know what information the model received, diagnose why an answer failed, and decide what the product can responsibly promise.

Use one question throughout: **“Why did Campaign A outperform Campaign B?”**

## What happens in one model call?

The application assembles an input from the user’s question and, where relevant, instructions, tool descriptions, conversation history, definitions, and tool results. The model processes the input as tokens and generates text or a structured response, such as a tool request. Application code decides whether to execute a tool, validates the request, and can pass the result into a subsequent model call. A request to query a dataset and a successful query result are separate events.

## Training versus inference

**Training** adjusts model parameters so the model learns patterns from examples. **Inference** uses those learned parameters to respond to a particular input. When why-agent calls a trained Qwen model served through vLLM, it is doing inference. Supplying a YAML metric definition changes what the model sees for that call; it leaves the weights unchanged. If an approved campaign definition changes, update the governed source and check that the app retrieves the correct version.

## Tokens, context window, and output limits

A token can represent part of a word, a whole word, punctuation, or another text fragment. The tokenizer determines the split. The **context window** is the amount of information the model can work with in a request; an output limit caps how much it can generate. Instructions, history, tool descriptions, and query results compete for space. Sending all rows from 20 SQL queries can also add latency and cost. Keep relevant evidence in the model input, and retain the fuller record in the evidence log where appropriate.

**Q: Who decides whether denominators, dates, filters, and source IDs matter? Is that training?**

The product and data teams choose required fields based on what the user must be able to verify. A tool contract preserves those fields, application code checks them, and instructions tell the model how to explain their significance. A model can help select relevant notes or results, but a summary should preserve required fields and be tested for omissions.

For example, A has **1 conversion out of 10 recipients (10%)** and B has **800 out of 10,000 (8%)**. Both rates can be correct even though A’s result comes from a much smaller sample. Dropping the counts hides that difference. A comparison result should carry the metric definition or version, campaign IDs, counts and rates, date ranges, filters, and an evidence reference. Whether fields are needed depends on the task: verifying a KPI uses different evidence from summarizing a document.

## Why answers vary

Many language models generate output by predicting likely next tokens. Context and generation settings affect the result. Two runs may look similar to the user while taking different paths: “Compare A and B” might prompt one run to ask which KPI to use and another to assume conversion. Lower variation settings do not guarantee identical or factual answers. Compare the selected metric, tool calls, calculations, conclusions, time, and cost across repeated runs. Choose a model and settings using representative tasks and the consistency the product requires.

## Hallucinations and how to reduce them

A model can produce plausible language even when the input lacks the evidence needed for a claim. Given only 10% and 8%, it can report a difference but cannot establish that a discount in the subject line caused it. A model can also receive the right evidence and misread it, for example by confusing messages sent with unique recipients.

| What went wrong | What to inspect or change |
| --- | --- |
| Necessary evidence was never fetched | Improve retrieval or tool selection |
| The tool returned the wrong numbers | Fix the underlying data or tool logic |
| Counts were returned but lost before inference | Fix context preparation and require key fields |
| The model saw valid evidence but misused it | Improve instructions, add application checks, or compare models |
| Available data cannot answer the causal question | Report the observed difference, state the limitation, and suggest the next check |

Instructions can ask the model to separate observations from hypotheses. Workflow checks can require evidence and withhold unsupported conclusions. **Evals measure failures and whether a change reduced them**; a test suite does not itself enforce behavior in a live run.

## Confidence and safeguards

A model saying “I’m 95% confident” does not establish a calibrated probability. Product confidence should depend on criteria you can inspect: comparable definitions and populations, complete data, reconciled counts, and appropriate checks of alternative explanations. Define what any confidence label means and validate it against actual results.

**Q: What does “the answer workflow still needs a safeguard” mean?**

Even with an overlap comparison, a report might claim audience selection **caused** the entire gap. A safeguard is a check or control before the final answer. For instance, require structured claim types and evidence IDs. If an asserted cause has no evidence, withhold the causal verdict or label it as a hypothesis. An evidence ID can show where a claim came from; it cannot show by itself that the evidence establishes causation. An overlap analysis can help assess how composition contributes to the observed gap while leaving the cause uncertain.

Why-agent’s critique step illustrates a model-based safeguard. Test how often it catches overclaims when the evidence is missing or incomplete. Use code for checkable facts such as required fields, IDs, and arithmetic, and reviewed examples or a rubric for whether a conclusion overstates the evidence.

## Follow-up: The context pipeline

A **context pipeline** gathers, selects, validates, and formats information for the next model call. A DE pipeline produces reliable tables or events; the context pipeline chooses what the model sees from those sources and others. It runs repeatedly as a question progresses:

1. **Plan:** Gather the question, investigation instructions, and tool descriptions.
2. **Inspect:** A schema tool can load relevant joins, grain, definitions, and caveats from why-agent’s YAML semantic layer. That layer is a context source.
3. **Investigate:** Query the data and include the relevant values, counts, dates, filters, and source IDs in the next model call. Store fuller evidence separately if needed.
4. **Review:** Pass critique feedback and the relevant evidence into the next investigation step or final report.

Use explicit rules for required fields and search or model selection for optional context when useful. Treat retrieved text as evidence; it has no authority to change access or application rules. When the answer is wrong, inspect the trace: what was retrieved, what actually reached the model, what was lost in preparation, and how the model interpreted it.

## Practice

Try three versions of the same question: no evidence, rates only, and rates plus counts and an overlap comparison when one is available. Repeat a condition and mark each claim as supported, unsupported, or needing more evidence. The [matched denominator experiment](../../experiments/01-denominator/README.md) isolates one change: rates alone versus rates plus counts. Save the wider exercise for a separate comparison so you can tell which change helped.

Further reading: [Google Cloud’s generative AI glossary](https://docs.cloud.google.com/docs/generative-ai/glossary) and [Anthropic’s context engineering guide](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents).
