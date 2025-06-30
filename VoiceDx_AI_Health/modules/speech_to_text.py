from transformers import pipeline
from huggingface_hub import login

# Token ile giriş yap (şifre gibi güvenli tut!)
login("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")

class SpeechToText:
    def __init__(self):
        self.asr = pipeline("automatic-speech-recognition", model="openai/whisper-base")

    def transcribe(self, audio_path):
        return self.asr(audio_path)["text"]
