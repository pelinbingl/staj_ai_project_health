import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

from symptom_classifier import SymptomClassifier

classifier = SymptomClassifier()

metin = "Son birkaç gündür başım dönüyor, göğsümde ağrı hissediyorum ve midem bulanıyor."
semptomlar = classifier.classify(metin)

print("Tespit edilen semptomlar:")
print(semptomlar)
