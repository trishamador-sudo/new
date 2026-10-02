#!/usr/bin/env bash
# Re-encode a background video to all-keyframe H.264 for smooth scroll scrubbing.
# Usage: scripts/swap-bg-video.sh <input.mp4>   (run from the lawgical-labour folder)
set -euo pipefail

INPUT="$1"
OUTPUT="website/public/bg.mp4"
POSTER="website/public/img/poster.jpg"

mkdir -p website/public/img

# Every frame a keyframe (-g 1) so seeking to any scroll position is instant.
# Scaled to 1600 wide to keep the file light; audio removed.
ffmpeg -y -i "$INPUT" -an -vf "scale=1600:-2" -c:v libx264 -preset slow -crf 27 \
  -g 1 -keyint_min 1 -sc_threshold 0 -pix_fmt yuv420p \
  -movflags +faststart "$OUTPUT"

# First frame as poster (shown before the video loads, on phones and with reduced motion).
ffmpeg -y -ss 0.2 -i "$INPUT" -frames:v 1 -vf "scale=1920:-2" -q:v 3 "$POSTER"

echo "Encoded all-keyframe background video to $OUTPUT"
