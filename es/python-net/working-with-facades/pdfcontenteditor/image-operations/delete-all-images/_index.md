---
title: Eliminar todas las imágenes del PDF
linktitle: Eliminar todas las imágenes del PDF
type: docs
weight: 10
url: /es/python-net/delete-all-images/
description: Eliminar todas las imágenes de un documento PDF usando Aspose.PDF for Python via the Facades API.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar todas las imágenes de un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo demuestra cómo eliminar todas las imágenes de un documento PDF usando Aspose.PDF for Python via the Facades API. Muestra cómo enlazar un PDF, eliminar todas las imágenes incrustadas y guardar el documento actualizado.
---

Los documentos PDF a menudo contienen imágenes para ilustraciones, marca o decoración. Puede haber casos en los que necesite eliminar todas las imágenes de un PDF, como reducir el tamaño del archivo, proteger imágenes sensibles o preparar una versión solo de texto.

Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)", puede eliminar programáticamente todas las imágenes de un PDF, asegurando que el documento solo contenga contenido textual. Este ejemplo enlaza un PDF de entrada, elimina todas las imágenes y guarda el archivo modificado."

1. Crear el objeto PdfContentEditor.
1. Vincular el PDF de entrada.
1. Eliminar todas las imágenes.
1. Guarda el Documento actualizado.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_all_image(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete all images from the document
    content_editor.delete_image()
    # Save updated document
    content_editor.save(outfile)
```
