---
title: Barcode-Felder ausfüllen
type: docs
weight: 50
url: /de/python-net/fill-barcode-fields/
description: Dieses Beispiel demonstriert, wie man Barcode-Felder in einem PDF-Formular programmgesteuert mit Aspose.PDF for Python via .NET ausfüllt. Es zeigt, wie man ein PDF-Dokument bindet, einem Barcode-Feld einen Wert zuweist und die aktualisierte Datei speichert.
lastmod: "2026-05-18"
---

Barcode-Felder in PDF-Formularen ermöglichen das Speichern codierter Informationen und deren visuelle Darstellung als Barcodes. In diesem Beispiel, die [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade aus der [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) Modul wird verwendet, um Formularfelder zuzugreifen und einen Barcode-Wert zuzuweisen. Sobald die Daten ausgefüllt sind, wird das PDF mit dem aktualisierten Barcode-Inhalt gespeichert.

1. Initialisieren Sie 'pdf_facades.Form()', um PDF-Formularinteraktionen zu verwalten.
1. Rufen Sie 'bind_pdf()' auf, um das PDF mit Barcode-Feldern anzuhängen.
1. Verwenden Sie 'fill_field()', um einen Barcode-Wert zuzuweisen.
1. Speichern Sie das aktualisierte Document.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Barcode Fields
def fill_barcode_fields(infile, outfile):
    """Fill barcode fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill barcode fields by name
    pdf_form.fill_field("product_barcode", "123456789012")

    # Save updated PDF
    pdf_form.save(outfile)
```
