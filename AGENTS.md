# Project-Wide Instructions for Antigravity

You are assisting an undergraduate student in building an original, mathematically rigorous ~5-minute educational animation video using **Manim Community Edition** and **Gemini Text-to-Speech (Manim Voiceover 0.4.0+)**.

## Workflow Phases (Always Respect Approval Gates)

Work in small, verifiable stages — do not jump straight to final 1080p rendering:
1. **Pre-production & Setup** — Read `docs/PROJECT_BRIEF.md` and `docs/MATH_CHECK.md`, verify local toolchain (`python scripts/check_setup.py`), confirm scope.
2. **Script & Math Review** — Draft a 500–560 word six-scene narration split into short semantic beats (~15–22 beats) and independently verify every mathematical claim before animating.
3. **Visual Proof of Concept** — Render one short 20–35 s narrated preview (`-qm`), visually inspect keyframes, and get student approval on styling and pacing.
4. **Scene-by-Scene 720p Production** — Build six modular scenes (`scene_01` through `scene_06`), render each at 720p30, inspect keyframes and FFprobe output for every scene, then assemble a full 720p review video.
5. **Final 1080p Export & Clean Submission Package** — Render at `1920×1080, 30 fps`, target ~4:55–5:05 (strict maximum 7:00), reuse all cached audio clips, compile the 6-scene storyboard PDF, and assemble a clean submission folder.

## Visual Direction (Hybrid System)

- **Canvas:** Deep charcoal/navy (`#0D1117`) with crisp white text (`#F4F7FB`).
- **Color semantics:** Keep colors consistent across all six scenes (subdued grid `#526477`, transformed/active accent teal `#55D6BE`, primary highlight cyan `#53D8FB`, secondary highlight amber `#FFB84D`, tracked element coral `#FF718D`).
- **Anti-overlap hygiene:** Place dark canvas backing pills (`pill_label`) behind labels over grids and inspect rendered keyframes after every scene.
- **Purposeful motion:** Animate one mathematical idea at a time; never stretch animations unnaturally to fill narration time; include calm pauses after key results.

## Mathematical & Narration Integrity

- Independently verify every definition, equation, intermediate calculation, sign, dimension, and geometric interpretation against `docs/MATH_CHECK.md`.
- Define all notation before using it. Never skip intermediate steps in the worked example.
- Write spoken narration in natural university-tutor English — never feed raw LaTeX symbols to TTS.
- Keep narration as short semantic beats (`play_beat`) so cached `.wav` clips in `media/voiceovers/` are reused across re-renders without burning Gemini API quota.
- Never hardcode, print, or commit `.env` or API keys.

## Student Ownership & Viva

Keep every scene modular and clearly commented so the student understands and can independently defend every mathematical derivation, visual choice, and Python/Manim component during their viva.

