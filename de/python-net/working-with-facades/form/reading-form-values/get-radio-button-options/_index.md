---
title: Radio-Button-Optionen abrufen
type: docs
weight: 20
url: /de/python-net/get-radio-button-options/
description: Dieser Artikel zeigt, wie man den aktuell ausgewählten Wert eines Radio-Button-Feldes in einem PDF-Dokument mithilfe der Aspose.PDF Facades API abruft.
lastmod: "2026-05-18"
---

Radio-Button-Felder in PDF-Formularen sind gruppierte Steuerelemente, bei denen gleichzeitig nur eine Option ausgewählt werden kann. Jede Gruppe hat einen Feldnamen und jede Option hat einen entsprechenden Wert.

1. Ein Form-Objekt erstellen.
1. Das PDF-Dokument binden.
1. Die ausgewählte Radio-Button-Option abrufen.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get radio button options
def get_radio_button_options(infile):
    """Get radio button options from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get radio button options by their names
    field_names = ["WorkType"]
    for field_name in field_names:
        options = pdf_form.get_button_option_current_value(field_name)
        print(f"Options for '{field_name}': {options}")
```
