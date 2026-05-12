---
title: Mover sello por índice
linktitle: Mover sello por índice
type: docs
weight: 50
url: /es/python-net/move-stamp-by-index/
description: Este ejemplo crea dos sellos de caucho en la página 2. Después de eso, un sello puede ser movido especificando su índice y nuevas coordenadas.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mover un sello de caucho por índice en un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo demuestra cómo reposicionar una anotación de sello de caucho en un PDF usando su índice con Aspose.PDF for Python via the Facades API. Muestra cómo agregar varios sellos y luego mover uno de ellos según su orden en la página.
---

Cuando existen varios sellos de caucho en una página, puedes mover uno específico usando su índice. El método move_stamp() permite reposicionar anotaciones según su secuencia, lo cual es útil cuando no rastreas los IDs de los sellos pero conoces su orden.

1. Crear un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instancia.
1. Vincula el documento PDF de entrada.
1. Agregar dos anotaciones de sello de caucho en la misma página.
1. Demostrar cómo mover un sello usando su índice.
1. Guarda el documento PDF actualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 380, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 480, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )
    content_editor.save(outfile)

    # Move first stamp on page 1 by index
    # content_editor.move_stamp(1, 1, 10, 10)
    # Save updated document
    content_editor.save(outfile)
```
