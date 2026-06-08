# Transcription Workflow

这是南京大学大一英语听说课程教材：智汇大学英语听说教程 4 的部分视频转写、中文校对翻译和中英对照 LaTeX/PDF 输出工作流。

仓库只保存有复用价值的内容：最终文稿、LaTeX 源文件、原始转写文本和转录/排版脚本。

## 主要文件

- `transcripts/welearn_theme2_bilingual_reviewed.pdf`：LaTeX 生成的最终中英对照 PDF。
- `transcripts/welearn_theme2_bilingual_reviewed.tex`：最终整理版 LaTeX 源文件。
- `transcripts/raw/`：Whisper 转写得到的 `.txt`、`.srt`、`.vtt`、`.tsv`、`.json` 原始结果。
- `tools/build_bilingual_latex.py`：从原始英文转写和中文校对稿生成 LaTeX。
- `tools/revised_translations.py`：人工校对后的中文译文，按每个视频分段对应。
- `run_whisper_transcribe.zsh`：批量提取音频并调用 Whisper 转写。
- `tools/transcribe_macos.swift`：macOS Speech 框架转写实验脚本。

## 转录方法

把需要转写的视频放在仓库根目录，安装好 `ffmpeg` 和 Python 后运行：

```bash
zsh run_whisper_transcribe.zsh
```

脚本会：

1. 创建 `transcripts/audio/` 和 `transcripts/raw/`。
2. 用 `ffmpeg` 把视频转成 16 kHz 单声道 WAV。
3. 安装/更新 `openai-whisper`。
4. 使用 `small.en` 模型输出所有字幕格式到 `transcripts/raw/`。

`transcripts/audio/`、`.whisper-cache/` 和视频文件不会提交到 Git。

## 重新生成文稿

```bash
python3 tools/build_bilingual_latex.py
xelatex -interaction=nonstopmode -halt-on-error -output-directory=transcripts transcripts/welearn_theme2_bilingual_reviewed.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=transcripts transcripts/welearn_theme2_bilingual_reviewed.tex
```

如果要继续校对翻译，优先修改 `tools/revised_translations.py`；如果要调整样式或章节顺序，修改 `tools/build_bilingual_latex.py`。
