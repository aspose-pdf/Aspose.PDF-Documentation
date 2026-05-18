---
title: Kontrollkästchenfelder ausfüllen
type: docs
weight: 20
url: /de/python-net/fill-check-box-fields/
description: Dieses Beispiel zeigt, wie man programmgesteuert Kontrollkästchenfelder in einem PDF-Formular mit Aspose.PDF for Python via .NET ausfüllt. Es demonstriert, wie man ein PDF-Dokument bindet, die Werte der Kontrollkästchen anhand des Feldnamens aktualisiert und die geänderte Datei speichert.
lastmod: "2026-05-18"
---

Das Kontrollkästchen wird häufig in PDF-Formularen verwendet, um binäre Entscheidungen wie Abonnements oder Bestätigungen von Vereinbarungen darzustellen. In diesem Beispiel wird das [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) Facade von [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) wird verwendet, um auf Formularfelder zuzugreifen und deren Werte auf einen ausgewählten Zustand zu setzen. Nach dem Aktualisieren der Kontrollkästchen wird das ausgefüllte PDF als neues Dokument gespeichert.

1. Initialisieren Sie 'pdf_facades.Form()', um Formularfeld-Interaktionen zu verwalten.
1. Verwenden Sie 'bind_pdf()', um die Quell‑PDF mit den Checkbox‑Feldern anzuhängen.
1. Rufen Sie 'fill_field()' auf, um Felder wie 'subscribe_newsletter' und 'accept_terms' als ausgewählt zu markieren.
1. Speichern Sie das aktualisierte Document.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Check Box Fields
def fill_check_box_fields(infile, outfile):
    """Fill check box fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill check box fields by name
    pdf_form.fill_field("subscribe_newsletter", "Yes")
    pdf_form.fill_field("accept_terms", "Yes")

    # Save updated PDF
    pdf_form.save(outfile)
```
