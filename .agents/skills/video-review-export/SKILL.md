---
name: video-review-export
description: Audits rendered Manim educational videos for visual clarity, FFprobe technical specs, audio loudness, synchronization, credits, and clean public GitHub packaging.
---

# Video Review & Export Skill

## Quality Gate Sequence

1. Render modular scenes individually at `720p30` (`-qm`), extract keyframes, and inspect visually for label collisions, clipping, or math typos.
2. Assemble a full `720p30` review video via `scenes/assemble_video.py` and confirm pacing and total runtime before rendering `1080p30` (`-r 1920,1080 --fps 30`).
3. Audit final MP4 with `ffprobe` and `ffmpeg -af volumedetect`:
   - `1920×1080`, `16:9`, `30 fps`, `h264` + `aac 48kHz stereo`
   - Total duration close to 5:00 and strictly below 7:00
   - Audible narration (`mean` around `-18` to `-22 dB`, `max < -1 dB`, zero clipping)
   - Opening frame (Title, Concept, Student Name & ID) and Closing frame (Summary, References, Music Credit, AI Disclosure)
4. Before publishing to GitHub, scan for `.env`, API keys, `.venv`, media caches, and unresolved placeholders, then verify public unauthenticated access (`HTTP 200`).

