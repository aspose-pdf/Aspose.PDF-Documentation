---
title: Vollständige Feldnamen auflösen
type: docs
weight: 60
url: /de/python-net/resolve-full-field-names/
description: Dieses Beispiel demonstriert, wie man die vollständig qualifizierten Namen von Formularfeldern in einem PDF-Dokument mithilfe der Aspose.PDF Facades API abruft.
lastmod: "2026-05-18"
---

In PDF-Formularen können Felder hierarchisch organisiert werden, insbesondere wenn Unterformulare verwendet werden. Jedes Feld hat einen Kurznamen und einen vollständig qualifizierten Namen. Der vollständig qualifizierte Name stellt den vollständigen Pfad des Feldes innerhalb der Formularhierarchie dar und wird von vielen API-Methoden, die Formulardaten manipulieren oder auslesen, benötigt.

1. Ein Form-Objekt erstellen.
1. Das PDF-Dokument binden.
1. Alle Formularfeldnamen abrufen.
1. Der vollständig qualifizierte Name jedes Feldes wird mit get_full_field_name() aufgelöst.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resolve full field names
def resolve_full_field_names(infile):
    """Resolve full field names in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Resolve full field names
    for field in pdf_form.field_names:
        name = pdf_form.get_full_field_name(field)
        print(f"Full field name: {name}")
```
