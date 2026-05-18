---
title: Quadrat-Anmerkung hinzufügen
type: docs
weight: 60
url: /de/python-net/add-square-annotation/
description: Dieses Beispiel bindet ein Eingabe‑PDF, fügt auf der ersten Seite eine ausgefüllte blaue Quadrat-Anmerkung hinzu und speichert das modifizierte Dokument.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Quadrat-Anmerkung zu einem PDF mit PdfContentEditor in Python hinzufügen
Abstract: Dieses Beispiel demonstriert, wie man eine Quadrat-Anmerkung zu einem PDF-Dokument hinzufügt, wobei Aspose.PDF for Python über die Facades‑API verwendet wird. Es zeigt, wie man das Anmerkungsrechteck, den Textinhalt, die Farbe, Fülloptionen definiert und das aktualisierte Dokument speichert.
---

Quadrat-Anmerkungen werden häufig verwendet, um Interessensbereiche hervorzuheben, wichtige Abschnitte zu markieren oder visuelle Hinweise in einem PDF-Dokument zu geben. Verwenden [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), können Sie Quadrat‑ (oder Kreis‑) Anmerkungen erstellen, indem Sie das Begrenzungsrechteck, den Inhaltstext, die Randfarbe, die Fülloption, die Seitenzahl und die Randbreite angeben.

1. Erstellen Sie das PdfContentEditor-Objekt.
1. Binden Sie das Eingabe-PDF.
1. Definieren Sie die Square-Anmerkung.
1. Fügen Sie die Square-Anmerkung hinzu.
1. Speichern Sie das aktualisierte Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_square_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create SquareAnnotation object
    rect = apd.Rectangle(100, 300, 200, 400)
    contents = "This is square annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, True, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```
