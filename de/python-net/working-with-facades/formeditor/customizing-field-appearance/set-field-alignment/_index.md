---
title: Feldausrichtung festlegen
type: docs
weight: 30
url: /de/python-net/set-field-alignment/
description: Dieses Beispiel demonstriert, wie man die Textausrichtung eines Formularfelds in einem PDF-Dokument mit Aspose.PDF for Python festlegt.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Textausrichtung für PDF-Formularfelder mit Python festlegen
Abstract: Dieser Artikel erklärt, wie man ein PDF-Dokument öffnet, die Ausrichtung eines bestimmten Feldes mit der FormEditor-Klasse festlegt und das aktualisierte PDF speichert. Das Beispiel legt die Textausrichtung eines Feldes mit dem Namen "First Name" auf zentriert fest.
---

PDF-Formularfelder erfordern häufig eine angepasste Textausrichtung, um ein konsistentes und professionelles Layout zu gewährleisten. Mit Aspose.PDF for Python können Entwickler programmgesteuert die Ausrichtung des Textinhalts eines Formularfelds festlegen.

Der [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class, in Kombination mit dem [FormFieldFacade](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) Konstanten, ermöglichen Entwicklern, die Ausrichtung vorhandener Formularfelder programmgesteuert zu ändern.

1. Öffnen Sie ein vorhandenes PDF-Dokument.
1. Erstellen Sie ein FormEditor-Objekt.
1. Setzen Sie die Ausrichtung eines Feldes mit dem Namen "First Name" auf zentriert.
1. Speichern Sie das geänderte Dokument.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_alignment(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field alignment to center
    if form_editor.set_field_alignment(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_CENTER
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception(
            "Failed to set field alignment. Field may not support alignment."
        )
```
