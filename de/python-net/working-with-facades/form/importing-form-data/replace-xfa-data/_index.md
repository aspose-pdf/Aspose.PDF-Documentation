---
title: XFA-Daten ersetzen
type: docs
weight: 50
url: /de/python-net/replace-xfa-data/
description: Dieses Beispiel zeigt, wie vorhandene XFA-Formulardaten in einem PDF mit Aspose.PDF for Python via .NET ersetzt werden können. Es zeigt, wie ein XFA-basiertes PDF-Dokument gebunden, neue Daten aus einer externen XFA-Datei geladen und der Formularinhalt programmgesteuert aktualisiert werden.
lastmod: "2026-05-18"
---

XFA (XML Forms Architecture)-Formulare speichern ihre Daten im XML-Format innerhalb der PDF-Struktur. In diesem Beispiel, das [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade aus der [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) Das Modul wird verwendet, um ein PDF zu binden und dessen vorhandenen XFA-Datensatz mithilfe eines externen XML-Streams zu ersetzen. Nachdem die neuen Daten angewendet wurden, wird das aktualisierte PDF als separate Datei gespeichert.

1. Initialisieren Sie pdf_facades.Form(), um XFA-Formulardaten zu verwalten.
1. Rufen Sie 'bind_pdf()' auf, um das PDF, das XFA-Formulare enthält, anzuhängen.
1. Verwenden Sie 'FileIO()', um die XFA XML-Datei zu lesen.
1. Rufen Sie 'set_xfa_data()' auf, um das PDF mit neuem XFA-Inhalt zu aktualisieren.
1. Speichern Sie das aktualisierte Document.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Replace from XFA data
def replace_xfa_data(infile, datafile, outfile):
    """Import form data from XFA file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open XFA file as stream
    with FileIO(datafile, "r") as xfa_stream:
        # Import data from XFA into PDF form fields
        form.set_xfa_data(xfa_stream)

    # Save updated PDF
    form.save(outfile)
```
