---
title: PDF-Dokumentenlink hinzufügen
type: docs
weight: 50
url: /de/python-net/add-pdf-document-link/
description: Dieses Beispiel bindet ein Eingabe‑PDF, fügt einen grün gefärbten Link zu einer Seite in einem anderen PDF hinzu und speichert das modifizierte Dokument.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Dokumentenlink mit PdfContentEditor in Python hinzufügen
Abstract: Dieses Beispiel zeigt, wie man mithilfe von Aspose.PDF for Python über die Facades‑API einen Link zu einem anderen PDF‑Dokument hinzufügt. Es zeigt, wie man einen anklickbaren Bereich erstellt, der ein anderes PDF öffnet, und das aktualisierte Dokument speichert.
---

PDF‑Dokumentenlinks ermöglichen es Benutzern, nahtlos von einem PDF zu einem anderen zu navigieren. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Sie können ein anklickbares Rechteck definieren, das zu einer Seite in einer anderen PDF‑Datei verlinkt und Ihre Dokumente interaktiv und vernetzt macht.

1. Erstellen Sie eine PdfContentEditor-Instanz.
1. Binden Sie das Eingabe‑PDF‑Dokument.
1. Definieren Sie ein Rechteck für den anklickbaren Link.
1. Geben Sie die verknüpfte PDF-Datei, die Quellseite und die Zielseite an.
1. Setzen Sie die Linkfarbe.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_pdf_document_link(infile, linked_pdf, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add link to another PDF document
    content_editor.create_pdf_document_link(
        apd.Rectangle(140, 590, 240, 20),
        linked_pdf,
        1,
        1,
        apd.Color.green,
    )
    # Save updated document
    content_editor.save(outfile)
```
