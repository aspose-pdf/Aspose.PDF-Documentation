---
title: Reemplazar imágenes en PDF
linktitle: Reemplazar imágenes en PDF
type: docs
weight: 30
url: /es/python-net/replace-image/
description: Este ejemplo enlaza un PDF de entrada, reemplaza la primera imagen en la página 1 con una imagen nueva y guarda el documento modificado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Reemplazar una imagen en un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo muestra cómo reemplazar una imagen existente en un documento PDF usando Aspose.PDF for Python via the Facades API. Demuestra cómo seleccionar una imagen específica en una página y reemplazarla con una imagen nueva, luego guardar el PDF actualizado.
---

Los PDFs a menudo contienen imágenes que pueden necesitar ser actualizadas o reemplazadas, como logotipos, diagramas o fotos. Con [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puede reemplazar una imagen específica en una página dada proporcionando el número de página, el índice de la imagen y la ruta del archivo de la nueva imagen.

1. Cree una instancia de PdfContentEditor.
1. Enlace el documento PDF de entrada.
1. Reemplazar una imagen específica en una página dada.
1. Guarde el documento PDF actualizado.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_image(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace image on page 1
    content_editor.replace_image(1, 1, image_file)
    # Save updated document
    content_editor.save(outfile)
```
