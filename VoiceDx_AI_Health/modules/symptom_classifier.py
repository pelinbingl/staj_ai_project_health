class SymptomClassifier:
    def __init__(self):
        self.symptom_list = [
            "baş dönmesi",
            "mide bulantısı",
            "göğüs ağrısı",
            "nefes darlığı",
            "halsizlik",
            "boğaz ağrısı",
            "ateş",
            "titreme",
            "yorgunluk",
            "kas ağrısı",
            "baş ağrısı",
            "öksürük",
            "burun akıntısı",
            "ishal",
            "kabızlık",
            "idrar yaparken yanma",
            "çarpıntı"
        ]

    def classify(self, text):
        metin = text.lower()

        # Eş anlamlıları ekleyerek metni genişlet
        es_anlamlilar = {
            "başım dönüyor": "baş dönmesi",
            "baş dönüyor": "baş dönmesi",
            "göğsümde ağrı": "göğüs ağrısı",
            "mide bulanıyor": "mide bulantısı",
            "midem bulanıyor": "mide bulantısı"
        }

        for ifade, semptom in es_anlamlilar.items():
            if ifade in metin and semptom not in metin:
                metin += " " + semptom

        return [s for s in self.symptom_list if s in metin]
