"""Reusable hybrid visual system, Gemini TTS wiring, and paced beat engine
for undergraduate mathematical animations in Manim Community Edition.

Customize the metadata constants and `BEATS` dictionary below for your own topic.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable, Sequence

import manimpango
import numpy as np
from dotenv import load_dotenv
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gemini import GeminiService

# ---------------------------------------------------------------------------
# 1. Customize Your Project Metadata
# ---------------------------------------------------------------------------
PROJECT_TITLE = "YOUR PROJECT TITLE"
PROJECT_SUBTITLE = "Your Focused Mathematical Subtitle"
CONCEPT_TAG = "Concept: Your Chosen M3 Concept"
COURSE_TAG = "M3 — First-Year Undergraduate Mathematics"
STUDENT_NAME = "Your Name"
STUDENT_ID = "Student ID: YOUR_ID"

# ---------------------------------------------------------------------------
# 2. Hybrid Dark Visual Design System
# ---------------------------------------------------------------------------
BG = "#0D1117"            # Deep charcoal/navy canvas
GRID = "#526477"          # Subdued cool blue/grey reference grid
AXIS = "#9AAFC2"          # Reference axes
CYAN = "#53D8FB"          # Primary highlight (e.g., e1 / curve / Row 1)
AMBER = "#FFB84D"         # Secondary highlight (e.g., e2 / tangent / Row 2)
CORAL = "#FF718D"         # Tracked point / focus marker
TEAL = "#55D6BE"          # Transformed layer / key result accent
TEAL_AXIS = "#8AEAD8"     # Transformed axes
TEXT_WHITE = "#F4F7FB"    # Crisp primary text
MUTED = "#A8B6C6"         # Secondary captions & subtitles
PANEL_BG = "#111B27"      # Dark translucent card background
PANEL_STROKE = "#34495E"  # Subtle card border

# ---------------------------------------------------------------------------
# 3. Approved Narration Beats (Replace with your own ~500-560 word script)
# ---------------------------------------------------------------------------
# Keep each beat to 1-3 spoken sentences in natural English (never raw LaTeX).
# Manim Voiceover caches audio by exact text string in media/voiceovers/.
BEATS: dict[str, str] = {
    "demo.1": (
        "Welcome to the M3 Manim Animation Starter Kit. Every visual step stays "
        "cleanly synchronized to your narration without stretching animations unnaturally."
    ),
    "demo.2": (
        "Edit the beats dictionary and scene modules with your own mathematical topic, "
        "verify every equation independently, and render in crisp 1080p."
    ),
}


def select_sans_font() -> str:
    """Pick a clean modern sans-serif installed on the current OS."""
    available = set(manimpango.list_fonts())
    for candidate in ("Avenir Next", "Helvetica Neue", "Inter", "DejaVu Sans", "Arial"):
        if candidate in available:
            return candidate
    return "Sans"


def pill_label(mobj: Mobject, opacity: float = 0.86, buff: float = 0.06) -> Mobject:
    """Add a canvas-matched halo behind a label so grid lines never cut through math text."""
    mobj.add_background_rectangle(color=BG, opacity=opacity, buff=buff)
    return mobj


def make_card(
    content: Mobject,
    pad_x: float = 0.44,
    pad_y: float = 0.30,
    stroke_color: str = PANEL_STROKE,
    fill_opacity: float = 0.96,
) -> VGroup:
    """Wrap any Mobject or VGroup inside a clean bordered dark card."""
    box = RoundedRectangle(
        width=content.width + pad_x,
        height=content.height + pad_y,
        corner_radius=0.14,
        stroke_color=stroke_color,
        stroke_width=1.25,
        fill_color=PANEL_BG,
        fill_opacity=fill_opacity,
    )
    content.move_to(box.get_center())
    return VGroup(box, content)


def make_scene_header(scene_tag: str, scene_title: str, font_name: str) -> VGroup:
    """Consistent upper-left header shared across all scenes."""
    tag = Text(scene_tag.upper(), font_size=13, weight=BOLD, color=TEAL, font=font_name)
    title = Text(scene_title, font_size=24, weight=BOLD, color=TEXT_WHITE, font=font_name)
    header = VGroup(tag, title).arrange(DOWN, aligned_edge=LEFT, buff=0.06)
    header.to_corner(UL, buff=0.34)
    return header


def make_bottom_caption(text: str, font_name: str, color: str = MUTED) -> Text:
    """Consistent bottom guide caption bar."""
    return Text(text.upper(), font_size=14, weight=MEDIUM, color=color, font=font_name).to_edge(
        DOWN, buff=0.28
    )


def make_plane_pair(
    x_range: Sequence[float] = (-2, 2, 1),
    y_range: Sequence[float] = (-2, 2, 1),
    unit_size: float = 0.92,
    center: np.ndarray = DOWN * 0.28,
) -> tuple[NumberPlane, NumberPlane]:
    """Create matching subdued original and bright teal transformed coordinate planes."""
    x_len = (x_range[1] - x_range[0]) * unit_size
    y_len = (y_range[1] - y_range[0]) * unit_size
    kwargs = dict(x_range=x_range, y_range=y_range, x_length=x_len, y_length=y_len)

    original = NumberPlane(
        **kwargs,
        axis_config={"stroke_color": AXIS, "stroke_width": 2.0},
        background_line_style={
            "stroke_color": GRID,
            "stroke_width": 1.3,
            "stroke_opacity": 0.65,
        },
    ).move_to(center)

    transformed = NumberPlane(
        **kwargs,
        axis_config={"stroke_color": TEAL_AXIS, "stroke_width": 2.1},
        background_line_style={
            "stroke_color": TEAL,
            "stroke_width": 1.5,
            "stroke_opacity": 0.72,
        },
    ).move_to(center)

    return original, transformed


def make_opening_title_block(font_name: str) -> VGroup:
    """Standard college-compliant opening title card."""
    course_label = Text(COURSE_TAG, font_size=16, weight=MEDIUM, color=TEAL, font=font_name)
    main_title = Text(PROJECT_TITLE, font_size=46, weight=BOLD, color=TEXT_WHITE, font=font_name)
    subtitle = Text(PROJECT_SUBTITLE, font_size=23, color=MUTED, font=font_name)
    accent_bar = Line(LEFT * 2.4, RIGHT * 2.4, color=TEAL, stroke_width=2.5)
    concept_line = Text(CONCEPT_TAG, font_size=17, color=CYAN, font=font_name)
    student_line = Text(f"{STUDENT_NAME}   •   {STUDENT_ID}", font_size=16, color=MUTED, font=font_name)

    block = VGroup(course_label, main_title, subtitle, accent_bar, concept_line, student_line)
    block.arrange(DOWN, buff=0.25).move_to(ORIGIN)
    return block


class BaseMathScene(VoiceoverScene):
    """Base Manim Voiceover scene pre-configured with Gemini TTS and natural beat pacing."""

    sans_font: str

    def setup_scene(
        self,
        voice: str = "Kore",
        model: str = "gemini-3.1-flash-tts-preview",
        auth_mode: str = "api_key",
    ) -> None:
        project_root = Path(__file__).resolve().parent.parent
        load_dotenv(project_root / ".env")
        load_dotenv()
        if auth_mode == "api_key" and not os.getenv("GEMINI_API_KEY") and not os.getenv("GOOGLE_API_KEY"):
            raise RuntimeError(
                "Gemini API key not found. Copy .env.example to .env and set GEMINI_API_KEY locally; "
                "never hardcode credentials in Python files or commit .env."
            )

        self.sans_font = select_sans_font()
        self.camera.background_color = BG
        self.set_speech_service(
            GeminiService(
                model=model,
                voice=voice,
                auth_mode=auth_mode,
            )
        )

    def play_beat(
        self,
        beat_id: str,
        steps: Sequence[tuple[Iterable[Animation] | None, float]],
        post_wait: float = 0.0,
    ) -> float:
        """Speak `BEATS[beat_id]` and play animation steps at natural speed inside its duration.

        - Steps are NOT stretched across long narration; instead, animations complete naturally
          and hold calmly for the remainder of the spoken beat.
        - If total desired step durations exceed 92% of the spoken beat, they scale smoothly
          so visuals always finish cleanly before speech moves on.
        """
        spoken_text = BEATS[beat_id]
        with self.voiceover(text=spoken_text) as tracker:
            total_desired = sum(dur for _, dur in steps)
            budget = max(0.5, tracker.duration * 0.92)
            scale = min(1.0, budget / total_desired) if total_desired > 0 else 1.0

            elapsed = 0.0
            for anims, desired in steps:
                dur = max(0.15, desired * scale)
                if anims:
                    self.play(*anims, run_time=dur, rate_func=smooth)
                else:
                    self.wait(dur)
                elapsed += dur

            remaining = max(0.0, tracker.duration - elapsed)
            if remaining > 0.04:
                self.wait(remaining)

            duration = tracker.duration

        if post_wait > 0.0:
            self.wait(post_wait)

        return duration

