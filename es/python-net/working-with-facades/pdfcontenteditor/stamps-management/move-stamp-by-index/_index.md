---
title: Mover Sello Por Índice
type: docs
weight: 90
url: /es/python-net/move-stamp-by-index/
description: Cómo reposicionar anotaciones de sello de goma en un PDF usando su índice en una página con Aspose.PDF for Python
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mover sellos de goma en un PDF usando posicionamiento basado en índices
Abstract: Este ejemplo muestra cómo reposicionar anotaciones de sello de goma en un PDF usando su índice en una página con Aspose.PDF for Python a través de la API Facades. Destaca la creación de varios sellos y su preparación para operaciones de movimiento.
---

En la edición de PDF, puede ser necesario ajustar la posición de los sellos de goma existentes. Este fragmento de código muestra cómo:

- Agregar varios sellos en la misma página
- Prepararlos para reposicionarlos usando su índice
- Opcionalmente mover un sello especificando su página, índice y nuevas coordenadas

El método 'move_stamp(page_number, stamp_index, new_x, new_y)' puede reposicionar los sellos de manera precisa.

1. Crear un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objeto.
1. Vincula el PDF al editor.
1. Añade varios sellos de goma a una página.
1. Guarda el documento antes de realizar operaciones de movimiento.
1. Mover un sello específico por su índice.
1. Guarde el PDF actualizado.

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
