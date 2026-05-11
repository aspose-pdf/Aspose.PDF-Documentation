---
title: Eliminar sello por ID
type: docs
weight: 85
url: /es/python-net/delete-stamp-by-ids-examples/
description:
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar sellos de caucho por ID único o múltiple en un PDF usando PdfContentEditor
Abstract: Este ejemplo muestra cómo eliminar anotaciones de sellos de caucho de un PDF basándose en sus IDs únicos usando Aspose.PDF for Python via the Facades API. Cubre tanto la eliminación por una sola ID como la eliminación por múltiples IDs.
---

Al trabajar con PDFs que contienen múltiples sellos, a menudo es necesario eliminar sellos específicos sin afectar a los demás. Usando la eliminación basada en ID, puedes controlar con precisión qué sellos eliminar:

- 'delete_stamp_by_id(stamp_id, page_number)' – elimina un solo sello por su ID en una página específica
- 'delete_stamp_by_ids(page_number, stamp_ids)' – elimina varios sellos por sus IDs en una página dada

1. Crear un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instancia.
1. Vincula el documento PDF de entrada.
1. Añade dos sellos de goma con IDs distintos.
1. Elimina sellos utilizando tanto el método de eliminación por ID único como el de eliminación por varios IDs.
1. Guardar el PDF actualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_ids_examples(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Create two stamps on page 1 so they can be deleted by ID
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(120, 320, 180, 60),
        "Draft",
        "Delete by single ID",
        apd.Color.orange,
    )
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(120, 250, 180, 60),
        "Draft",
        "Delete by multiple IDs",
        apd.Color.orange,
    )

    # Delete by single ID overload and by IDs overload
    content_editor.delete_stamp_by_id(1, 1)
    content_editor.delete_stamp_by_ids(1, [2])

    # Save updated document
    content_editor.save(outfile)
```

