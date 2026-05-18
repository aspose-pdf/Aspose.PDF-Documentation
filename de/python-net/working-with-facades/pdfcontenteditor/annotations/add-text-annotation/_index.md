---
title: Textanmerkungen hinzufügen
type: docs
weight: 50
url: /de/python-net/add-text-annotation/
description: Fügen Sie Textanmerkungen zu einem PDF-Dokument hinzu, indem Sie die PdfContentEditor-Klasse in Aspose.PDF für Python via .NET verwenden.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Textanmerkungen in Python hinzufügen
Abstract: Erfahren Sie, wie Sie Textanmerkungen zu einem PDF-Dokument hinzufügen, indem Sie die PdfContentEditor-Klasse in Aspose.PDF für Python via .NET verwenden. Dieses Beispiel zeigt, wie man eine Textanmerkung an einer bestimmten Position platziert, ihren Titel und Inhalt definiert und die aktualisierte PDF-Datei speichert.
---

Dieser Artikel zeigt, wie man eine Textanmerkung zu einem PDF-Dokument hinzufügt, indem man die [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Klasse in Aspose.PDF.

Textanmerkungen ermöglichen es Ihnen, Kommentare, Notizen oder zusätzliche Informationen an bestimmten Teilen einer PDF-Seite anzubringen. Diese Anmerkungen können als Symbole angezeigt werden und vom Benutzer beim Betrachten des Dokuments erweitert werden.

In diesem Beispiel:

- Ein PDF-Dokument wird in den PdfContentEditor geladen.
- Eine Textannotation wird an einer bestimmten Position auf der Seite hinzugefügt.
- Die Annotation enthält einen Titel, Inhalt, Symboltyp und Sichtbarkeitseinstellungen.
- Das geänderte Dokument wird in einer neuen Datei gespeichert.

1. Erstellen Sie ein PdfContentEditor-Objekt.
1. Binden Sie das Eingabe-PDF-Dokument.
1. Definieren Sie die Annotationsposition.
1. Textannotation hinzufügen.
1. Speichere das aktualisierte PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add text annotation to page 1
    content_editor.create_text(
        apd.Rectangle(100, 400, 50, 50),
        "Text Annotation",
        "This is a text annotation",
        True,
        "Insert",
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```
