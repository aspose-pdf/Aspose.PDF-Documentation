---
title: Feldwerte abrufen
type: docs
weight: 50
url: /de/python-net/get-field-values/
description: Abrufen von Feldwerten aus einem PDF-Formular mit Aspose.PDF Facades unter Verwendung der Form-Klasse.
lastmod: "2026-05-18"
---

Dieses Code‑Snippet zeigt, wie die aktuellen Werte von Formularfeldern aus einem PDF‑Dokument mithilfe der Aspose.PDF Facades‑API abgerufen werden. Die [get_field()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/#methods) Methode ermöglicht es Ihnen, programmatisch auf Daten zuzugreifen, die in Textfeldern, Kontrollkästchen, Optionsschaltern und anderen AcroForm‑Elementen eingegeben wurden.

1. Binden Sie das PDF an ein Form‑Objekt.
1. Geben Sie die Feldnamen an, die Sie lesen möchten.
1. Rufen Sie den Wert jedes Feldes mit get_field() ab.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir


    # Get field values
    def get_field_values(infile):
        """Get field values from a PDF document."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Get field values by their names
        field_names = ["First Name", "Last Name"]
        for field_name in field_names:
            value = pdf_form.get_field(field_name)
            print(f"Value of '{field_name}': {value}")
```