---
name: brainstorming
description: Brainstorm ideas when the user wants to explore possibilities, generate alternatives, reframe a problem, discover unconventional approaches, or compare promising concepts before implementation.
---

# Brainstorming

Use this skill to turn a fuzzy problem into a set of differentiated, pressure-tested ideas. The goal is not idea volume by itself. The goal is to uncover useful directions that would not appear from the first obvious pass.

## Core loop

Run this sequence unless the user explicitly asks for a lighter session:

1. **Frame** — state the actual problem, desired outcome, constraints, and important unknowns.
2. **Reframe** — produce at least 3 materially different ways to view the problem.
3. **Diverge** — generate ideas across multiple thinking modes rather than one theme.
4. **Cross-pollinate** — import patterns from other industries, workflows, products, or disciplines.
5. **Attack** — identify why the strongest ideas could fail, be ignored, or be too expensive.
6. **Combine** — merge complementary ideas into stronger concepts.
7. **Evaluate** — compare the surviving concepts against explicit criteria.
8. **Re-explore** — if the survivors are obvious, repetitive, or weak, change the framing and run another divergence pass.
9. **Synthesize** — present the strongest options, why they matter, and the next experiment or decision for each.

Do not jump to ranking until the divergent pass is complete.

## 1. Frame

Extract or infer:

- target user or stakeholder
- job to be done
- desired outcome
- constraints
- current workaround or baseline
- what would make the idea meaningfully better than the obvious solution

When context is sufficient, continue without interrogating the user. State important assumptions briefly.

A useful problem statement is:

> How might we help **[user]** achieve **[outcome]** despite **[constraint]**, in a way that is meaningfully better than **[baseline]**?

## 2. Reframe

Create at least 3 distinct frames. Prefer frames that change what success means, who owns the problem, or where the intervention occurs.

Useful lenses:

- eliminate the task instead of improving it
- move work earlier or later in the workflow
- change the primary user
- convert a manual decision into a system decision
- turn a reactive process into a predictive one
- make the hidden state visible
- remove a coordination handoff
- invert the constraint
- ask what would make the problem disappear entirely

Treat each reframe as a separate search space.

## 3. Diverge

Generate ideas from several modes. Do not produce twenty cosmetic variants of the same concept.

Use at least 4 of these modes for a full session:

### SCAMPER

- Substitute
- Combine
- Adapt
- Modify or magnify
- Put to another use
- Eliminate
- Reverse or rearrange

### Inversion

Ask:

- How would we make this problem worse?
- What assumption would we remove if the opposite were true?
- What if the user did nothing?
- What if the system had to solve this before the user noticed it?

Reverse useful answers into candidate solutions.

### Constraint mutation

Change one constraint at a time:

- near-zero budget
- near-zero user effort
- ten times the scale
- one tenth the time
- no new UI
- no manual data entry
- privacy-first / offline-first
- must work with existing tools only

A changed constraint should force a different architecture or workflow, not merely different wording.

### Analogy

Ask how the same structural problem is handled in domains such as:

- aviation
- healthcare
- logistics
- finance
- gaming
- manufacturing
- emergency response
- marketplaces
- cybersecurity
- social products

Transfer the mechanism, not the surface appearance.

### Actor shift

Generate ideas from the viewpoint of:

- end user
- manager
- operator
- customer
- regulator
- support team
- system administrator
- AI agent
- external partner

### Time shift

Explore interventions:

- before the problem occurs
- at detection
- during resolution
- after resolution
- across repeated occurrences

## 4. Cross-pollinate

For the most promising search spaces, explicitly borrow 2–5 mechanisms from unrelated domains.

Use this form:

**Mechanism from X → applied to Y → resulting idea**

Example:

> Air-traffic conflict detection → project workload → predict task collisions before deadlines rather than alerting only after a task is late.

If web or repository research is available and the user wants evidence-backed ideation, research current examples before completing this step.

## 5. Attack

Act as a skeptical critic for the strongest ideas.

For each candidate ask:

- Why would users ignore it?
- Which assumption is most fragile?
- What data or dependency does it require?
- Where does it add work instead of remove work?
- What makes it hard to trust?
- How could it fail at scale?
- Could a simpler feature produce 80% of the value?
- Is this actually differentiated, or just AI added to an existing workflow?

A criticism should either kill the idea or identify a concrete redesign.

## 6. Combine

Look for complementary pairs:

- insight + action
- detection + prevention
- automation + human control
- personalization + shared workflow
- prediction + explanation
- private workspace + team visibility
- fast heuristic + deep analysis

Create hybrids only when the combination removes a weakness or produces a new capability. Do not combine ideas merely to make them larger.

## 7. Evaluate

Choose criteria that fit the problem. Default criteria:

- user value
- originality / differentiation
- feasibility
- implementation effort
- time to validate
- adoption friction
- defensibility or strategic leverage

Use a 1–5 score only when comparison benefits from it. Scores must include a short reason; unsupported numbers are noise.

Prefer a portfolio over one winner when appropriate:

- **Quick win** — valuable and easy to test
- **Core bet** — strongest balance of value and feasibility
- **Bold bet** — higher uncertainty with potentially outsized value

## 8. Re-explore gate

Before finishing, inspect the survivors.

Run another divergence pass when two or more of these are true:

- the ideas could have been produced from the original prompt in one obvious pass
- several ideas share the same mechanism
- the best concept is mostly a feature list
- every idea depends on the same assumption
- no concept changes the workflow or decision model
- there is no credible bold bet

For the second pass, change the problem frame or constraint. Do not simply ask for more ideas.

## 9. Synthesize

For each final concept provide:

- **Concept** — one-line description
- **Why it matters** — the user or business value
- **Mechanism** — what makes it work
- **Differentiator** — why it is not the obvious solution
- **Main risk** — the assumption most likely to break
- **Next test** — the cheapest experiment that would reduce uncertainty

End with a clear recommendation or a small portfolio of options when the evidence does not justify one winner.

## Session modes

### Quick brainstorm

Use when the user wants fast ideation.

- 2 reframes
- 8–12 ideas
- one attack pass
- top 3 synthesis

### Deep brainstorm

Use for product strategy, competitions, difficult workflow problems, or consequential design work.

- 3–5 reframes
- 20+ raw ideas across multiple modes
- cross-domain analogies
- attack and combination passes
- evaluation matrix
- re-explore gate
- top portfolio with experiments

### Improve an existing idea

When the user already has a concept, do not restart from zero.

1. identify the concept's core mechanism
2. expose assumptions and weak points
3. generate alternatives for the weakest parts
4. import mechanisms from other domains
5. create 3 materially different upgraded versions
6. compare them with the original

## Output discipline

Keep raw divergence broader than the final answer. Compress duplicates before presenting results.

Prefer concepts that alter one of these:

- who acts
- when action happens
- what information is visible
- what decision is automated
- how coordination occurs
- where trust is created
- what work disappears

A brainstorm is complete when the user has genuinely different directions, the strongest ones survived criticism, and each finalist has a concrete way to test it.
