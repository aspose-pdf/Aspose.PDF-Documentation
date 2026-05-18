---
title: Button-Felder und Bilder
type: docs
weight: 40
url: /de/python-net/button-fields-and-images/
description: Dieses Beispiel demonstriert, wie man Button-Felder in einem PDF-Formular mithilfe der Aspose.PDF Facades API verwaltet.
lastmod: "2026-05-18"
TechArticle: true
AlternativeHeadline: Hinzufügen einer Bilddarstellung zu Button-Feldern & Lesen von Submit-Flags
Abstract: PDF-Formulare enthalten oft interaktive Schaltflächen, die entweder JavaScript-Aktionen auslösen oder die Formulardaten übermitteln. Sie können Button-Felder optisch verbessern, indem Sie Bilder als deren Darstellung hinzufügen, und das Übermittlungsverhalten programmgesteuert untersuchen.
---

## Bilddarstellung zu Button-Feldern hinzufügen

Dieser Codeausschnitt erklärt, wie man einer bestehenden Button-Feld in einem PDF-Formular eine Bilddarstellung hinzufügt. Der Vorgang verbessert die visuelle Darstellung eines PDF-Buttons, indem er dessen Standarddarstellung durch ein benutzerdefiniertes Bild ersetzt.

1. Erstellen Sie ein Form-Objekt.
1. Binden Sie die PDF-Datei an das Form-Objekt.
1. Bild zum Button Field hinzufügen.

    - Bestimmen Sie den Pfad zur Bilddatei, die mit dem PDF verknüpft ist
    - Öffnen Sie das Bild im Binärmodus als image_stream.
    - Rufen Sie fill_image_field() mit dem vollständig qualifizierten Button-Feldnamen auf.

1. Speichern Sie das aktualisierte PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add image appearance to button fields
def add_image_appearance_to_button_fields(infile, outfile):
    """Add image appearance to button fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Add image appearance to button fields by providing the field name and image stream
    image_path = infile.replace(".pdf", ".jpg")
    with open(image_path, "rb") as image_stream:
        pdf_form.fill_image_field("Image1_af_image", image_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```

## Abrufen von Submit-Flags

Python‑Bibliothek hilft Ihnen, die Submit‑Flags einer Schaltfläche zum Senden in einem PDF‑Formular mithilfe der Aspose.PDF Facades‑API abzurufen. Submit‑Flags definieren das Verhalten einer Submit‑Schaltfläche, z. B. ob sie das gesamte Formular sendet, Anmerkungen einschließt oder im FDF-, XFDF-, PDF- oder HTML‑Format übermittelt.

1. Erstellen Sie ein Form-Objekt.
1. Rufen Sie get_submit_flags() auf dem Form‑Objekt mit dem vollqualifizierten Namen der Submit‑Schaltfläche auf.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_submit_flags(infile, outfile):
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)
    flags = pdf_form.get_submit_flags("Submit1_af_submit")

    print(f"Submit flags: {flags}")
```
