---
title: XFA-Daten extrahieren
type: docs
weight: 50
url: /de/python-net/extract-xfa-data/
description: Dieses Beispiel erklärt, wie man XFA-Formulardaten aus einer PDF-Datei mit Aspose.PDF for Python via .NET extrahiert. Es zeigt, wie man ein XFA-basiertes PDF-Dokument an die Form-Fassade bindet und seine interne Datenstruktur in einen Dateistream exportiert.
lastmod: "2026-05-18"
---

XFA (XML Forms Architecture)-Formulare unterscheiden sich von herkömmlichen AcroForms, weil ihre Daten als XML innerhalb der PDF gespeichert werden. In diesem Beispiel wird der [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) Objekt aus dem [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) Modul wird verwendet, um die PDF zu binden und ihre XFA-Daten direkt in eine Datei zu extrahieren.

1. Erstellen Sie eine Instanz von pdf_facades.Form(), um Formulardaten zu verwalten.
1. Rufen Sie 'bind_pdf()' auf, um die Quell-PDF mit XFA-Formularen anzuhängen.
1. Verwenden Sie 'FileIO()', um einen schreibbaren Dateistream zu erstellen.
1. Rufen Sie 'extract_xfa_data()' auf, um die eingebetteten XFA-XML-Daten zu exportieren.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Extract XFA Data
def export_xfa_data(infile, outfile):
    """Export XFA form data."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    with FileIO(outfile, "w") as stream:
        # Export embedded XFA XML data to the output stream
        form.extract_xfa_data(stream)
```
