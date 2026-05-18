---
title: Rich-Text-Werte abrufen
type: docs
weight: 40
url: /de/python-net/get-rich-text-values/
description: Dieser Abschnitt erklärt, wie man den Rich‑Text‑Inhalt eines Formularfeldes in einem PDF‑Dokument mit der Aspose.PDF Facades API abruft. Im Gegensatz zu einfachen Textfeldern können Rich‑Text‑Felder formatierte Inhalte wie fetten Text, unterschiedliche Schriftarten, Farben und Absatzformatierungen enthalten.
lastmod: "2026-05-18"
---

PDF‑Formulare können Textfelder enthalten, die Rich‑Text‑Formatierung unterstützen. Diese Felder können Inhalte mit Stil‑Attributen zusätzlich zu einfachen Textwerten speichern.

1. Ein Form-Objekt erstellen.
1. Das PDF-Dokument binden.
1. Rich‑Text‑Werte abrufen

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get rich text values
def get_rich_text_values(infile):
    """Get rich text values from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get rich text values by their names
    field_names = ["Summary"]
    for field_name in field_names:
        rich_text_value = pdf_form.get_rich_text(field_name)
        print(f"Rich text value of '{field_name}': {rich_text_value}")
```
