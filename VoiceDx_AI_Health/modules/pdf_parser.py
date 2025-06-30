import pdfplumber
import re

class PDFParser:
    def __init__(self):
        pass

    def parse(self, pdf_path):
        results = []

        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if not text:
                    continue

                lines = text.split('\n')
                for line in lines:
                    parts = line.split()

                    if len(parts) >= 3:
                        test_name = parts[0]
                        value_match = re.findall(r"[\d.]+", parts[1])
                        unit = parts[2]

                        if value_match:
                            try:
                                value = float(value_match[0])
                                results.append({
                                    "test": test_name,
                                    "value": value,
                                    "unit": unit
                                })
                            except:
                                continue

        return results
