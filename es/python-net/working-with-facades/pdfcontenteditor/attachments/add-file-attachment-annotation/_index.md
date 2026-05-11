---
title: Agregar anotación de archivo adjunto
linktitle: Agregar anotación de archivo adjunto
type: docs
weight: 30
url: /es/python-net/add-file-attachment-annotation/
description: El ejemplo asocia un PDF de entrada, agrega una anotación de archivo adjunto a la primera página usando la ruta del archivo y guarda el documento actualizado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar anotaciones de archivo adjunto a un PDF usando Python
Abstract: Este ejemplo muestra cómo crear una anotación de archivo adjunto en un PDF usando una ruta de archivo con Aspose.PDF for Python via the Facades API. Muestra cómo definir la ubicación de la anotación, establecer el texto de descripción, elegir un tipo de ícono y guardar el documento modificado.
---

Las anotaciones de archivo adjunto le permiten incrustar archivos externos como íconos interactivos en una página PDF. Usando la sobrecarga de ruta de archivo, puede adjuntar archivos directamente desde el disco sin abrir manualmente los flujos. Este método también le permite personalizar el ícono de la anotación y proporcionar una descripción para los usuarios.

1. Crear el [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objeto.
1. Vincular el PDF de entrada.
1. Defina el rectángulo de la anotación.
1. Agregar la anotación de adjunto de archivo.
1. Guardar el documento actualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_file_attachment_annotation(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create file attachment annotation on page 1
    content_editor.create_file_attachment(
        apd.Rectangle(100, 520, 20, 20),
        "Attachment annotation contents",
        attachment_file,
        1,
        "PushPin",
    )
    # Save updated document
    content_editor.save(outfile)
```
