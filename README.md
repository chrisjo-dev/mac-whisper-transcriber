# mac-whisper-transcriber

A local speech-to-text web UI for Mac, powered by [whisper.cpp](https://github.com/ggerganov/whisper.cpp) and ffmpeg.  
Drag & drop an audio file, get a transcript. Everything runs on your machine — no cloud, no API keys.

## How it works

```
Browser (file upload)
  → Flask server
    → ffmpeg (input → 16kHz mono WAV)
    → whisper-cli (WAV → text/subtitles)
  → Browser (display result)
```

## Requirements

- macOS
- Python 3 + Flask
- ffmpeg
- whisper-cpp (`brew install whisper-cpp`)
- Whisper model file (`~/.whisper/ggml-medium.bin`)

## Download model

```bash
mkdir -p ~/.whisper
curl -L -o ~/.whisper/ggml-medium.bin \
  https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-medium.bin
```

## Install & Run

```bash
pip install flask
python3 app.py
```

Open http://127.0.0.1:5111

## Usage

1. Drag & drop an audio file (or click to select)
2. Choose language (Korean, English, Japanese, Chinese, Auto)
3. Click "Transcribe"
4. Copy result or download as TXT/SRT

## Supported formats

m4a, mp3, wav, webm, ogg — any audio format ffmpeg can handle

---

## 한국어

로컬 Mac에서 돌아가는 음성 → 텍스트 변환 웹 UI.  
[whisper.cpp](https://github.com/ggerganov/whisper.cpp)와 ffmpeg을 사용합니다. 클라우드 없이 로컬에서 모두 처리됩니다.

보다 자세한 사항 [블로그 참고](https://chrisjo-dev.github.io/notion-blog/posts/macbook-m4%EC%97%90%EC%84%9C-whisper-%EB%AA%A8%EB%8D%B8%EC%9D%84-%EB%A1%9C%EC%BB%AC%EB%A1%9C-%EB%8F%8C%EB%A0%A4%EB%B3%B4%EC%9E%90-whispercpp-%EC%84%A4%EC%B9%98%EB%B6%80%ED%84%B0-%ED%95%9C%EA%B5%AD%EC%96%B4-%EC%9D%8C%EC%84%B1-%EB%B3%80%ED%99%98%EA%B9%8C%EC%A7%80/)

### 동작 방식

```
브라우저 (파일 업로드)
  → Flask 서버
    → ffmpeg (입력 → 16kHz mono WAV)
    → whisper-cli (WAV → 텍스트/자막)
  → 브라우저 (결과 표시)
```

### 요구사항

- macOS
- Python 3 + Flask
- ffmpeg
- whisper-cpp (`brew install whisper-cpp`)
- whisper 모델 파일 (`~/.whisper/ggml-medium.bin`)

### 모델 다운로드

```bash
mkdir -p ~/.whisper
curl -L -o ~/.whisper/ggml-medium.bin \
  https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-medium.bin
```

### 설치 및 실행

```bash
pip install flask
python3 app.py
```

http://127.0.0.1:5111 접속

### 사용법

1. 오디오 파일을 드래그 & 드롭 (또는 클릭해서 선택)
2. 언어 선택 (한국어, English, 日本語, 中文, Auto)
3. "변환하기" 클릭
4. 결과를 복사하거나 TXT/SRT로 다운로드

### 지원 포맷

m4a, mp3, wav, webm, ogg 등 ffmpeg이 처리 가능한 모든 오디오 포맷
