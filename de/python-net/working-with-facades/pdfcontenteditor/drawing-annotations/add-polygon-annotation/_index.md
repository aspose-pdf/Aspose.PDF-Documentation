---
title: Polygon-Anmerkung hinzufügen
type: docs
weight: 40
url: /de/python-net/add-polygon-annotation/
description: Dieses Beispiel bindet ein Eingabe‑PDF, zeichnet ein gefülltes Polygon auf der ersten Seite und speichert das modifizierte Dokument mit einer Anmerkung.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Polygon-Anmerkung zu einem PDF mit PdfContentEditor in Python hinzufügen
Abstract: Dieses Beispiel zeigt, wie man einer PDF‑Datei eine Polygon‑Anmerkung hinzufügt, indem man Aspose.PDF für Python über die Facades‑API verwendet. Es demonstriert, wie man Polygon‑Scheitelpunkte, Randstil, Anmerkungsgrenzen, beschreibenden Text definiert und das aktualisierte Dokument speichert.
---

Polygon‑Anmerkungen werden verwendet, um unregelmäßige Bereiche oder Formen in einem PDF hervorzuheben, visuelle Akzente zu setzen oder bestimmte Regionen zu markieren. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), können Sie Polygone erstellen, indem Sie die Koordinaten der Scheitelpunkte, den Randstil, die Seitennummer und das Anmerkungsrechteck angeben.

1. Erstellen Sie das PdfContentEditor-Objekt.
1. Binden Sie das Eingabe-PDF.
1. Polygon-Eigenschaften konfigurieren.
1. Polygon-Annotation hinzufügen.
1. Speichern Sie das aktualisierte Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_polygon_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0  # 0 - Solid
    line_info.vertice_coordinate = [100, 200, 150, 260, 220, 220, 200, 160]
    content_editor.create_polygon(
        line_info,
        1,
        apd.Rectangle(90, 150, 150, 120),
        "This is polygon annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
