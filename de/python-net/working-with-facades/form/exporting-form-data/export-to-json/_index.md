---
title: Exportieren nach JSON
type: docs
weight: 30
url: /de/python-net/export-to-json/
description: Dieses Beispiel zeigt, wie man PDF-Formularfeldwerte in eine JSON-Datei exportiert, indem man Aspose.PDF for Python via .NET verwendet. Es erklärt, wie man ein PDF-Formular lädt, über die Form-Fassade auf seine Felder zugreift und die extrahierten Daten in einem strukturierten JSON-Format speichert.
lastmod: "2026-05-18"
---

JSON ist ein weit verbreitetes Datenformat, das einen nahtlosen Austausch zwischen Anwendungen und Diensten ermöglicht. In diesem Beispiel wird das [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) Objekt aus dem [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) Modul wird verwendet, um eine PDF-Datei zu binden und deren Formularfeldwerte in eine lesbare JSON-Struktur zu exportieren.

1. Initialisieren Sie pdf_facades.Form(), um mit Formularfeldern zu arbeiten.
1. Verwenden Sie 'bind_pdf()', um das Quell-PDF-Dokument anzuhängen.
1. Erstellen Sie einen beschreibbaren Stream mit 'FileIO()'.
1. Rufen Sie 'export_json()' auf, um Formularfeldwerte zu extrahieren und sie im formatierten JSON zu speichern.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to JSON
def export_form_to_json(infile, outfile):
    """Export PDF form field values to JSON file."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Create JSON file stream
    with FileIO(outfile, "w") as json_stream:
        # Export form field values to JSON
        form.export_json(json_stream, indented=True)
```
