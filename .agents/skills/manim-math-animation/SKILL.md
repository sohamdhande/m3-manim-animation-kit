---
name: manim-math-animation
description: Plans and builds clean, mathematically faithful Manim Community Edition animations with a high-contrast dark hybrid visual style and frame-safe layout.
---

# Manim Mathematical Animation Skill

## Hybrid Visual System

- Deep charcoal/navy canvas (`#0D1117`), crisp white text (`#F4F7FB`), subdued reference grid (`#526477`), bright teal active/transformed layer (`#55D6BE`), cyan primary highlight (`#53D8FB`), amber secondary highlight (`#FFB84D`), coral tracked point/element (`#FF718D`).
- Keep visual helpers modular in `scenes/common.py` (`BaseMathScene`, `play_beat`, `pill_label`, `make_card`, `make_scene_header`, `make_plane_pair`).

## Manim Community Guardrails

- Never mix ManimGL APIs with Manim Community Edition (`manim>=0.19.0`).
- `ApplyMatrix(matrix, mobject, about_point=ORIGIN)` accepts only ONE mobject — never pass a second mobject as the 3rd positional argument, and never shear a `Dot` or label with `ApplyMatrix` (use `.animate.move_to(...)` instead).
- Avoid calling `Indicate` on a filled `RoundedRectangle` card (it temporarily tints the entire fill); call `Indicate` on the text/formula submobject inside the card instead.
- Always wrap labels over coordinate grids with `pill_label(...)` so grid lines never cut through equations.
- Visually inspect extracted keyframes after every scene render before moving on.

