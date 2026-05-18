---
title: Listeneintrag hinzufügen
type: docs
weight: 10
url: /de/python-net/add-list-item/
description: Dieses Beispiel demonstriert, wie man Elemente zu einem Listenfeld-Formularfeld in einem PDF-Dokument mit Aspose.PDF für Python hinzufügt.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Elemente zu PDF-Listenfeld-Feldern mit Python hinzufügen
Abstract: Dieser Artikel zeigt, wie man ein PDF-Dokument öffnet, Elemente an ein Listenfeld mit dem Namen "Country" anhängt und das aktualisierte Dokument speichert.
---

Listenfeld-Felder in PDFs ermöglichen es Benutzern, eine oder mehrere Optionen aus einem vordefinierten Satz auszuwählen. Mit Aspose.PDF für Python können Entwickler programmgesteuert neue Elemente zu diesen Feldern hinzufügen. Das [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Klasse stellt die ’add_list_item’-Methode bereit, um Elemente an ein bestehendes Listenfeld anzuhängen.

1. Öffnen Sie ein vorhandenes PDF-Formular.
1. Erstellen Sie ein FormEditor-Objekt.
1. Binden Sie das PDF an den FormEditor.
1. Fügen Sie dem Listenfeld "Country" Elemente hinzu.
1. Speichern Sie das aktualisierte Dokument.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Add list item to list box field
    form_editor.add_list_item("Country", ["New Zealand", "New Zealand"])
    # Save updated document
    form_editor.save(outfile)
```
