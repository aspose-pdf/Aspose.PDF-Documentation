---
title: Eliminar sellos globalmente
linktitle: Eliminar sellos globalmente
type: docs
weight: 60
url: /es/python-net/delete-stamps-globally/
description: Este ejemplo demuestra cómo eliminar anotaciones de sellos de goma globalmente en todas las páginas de un PDF usando Aspose.PDF for Python via the Facades API. Muestra cómo quitar los sellos por ID sin especificar páginas individuales.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar sellos de goma globalmente en un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo demuestra cómo eliminar anotaciones de sellos de goma globalmente en todas las páginas de un PDF usando Aspose.PDF for Python via the Facades API. Muestra cómo quitar los sellos por ID sin especificar páginas individuales.
---

Al trabajar con múltiples páginas, es posible que necesite eliminar ciertos sellos en todo el documento. Los métodos \u0027delete_stamp_by_id()\u0027 y \u0027delete_stamp_by_ids()\u0027 le permiten eliminar sellos globalmente por sus identificadores, eliminando la necesidad de iterar manualmente a través de cada página.

1. Crear un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instancia.
1. Vincula el documento PDF de entrada.
1. Agregar sellos de goma a múltiples páginas.
1. Eliminar sellos globalmente usando sus IDs.
1. Guarda el documento PDF actualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamps_globally(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Add stamps across multiple pages so global deletion is meaningful
    for page in range(1, 5):
        content_editor.create_rubber_stamp(
            page,
            apd.Rectangle(120, 500, 180, 60),
            "Draft",
            "Stamp for global deletion",
            apd.Color.gray,
        )

    # delete_stamp_by_id without page number removes stamp ID from all pages
    content_editor.delete_stamp_by_id(1)
    # delete_stamp_by_ids without page number removes a list of IDs from all pages
    content_editor.delete_stamp_by_ids([2, 3])

    # Save updated document
    content_editor.save(outfile)
```
