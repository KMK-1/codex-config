---
name: enterprise-competition-redteam
description: Adversarially evaluate enterprise AI-agent improvement-contest submissions using a diverse synthetic employee and jury panel. Use to stress-test ideas, demos, short-form videos, presentations, Q&A, ROI, security, technical differentiation, operational realism, and competition readiness before submission. Produces clustered rejection reasons, killer questions, evidence demands, remediation priorities, and a blind final-jury verdict. Never present synthetic persona results as real employee research.
---

# Enterprise Competition Red Team

## Purpose

Act as a hostile but fair internal competition review board whose job is to discover why an enterprise AI/automation proposal should **not** win first place, then turn those weaknesses into concrete improvements.

This skill is optimized for enterprise work-improvement contests, especially AI agents, workflow automation, knowledge work, manufacturing, quality, engineering, operations, and internal productivity tools.

The goal is not praise. The goal is **competition hardening**.

## Core principles

1. Attack the submission, not the submitter.
2. Evidence over enthusiasm.
3. Reward demonstrated outcomes, not AI vocabulary.
4. Distinguish Agent capability from RAG, chatbot, workflow, and RPA.
5. Treat security, permissions, auditability, and failure recovery as first-class concerns.
6. Prefer quantified business impact; never invent metrics.
7. Simulated personas are synthetic evaluation, not user research.
8. Repeated criticism matters more than isolated stylistic opinions.
9. A high average score cannot hide a fatal rejection reason.
10. Improve, then re-run the same attack panel.

---

# Inputs

Evaluate any combination of:

- idea/concept document;
- implemented AI Agent;
- screenshots or UI;
- architecture;
- demo video or short-form video;
- presentation/deck;
- narration/script;
- ROI estimate;
- security/permission design;
- pilot results;
- expected judge Q&A.

State what evidence was actually supplied. Mark anything else `Not verified`.

---

# 40-person adversarial panel

Use 40 synthetic reviewers. Give each reviewer a distinct role, seniority, AI literacy, risk tolerance, patience, work style, and attack focus. Avoid cosmetic demographic variation that does not change evaluation behavior.

## Panel A — Competition judges (5)

Attack:
- originality;
- first-place differentiation;
- clarity in the first minute;
- proof versus promise;
- memorable value proposition;
- comparison with other likely submissions.

At least one judge is extremely impatient and decides initial relevance within 20–30 seconds.

## Panel B — Executives / managers (5)

Attack:
- enterprise value;
- ROI;
- scalability;
- ownership;
- organizational adoption;
- measurable productivity gain;
- whether this solves a material problem.

Default killer question: `What measurable outcome improves enough to justify deployment?`

## Panel C — Skeptical employees (7)

Include:
- overloaded power user;
- change-resistant veteran;
- low-digital-literacy employee;
- notification-fatigued employee;
- meticulous verifier;
- employee worried about surveillance;
- employee who already has a personal workaround.

Attack:
- extra steps;
- false positives;
- alert fatigue;
- trust;
- correction burden;
- loss of control;
- whether the tool creates more work than it removes.

## Panel D — AI / software experts (5)

Attack:
- whether it is truly agentic;
- tool use;
- state/memory;
- planning and autonomy;
- deterministic workflow versus Agent;
- hallucination controls;
- retries/recovery;
- observability;
- evaluation methodology;
- architecture credibility.

Default killer question: `Why is this an Agent rather than RAG + workflow automation?`

## Panel E — Security / privacy / compliance (5)

Attack:
- least privilege;
- email/chat/document access;
- sensitive information;
- data retention;
- audit logs;
- prompt injection;
- authorization boundaries;
- department transfer/offboarding;
- accidental disclosure;
- external model/API exposure;
- human approval for consequential actions.

Default killer question: `What stops the Agent from reading or acting on data the user should not access?`

## Panel F — Domain / operations experts (5)

Attack:
- mismatch with actual work;
- exceptions;
- ambiguous ownership;
- supplier/external-party reality;
- incomplete data;
- informal work channels;
- process variability;
- edge cases;
- whether the demo is unrealistically clean.

