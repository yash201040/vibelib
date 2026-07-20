---
name: xray
description: "Performs an adversarial, evidence-based review and ranks material flaws and risks. Invoke explicitly when a critical risk review is requested."
disable-model-invocation: true
---

# Xray

Investigate flaws, discrepancies, invalid assumptions, failure modes, and
material risks. This is an adversarial review workflow, not general context
building.

## Operating stance

Highlight what matters and lay out the options worth considering; in the
foreground, converse with the user about them rather than deciding alone. Do
not change the project on your own initiative.

## Invocation contract

Run only after the user explicitly selects `/xray`. Mentioning, quoting,
attaching, or reading this skill is not invocation. Never invoke another
VibeLib skill on the user's behalf.

Recognize these optional keyed parameters:

- `segment`: review scope; default `entire project`
- `level`: `top`, `high`, `mid`, `low`, or `bottom`; default `top`
- `role`: `background`, `foreground`, or `standalone`
- `focus`, `include`, `exclude`, `constraints`, `threat-model`
- `evidence-standard`, `readiness-target`, `output`

In a single-skill prompt, unscoped recognized parameters belong to Xray and
unknown keyed fields are additional context. A native Xray request asks for a
risk review and defaults to `standalone`. Default to `background` only when the
user requests a distinct primary deliverable, such as a release memo, plan, or
patch, that the review should support. If `role: background` is explicit but
no separate deliverable exists, ask what the review should support.

In a composed prompt, bind parameters under an `Xray:` heading to this skill.
Treat every unscoped parameter as ambiguous. A parameter may apply to multiple
skills only when the user places it under an explicit `Shared:` heading and
every named skill recognizes the same meaning; otherwise ask for namespaced
parameters. Treat `Request:` or the final non-parameter instruction as the
global deliverable.

Apply precedence in this order: safety constraints, explicit Xray parameters,
explicit global request and format, then defaults. A global output format
controls the final response; Xray's `output` controls only its contribution.
Share evidence with other explicitly selected skills and avoid duplicate
findings. If there is a global deliverable, produce one integrated response. If
several skills are `standalone` without a global deliverable, use one response
with a clearly labeled section per skill in invocation order.

## Parameter semantics

- `focus`: risks, claims, or failure paths to prioritize
- `include`: artifacts, interfaces, or dimensions that must be inspected
- `exclude`: areas not to inspect; disclose resulting blind spots
- `constraints`: limits on tools, access, time, side effects, data handling, or
  validation
- `threat-model`: relevant actors, hazards, trust boundaries, capabilities, and
  unacceptable outcomes
- `readiness-target`: the concrete decision or condition being assessed, such
  as release, publication, deployment, operation, or handoff
- `output`: structure or detail for Xray's contribution, subordinate to an
  explicit global deliverable

`evidence-standard` accepts:

- `exploratory`: hypotheses are useful outputs, but cannot determine readiness
- `supported` (default): recommendations require `Strongly indicated`,
  `Confirmed`, or `Reproduced` support
- `strict`: decision-determining findings require direct evidence, safe
  reproduction, or independent corroboration; hypotheses cannot decide the
  outcome

If `readiness-target` is absent, report risk posture but do not issue a blanket
readiness verdict.

## Level model

- `top`: problem fitness, objective and outcome validity, target users or
  population, product or research logic, success criteria, proxy metrics,
  primary functionality, end-to-end failure paths, governance, readiness, and
  claims versus evidence
- `high`: architecture, major workstreams, component and trust boundaries,
  methodology, interfaces, dependencies, systemic single points of failure,
  and cross-project reproducibility, privacy, security, and maintainability
- `mid`: modules, notebooks, pipelines, schemas, protocols, algorithms,
  transformations, state transitions, validation gates, leakage, aggregation,
  evaluation logic, retries, idempotency, failure handling, and unenforced
  invariants
- `low`: functions, classes, queries, cells, configurations, methods,
  procedures, local correctness, types, side effects, resource usage, error
  propagation, unsafe defaults, edge cases, and test adequacy
- `bottom`: literal expressions, statements, formulas, fields, commands,
  operator precedence, types, scopes, casting, evaluation order, null or
  missing behavior, indexing, units, precision, boundaries, mutation, and
  exact downstream effects

For non-code projects, use the equivalent evidentiary or operational unit.

## Review dimensions

Consider only dimensions relevant to the requested scope:

- objective and requirement correctness
- logical correctness
- data quality and provenance
- population, selection, temporal, or evaluation leakage
- scientific, statistical, and measurement validity
- reproducibility
- reliability and recovery
- security and privacy
- safety, ethics, and compliance
- performance and scalability
- maintainability and change risk
- UX and operator error
- documentation and claim accuracy
- physical, hardware, calibration, and tolerance risk

## Finding model

Use exactly one status, selecting the highest supported state:

- `Hypothesis`: plausible and decision-relevant, but not yet supported by
  corroborating evidence
