---
title: Text ersetzen mit Regex
type: docs
weight: 30
url: /de/python-net/replace-text-regex/
description: In diesem Beispiel werden alle vierstelligen Zahlen im Dokument durch den Platzhalter "[NUMBER]" ersetzt. Dies ist nützlich, um sensible Daten zu maskieren, Inhalte zu normalisieren oder Dokumente zu anonymisieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Text ersetzen mit regulären Ausdrücken mit PdfContentEditor in Python
Abstract: Dieses Beispiel demonstriert, wie man Text in einem PDF mit regulären Ausdrücken mithilfe von Aspose.PDF für Python über die Facades-API ersetzt. Es zeigt, wie man nach Mustern sucht und alle Übereinstimmungen im gesamten Dokument ersetzt.
---

Reguläre Ausdrücke ermöglichen eine flexible Textersetzung basierend auf Mustern anstelle fester Zeichenketten. Durch das Aktivieren der Regex-Unterstützung in 'replace_text_strategy' können Sie dynamische Inhalte wie Zahlen, Datumsangaben oder formatierte Zeichenketten abgleichen.

1. Erstelle ein [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Instanz.
1. Binden Sie das Eingabe‑PDF‑Dokument.
1. Konfigurieren Sie die Ersetzungsstrategie, um Regex zu verwenden.
1. Ersetzen Sie übereinstimmende Muster im gesamten Dokument.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_regex(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text in the whole document
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text_strategy.is_regular_expression_used = True
    content_editor.replace_text(r"\d{4}", "[NUMBER]")
    # Save updated document
    content_editor.save(outfile)
```
