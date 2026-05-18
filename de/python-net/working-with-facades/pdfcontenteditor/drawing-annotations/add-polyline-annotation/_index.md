---
title: Polyline-Annotation hinzufügen
type: docs
weight: 50
url: /de/python-net/add-polyline-annotation/
description: Das Beispiel bindet ein Eingabe‑PDF, erstellt eine solide Polylinie auf der ersten Seite und speichert das geänderte Dokument mit einer Anmerkung.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Polyline-Annotation zu einem PDF mit PdfContentEditor in Python hinzufügen
Abstract: Dieses Beispiel zeigt, wie man einer PDF‑Datei mit Aspose.PDF for Python via the Facades API eine Polyline‑Annotation hinzufügt. Es demonstriert, wie man eine Sequenz von Scheitelpunkten, den Randstil, das Annotationsrechteck, Text definiert und das aktualisierte Dokument speichert.
---

Polyline‑Annotationen ermöglichen es, eine Reihe zusammenhängender Liniensegmente in einem PDF hervorzuheben. Verwenden [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), können Sie eine Polylinie zeichnen, indem Sie die Koordinaten der Scheitelpunkte, den Randstil, die Seitenzahl und die Annotationsgrenzen angeben. Dies ist nützlich, um Pfade, Trends oder Verbindungen in Diagrammen und Dokumenten visuell darzustellen.

1. Erstellen Sie das PdfContentEditor-Objekt.
1. Binden Sie das Eingabe-PDF.
1. Konfigurieren Sie die Eigenschaften der Polylinie.
1. Fügen Sie die Polylinie-Annotation hinzu.
1. Speichern Sie das aktualisierte Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_polyline_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0  # 0 - Solid
    line_info.vertice_coordinate = [120, 420, 180, 460, 230, 430, 290, 470]
    content_editor.create_poly_line(
        line_info,
        1,
        apd.Rectangle(110, 410, 200, 90),
        "This is polyline annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
