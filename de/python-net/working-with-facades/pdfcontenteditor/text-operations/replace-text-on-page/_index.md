---
title: Text auf Seite ersetzen
type: docs
weight: 10
url: /de/python-net/replace-text-on-page/
description: In diesem Beispiel wird das erste Vorkommen des Wortes "PDF" durch "Page 1 Replaced Text" ersetzt, wobei eine bestimmte Schriftgröße verwendet wird.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Text auf einer bestimmten Seite mit PdfContentEditor in Python ersetzen
Abstract: Dieses Beispiel zeigt, wie man Text in einem PDF-Dokument mit Aspose.PDF for Python über die Facades-API ersetzt. Es demonstriert, wie das erste Vorkommen von Text auf einer Seite ersetzt und das aktualisierte Dokument gespeichert wird.
---

Das Ersetzen von Text ist eine häufige Anforderung beim Aktualisieren von PDF-Dokumenten. Verwenden [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), können Sie nach bestimmtem Text suchen und ihn durch neue Inhalte ersetzen. Die Eigenschaft 'replace_text_strategy' ermöglicht es Ihnen, zu steuern, wie viele Vorkommen ersetzt werden.

1. Erstellen Sie eine PdfContentEditor-Instanz.
1. Binden Sie das Eingabe‑PDF‑Dokument.
1. Konfigurieren Sie die Text-Ersetzungsstrategie.
1. Ersetzen Sie den Zieltext.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_on_page(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text on page 1
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_FIRST
    )
    content_editor.replace_text("PDF", "Page 1 Replaced Text", 14)
    # Save updated document
    content_editor.save(outfile)
```