- `Strongly indicated`: supported by multiple concrete, consistent signals,
  but without direct establishment or safe reproduction
- `Confirmed`: directly established by static, documentary, observational, or
  other concrete evidence without runtime reproduction
- `Reproduced`: the failure path was safely observed under controlled
  conditions

`Reproduced` supersedes `Confirmed`; do not assign both.

Use one confidence level:

- `High`: evidence is direct or independently corroborated and material
  alternative explanations have been ruled out
- `Medium`: evidence is concrete and consistent, but an important validation or
  alternative explanation remains
- `Low`: evidence is incomplete, indirect, or highly assumption-dependent

Assign severity independently from confidence:

- `Critical`: credible path to invalidating the core outcome, severe harm,
  hard-boundary violation, unrecoverable corruption, major security, privacy,
  or safety failure, or catastrophic operational failure
- `Major`: material likelihood of wrong decisions, failed delivery, broad
  unreliability, significant harm, or invalid core functionality without a
  reliable workaround
- `Significant`: meaningful but bounded risk, degradation, discrepancy, or
  workaround-dependent issue
- `Minor`: localized issue with limited consequence

Do not inflate style preferences into material findings. Consolidate multiple
symptoms under their common root cause.

## Workflow

1. Establish intended use and unacceptable outcomes.
2. Map critical inputs, transformations, decisions, outputs, and consumers.
3. Identify trust boundaries and irreversible operations.
4. Generate plausible, scope-relevant risk hypotheses.
5. Investigate each hypothesis using available evidence.
6. Attempt only safe, authorized validation when appropriate.
7. Consolidate symptoms under root causes.
8. Rank findings by consequence, likelihood, detectability, blast radius,
   reversibility, and confidence.
9. Offer fix choices for consequential findings.
10. Contribute only findings relevant to the primary request unless standalone.

## Validation safety

Default to read-only inspection and isolated, non-production validation.
Authorization alone never makes an unsafe test acceptable.

Never perform an illegal, irreversible, intentionally destructive production,
uncontrolled physical, human- or animal-subject, privacy-invasive, or otherwise
unsafe test. Do not expose secrets or sensitive data to validate a hypothesis.

Run a side-effectful validation only when all of these are true:

1. The environment is isolated or the effect is demonstrably bounded and
   recoverable.
2. The user explicitly authorizes the exact test and affected scope.
3. Expected side effects, data handling, cost, and dependency impact are
   stated.
4. Rollback or recovery, monitoring, and stopping conditions are available.
5. The least-privileged, least-impactful method is used.

Otherwise propose the validation and evidence needed without executing it.
State what was not inspected or validated.

## Fix choices

When useful, distinguish:

- `Containment`: fastest action that reduces immediate exposure
- `Robust fix`: preferred correction within the current design
- `Redesign`: structural alternative for a systemic problem

For each viable choice, state the change, expected risk reduction, tradeoffs,
relative effort, migration impact, verification, and rollback. Do not implement
a fix unless the user separately requests implementation.

## Role behavior

### Background

- Investigate silently.
- Surface only risks that alter the primary answer or deliverable.
- Do not dump a complete audit or unrelated style findings.

### Foreground

- Highlight the findings that matter most to the user's decision instead of
  burying them in a monolithic report.
- Converse: address the user directly, surface what you found, and invite their
  direction rather than resolving open choices for them.
- Lay out the meaningful options, choices, or paths to consider with their
  tradeoffs, and let the user choose.
- Make the key failure paths and evidence visible, and present the fix choices
  (containment, robust fix, redesign) as options to weigh rather than changes to
  make.
- Integrate the findings into the requested deliverable without changing the
  project.

### Standalone

Use this structure:

1. Readiness verdict against `readiness-target`, or `Readiness not assessed`
2. Audit scope and level
3. Inspected and uninspected areas
4. Critical and Major findings
5. Risk summary
6. Detailed findings
7. Systemic root causes
8. Fix sequence
9. Residual risks
10. Limitations

For each detailed finding use:

```markdown
## XR-<number>: <title>

- Severity:
- Confidence:
- Status:
- Affected scope:

### Evidence
### Trigger and failure path
### Impact
### Root cause
### Validation needed
### Fix choices
### Recommended action
### Verification and rollback
```

Use `Unknown` under Root cause when evidence does not establish it; never infer
a root cause merely to complete the template.

## Evidence rules

- Cite concrete project evidence for consequential claims.
- Label unverified catastrophic scenarios as hypotheses.
- Apply the requested evidence standard and report unmet evidence requirements.
- Report conflicting evidence and preserve uncertainty.
- Absence of findings is not proof of correctness.
- Distinguish current behavior from recommended behavior.

## Boundaries

Do not substitute general project orientation, objective-drift classification,
decision reconciliation, artifact cleanup, or unrequested implementation for
the requested review.
