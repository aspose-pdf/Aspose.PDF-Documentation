---
title: Feldaussehen festlegen
type: docs
weight: 50
url: /de/python-net/set-field-appearance/
description: Dieses Beispiel zeigt, wie das visuelle Aussehen eines PDF-Formularfelds mit Aspose.PDF for Python geändert werden kann.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Formularfeldaussehen mit Python festlegen
Abstract: Dieser Artikel erklärt, wie man ein PDF öffnet, das Aussehen eines Formularfelds mit der FormEditor-Klasse festlegt und das aktualisierte Dokument speichert. Das Beispiel setzt das Aussehen eines Feldes namens "First Name" auf unsichtbar, indem es das AnnotationFlags.INVISIBLE-Flag verwendet.
---

PDF-Formularfelder unterstützen Aussehen-Flags, die Sichtbarkeit, Druckbarkeit und Interaktivität steuern. Mit Aspose.PDF for Python können Entwickler diese Flags programmgesteuert für bestimmte Formularfelder ändern.

Verwenden des [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Klasse, Entwickler können diese Flags ändern, um Formularfelder in einem interaktiven PDF auszublenden, anzuzeigen oder das Verhalten anzupassen.

1. Öffnen Sie ein vorhandenes PDF-Dokument.
1. Erstellen Sie ein FormEditor-Objekt.
1. Setze das Erscheinungsbild des Feldes mit dem Namen "First Name" auf unsichtbar.
1. Speichern Sie das aktualisierte Dokument.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_appearance(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field appearance to invisible
    if not form_editor.set_field_appearance(
        "First Name", ap.annotations.AnnotationFlags.INVISIBLE
    ):
        raise Exception(
            "Failed to set field appearance. Field may not support appearance flags."
        )

    # Save updated document
    form_editor.save(outfile)
```
