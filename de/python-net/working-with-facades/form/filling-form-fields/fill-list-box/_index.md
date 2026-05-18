---
title: Listenfeld ausfüllen
type: docs
weight: 40
url: /de/python-net/fill-list-box/
description: Dieses Beispiel demonstriert, wie man programmgesteuert Listenfelder und Mehrfachauswahlfelder in einem PDF-Formular mithilfe von Aspose.PDF for Python via .NET ausfüllt. Es zeigt, wie man ein PDF-Dokument bindet, Werte innerhalb eines listenbasierten Formularfelds auswählt und die aktualisierte Datei speichert.
lastmod: "2026-05-18"
---

Listenfelder und Mehrfachauswahlfelder ermöglichen es Benutzern, einen oder mehrere Werte aus einem vordefinierten Satz von Optionen auszuwählen. In diesem Beispiel, das [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) Facade von [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) wird verwendet, um auf das PDF-Formular zuzugreifen und einen ausgewählten Wert dem Feld favorite_colors zuzuweisen. Sobald die gewünschte Option ausgewählt ist, wird das aktualisierte Dokument gespeichert.

1. Initialisieren Sie 'pdf_facades.Form()', um Formularfelder zu verwalten und zu aktualisieren.
1. Rufen Sie 'bind_pdf()' auf, um das Quell-PDF anzuhängen, das Listenfelder oder Mehrfachauswahlfelder enthält.
1. Verwenden Sie 'fill_field()', um einen Wert aus den verfügbaren Optionen auszuwählen.
1. Speichern Sie das aktualisierte Document.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill List Box / Multi-Select Fields
def fill_list_box_fields(infile, outfile):
    """Fill list box and multi-select fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill list box / multi-select fields by name
    pdf_form.fill_field("favorite_colors", "Red")

    # Save updated PDF
    pdf_form.save(outfile)
```
