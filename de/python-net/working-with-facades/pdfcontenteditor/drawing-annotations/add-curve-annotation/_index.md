---
title: Kurven-Anmerkung hinzufügen
type: docs
weight: 20
url: /de/python-net/add-curve-annotation/
description: Dieses Beispiel bindet ein Eingabe‑PDF, zeichnet eine gestrichelte Kurve auf der ersten Seite und speichert das geänderte Dokument.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Kurven-Anmerkung zu einem PDF mit PdfContentEditor in Python hinzufügen
Abstract: Dieses Beispiel demonstriert, wie man eine Kurven‑Anmerkung zu einem PDF‑Dokument mithilfe von Aspose.PDF for Python via the Facades API hinzufügt. Es zeigt, wie man Kurven‑Scheitelpunkte, Rahmenstil, Anmerkungsgrenzen, Textinhalt definiert und das aktualisierte Dokument speichert.
---

Kurven‑Anmerkungen werden verwendet, um unregelmäßige Pfade oder Formen in einem PDF hervorzuheben, visuelle Betonung zu geben oder wichtige Bereiche zu markieren. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Sie können Kurven zeichnen, indem Sie eine Sequenz von Scheitelpunkten, Rahmenstil, Sichtbarkeit, Anmerkungsrechteck und beschreibenden Text angeben.

1. Erstellen Sie das PdfContentEditor-Objekt.
1. Binden Sie das onput PDF.
1. Konfigurieren Sie die Curve-Eigenschaften.
1. Zeichnen Sie die Curve-Anmerkung.
1. Speichern Sie das aktualisierte Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_curve_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 1  # 1 - Dashed
    line_info.vertice_coordinate = [120, 520, 160, 560, 220, 540, 280, 580]
    line_info.visibility = True
    content_editor.draw_curve(
        line_info,
        1,
        apd.Rectangle(110, 510, 220, 100),
        "This is curve annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
