import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

from speech_to_text import SpeechToText

# Modeli başlat
stt = SpeechToText()

# Buraya kendi ses dosyanın yolunu yaz
ses_yolu = "C:\\Users\\Pelin\\OneDrive\\Belgeler\\SesKayitlari\\ornek_kayit.wav"

# Yazıya dök
metin = stt.transcribe(ses_yolu)

print("Sesli şikayet yazıya döküldü:")
print(metin)
