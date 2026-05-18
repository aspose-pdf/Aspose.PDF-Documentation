---
title: Dokumentenaktion hinzufügen
type: docs
weight: 20
url: /de/python-net/add-document-action/
description: Dieses Beispiel fügt eine JavaScript‑Warnung hinzu, die angezeigt wird, wenn das PDF geöffnet wird. Das Skript ist an das Dokument‑Öffnen‑Ereignis angehängt und wird in unterstützten PDF‑Betrachtern automatisch ausgeführt.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaScript‑Aktion zum Öffnen eines Dokuments zu einem PDF mit Python hinzufügen
Abstract: Dieses Beispiel zeigt, wie man eine dokumentbezogene JavaScript‑Aktion hinzufügt, die ausgelöst wird, wenn ein PDF geöffnet wird. Mit Aspose.PDF for Python via the Facades API demonstriert das Beispiel, wie man ein Dokument bindet, eine Öffnen‑Ereignis‑Aktion zuweist und das aktualisierte PDF speichert.
---

Dokumentbezogene Aktionen ermöglichen es Ihnen, Verhaltensweisen zu definieren, die automatisch ausgeführt werden, wenn bestimmte Ereignisse eintreten, wie z. B. das Öffnen eines PDFs. Mit [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), können Sie JavaScript‑Code an diese Ereignisse anhängen. Dies kann für Benachrichtigungen, Validierungslogik oder interaktive Workflows verwendet werden.

1. Erstellen Sie das PdfContentEditor-Objekt.
1. Binden Sie das Eingabe-PDF.
1. Dokumentebene‑Aktion hinzufügen.
1. Speichern Sie das aktualisierte Document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_document_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add JavaScript action for document open event
    content_editor.add_document_additional_action(
        content_editor.DOCUMENT_OPEN,
        "app.alert('Document opened with PdfContentEditor action');",
    )
    # Save updated document
    content_editor.save(outfile)
```
