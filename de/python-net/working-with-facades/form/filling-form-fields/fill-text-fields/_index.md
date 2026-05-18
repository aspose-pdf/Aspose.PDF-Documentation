---
title: Textfelder ausfüllen
type: docs
weight: 10
url: /de/python-net/fill-text-fields/
description: Dieses Beispiel demonstriert, wie Textfelder in einem PDF-Formular mithilfe von Aspose.PDF for Python via .NET automatisch ausgefüllt werden können. Es zeigt, wie ein PDF-Dokument geladen, bestimmte Formularfelder anhand ihres Namens befüllt und die aktualisierte Datei gespeichert wird.
lastmod: "2026-05-18"
---

Das programmgesteuerte Ausfüllen von Textfeldern ermöglicht es Anwendungen, PDF-Vorlagen wiederzuverwenden und dynamische Inhalte ohne manuelle Bearbeitung einzufügen. In diesem Beispiel wird das [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) Facade von [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) wird verwendet, um ein PDF-Formular zu binden und mehrere Felder wie Name, Adresse und E‑Mail zu aktualisieren. Nach dem Zuweisen der Werte wird das modifizierte PDF als neues Dokument gespeichert.

1. Initialisieren Sie \u0027pdf_facades.Form()\u0027, um Formularfeldoperationen zu verwalten.
1. Verwenden Sie \u0027bind_pdf()\u0027, um das Eingabe‑PDF mit Textfeldern anzuhängen.
1. Rufen Sie 'fill_field()' auf, um Daten in Felder wie name, address und email einzufügen.
1. Speichere das aktualisierte PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Text Fields
def fill_text_fields(infile, outfile):
    """Fill text fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill text fields by name
    pdf_form.fill_field("name", "John Doe")
    pdf_form.fill_field("address", "123 Main St, Anytown, USA")
    pdf_form.fill_field("email", "john.doe@example.com")

    # Save updated PDF
    pdf_form.save(outfile)
```
