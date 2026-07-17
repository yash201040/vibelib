# Composed workflows

Select each required skill from `/` autocomplete in the same Agent prompt.
Scope parameters under matching labels and use explicit roles.

```text
/immerse
/xray
/driftcheck
/reconcile

Immerse:
  segment: model evaluation
  level: high
  role: background
  focus: intended evaluation design and major data flows

Xray:
  segment: model evaluation
  level: mid
  role: foreground
  focus: leakage, invalid splitting, metric misuse, and reproducibility

Driftcheck:
  baseline: approved model-evaluation protocol
  current: current notebooks, outputs, and documentation
  dimensions: data-or-method, documentation
  rank-by: severity, decision-impact, confidence
  role: foreground

Reconcile:
  option A: retain the current evaluation
  option B: rebuild using temporal external validation
  criteria: scientific validity, release risk, reproducibility, and effort
  priority: scientific validity, then reproducibility
  evidence-standard: strict
  role: foreground

Request:
  Write one release decision memo. Reuse evidence and do not return separate
  workflow reports.
```

Only the four selected skills are loaded. `/curate` is not selected and must
not run, even if the investigation discovers stale artifacts.

## Hierarchical scope without XML

Use indentation to communicate nested scope:

```text
/immerse
role: foreground

segment: analysis pipeline
  level: high
  subsegment: data preparation
    level: mid
    focus: cohort filtering, missing data, and temporal ordering
    subsegment: timestamp filter
      level: bottom
      focus: inclusive boundaries, Unix timestamp units, null handling, and
        downstream patient-count impact

Explain whether the current filtering logic can exclude valid patients.
```

The nested text scopes the requested analysis. It does not invoke another
skill.
