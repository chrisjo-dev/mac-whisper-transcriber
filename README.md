# mac-whisper-transcriber

로컬 Mac에서 돌아가는 음성 → 텍스트 변환 웹 UI.  
내부적으로 [whisper.cpp](https://github.com/ggerganov/whisper.cpp)와 ffmpeg을 사용합니다.

## 동작 방식

```
브라우저 (파일 업로드)
  → Flask 서버
    → ffmpeg (입력 → 16kHz mono WAV)
    → whisper-cli (WAV → 텍스트/자막)
  → 브라우저 (결과 표시)
```

## 요구사항

- macOS
- Python 3 + Flask
- ffmpeg
- whisper-cpp (`brew install whisper-cpp`)
- whisper 모델 파일 (`~/.whisper/ggml-medium.bin`)

## 모델 다운로드

```bash
mkdir -p ~/.whisper
curl -L -o ~/.whisper/ggml-medium.bin \
  https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-medium.bin
```

## 설치 및 실행

```bash
pip install flask
python3 app.py
```

http://127.0.0.1:5111 접속

## 사용법

1. 오디오 파일을 드래그 & 드롭 (또는 클릭해서 선택)
2. 언어 선택 (한국어, English, 日本語, 中文, Auto)
3. "변환하기" 클릭
4. 결과를 복사하거나 TXT/SRT로 다운로드

## 지원 포맷

m4a, mp3, wav, webm, ogg 등 ffmpeg이 처리 가능한 모든 오디오 포맷
