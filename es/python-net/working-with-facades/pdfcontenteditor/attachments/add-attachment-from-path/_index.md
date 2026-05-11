---
title: Agregar adjunto desde la ruta
type: docs
weight: 20
url: /es/python-net/add-attachment-from-path/
description: Este ejemplo vincula un PDF de entrada, adjunta un archivo externo usando su ruta de archivo y guarda el PDF modificado con el adjunto incorporado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adjuntar archivos a un PDF usando sobrecarga de ruta de archivo en Python
Abstract: Este ejemplo muestra cómo adjuntar archivos externos a un documento PDF usando la sobrecarga de ruta de archivo de \u0027add_document_attachment()\u0027 en Aspose.PDF for Python a través de la API Facades. Simplifica la adición de adjuntos sin abrir manualmente un flujo de archivo.
---

El PDF puede incluir archivos incrustados como documentos, hojas de cálculo o imágenes para referencia o distribución. La sobrecarga de ruta de archivo de \u0027add_document_attachment()\u0027 le permite agregar adjuntos directamente desde una ruta de archivo, eliminando la necesidad de abrir el archivo manualmente.

1. Crear el [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objeto.
1. Vincular el PDF de entrada.
1. Agregar el adjunto usando la ruta de archivo.
1. Guardar el documento actualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment_from_path(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment using file-path overload
    content_editor.add_document_attachment(
        attachment_file,
        "Attachment added using file path overload.",
    )
    # Save updated document
    content_editor.save(outfile)
```
