---
title: Erforderliche Feldnamen abrufen
type: docs
weight: 30
url: /de/python-net/get-required-field-names/
description: Dieses Beispiel zeigt, wie man die Namen der erforderlichen Formularfelder in einem PDF‑Dokument mithilfe der Aspose.PDF Facades‑API ermittelt und abruft.
lastmod: "2026-05-18"
---

PDF‑Formulare können Pflichtfelder enthalten, die Benutzer vor dem Absenden ausfüllen müssen. Diese Felder sind typischerweise in den Eigenschaften des Formular's markiert.

1. Ein Form-Objekt erstellen.
1. Das PDF-Dokument binden.
1. Greifen Sie auf alle Feldnamen zu, indem Sie 'pdf_form.field_names' verwenden.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get required field names
def get_required_field_names(infile):
    """Get required field names from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get required field names
    for field in pdf_form.field_names:
        if pdf_form.is_required_field(field):
            print(f"Required field: {field}")
```
