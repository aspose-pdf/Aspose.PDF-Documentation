---
title: Eliminar imágenes de PDF
linktitle: Eliminar imágenes de PDF
type: docs
weight: 20
url: /es/python-net/delete-images/
description:
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar imágenes específicas de una página PDF usando PdfContentEditor en Python
Abstract: Este ejemplo muestra cómo eliminar imágenes específicas de un documento PDF usando Aspose.PDF for Python via the Facades API. Muestra cómo seleccionar imágenes en una página específica y guardar el documento actualizado.
---

A veces, puede que desee eliminar solo ciertas imágenes de un PDF en lugar de borrar todos los elementos visuales. Con [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puede eliminar imágenes seleccionadas especificando el número de página y el índice de la imagen.

Este fragmento de código enlaza un PDF de entrada, elimina la segunda imagen en la página 1 y guarda el PDF modificado, dejando intactas las demás imágenes.

1. Cree una instancia de PdfContentEditor.
1. Enlace el documento PDF de entrada.
1. Elimine imágenes específicas de una página designada.
1. Guarde el documento PDF actualizado.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_images(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete image on page 1
    content_editor.delete_image(1, [2])
    # Save updated document
    content_editor.save(outfile)
```
