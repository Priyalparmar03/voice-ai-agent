import whisper
import tempfile

# load model once
model = whisper.load_model("base")   # if slow → change to "tiny"

def transcribe_audio(file):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(file.read())
        result = model.transcribe(tmp.name)

    return result["text"]