---
title: JSON-Daten importieren
type: docs
weight: 30
url: /de/python-net/import-json-data/
description: Dieses Beispiel demonstriert, wie Formularfelddaten aus einer JSON‑Datei in ein PDF‑Formular mit Aspose.PDF for Python via .NET importiert werden. Es zeigt, wie ein PDF‑Dokument gebunden, strukturierte JSON‑Daten über einen Dateistream gelesen und passende Formularfelder automatisch befüllt werden.
lastmod: "2026-05-18"
---

JSON wird häufig zum Speichern und Übertragen strukturierter Daten zwischen Systemen verwendet. In diesem Beispiel wird das [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade aus der [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) Modul wird verwendet, um ein PDF‑Formular zu binden und Feldwerte aus einer externen JSON‑Datei zu importieren. Nach dem Importvorgang wird das aktualisierte Dokument als neue PDF‑Datei gespeichert.

1. Initialisieren Sie pdf_facades.Form(), um mit PDF‑Formularfeldern zu interagieren.
1. Rufen Sie 'bind_pdf()' auf, um die PDF‑Formularvorlage anzuhängen.
1. Verwenden Sie 'FileIO()', um die JSON‑Datei mit den Formularwerten zu lesen.
1. Rufen Sie 'import_json()' auf, um PDF‑Felder mit JSON‑Schlüssel‑Wert‑Paaren zu füllen.
1. Speichere das aktualisierte PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import from JSON
def import_json_to_pdf_form(infile, datafile, outfile):
    """Import form data from JSON file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open JSON file as stream
    with FileIO(datafile, "r") as json_stream:
        # Import data from JSON into PDF form fields
        form.import_json(json_stream)

    # Save updated PDF
    form.save(outfile)
```
