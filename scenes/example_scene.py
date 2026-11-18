"""Minimal runnable starter scene demonstrating the hybrid visual system + Gemini TTS.

Run from the repository root:
    manim -ql scenes/example_scene.py ExampleStarterScene
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from manim import *

from common import (
    AMBER,
    AXIS,
    CORAL,
    CYAN,
    GRID,
    MUTED,
    TEAL,
    TEXT_WHITE,
    BaseMathScene,
    make_bottom_caption,
    make_card,
    make_scene_header,
    pill_label,
)


class ExampleStarterScene(BaseMathScene):
    """Short ~15 s starter demo showing a parabola and tangent line."""

    def construct(self):
        self.setup_scene()

        header = make_scene_header("Starter Demo", "Hybrid Style + Voiceover Sync", self.sans_font)

        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 5, 1],
            x_length=6.4,
            y_length=4.4,
            axis_config={"color": AXIS, "stroke_width": 2.0},
            tips=False,
        ).move_to(LEFT * 2.2 + DOWN * 0.25)

        curve = axes.plot(lambda x: 0.5 * x**2, x_range=[-2.8, 2.8], color=CYAN, stroke_width=3.5)
        dot = Dot(axes.c2p(1.5, 0.5 * 1.5**2), color=CORAL, radius=0.085).set_z_index(4)
        tangent = axes.plot(lambda x: 1.5 * (x - 1.5) + 0.5 * 1.5**2, x_range=[0.2, 2.8], color=AMBER, stroke_width=2.8)
        pt_lbl = pill_label(MathTex(r"(x_0, f(x_0))", color=CORAL).scale(0.58).next_to(dot, UL, buff=0.14)).set_z_index(5)

        formula = MathTex(r"f(x) = \tfrac{1}{2}x^2, \quad f'(x) = x", color=TEXT_WHITE).scale(0.72)
        formula_card = make_card(formula, pad_x=0.48, pad_y=0.30, stroke_color=TEAL)
        formula_card.to_corner(UR, buff=0.36)

        caption = make_bottom_caption("REPLACE THIS STARTER SCENE WITH YOUR OWN 6 SCENES", self.sans_font, MUTED)

        self.play_beat(
            "demo.1",
            [
                ([FadeIn(header, shift=DOWN * 0.1), FadeIn(formula_card), Create(axes), FadeIn(caption)], 1.6),
                ([Create(curve)], 1.4),
            ],
            post_wait=0.5,
        )

        self.play_beat(
            "demo.2",
            [
                ([FadeIn(dot, scale=1.3), FadeIn(pt_lbl), Create(tangent)], 1.6),
                ([Indicate(formula, color=TEAL, scale_factor=1.08)], 1.0),
            ],
            post_wait=1.0,
        )

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)

