# Enterprise Competition Red Team

사내 AI/업무개선 공모전 제출물을 **칭찬보다 탈락 사유 중심으로 공격적으로 검증**하는 Codex/Claude Code용 평가 스킬입니다.

## 핵심

- 40명의 synthetic enterprise reviewer panel
- 공모전 심사위원 / 임원 / 회의적 현업 / AI 전문가 / 보안 / 업무 전문가 / 재무 / Devil's Advocate
- Reject Reason
- Killer Question
- Evidence Demand
- Competitor Attack
- Hidden Risk
- Criticism clustering
- Competition Blocker gate
- 수정 후 동일 패널 재평가
- 마지막 5인 Blind Final Jury

## AI Agent 공모전 특화

`Agent`라는 이름을 그대로 받아들이지 않고 실제로 다음을 검증합니다.

- event/work perception
- persistent task state
- planning/action sequencing
- tool use
- monitoring
- retry/recovery/escalation
- human approval boundary
- auditability

그리고 LLM feature / RAG assistant / deterministic workflow / agent-assisted workflow / genuinely agentic workflow 중 어디에 해당하는지 증거 기반으로 분류합니다.

## 사용 예시

```text
enterprise-competition-redteam으로 이 AI Agent 공모전 제출물을 평가해.
칭찬 위주로 하지 말고 40명의 adversarial reviewer를 사용해서
1등을 주지 않을 이유를 최대한 찾아줘.
반복되는 비판은 clustering하고 Competition Blocker부터 보여줘.
```

숏폼까지 포함:

```text
Agent 구현과 공모전 숏폼을 함께 평가해.
제품이 실제로 증명하는 내용과 영상이 주장하는 내용을 비교하고,
과장되거나 증거가 부족한 부분을 찾아줘.
Killer Question 10개와 발표 답변에 필요한 evidence도 정리해줘.
```

수정 후:

```text
V2를 동일한 40명 panel로 재평가하고 V1 대비 rejection cluster가
얼마나 감소했는지 비교해. 마지막에는 이전 평가를 보지 않은
Blind Final Jury 5명으로 최종 판정해.
```

## 주의

이 스킬의 40명은 실제 직원이나 실제 심사위원이 아닙니다. 결과는 반드시 **synthetic adversarial review**로 표현해야 하며 실제 사용자 조사 결과처럼 주장하면 안 됩니다.
