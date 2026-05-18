---
title: Linienannotation hinzufügen
type: docs
weight: 30
url: /de/python-net/add-line-annotation/
description: Dieses Beispiel bindet ein Eingabe-PDF, zeichnet eine rote Linienannotation mit quadratischen Linienenden und speichert das modifizierte PDF.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Linienannotation zu einem PDF mit PdfContentEditor in Python hinzufügen
Abstract: Dieses Beispiel zeigt, wie man mithilfe von Aspose.PDF for Python über die Facades-API eine Linienannotation zu einem PDF-Dokument hinzufügt. Es erklärt, wie man die Start- und Endpunkte der Linie, die Rechteckgrenzen, Darstellungseigenschaften definiert und das aktualisierte Dokument speichert.
---

Linienannotationen sind nützlich, um Text zu betonen, Beziehungen hervorzuheben oder die Aufmerksamkeit auf bestimmte Bereiche in einem PDF zu lenken. Mit [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), können Sie programmgesteuert Linienannotationen erstellen, indem Sie die Start- und Endpunkte, das Begrenzungsrechteck, die Farbe, den Rahmenstil und die Linienenden angeben.

1. Erstellen Sie das PdfContentEditor-Objekt.
1. Binden Sie das Eingabe-PDF.
1. Definiere Line Annotation-Eigenschaften.
1. Füge die Line-Annotation hinzu.
1. Speichern Sie das aktualisierte Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_line_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create LineAnnotation object
    rect = apd.Rectangle(100, 100, 200, 200)
    contents = "This is line annotation"
    content_editor.create_line(
        rect,
        contents,
        100,
        100,
        200,
        200,
        1,
        1,
        apd.Color.red,
        "Solid",
        [3, 2],
        ["Square"],
    )

    # Save output PDF file
    content_editor.save(outfile)
```
