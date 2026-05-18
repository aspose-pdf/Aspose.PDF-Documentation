---
title: Einzeiliges Feld zu mehrzeiligem Feld
type: docs
weight: 80
url: /de/python-net/single-to-multiple/
description: Konvertieren Sie ein einzeiliges Textfeld in ein mehrzeiliges Feld in einem PDF-Dokument mit Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Konvertieren Sie ein einzeiliges Textfeld in ein mehrzeiliges Feld in einem PDF mit Python
Abstract: Dieses Beispiel zeigt, wie man ein einzeiliges Textfeld in ein mehrzeiliges Feld in einem PDF-Dokument mit Aspose.PDF for Python konvertiert. Der Code lädt ein vorhandenes PDF-Formular, ändert das angegebene Feld, um mehrere Textzeilen zu ermöglichen, und speichert das aktualisierte Dokument.
---

PDF-Formulare enthalten manchmal Textfelder, die für einzeilige Eingaben vorgesehen sind, was für bestimmte Datenarten nicht ausreichend sein kann. Mit Aspose.PDF for Python können Entwickler solche Felder einfach in mehrzeilige Textfelder konvertieren, ohne sie neu zu erstellen.

Verwenden des [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Klasse, Entwickler können vorhandene Textfelder ändern, ohne deren Position oder andere Eigenschaften zu beeinflussen.

1. Laden Sie das vorhandene PDF-Dokument.
1. Erstellen Sie eine FormEditor-Instanz.
1. Binden Sie das PDF-Dokument an den Editor.
1. Konvertieren Sie das ausgewählte Feld zu mehrzeilig.
1. Speichern Sie das aktualisierte Dokument.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def single2multiple(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Change a single-lined text field to a multiple-lined one
    form_editor.single_2_multiple("City")
    # Save updated document
    form_editor.save(outfile)
```

