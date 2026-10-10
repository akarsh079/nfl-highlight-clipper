# CLAUDE.md

## Project

Automatic NFL highlight clipper. Extracts audio from game video with FFmpeg, detects
crowd-noise spikes with librosa/NumPy, and cuts the detected moments into a highlight reel.
Planned additions: Whisper commentary analysis (faster-whisper) and OpenCV scoreboard
detection. Targets Python 3.11.

## Layout

```
run.py                        CLI entry point
src/nfl_highlight_clipper/
  extract.py                  FFmpeg audio/frame extraction
  audio.py                    crowd-noise spike detection
  commentary.py               Whisper transcription and scoring
  vision.py                   OpenCV scoreboard detection
  fuse.py                     combine signals into highlight candidates
  edit.py                     cut clips and assemble the reel
tests/                        pytest tests
eval/labels.csv               hand-labeled highlights (timestamp_sec,play_type,notes)
data/                         local video/audio files (gitignored)
```

## Commands

```bash
source .venv/bin/activate
pytest                        # run tests
ruff check .                  # lint
ruff format .                 # format
```

## Rules

- Never commit anything in `data/`.
- Keep functions small and testable.
- The audio module must not depend on FFmpeg or video files.
- Do not add new dependencies without asking.
