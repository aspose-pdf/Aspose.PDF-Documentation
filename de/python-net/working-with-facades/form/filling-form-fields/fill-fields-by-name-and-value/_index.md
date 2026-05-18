---
title: Felder nach Name und Wert ausfüllen
type: docs
weight: 60
url: /de/python-net/fill-fields-by-name-and-value/
description: Dieser Artikel zeigt, wie man mehrere PDF-Formularfelder dynamisch nach Name und Wert ausfüllt, wobei Aspose.PDF for Python via .NET verwendet wird. Anstatt jedes Feld einzeln zu setzen, wird eine Dictionary‑Struktur verwendet, um Feldnamen den Werten zuzuordnen und sie in einer Schleife zu füllen.
lastmod: "2026-05-18"
---

Das Ausfüllen von Formularfeldern mit einer Namens‑Wert‑Sammlung ermöglicht es Entwicklern, skalierbare und flexible Lösungen für die PDF-Formularautomatisierung zu erstellen. In diesem Beispiel wird das [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) Facade von [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) wird verwendet, um ein PDF‑Dokument zu binden und durch ein Dictionary mit Felddaten zu iterieren. Jeder Eintrag wird mittels der 'fill_field method' angewendet, wodurch effiziente Massenaktualisierungen von Formularfeldern ermöglicht werden.

1. Initialisieren Sie 'pdf_facades.Form()', um mit interaktiven Formularfeldern zu arbeiten.
1. Verwenden Sie 'bind_pdf()', um das Quell-PDF-Dokument anzuhängen.
1. Erstellen Sie ein Dictionary, das Feldnamen und die Werte enthält, die Sie einfügen möchten.
1. Durchlaufen Sie das Wörterbuch und rufen Sie 'fill_field()' für jeden Eintrag auf.
1. Speichern Sie das aktualisierte Document.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Fields by Name and Value
def fill_fields_by_name_and_value(infile, outfile):
    """Fill PDF form fields by name and value."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill fields by name and value
    fields = {
        "name": "Jane Smith",
        "address": "456 Elm St, Othertown, USA",
        "email": "jane.smith@example.com",
    }
    for field_name, value in fields.items():
        pdf_form.fill_field(field_name, value)

    # Save updated PDF using outfile
    pdf_form.save(outfile)
```
