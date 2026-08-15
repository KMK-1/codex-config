# Methodology Sources

This skill intentionally separates established frameworks from the skill author's scoring synthesis.

## Primary / authoritative references

### Web Content Accessibility Guidelines (WCAG) 2.2
- Organization: W3C Web Accessibility Initiative (WAI)
- Role in this skill: accessibility reference target
- Official specification: https://www.w3.org/TR/WCAG22/

### 10 Usability Heuristics for User Interface Design
- Organization: Nielsen Norman Group
- Origin: Jakob Nielsen's heuristic evaluation work
- Role in this skill: expert usability inspection principles
- Reference: https://www.nngroup.com/articles/ten-usability-heuristics/

### HEART framework
- Authors: Kerry Rodden, Hilary Hutchinson, Xin Fu
- Paper: *Measuring the User Experience on a Large Scale: User-Centered Metrics for Web Applications*
- Venue: CHI 2010
- Role in this skill: Goal → Signal → Metric product UX measurement
- DOI: https://doi.org/10.1145/1753326.1753687

### System Usability Scale (SUS)
- Author: John Brooke
- Work: *SUS: A “Quick and Dirty” Usability Scale* (1996)
- Role in this skill: standardized perceived-usability questionnaire and scoring method

### ISO 9241-11:2018
- Standard: *Ergonomics of human-system interaction — Part 11: Usability: Definitions and concepts*
- Role in this skill: conceptual grounding for effectiveness, efficiency, and satisfaction in context of use
- Reference: https://www.iso.org/standard/63500.html

## Supporting implementation tools (optional)

### axe-core
- Maintainer: Deque Systems
- Role: automated accessibility rule checking; supplemental evidence only
- Repository: https://github.com/dequelabs/axe-core

### Lighthouse
- Maintainer: Google Chrome team
- Role: supplemental automated audits; not a replacement for manual UX/accessibility evaluation
- Documentation: https://developer.chrome.com/docs/lighthouse/

## Important methodology note

The **100-point weighting, S0–S4 finding severity table, release gate, and combined report format in this repository are a practical synthesis created for this skill**. They are not themselves official Nielsen, W3C, Google, SUS, or ISO scoring systems.

This distinction should remain visible in reports so that users do not mistake a custom composite score for a standardized certification score.
