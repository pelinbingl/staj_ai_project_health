import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

from pdf_parser import PDFParser

parser = PDFParser()

# Buraya test PDF dosyasının yolunu yaz (örnek: ornek_tahlil.pdf)
pdf_yolu = "C:\\Users\\Pelin\\Downloads\\Enabiz-Tahlilleri.pdf"

sonuclar = parser.parse(pdf_yolu)

print("Tahlil verileri:")
for item in sonuclar:
    print(f"{item['test']} = {item['value']} {item['unit']}")
