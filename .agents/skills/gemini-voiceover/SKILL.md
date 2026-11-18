---
name: gemini-voiceover
description: Configures, generates, caches, and synchronizes clear educational English narration with Manim Community using Manim Voiceover 0.4.0+ and Gemini TTS.
---

# Gemini Voiceover Skill

## Setup & Configuration

Use `manim-voiceover[gemini]>=0.4.0`:
```python
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gemini import GeminiService

self.set_speech_service(
    GeminiService(
        model="gemini-3.1-flash-tts-preview",
        voice="Kore",
        auth_mode="api_key",
    )
)
```
Load `GEMINI_API_KEY` from local `.env` via `python-dotenv` (never commit `.env` or print keys).

## Quota & Cache Hygiene

- Gemini Free Tier caps TTS requests per model/day (typically 10/day).
- Split narration into short semantic beats and **approve the exact text before synthesizing**.
- Manim Voiceover hashes `(text, voice, model)` in `media/voiceovers/` — changing even one comma triggers a new API call, whereas unchanged text reuses cached `.wav` files across 480p, 720p, and 1080p renders at zero API cost.
- If quota or authentication fails, stop and report the exact error rather than silently switching TTS providers.

## Spoken Authoring Rules

- Write natural spoken English; never feed raw LaTeX or subscripts (`e_1`, `\det(A)`) to TTS — write *"e one"*, *"the determinant of A"*, *"two x plus y"*.
- Audition one short phrase containing your lesson's hardest mathematical terms before synthesizing full scenes.
- Keep pronunciation notes separated from the spoken beat strings.

