---
title: Radio-Button-Felder ausfüllen
type: docs
weight: 30
url: /de/python-net/fill-radio-button-fields/
description: Dieses Beispiel zeigt, wie man Radio-Button-Felder in einem PDF-Formular programmgesteuert mit Aspose.PDF for Python via .NET ausfüllt. Es demonstriert, wie man ein PDF-Dokument bindet, eine Radio-Button-Option nach Index auswählt und die aktualisierte Datei speichert.
lastmod: "2026-05-18"
---

Radio-Buttons ermöglichen es Benutzern, eine einzelne Option aus einer vordefinierten Gruppe auszuwählen, beispielsweise bei Geschlechts- oder Präferenzfeldern. In diesem Beispiel wird das [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade aus der [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) Modul wird verwendet, um das Quell-PDF zu binden und eine ausgewählte Option anhand ihres Indexwertes zuzuweisen. Sobald die gewünschte Option gewählt ist, wird das geänderte Dokument gespeichert.

1. Initialisieren Sie pdf_facades.Form(), um PDF-Formularfelder zu verwalten.
1. Rufen Sie 'bind_pdf()' auf, um das PDF mit Radio-Button-Feldern anzuhängen.
1. Verwenden Sie 'fill_field()', um die erste Option (Index 0) auszuwählen.
1. Speichere das aktualisierte PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Radio Button Fields
def fill_radio_button_fields(infile, outfile):
    """Fill radio button fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill radio button fields by name
    pdf_form.fill_field("gender", 0)  # Select male option (index 0)
    # pdf_form.fill_field("gender", 1) # Select female option (index 1)

    # Save updated PDF
    pdf_form.save(outfile)
```
