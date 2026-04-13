import os
import subprocess
import tempfile
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

WHISPER_MODEL = os.path.expanduser("~/.whisper/ggml-medium.bin")

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    lang = request.form.get("lang", "ko")

    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, file.filename)
        file.save(input_path)

        # convert to 16kHz mono wav
        wav_path = os.path.join(tmpdir, "audio.wav")
        ffmpeg = subprocess.run(
            ["ffmpeg", "-i", input_path, "-ar", "16000", "-ac", "1", wav_path],
            capture_output=True, text=True,
        )
        if ffmpeg.returncode != 0:
            return jsonify({"error": f"ffmpeg failed: {ffmpeg.stderr}"}), 500

        output_base = os.path.join(tmpdir, "result")
        whisper = subprocess.run(
            [
                "whisper-cli",
                "-m", WHISPER_MODEL,
                "-l", lang,
                "-otxt",
                "-osrt",
                "-of", output_base,
                "-f", wav_path,
            ],
            capture_output=True, text=True,
        )
        if whisper.returncode != 0:
            return jsonify({"error": f"whisper failed: {whisper.stderr}"}), 500

        txt = ""
        srt = ""
        txt_path = output_base + ".txt"
        srt_path = output_base + ".srt"
        if os.path.exists(txt_path):
            txt = open(txt_path).read()
        if os.path.exists(srt_path):
            srt = open(srt_path).read()

        return jsonify({"txt": txt, "srt": srt})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5111, debug=True)
