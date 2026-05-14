---
title: Agregar anotación de archivo adjunto desde flujo
linktitle: Agregar anotación de archivo adjunto desde flujo
type: docs
weight: 40
url: /es/python-net/add-file-attachment-annotation-from-stream/
description: El ejemplo carga un PDF, lee un archivo externo en un flujo de memoria, agrega una anotación de archivo adjunto a la primera página y guarda el documento modificado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar anotaciones de archivo adjunto a un PDF desde un flujo en Python
Abstract: Este ejemplo demuestra cómo crear una anotación de archivo adjunto en un PDF usando un flujo de archivo con Aspose.PDF for Python via the Facades API. Muestra cómo especificar la posición de la anotación, establecer una descripción, incluir un valor de opacidad y guardar el documento modificado.
---

Las anotaciones de archivo adjunto permiten incrustar archivos como iconos interactivos dentro de una página PDF. Usando un enfoque basado en flujos, puedes adjuntar archivos dinámicamente sin depender de una ruta de archivo física. Este método también admite la personalización de la apariencia de la anotación, incluida la opacidad.

1. Crear el objeto PdfContentEditor.
1. Vincular el PDF de entrada.
1. Leer el archivo adjunto como un flujo.
1. Agregar la anotación de archivo adjunto.
1. Guarda el Documento actualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_file_attachment_annotation_from_stream(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    with open(attachment_file, "rb") as source_stream:
        attachment_stream = BytesIO(source_stream.read())

    # Create file attachment annotation using stream+opacity overload
    content_editor.create_file_attachment(
        apd.Rectangle(130, 520, 20, 20),
        "Attachment annotation from stream",
        attachment_stream,
        path.basename(attachment_file),
        1,
        "Tag",
        0.75,
    )
    # Save updated document
    content_editor.save(outfile)
```
