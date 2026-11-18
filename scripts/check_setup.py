"""One-command environment doctor for M3 Manim + Gemini Voiceover projects.

Run from the repository root:
    python scripts/check_setup.py

Never prints API keys or credentials.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path


def _check_bin(name: str, extra_paths: tuple[str, ...] = ("/Library/TeX/texbin",)) -> tuple[bool, str]:
    found = shutil.which(name)
    if not found:
        for ep in extra_paths:
            cand = Path(ep) / name
            if cand.exists():
                found = str(cand)
                break
    if not found:
        return False, "NOT FOUND"
    try:
        out = subprocess.check_output([found, "--version"], stderr=subprocess.STDOUT, text=True)
        first_line = out.strip().splitlines()[0] if out.strip() else found
        return True, f"{found} ({first_line})"
    except Exception:
        return True, found


def main() -> int:
    print("=== M3 Manim Animation Kit — Environment Check ===\n")
    ok_all = True

    py_ok = sys.version_info >= (3, 11)
    print(f"[{'PASS' if py_ok else 'FAIL'}] Python        : {sys.version.split()[0]} (need 3.11+)")
    ok_all &= py_ok

    for pkg, import_name in [
        ("manim", "manim"),
        ("manim-voiceover", "manim_voiceover"),
        ("GeminiService", "manim_voiceover.services.gemini"),
        ("python-dotenv", "dotenv"),
        ("numpy", "numpy"),
    ]:
        try:
            mod = __import__(import_name, fromlist=["__version__"])
            ver = getattr(mod, "__version__", "imported")
            print(f"[PASS] {pkg:14s}: {ver}")
        except Exception as exc:
            print(f"[FAIL] {pkg:14s}: {type(exc).__name__}: {exc}")
            ok_all = False

    for tool in ("ffmpeg", "ffprobe", "sox", "pdflatex", "dvisvgm"):
        ok, info = _check_bin(tool)
        print(f"[{'PASS' if ok else 'WARN'}] {tool:14s}: {info}")
        if tool in ("ffmpeg", "ffprobe", "sox"):
            ok_all &= ok

    env_path = Path(".env")
    if env_path.exists():
        try:
            from dotenv import load_dotenv

            load_dotenv(env_path)
        except Exception:
            pass
    has_key = bool(os.getenv("GEMINI_API_KEY", "").strip() or os.getenv("GOOGLE_API_KEY", "").strip())
    print(f"[{'PASS' if has_key else 'WARN'}] GEMINI_API_KEY: {'SET (hidden)' if has_key else 'NOT SET (copy .env.example to .env)'}")

    print("\nResult:", "READY FOR PRODUCTION!" if ok_all and has_key else "ACTION NEEDED (see FAIL/WARN items above)")
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())

