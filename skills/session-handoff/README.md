# Session Handoff

Codex와 Claude Code 등 서로 다른 코딩 에이전트/세션 사이에서 작업 상태를 이어가기 위한 공용 handoff 스킬입니다.

softaworks `session-handoff`의 CREATE/RESUME, 검증, handoff chaining 아이디어를 기반으로 하되 저장 위치와 문서 형식을 특정 에이전트에 종속되지 않게 조정했습니다.

## 핵심 기능

- CREATE: 현재 작업 상태를 구조화된 Markdown으로 저장
- RESUME: 최신 handoff를 읽고 실제 Git 상태와 대조 후 작업 재개
- Codex ↔ Claude Code 교차 사용
- Decisions / Changed Files / Tests / Failed Attempts / Blockers / Exact Next Steps 기록
- 이전 handoff와 chain 연결
- credential/secret 기본 검증
- transcript 전체 복사 대신 repository reference 중심 context 압축

## 프로젝트 내 저장 위치

```text
.agent-handoffs/
└── YYYY-MM-DD-HHMMSS-task-name.md
```

`.agent-handoffs/`를 Git에 커밋할지는 프로젝트 성격에 따라 결정하세요. 민감한 내부 작업이라면 저장소 정책을 먼저 확인합니다.

## 사용 예

```text
create a handoff for this session
```

```text
현재 작업을 handoff로 저장해. 다음 세션은 Claude Code에서 이어갈 거야.
```

```text
latest handoff를 읽고 이어서 작업해.
```

```text
Codex가 남긴 handoff에서 Claude Code로 이어서 작업해.
```

## 구조

```text
session-handoff/
├── SKILL.md
├── README.md
├── references/
│   ├── HANDOFF_TEMPLATE.md
│   └── RESUME_CHECKLIST.md
└── scripts/
    └── validate_handoff.py
```

## 원칙

1. Handoff는 transcript dump가 아니라 operational state다.
2. 현재 repository가 handoff보다 우선하는 source of truth다.
3. 중요한 실패 시도를 기록해 다음 agent가 반복하지 않게 한다.
4. secret 값은 handoff에 기록하지 않는다.
5. Git 변경 작업은 handoff 생성 권한과 별개다.
