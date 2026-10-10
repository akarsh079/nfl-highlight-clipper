"""Command-line entry point for the NFL highlight clipper."""

import argparse
from pathlib import Path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Clip highlights from an NFL game video.")
    parser.add_argument("video", type=Path, help="Path to the input game video.")
    parser.add_argument(
        "--out", type=Path, default=Path("highlights.mp4"), help="Path for the output reel."
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    print(f"Pipeline not implemented yet (video={args.video}, out={args.out}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
