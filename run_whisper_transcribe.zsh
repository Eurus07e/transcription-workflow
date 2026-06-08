#!/bin/zsh
set -euo pipefail

cd "${0:A:h}"

mkdir -p .whisper-cache transcripts/raw transcripts/audio

echo "Installing/updating openai-whisper..."
python3 -m pip install -U openai-whisper

videos=(
  ./*.mp4(N)
  ./*.MP4(N)
  ./*.m4v(N)
  ./*.M4V(N)
  ./*.mov(N)
  ./*.MOV(N)
  ./*.mkv(N)
  ./*.MKV(N)
  ./*.webm(N)
  ./*.WEBM(N)
)

if [ ${#videos[@]} -eq 0 ]; then
  echo "No video files found in: $PWD"
  exit 1
fi

echo "Found ${#videos[@]} video file(s)."
printf ' - %s\n' "${videos[@]}"

echo "Extracting normalized audio files..."
for video in "${videos[@]}"; do
  base="${video:t:r}"
  audio="transcripts/audio/${base}.wav"
  if [ ! -s "$audio" ]; then
    ffmpeg -y -i "$video" -vn -ac 1 -ar 16000 -c:a pcm_s16le "$audio" >/dev/null 2>&1
  fi
done

echo "Running Whisper transcription. First run will download the model."
python3 -m whisper "${videos[@]}" \
  --model small.en \
  --model_dir ./.whisper-cache \
  --language English \
  --task transcribe \
  --output_dir transcripts/raw \
  --output_format all \
  --fp16 False

echo "Done. Outputs are in: transcripts/raw"
