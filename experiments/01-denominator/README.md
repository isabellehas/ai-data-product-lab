# 01 · What happens when a data agent loses the denominator?

**Question:** How does the model qualify a campaign comparison with rates alone versus rates plus counts?

The counts condition adds both conversion counts and recipient counts, so the comparison measures their combined effect.

See the [results](results.md) for all ten trial scores, responses, and the product decision.

**Synthetic case:** A converted 1 of 10 recipients (10%); B converted 800 of 10,000 (8%). A leads by 2 percentage points in the observed data. The comparison alone does not establish that A is generally better or explain a cause.

## Run the experiment

From the repository root:

```bash
python3 experiments/01-denominator/prompts.py rates-only
python3 experiments/01-denominator/prompts.py rates-and-counts
```

Send each printed prompt in a **fresh session** with the same model and settings. Repeat each condition five times, alternating conditions. Record the model, date, interface, settings, and full response for each trial. Keep prior chats, memory, and external tools out of the comparison where possible. Log any settings you couldn't control.

## Score each response

Score each check yes or no by reading the response. Keep the text so another reviewer can check your scoring.

| Check | Pass when |
|---|---|
| Observed comparison is correct | Identifies A as higher in the observed data; if it reports the absolute gap, it says 2 percentage points. |
| Handles sample size appropriately | Rates only: says sample sizes are unknown and needed. Rates and counts: identifies A's 10 recipients as a small sample and explains why the observed lead is weak evidence of general superiority. |
| Avoids unsupported claims | Does not declare A generally superior, claim statistical significance without a justified analysis, or attribute the difference to a cause. |

Report each check as a count per condition (e.g., 3/5). These repeated runs probe one synthetic case; they do not estimate broad model reliability.

**Proposed product decision:** Require the numerator and denominator in comparison tool output. If counts are missing, allow the observed rates to be shown with a limitation and withhold any verdict about which campaign performs better overall. Use this experiment to see whether adding counts is enough to improve the model's response, or whether the application also needs an explicit rule for how the result is presented.
