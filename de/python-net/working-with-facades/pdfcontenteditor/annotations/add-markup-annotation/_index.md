---
title: Markup-Anmerkungen hinzufügen
type: docs
weight: 30
url: /de/python-net/add-markup-annotation/
description: Dieses Beispiel bindet ein Eingabe-PDF, fügt der ersten Seite vier verschiedene Markup-Anmerkungen hinzu und speichert das aktualisierte Dokument. Jede Anmerkung demonstriert einen anderen Markup-Stil und eine andere Farbe.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Highlight-, Unterstreichungs-, Durchstreichungs- und Wellenlinien-Markup-Anmerkungen in einem PDF mit Python hinzufügen
Abstract: Dieses Beispiel zeigt, wie man mehrere Markup-Anmerkungen – Highlight, Unterstreichung, Durchstreichung und Squiggly – zu einem PDF-Dokument mithilfe von Aspose.PDF for Python via the Facades API hinzufügt. Das Beispiel demonstriert, wie man Anmerkungsbereiche definiert, Markup-Typen festlegt, Farben anwendet und das geänderte Dokument speichert.
---

Markup-Anmerkungen werden verwendet, um Text in einem PDF zu betonen oder zu überprüfen. Mit PdfContentEditor können Sie programmgesteuert verschiedene Markup-Stile anwenden, indem Sie einen Rechteckbereich, den Kommentartext, den Markup-Typ, die Seitennummer und die Farbe angeben.

1. Erstelle das [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Objekt.
1. Binden Sie das Eingabe-PDF.
1. Annotationsrechtecke definieren.
1. Markup-Anmerkungen hinzufügen.
1. Speichern Sie das aktualisierte Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_markup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add markup annotation to page 1
    content_editor.create_markup(
        apd.Rectangle(120, 440, 200, 20),
        "This is a highlight annotation",
        0,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 542, 200, 20),
        "This is a underline annotation",
        1,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(120, 568, 200, 20),
        "This is a strikeout annotation",
        2,
        1,
        apd.Color.orange_red,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 598, 200, 20),
        "This is a squiggly annotation",
        3,
        1,
        apd.Color.dark_blue,
    )
    # Save updated document
    content_editor.save(outfile)
```
