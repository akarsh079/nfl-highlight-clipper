# NFL Highlight Clipper

Automatically finds the big moments in an NFL game video and cuts them into a highlight reel.

Pipeline (in progress):

1. **Extract** – pull audio from the video with FFmpeg.
2. **Audio** – detect crowd-noise spikes with librosa/NumPy.
3. **Commentary** – transcribe the broadcast with faster-whisper (planned).
4. **Vision** – detect scoreboard changes with OpenCV (planned).
5. **Fuse** – combine signals into ranked highlight candidates.
6. **Edit** – cut the clips and assemble the reel.

## Setup

Requires Python 3.11 and FFmpeg.

```bash
brew install python@3.11 ffmpeg

python3.11 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install
```

## Usage

Put game videos in `data/` (gitignored), then:

```bash
python run.py data/game.mp4 --out highlights.mp4
```

## Development

```bash
pytest                # run tests
ruff check .          # lint
ruff format .         # format
```

Hand-labeled highlight timestamps for evaluation live in `eval/labels.csv`.
