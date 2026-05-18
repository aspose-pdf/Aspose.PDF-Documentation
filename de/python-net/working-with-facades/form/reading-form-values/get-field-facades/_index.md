---
title: Feld-Facades abrufen
type: docs
weight: 10
url: /de/python-net/get-field-facades/
description: Dieses Beispiel demonstriert, wie man die Werte bestimmter Formularfelder aus einem PDF-Dokument mit der Aspose.PDF Facades API liest.
lastmod: "2026-05-18"
---

PDF-Formulare enthalten Felder, in die Benutzer Daten eingeben können, wie Textfelder, Kontrollkästchen oder Optionskästchen. Um diese Formulare programmgesteuert zu verarbeiten, ist es häufig erforderlich, die aktuellen Werte dieser Felder abzurufen.

1. Erstellen Sie ein Form-Objekt.
1. Binden Sie das PDF-Dokument an das Formularobjekt.
1. Feldwerte abrufen.

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