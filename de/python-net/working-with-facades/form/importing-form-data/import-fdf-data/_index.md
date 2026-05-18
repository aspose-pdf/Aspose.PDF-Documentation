---
title: FDF-Daten importieren
type: docs
weight: 10
url: /de/python-net/import-fdf-data/
description: Dieses Beispiel zeigt, wie Formulardaten aus einer FDF‑Datei in ein PDF‑Formular mit Aspose.PDF for Python via .NET importiert werden. Es demonstriert, wie ein PDF‑Dokument gebunden, Formularfeldwerte aus einem FDF‑Stream gelesen und die entsprechenden Felder automatisch ausgefüllt werden.
lastmod: "2026-05-18"
---

FDF (Forms Data Format) ist ein leichtgewichtiges Format, das zum Speichern und Übertragen von PDF‑Formularfeldwerten verwendet wird, ohne das gesamte Dokument zu enthalten. In diesem Beispiel wird das [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) Facade von [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) wird verwendet, um ein PDF‑Formular zu laden und Felddaten aus einer externen FDF‑Datei zu importieren. Nach dem Importvorgang wird das aktualisierte PDF als neue Datei gespeichert.

1. Initialisieren Sie pdf_facades.Form(), um mit interaktiven PDF‑Formularfeldern zu arbeiten.
1. Rufen Sie 'bind_pdf()' auf, um die PDF‑Formularvorlage anzuhängen.
1. Verwenden Sie 'open()', um die FDF‑Datei im Binärmodus zu lesen.
1. Rufen Sie 'import_fdf()' auf, um PDF-Felder mit Daten aus der FDF-Datei zu füllen.
1. Speichere das aktualisierte PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import Data from FDF
def import_fdf_to_pdf_form(infile, datafile, outfile):
    """Import form data from FDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open FDF file as stream
    with open(datafile, "rb") as fdf_input_stream:
        pdf_form.import_fdf(fdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
