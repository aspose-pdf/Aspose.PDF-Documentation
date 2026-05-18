---
title: Kreisannotation hinzufügen
type: docs
weight: 10
url: /de/python-net/add-circle-annotation/
description: Dieses Beispiel bindet ein Eingabe-PDF, erstellt eine Kreisannotation auf der ersten Seite und speichert das modifizierte Dokument.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Kreisannotation zu einem PDF mit PdfContentEditor in Python hinzufügen
Abstract: Dieses Beispiel zeigt, wie man eine Kreisannotation zu einem PDF-Dokument mit Aspose.PDF for Python via the Facades API hinzufügt. Es zeigt, wie man Anmerkungsgrenzen definiert, Inhaltstext festlegt, Farbe und Erscheinungsbild konfiguriert und das aktualisierte Dokument speichert.
---

Kreisannotationen sind nützlich, um Interessensbereiche in einem PDF-Dokument hervorzuheben. Mit [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Sie können kreisförmige Formen erstellen, indem Sie das Rechteck angeben, das die Grenzen des Kreises definiert, zusammen mit Anmerkungstext, Farbe, Fülloptionen, Seitenzahl und Randbreite.

1. Erstellen Sie das PdfContentEditor-Objekt.
1. Binden Sie das Eingabe-PDF.
1. Definieren Sie die Kreisgrenzen.
1. Fügen Sie die Kreisannotation hinzu.
1. Speichern Sie das aktualisierte Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_circle_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create CircleAnnotation object
    rect = apd.Rectangle(300, 300, 400, 400)
    contents = "This is circle annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, False, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```
