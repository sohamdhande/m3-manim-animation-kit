# M3 Manim Animation Starter Kit

An open-source, reusable production kit for creating clean, mathematically rigorous **5-minute educational animations** using **Manim Community Edition**, **Gemini Text-to-Speech (Manim Voiceover 0.4.0+)**, **LaTeX (`MathTex` + Storyboard PDF)**, and **Google Antigravity** workspace skills.

Originally created by **Soham Dhande** while building a first-year undergraduate Mathematics (M3) animation project, generalized into a clean MIT-licensed starter template so any student can build an **original** video on *any* Linear Algebra, Calculus, or Optimization topic.

---

## What's Included

- **Hybrid Visual System (`scenes/common.py`)** — Deep charcoal/navy canvas (`#0D1117`), restrained cyan/amber/teal/coral color semantics, `pill_label()` dark halos so grid lines never cut through equations, reusable card & header builders, and a paced `play_beat()` voiceover engine that never stretches animations unnaturally.
- **Starter Scene & Video Assembler (`scenes/`)** — A short runnable `example_scene.py` plus `assemble_video.py` (FFmpeg `filter_complex` concat + cumulative `.srt` subtitle merger).
- **Five Reusable Antigravity Skills (`.agents/skills/`)** — Storyboarding, Gemini Voiceover, Manim Math Animation, Independent Mathematical Integrity Review, and Video Review/Export QA.
- **One-Command Environment Doctor (`scripts/check_setup.py`)** — Checks Python 3.11+, Manim, Manim Voiceover, FFmpeg, SoX, LaTeX (`pdflatex`, `dvisvgm`), and `.env` without printing any secrets.
- **Publication-Grade Storyboard & Docs Templates (`storyboard/`, `docs/`)** — 2-page LaTeX storyboard PDF template, project brief template, math verification oracle template, AI disclosure & credits templates, and copy-paste Antigravity prompts (`docs/PROMPTS.md`).

---

## Quick Start

### 1. Clone & Create a Python 3.11 Virtual Environment

> **Tip:** Use **Python 3.11 or 3.12** rather than brand-new Python 3.14, so scientific wheels (`numpy`, `scipy`, `manimpango`) install cleanly.

```bash
git clone https://github.com/sohamdhande/m3-manim-animation-kit.git
cd m3-manim-animation-kit

python3.11 -m venv .venv
source .venv/bin/activate          # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Install System Dependencies

#### macOS (Homebrew)
```bash
brew install python@3.11 cairo pango pkg-config ffmpeg sox
brew install --cask basictex
eval "$(/usr/libexec/path_helper)"

# Required LaTeX packages for Manim MathTex & storyboard PDF
sudo /Library/TeX/texbin/tlmgr update --self
sudo /Library/TeX/texbin/tlmgr install standalone preview dvisvgm doublestroke relsize physics rsfs wasysym
```

#### Ubuntu / Debian Linux
```bash
sudo apt update
sudo apt install -y python3.11 python3.11-venv libcairo2-dev libpango1.0-dev pkg-config ffmpeg sox texlive texlive-latex-extra dvisvgm
```

#### Windows
- Install **Python 3.11**, **FFmpeg**, **SoX**, and **MiKTeX** (enable auto-install missing packages), ensuring `ffmpeg`, `sox`, `pdflatex`, and `dvisvgm` are on your `PATH`.

### 3. Configure Your Local Gemini API Key (Never Commit `.env`)

```bash
cp .env.example .env
```
Open `.env` and add your key from [Google AI Studio](https://aistudio.google.com/):
```env
GEMINI_API_KEY=your_api_key_here
```
*(The `.env` file is already listed in `.gitignore`.)*

### 4. Run the Environment Doctor

```bash
export PATH="/Library/TeX/texbin:$PATH"   # macOS BasicTeX PATH
python scripts/check_setup.py
```

### 5. Test the Starter Scene

```bash
manim -ql scenes/example_scene.py ExampleStarterScene
```

---

## Building Your Own Original 5-Minute Video

1. Copy `docs/PROJECT_BRIEF_TEMPLATE.md` → `docs/PROJECT_BRIEF.md` and `docs/MATH_CHECK_TEMPLATE.md` → `docs/MATH_CHECK.md`, and fill in **your own chosen M3 topic**.
2. Open this folder as your workspace in **Google Antigravity** (it automatically discovers `AGENTS.md` and all five skills in `.agents/skills/`).
3. Follow the staged prompts in [docs/PROMPTS.md](docs/PROMPTS.md):
   - **Phase 0:** Pre-production & math verification
   - **Phase 1:** 500–560 word 6-scene script & independent math audit
   - **Phase 2:** 20–35 s Visual Proof of Concept
   - **Phase 3:** Six modular scenes (`scene_01`–`scene_06`) rendered & visually inspected at 720p30
   - **Phase 4:** Final `1920×1080, 30 fps` render + 2-page Storyboard PDF + clean submission folder
4. Assemble all six scenes into one final MP4:
   ```bash
   python scenes/assemble_video.py --quality 1080p30 --output output/Final_Video.mp4
   ```
5. Compile your storyboard PDF:
   ```bash
   cd storyboard && pdflatex storyboard_template.tex && pdflatex storyboard_template.tex
   ```

---

## Real-World Tips & Troubleshooting

- **Gemini Free-Tier Daily TTS Limit (10 requests/day):**  
  `gemini-3.1-flash-tts-preview` on Free Tier typically allows **10 requests per day**. **Finalize and approve your exact wording before rendering** — Manim Voiceover caches every `.wav` clip by exact text hash in `media/voiceovers/`, so once cached, re-rendering at 480p, 720p, and 1080p uses **zero API calls**.
- **`pycairo` fails to build on macOS:** Install `pkg-config` (`brew install pkg-config`) so Meson finds Homebrew Cairo.
- **`SoX could not be found` warning:** Install the `sox` CLI (`brew install sox`).
- **`MathTex` fails with missing `dvisvgm` or `standalone.sty`:** Run the `sudo tlmgr install ...` command in Step 2 above.
- **GitHub rejects push with `GH007` (private email):** Set your local git author email to your GitHub noreply address (`<id>+<username>@users.noreply.github.com`).
- **Large MP4 push times out (`HTTP 408`):** Run `git -c http.postBuffer=524288000 push origin main`.

---

## Academic Integrity Note

This template provides reusable **code infrastructure, visual styling, and workflow prompts** — not a pre-built solution to submit verbatim. Choose your own mathematical concept, independently verify every derivation, disclose all AI tools accurately, and make sure you can explain every line of math and code in your viva.

---

## License

Released under the [MIT License](LICENSE) © 2026 Soham Dhande.