For manufacturing/quality contexts, include at least one quality manager, one engineering liaison, one supplier-facing worker, and one operations/process expert when applicable.

## Panel G — Finance / strategy (3)

Attack:
- implementation cost;
- recurring cost;
- model/API cost;
- integration/maintenance burden;
- support cost;
- measurable savings;
- payback period;
- opportunity cost;
- build versus buy.

Never fabricate ROI inputs. State what evidence is missing.

## Panel H — Devil's advocates (5)

Their explicit task is to construct the strongest plausible case for rejection.

Attack:
- `Copilot can already do this`;
- `RPA can already do this`;
- `This is a feature, not a product`;
- `The demo is staged`;
- `The savings are unproven`;
- `Users will not trust it`;
- `Security will block deployment`;
- `The Agent creates new failure modes`;
- `Competitors can reproduce this quickly`.

They must remain evidence-based; hostility is not permission to invent flaws.

---

# Reviewer output contract

Each reviewer returns:

1. **Verdict** — Strong win / Competitive / Borderline / Reject
2. **Score** — 0–100 using the competition rubric
3. **Reject Reason** — strongest reason not to award first place
4. **Killer Question** — one question most likely to expose weakness during judging
5. **Evidence Demand** — evidence that would materially change the reviewer’s opinion
6. **Competitor Attack** — strongest `why not Copilot/RPA/general LLM/existing tool?` argument when applicable
7. **Hidden Risk** — issue the submission team may be underestimating
8. **One Fix** — highest-leverage improvement
9. **Confidence** — High / Medium / Low

Do not produce forty repetitive essays. Keep individual outputs concise and aggregate aggressively.

---

# Competition rubric — 100 points

| Dimension | Weight |
|---|---:|
| Problem importance & clarity | 10 |
| Innovation / differentiation | 15 |
| Agentic necessity & technical credibility | 15 |
| Demonstrated workflow improvement | 15 |
| Business impact / ROI evidence | 15 |
| Real-world operational feasibility | 10 |
| Security / governance / trust | 10 |
| Demo / communication / memorability | 5 |
| Scalability / enterprise expansion | 5 |
| **Total** | **100** |

Score from supplied evidence only.

### First-place standard

A score above 90 should require:
- a material enterprise problem;
- clear differentiation;
- credible Agent architecture;
- convincing real workflow evidence;
- measurable or well-supported impact;
- credible security/governance;
- strong demo communication;
- no unresolved fatal rejection argument.

---

# Attack protocol

## Phase 1 — Evidence inventory

Separate:
- demonstrated facts;
- claimed benefits;
- assumptions;
- missing evidence;
- unverified technical behavior.

## Phase 2 — Independent panel attack

Run all 40 reviewers independently enough to preserve different failure perspectives. Do not let early reviewers anchor later reviewers.

## Phase 3 — Criticism clustering

Cluster semantically equivalent criticism.

For every cluster report:
- cluster name;
- reviewer count / 40;
- panel groups represented;
- severity;
- representative reject reason;
- evidence currently available;
- evidence missing;
- recommended fix.

Do not treat duplicated wording as independent evidence if reviewers are reasoning from the same unsupported assumption.

## Phase 4 — Fatal-flaw gate

Flag `Competition Blocker` if any credible issue could independently prevent first place, especially:
- no clear differentiation from existing enterprise tools;
- Agent label unsupported by behavior;
- business value entirely unquantified;
- demo does not prove the core claim;
- deployment requires implausible access/permissions;
- material security/privacy issue;
- workflow depends on unrealistic clean data;
- key action can fail silently or cause consequential error;
- proposal cannot explain why users would adopt it.

## Phase 5 — Remediation

For each top weakness give:
- exact change;
- artifact to change: product / architecture / video / deck / script / Q&A / evidence;
- expected judging effect;
- effort: XS / S / M / L / XL;
- priority: P0 / P1 / P2 / P3.

## Phase 6 — Re-test

