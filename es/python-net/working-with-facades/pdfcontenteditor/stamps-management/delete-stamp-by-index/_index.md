---
title: Eliminar sello por índice
type: docs
weight: 50
url: /es/python-net/delete-stamp-by-index/
description: Este ejemplo crea dos sellos de goma en la página 2. Después de eso, se puede eliminar un sello especificando su índice.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar un sello de goma por índice en un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo demuestra cómo eliminar una anotación de sello de goma en un PDF usando su índice con Aspose.PDF for Python a través de la API Facades. Muestra cómo agregar varios sellos y luego eliminar uno de ellos según su orden en la página.
---

Cuando existen varios sellos de goma en una página, puedes eliminar uno específico usando su índice. El método delete_stamp() permite eliminar anotaciones según su secuencia, lo que es útil cuando no llevas un registro de los IDs de los sellos pero conoces su orden.

1. Crear un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instancia.
1. Vincular el documento PDF de entrada.
1. Vincular el archivo PDF de entrada a la instancia de PdfContentEditor usando bind_pdf(infile).
1. Llamar a 'delete_stamp(1, [2, 3])' para eliminar el sello con índice 1 de las páginas 2 y 3.
1. Guardar el documento PDF modificado en el archivo de salida usando save(outfile).

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    content_editor.delete_stamp(1, [2, 3])
    # Save updated document
    content_editor.save(outfile)
```
