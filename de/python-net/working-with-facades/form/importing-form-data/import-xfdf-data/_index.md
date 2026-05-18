---
title: XFDF-Daten importieren
type: docs
weight: 20
url: /de/python-net/import-xfdf-data/
description: Dieses Beispiel zeigt, wie Formulardaten aus einer XFDF-Datei in ein PDF-Formular importiert werden können, und zwar mit Aspose.PDF for Python via .NET. Es wird gezeigt, wie ein PDF-Dokument gebunden, XML-basierte XFDF-Daten über einen Dateistream gelesen und passend zugehörige Formularfelder automatisch ausgefüllt werden. Das Importieren von XFDF-Daten ermöglicht einen effizienten Austausch von Formulardaten und unterstützt automatisierte Dokumenten‑Workflows, die auf strukturierten XML‑Formaten basieren.
lastmod: "2026-05-18"
---

XFDF (XML Forms Data Format) ist eine XML-Darstellung von PDF-Formulardaten, die für Interoperabilität und Datenaustausch konzipiert ist. In diesem Beispiel wird das [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade aus der [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) Modul wird verwendet, um ein PDF-Formular zu binden und Feldwerte aus einer externen XFDF-Datei zu importieren. Nach dem Import der Daten wird das aktualisierte PDF als neues Dokument gespeichert.

1. Initialisieren Sie pdf_facades.Form(), um mit PDF‑Formularfeldern zu interagieren.
1. Rufen Sie 'bind_pdf()' auf, um die PDF‑Formularvorlage anzuhängen.
1. Verwenden Sie 'open()', um die XFDF-Datei zu lesen.
1. Rufen Sie 'import_xfdf()' auf, um PDF-Felder mit Werten aus der XFDF-Datei zu befüllen.
1. Speichern Sie das aktualisierte Document.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import Data from XFDF
def import_data_from_xfdf(infile, datafile, outfile):
    """Import form data from XFDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XFDF file as stream
    with open(datafile, "rb") as xfdf_input_stream:
        # Import data from XFDF into PDF form fields
        pdf_form.import_xfdf(xfdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
