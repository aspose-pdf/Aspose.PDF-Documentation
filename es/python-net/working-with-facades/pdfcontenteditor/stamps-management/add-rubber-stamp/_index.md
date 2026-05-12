---
title: Agregar sello de goma
linktitle: Agregar sello de goma
type: docs
weight: 10
url: /es/python-net/add-rubber-stamp/
description: Este ejemplo enlaza un PDF de entrada, agrega un sello de goma verde “Approved” a las primeras cuatro páginas y guarda el documento modificado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar una anotación de sello de goma a un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo muestra cómo agregar una anotación de sello de goma a un documento PDF usando Aspose.PDF for Python via the Facades API. Los sellos de goma le permiten marcar visualmente las páginas con aprobaciones, revisiones o etiquetas personalizadas.
---

Las anotaciones de sello de goma se usan comúnmente en PDFs para indicar aprobación, estado de revisión u otras notas. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puede definir un rectángulo para el sello, establecer su texto y comentarios, elegir un color y aplicarlo a varias páginas de un documento.

1. Crea una instancia de PdfContentEditor.
1. Vincula el documento PDF de entrada.
1. Recorrer las páginas 1–34.
1. Agregar una anotación de sello de goma con texto personalizado, comentarios y color.
1. Guarda el documento PDF actualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_rubber_stamp(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    for i in range(1, 5):
        content_editor.create_rubber_stamp(
            i,
            apd.Rectangle(120, 450, 180, 60),
            "Approved",
            "Approved by reviewer",
            apd.Color.green,
        )
    # Save updated document
    content_editor.save(outfile)
```
