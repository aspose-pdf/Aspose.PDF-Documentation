---
title: Mover sello por ID
linktitle: Mover sello por ID
type: docs
weight: 80
url: /es/python-net/move-stamp-by-id-example/
description: En este ejemplo, se agrega un sello de goma a la página 1 y luego se mueve a una nueva posición usando su ID antes de guardar el documento actualizado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mover un sello de goma por ID en un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo demuestra cómo reposicionar una anotación de sello de goma existente en un PDF usando Aspose.PDF for Python a través de la API Facades. Muestra cómo crear un sello y luego moverlo programáticamente usando su ID.
---

Después de agregar una anotación de sello de goma a un PDF, es posible que necesite ajustar su posición. El método ‘move_stamp_by_id()’ le permite reubicar un sello basado en su identificador, sin recrearlo. Esto es útil en flujos de trabajo automatizados donde la colocación del sello debe ajustarse dinámicamente.

1. Crear un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instancia.
1. Vincula el documento PDF de entrada.
1. Agregar una anotación de sello de goma.
1. Mueve el sello usando su ID.
1. Guarda el documento PDF actualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_id_example(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(300, 420, 180, 60),
        "Approved",
        "Move this stamp by ID",
        apd.Color.green,
    )

    # Move stamp by ID overload
    content_editor.move_stamp_by_id(1, 1, 240, 360)

    # Save updated document
    content_editor.save(outfile)
```    
