---
title: Exportieren nach XFDF
type: docs
weight: 20
url: /de/python-net/export-to-xfdf/
description: Dieses Beispiel zeigt, wie man PDF-Formularfelddaten in eine XFDF (XML Forms Data Format)-Datei exportiert, wobei Aspose.PDF for Python via .NET verwendet wird. Es demonstriert, wie man ein PDF-Formular lädt, über die Form-Fassade auf seine Felder zugreift und die extrahierten Werte in einen XFDF-Stream speichert.
lastmod: "2026-05-18"
---

XFDF ist eine XML-Darstellung von PDF-Formulardaten, die es Entwicklern ermöglicht, Formularfeldwerte unabhängig vom Originaldokument zu übertragen. In diesem Beispiel ist die [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) Objekt von [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) wird verwendet, um das Quell-PDF zu binden und seine Daten in eine strukturierte XFDF-Datei zu exportieren.

1. Initialisieren Sie pdf_facades.Form(), um PDF-Formulardaten zu verwalten.
1. Rufen Sie 'bind_pdf()' auf, um das Quell-PDF-Dokument anzuhängen.
1. Verwenden Sie 'open()', um einen beschreibbaren Binärstream zu erstellen.
1. Formulardaten exportieren. Rufen Sie 'export_xfdf()' auf, um Werte von Formularfeldern zu extrahieren und im XFDF-Format zu speichern.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to XFDF
def export_pdf_form_to_xfdf(infile, outfile):
    """Export PDF form data to XFDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create XFDF file stream
    with open(outfile, "wb") as xfdf_output_stream:
        # Export form data to XFDF file
        pdf_form.export_xfdf(xfdf_output_stream)
```
