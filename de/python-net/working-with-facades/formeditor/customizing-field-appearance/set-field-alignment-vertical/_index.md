---
title: Vertikale Feldausrichtung festlegen
type: docs
weight: 40
url: /de/python-net/set-field-alignment-vertical/
description: Dieses Beispiel demonstriert, wie die vertikale Ausrichtung eines Formularfelds in einem PDF-Dokument mithilfe von Aspose.PDF for Python festgelegt wird.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Vertikale Ausrichtung für PDF-Formularfelder mit Python festlegen
Abstract: Dieser Artikel erklärt, wie man ein PDF öffnet, die vertikale Ausrichtung für ein Feld mithilfe der FormEditor-Klasse festlegt und das aktualisierte PDF speichert. Das Beispiel legt die vertikale Ausrichtung eines Feldes mit dem Namen "First Name" an den unteren Rand des Feldbereichs fest.
---

PDF-Formularfelder können Text enthalten, der für ein konsistentes und professionelles Erscheinungsbild einer korrekten vertikalen Ausrichtung bedarf. Mit Aspose.PDF for Python können Entwickler die vertikale Ausrichtung von Formularfeldern programmgesteuert ändern.
Die vertikale Ausrichtung ermöglicht es Entwicklern, zu steuern, ob der Text eines Feldes oben, mittig oder unten im Begrenzungsrahmen des Feldes angezeigt wird, wodurch das Layout und die Lesbarkeit der Formulardaten verbessert werden.

Verwenden des [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Klasse und die [FormFieldFacade](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) Konstanten, Entwickler können die vertikale Ausrichtung programmgesteuert anpassen, um ein konsistentes Formularlayout zu erreichen:

1. Öffnen Sie ein vorhandenes PDF-Dokument.
1. Erstellen Sie ein FormEditor-Objekt.
1. Setzen Sie die vertikale Ausrichtung eines Feldes namens "First Name" auf unten.
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


def set_field_alignment_vertical(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Attempt to set vertical alignment of the "First Name" field to bottom
    if form_editor.set_field_alignment_v(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_BOTTOM
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception(
            "Failed to set field vertical alignment. Field may not support vertical alignment."
        )
```
