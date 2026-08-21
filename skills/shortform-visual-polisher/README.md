# Shortform Visual Polisher

이미 완성된 숏폼 영상의 **내용은 고정하고 시각적 연출만 개선**하기 위한 Codex / Claude Code용 스킬입니다.

## 기본 LOCK
- 러닝타임/타임라인
- 스토리와 장면 순서
- 내레이션/음성
- 자막 문구와 타이밍
- 사실/수치/주장
- 핵심 UI/demo 내용

## 수정 가능 영역
Transition, zoom/pan, crop, UI spotlight, cursor/click emphasis, blur/dim, overlays, masks/reveals, depth/shadow, subtle glow, KPI emphasis, before/after treatment, motion graphics 등.

핵심 원칙은 하나입니다:

> **Every effect must Explain, Focus, or Transition. Otherwise remove it.**

## 사용 예시

```text
shortform-visual-polisher를 사용해서 이 90초 공모전 영상을 분석해.
자막 문구/타이밍, 내레이션, 장면 순서, 러닝타임은 절대 바꾸지 말고
시각적 이펙트만 Clean / Minimal / Premium Enterprise Tech 스타일로 개선해.
먼저 초 단위 Visual Treatment Plan을 만들고 그 뒤 구현해.
```

더 보수적으로:

```text
기존 영상의 좋은 부분을 최대한 보존해.
새 효과를 넣기 전에 Remove-before-add 원칙을 적용하고,
각 효과를 EXPLAIN / FOCUS / TRANSITION 중 하나로 정당화할 수 없으면 넣지 마.
```

## 평가
`references/VISUAL_TREATMENT_RUBRIC.md`의 100점 루브릭으로 수정 전/후를 비교할 수 있습니다.
