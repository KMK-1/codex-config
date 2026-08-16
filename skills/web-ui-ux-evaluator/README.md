# Web UI/UX Evaluator Skill

웹서비스 UI/UX를 취향이 아니라 **일관된 기준과 증거**로 평가하기 위한 에이전트 스킬입니다.

## 핵심 구성

- Nielsen 계열 휴리스틱 기반 사용성 점검
- WCAG 2.2 AA 기준 접근성 점검
- Visual hierarchy / consistency
- Task effectiveness / information architecture
- Responsive behavior
- Content clarity / trust
- Loading / empty / error / success state
- SUS / HEART는 실제 사용자 데이터가 있을 때만 별도 평가
- S0–S4 Severity + Confidence + Effort 기반 우선순위
- A/B UI 비교 및 release gate 지원
- **Visual Design Audit 모드**: 기능/UX 로직과 분리해 시각 디자인만 100점 루브릭으로 심층 평가

## Visual Design Audit

`visual-only`, `design-only`, `시각 디자인만`, `디자인 완성도`, `visual polish`처럼 요청하면 Visual Design Audit 모드를 사용합니다.

평가 영역:

- Visual hierarchy & composition — 20
- Layout & grid — 15
- Spacing & whitespace — 15
- Typography — 15
- Color & visual contrast — 10
- Component consistency — 10
- Visual density & scanability — 5
- Polish & micro-detail — 5
- Responsive visual quality — 5

Visual Score에는 API, 데이터 정확성, 비즈니스 로직, 실제 task success, SUS/HEART 등을 포함하지 않습니다. 구체적인 기준은 `references/VISUAL_DESIGN_RUBRIC.md`를 사용합니다.

## 폴더 구조

```text
web-ui-ux-evaluator/
├── SKILL.md
├── README.md
├── references/
│   ├── RUBRIC.md
│   ├── VISUAL_DESIGN_RUBRIC.md
│   ├── USER_EVIDENCE.md
│   └── FINDING_TEMPLATE.md
└── examples/
    └── EXAMPLE_REPORT.md
```

## 사용 예시

에이전트에게 다음과 같이 요청합니다.

```text
이 웹앱을 web-ui-ux-evaluator 기준으로 평가해.
핵심 사용자는 사내 품질 담당자이고,
주요 업무는 이슈 확인 → 담당자 지정 → 조치상태 업데이트야.
모바일과 데스크톱을 모두 확인하고 S3 이상부터 우선 정리해줘.
```

시각 디자인만 깊게 평가하려면:

```text
이 웹앱을 web-ui-ux-evaluator의 Visual Design Audit 모드로 평가해.
기능/API/비즈니스 로직은 평가하지 말고,
hierarchy, layout/grid, spacing, typography, color, component consistency,
density, polish, responsive visual quality만 평가해.
Visual Score / 100과 구체적인 수정안을 보여줘.
```

또는:

```text
A 버전과 B 버전을 동일한 task flow로 비교하고
score delta, regression, quick win을 보여줘.
```

## 평가 철학

1. Evidence over taste
2. Critical task first
3. Expert review ≠ user research
4. SUS/HEART 숫자 임의 생성 금지
5. 미검증 상태는 `Not verified`
6. Accessibility 자동검사만으로 WCAG 준수 판정 금지
7. 문제뿐 아니라 유지해야 할 강점도 기록
8. Visual Audit에서는 hierarchy/layout 문제를 decorative polish보다 우선
