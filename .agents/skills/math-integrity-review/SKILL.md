---
name: math-integrity-review
description: Independently recalculates and verifies every mathematical definition, equation, derivation, numerical example, and geometric interpretation before animation rendering.
---

# Mathematics Integrity Review Skill

## Verification Standard

Never trust generated prose, captions, or LaTeX merely because it compiles. Independently recalculate every mathematical step against `docs/MATH_CHECK.md`:

1. Verify every definition, domain/codomain, dimension, sign, and notation convention.
2. Independently compute every algebraic expansion, matrix product, derivative, integral, eigenvalue, or geometric area/volume.
3. Check boundary conditions and assumptions (e.g., nonzero determinant for invertibility, differentiability assumptions, absolute value for area scaling).
4. Ensure narration, on-screen equations, storyboard PDF, and worked code agree 100%.

## Review Table Format

Record every claim in `docs/MATH_REVIEW.md` using outcomes `PASS`, `CORRECTION REQUIRED`, or `CLARIFICATION REQUIRED`. Resolve every non-`PASS` item before rendering video.

