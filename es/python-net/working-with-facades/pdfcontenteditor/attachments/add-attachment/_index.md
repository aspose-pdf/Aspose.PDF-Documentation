---
title: Agregar archivo adjunto
linktitle: Agregar archivo adjunto
type: docs
weight: 10
url: /es/python-net/add-attachment/
description: Este ejemplo enlaza un PDF de entrada, adjunta un archivo externo a la primera página y guarda el PDF modificado con el archivo adjunto incrustado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar archivos adjuntos a un PDF usando Python
Abstract: Este ejemplo muestra cómo adjuntar archivos externos a un documento PDF usando Aspose.PDF for Python a través de la API Facades. Demuestra cómo enlazar un PDF, agregar archivos adjuntos con descripciones y guardar el documento actualizado.
---

Los archivos adjuntos en PDFs le permiten incluir documentos suplementarios, imágenes u otros recursos directamente dentro del PDF. Con [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puede adjuntar archivos a páginas específicas de forma programática, establecer el nombre del adjunto y proporcionar una descripción.

1. Crea el objeto PdfContentEditor.
1. Vincular el PDF de entrada.
1. Abra el archivo de adjunto.
1. Agregue el adjunto al PDF.
1. Guardar el documento actualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment to page 1
    with open(attachment_file, "rb") as attachment_stream:
        content_editor.add_document_attachment(
            attachment_stream,
            path.basename(attachment_file),
            "This is a sample attachment for demonstration purposes.",
        )
    # Save updated document
    content_editor.save(outfile)
```
