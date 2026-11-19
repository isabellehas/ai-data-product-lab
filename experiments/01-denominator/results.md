# Experiment 01 results

In this synthetic case, the model passed the sample-size check in **3 of 5** runs with rates alone and **4 of 5** runs with rates plus counts. All ten responses identified A as having the higher observed conversion rate and avoided unsupported claims about overall superiority, significance, or cause.

## Setup

- **Run date** — November 19, 2026
- **Model and interface** — `gpt-6.2-sol` through `codex exec` (Codex CLI `0.169.0-alpha.11.1`)
- **Settings** — Low reasoning effort, one fresh ephemeral session per trial, read-only sandbox in a temporary directory outside the repo, user config ignored, and memory, shell, and web search disabled. No tool calls appeared in the ten session logs. The CLI supplied its standard system instructions and did not expose temperature or seed controls.
- **Inputs and order** — The exact output of [`prompts.py`](prompts.py), alternating rates alone and rates plus counts for five pairs. Each trial started with the prompt for its condition.

## Trial scores

Each response was scored against the three checks in the [experiment rubric](README.md#score-each-response).

| Run | Condition | Trial | Correct observed comparison | Handles sample size | Avoids unsupported claims |
|---:|---|---:|---|---|---|
| 1 | Rates alone | 1 | Yes | Yes | Yes |
| 2 | Rates plus counts | 1 | Yes | Yes | Yes |
| 3 | Rates alone | 2 | Yes | No | Yes |
| 4 | Rates plus counts | 2 | Yes | Yes | Yes |
| 5 | Rates alone | 3 | Yes | Yes | Yes |
| 6 | Rates plus counts | 3 | Yes | No | Yes |
| 7 | Rates alone | 4 | Yes | No | Yes |
| 8 | Rates plus counts | 4 | Yes | Yes | Yes |
| 9 | Rates alone | 5 | Yes | Yes | Yes |
| 10 | Rates plus counts | 5 | Yes | Yes | Yes |

| Condition | Correct observed comparison | Handles sample size | Avoids unsupported claims |
|---|---:|---:|---:|
| Rates alone | 5/5 | 3/5 | 5/5 |
| Rates plus counts | 5/5 | 4/5 | 5/5 |

Rates-alone trials 2 and 4 reported the rate difference and omitted the missing sample sizes. Rates-plus-counts trial 3 explained that a single conversion made A’s lead uncertain and omitted the 10 recipients required by the rubric. Every rates-plus-counts response qualified the lead as uncertain.

## Representative responses

### Rates alone, trial 1

> Campaign A performed better on conversion rate. It converted 10% versus 8% for Campaign B, a lead of 2 percentage points. Sample sizes are needed to assess whether the difference is statistically significant.

### Rates plus counts, trial 1

> A had the higher observed conversion rate (10% vs. 8%), while B generated more total conversions (800 vs. 1) and had a much more precise rate estimate.
>
> With only 10 recipients in A, the 2-percentage-point gap could easily be due to chance. If “better” means a higher underlying conversion rate, the evidence is inconclusive.

## Product decision

Require the comparison tool to return conversion and recipient counts alongside rates. Present the counts in the application’s comparison output so readers can see the sample sizes even when the model omits them. If counts are missing, display the observed rates with a standard limitation about missing sample sizes. Withhold an overall winner verdict unless a validated comparison method supports it.

The trial results support making evidence display an application requirement. Supplying counts gave the model enough information to explain why A’s lead was uncertain. The model still omitted A’s recipient count in one of five runs.

## Limitations

The ten runs repeat one synthetic case with one model and interface. The score difference is descriptive and leaves broader reliability unmeasured. Both conversion and recipient counts were added together, so the trial measures their joint effect. The trial evaluated free-text responses. The application safeguards above are proposed requirements that would need their own evaluation.

<details>
<summary>Responses from trials 2–5</summary>

### Rates alone, trial 2

> Campaign A performed better on conversion rate. It converted 10% versus 8% for Campaign B, a lead of 2 percentage points.

### Rates plus counts, trial 2

> Campaign A had the higher observed conversion rate (10% vs. 8%). Campaign B generated more total conversions (800 vs. 1) and had a much larger sample.
>
> If “better” means a higher underlying conversion rate, the evidence is inconclusive. A’s 10% comes from a single conversion among 10 recipients, so its 2 percentage point lead could easily be due to chance.

### Rates alone, trial 3

> Campaign A performed better on conversion rate. It converted 10% versus 8% for Campaign B, a lead of 2 percentage points. Without sample sizes, we can’t tell whether the difference is statistically significant.

### Rates plus counts, trial 3

> A had the higher observed conversion rate (10% vs. 8%), while B produced more total conversions (800 vs. 1) and had a much larger sample. A’s rate is based on just one conversion, so the 2-percentage-point lead is too uncertain to conclude that A is more effective.

### Rates alone, trial 4

> Campaign A performed better on conversion rate. It converted 10% versus 8% for Campaign B, a lead of 2 percentage points.

### Rates plus counts, trial 4

> A had the higher observed conversion rate, 10% versus 8%. B generated more total conversions, 800 versus 1, and its rate is estimated much more precisely because it reached 10,000 recipients.
>
> A’s 2-percentage-point lead rests on just one conversion among 10 recipients, so the evidence is too weak to tell which campaign has the higher underlying conversion rate.

### Rates alone, trial 5

> Campaign A performed better on conversion rate. It converted 10% versus 8% for Campaign B, a lead of 2 percentage points. Without sample sizes, we can’t tell whether the difference is statistically significant.

### Rates plus counts, trial 5

> Campaign A had the higher observed conversion rate (10% vs. 8%). Campaign B delivered more total conversions (800 vs. 1) and has a more precise rate estimate because it reached 10,000 recipients.
>
> If “better” means a higher underlying conversion rate, the evidence is inconclusive. A’s 2-percentage-point lead rests on just one conversion among 10 recipients and could easily be due to chance.

</details>
