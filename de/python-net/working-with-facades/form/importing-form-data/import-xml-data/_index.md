---
title: XML-Daten importieren
type: docs
weight: 40
url: /de/python-net/import-xml-data/
description: Dieses Beispiel demonstriert, wie Formulardaten aus einer XML‑Datei in PDF‑Formularfelder importiert werden, wobei Aspose.PDF for Python via .NET verwendet wird. Es zeigt, wie ein PDF‑Dokument gebunden, strukturierte XML‑Daten über einen Dateistream gelesen und die entsprechenden Formularfelder automatisch ausgefüllt werden.
lastmod: "2026-05-18"
---

XML wird häufig verwendet, um strukturierte Formulardaten zu speichern, was es zu einem praktischen Format für den Austausch von Werten zwischen Systemen macht. In diesem Beispiel wird das [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) Facade von [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) wird verwendet, um ein PDF‑Formular zu laden und Feldwerte direkt aus einer XML‑Datei anzuwenden. Nach dem Importieren der Daten wird das aktualisierte PDF als neues Dokument gespeichert.

1. Initialisieren Sie pdf_facades.Form(), um mit PDF‑Formularfeldern zu interagieren.
1. Rufen Sie 'bind_pdf()' auf, um die PDF‑Formularvorlage anzuhängen.
1. Verwenden Sie 'FileIO()', um auf die XML‑Datei zuzugreifen, die Formulardaten enthält.
1. Rufen Sie 'import_xml()' auf, um PDF‑Felder mit Werten aus der XML‑Datei zu füllen.
1. Speichere das aktualisierte PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import data from XML
def import_xml_to_pdf_fields(infile, datafile, outfile):
    """Import form data from XML file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, "r") as xml_input_stream:
        # Import data from XML into PDF form fields
        pdf_form.import_xml(xml_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
