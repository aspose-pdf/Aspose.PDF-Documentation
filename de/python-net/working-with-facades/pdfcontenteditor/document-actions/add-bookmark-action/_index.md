---
title: Lesezeichen hinzufügen Aktion
type: docs
weight: 10
url: /de/python-net/add-bookmark-action/
description: Dieses Beispiel bindet ein Eingabe-PDF, erstellt ein Lesezeichen mit der Bezeichnung "PdfContentEditor Bookmark", das zu Seite 1 navigiert, und speichert das aktualisierte Dokument.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Lesezeichen mit Navigationsaktion in einem PDF mit Python erstellen
Abstract: Dieses Beispiel zeigt, wie Sie ein Lesezeichen mit einer Navigationsaktion zu einem PDF-Dokument hinzufügen können, wobei Aspose.PDF für Python über die Facades API verwendet wird. Es zeigt, wie Sie den Lesezeichentext, das Erscheinungsbild und eine Aktion konfigurieren, die den Benutzer zu einer bestimmten Seite leitet.
---

Lesezeichen ermöglichen schnelle Navigation innerhalb von PDF-Dokumenten. Verwenden [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), können Sie programmgesteuert Lesezeichen erstellen und Aktionen zuweisen, z. B. das Navigieren zu einer Seite. Sie können das Erscheinungsbild des Lesezeichens ebenfalls anpassen, einschließlich Farb- und Stiloptionen wie fett oder kursiv.

1. Erstellen Sie das PdfContentEditor-Objekt.
1. Binden Sie das Eingabe-PDF.
1. Lesezeichen-Eigenschaften definieren.
1. Lesezeichen-Aktion zuweisen.
1. Speichern Sie das aktualisierte Document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_bookmark_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a bookmark action to navigate to page 1
    content_editor.create_bookmarks_action(
        "PdfContentEditor Bookmark",
        apd.Color.blue,
        True,
        False,
        "",
        "GoTo",
        "1",
    )
    # Save updated document
    content_editor.save(outfile)
```