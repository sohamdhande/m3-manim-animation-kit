# Copy-Paste Antigravity Workflow Prompts

After filling out `docs/PROJECT_BRIEF.md` and `docs/MATH_CHECK.md` for **your own chosen topic**, open this folder in Google Antigravity and run these phases one by one. Wait for each phase's review gate before moving to the next.

---

## Phase 0 — Pre-Production & Environment Check

```text
Read AGENTS.md, docs/PROJECT_BRIEF.md, docs/MATH_CHECK.md, and all five skills under .agents/skills/.
Do pre-production only — do NOT write animation code or generate audio yet.
1. Confirm you detect all five workspace skills.
2. Summarize my chosen concept, learning objective, and six-scene plan (~5:00 target, max 7:00).
3. Independently recalculate and verify every equation and example in docs/MATH_CHECK.md.
4. Run `python scripts/check_setup.py` and report any missing dependencies or LaTeX tools.
Stop after the readiness report.
```

---

## Phase 1 — Six-Scene Narration Script & Independent Math Review

```text
Draft the complete six-scene spoken narration (~500-560 words total, split into 15-22 short semantic beats)
in docs/SCRIPT_NARRATION.md, tailored to my topic in docs/PROJECT_BRIEF.md.
Also create docs/MATH_REVIEW.md with a claim-by-claim independent mathematical verification table
(PASS / CORRECTION REQUIRED / CLARIFICATION REQUIRED) against docs/MATH_CHECK.md.
Do NOT generate audio or animation code yet. Stop and wait for my approval of the script.
```

---

## Phase 2 — Visual Proof of Concept (20–35 s)

```text
The narration script is approved. Build ONLY a short 20-35 second Visual Proof of Concept scene
in scenes/visual_poc.py using scenes/common.py and 2-3 excerpts from my approved script.
Render at 720p30 (-qm), inspect keyframes for overlapping labels or clipping, verify with FFprobe,
and stop for my review before building all six scenes.
```

---

## Phase 3 — Modular 6-Scene Build & 720p Review Video

```text
Visual Proof of Concept approved. Build all six modular scenes (scene_01 through scene_06)
preserving my exact approved narration in scenes/common.py.
Render each scene individually at 720p30, extract and visually inspect keyframes after every scene,
verify FFprobe duration and audio levels, and assemble a complete 720p review video via
scenes/assemble_video.py. Stop before 1080p final export so I can watch the full review video.
```

---

## Phase 4 — Final 1080p30 Export & Clean College Submission Folder

```text
Full 720p review video approved. My official Student ID is [YOUR_ID].
1. Update STUDENT_NAME and STUDENT_ID in scenes/common.py (opening title + closing credits).
2. Re-render all six scenes at 1920x1080, 30 fps reusing all cached narration clips (zero extra API calls).
3. Assemble final MP4 (~4:55-5:05, strictly < 7:00) and verify with FFprobe + keyframe inspection.
4. Compile my filled-out storyboard/storyboard.tex to Storyboard.pdf via pdflatex.
5. Package ONLY the required submission deliverables into a clean folder named
   M3_AnimationVideo_<Concept>_<YOUR_ID>/ (MP4, Storyboard.pdf, standalone runnable Code/,
   and Supporting_Documents/AI_Disclosure.md + References_and_Credits.md) — NO .env, .venv, caches, or logs.
Stop and show me the audit before pushing to GitHub.
```