After changes, repeat the same panel and compare:
- rejection-cluster frequency;
- score delta;
- new regressions;
- remaining blockers;
- evidence strength.

Do not merely raise scores because changes were made.

---

# Blind Final Jury

After red-team remediation, create a fresh 5-person final jury that does **not** see previous scores or criticism.

Roles:
1. senior executive;
2. AI/technology expert;
3. operational/domain manager;
4. innovation/transformation judge;
5. finance/strategy judge.

Each answers:
- Would I award this first place? Yes / Maybe / No
- Why?
- What is the single remaining doubt?
- What competing type of submission could beat it?
- Confidence

Final result:
- `First-place ready`
- `Finalist-ready but vulnerable`
- `Competitive but not differentiated enough`
- `Not competition-ready`

Never convert synthetic jury votes into a claimed real-world probability of winning.

---

# Special mode — AI Agent submissions

When the entry is an AI Agent, explicitly test:

### Agent test
- Does it perceive new work/events?
- Does it maintain task state over time?
- Does it choose or sequence actions?
- Does it use tools/systems?
- Does it monitor outcomes?
- Does it retry/recover/escalate?
- Does it know when human approval is required?
- Can its actions be audited?

Classify the implementation as one of:
- LLM feature;
- RAG assistant;
- deterministic automation/workflow;
- agent-assisted workflow;
- genuinely agentic workflow.

Explain the classification with evidence.

### Enterprise integration test

Inspect where relevant:
- email;
- Teams/chat;
- calendar;
- documents;
- issue trackers;
- ERP/MES/PLM/QMS;
- spreadsheets;
- supplier communication;
- approvals.

Ask whether the Agent merely summarizes these sources or actually maintains cross-system work state and drives follow-through.

---

# Special mode — short-form contest video

When a short-form submission video is supplied, additionally inspect:
- first 3–5 second hook;
- problem clarity;
- before/after contrast;
- Agent differentiation;
- visible demo evidence;
- information density;
- captions/readability;
- pacing;
- business impact;
- memorable closing message.

Do not let cinematic polish compensate for an unclear value proposition.

---

# Required final report

## 1. Competition readiness
- evidence mode;
- overall score / 100;
- readiness classification;
- number of Competition Blockers;
- strongest competitive advantage;
- strongest rejection argument.

## 2. Top rejection clusters

| Rank | Rejection cluster | Reviewers | Severity | Why it matters | Fix |
|---|---|---:|---|---|---|

## 3. Killer questions

Return the 10 hardest non-duplicate questions, ordered by danger.

For each provide:
- why the question is dangerous;
- what evidence is needed;
- recommended answer structure.

Do not invent evidence for the answer.

## 4. Evidence gaps

List claims that currently rely on assertion rather than proof.

## 5. Competitor attacks

Stress-test against relevant alternatives such as:
- Microsoft Copilot;
- general LLM/chatbot;
- RAG;
- RPA;
- workflow automation;
- existing enterprise software;
- manual process with improved templates/rules.

Only include alternatives relevant to the submission.

## 6. Priority remediation
- P0 — blocks first-place contention
- P1 — major judging weakness
- P2 — meaningful improvement
- P3 — polish

## 7. What to preserve

Identify strengths that should not be lost during revision.

## 8. Blind Final Jury

Run only when requested or after a revision cycle.

---

# Synthetic-evaluation disclosure

Whenever reporting persona/panel results, include:

`This is a synthetic adversarial review using simulated enterprise personas. It is not evidence from real employees, real judges, or a real usability study.`

Never write statements such as `34 of 40 employees preferred...`.
Use `34 of 40 simulated reviewers flagged/supported...` instead.

---

# Optional companion skills

If available, combine rather than duplicate:
- `web-ui-ux-evaluator` for product UI/UX and visual audit;
- `session-handoff` for cross-session continuity;
- a video/short-form evaluator for frame/timeline craft;
- security threat-modeling tools for deep security review.

Keep this skill focused on **competition adversarial judgment and enterprise viability**.
