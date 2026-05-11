---
title: Agregar acción de documento
linktitle: Agregar acción de documento
type: docs
weight: 20
url: /es/python-net/add-document-action/
description: Este ejemplo agrega una alerta de JavaScript que aparece cuando se abre el PDF. El script está adjunto al evento de apertura del documento y se ejecuta automáticamente en los visores de PDF compatibles.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar acción de JavaScript de apertura de documento a un PDF usando Python
Abstract: Este ejemplo muestra cómo agregar una acción de JavaScript a nivel de documento que se activa cuando se abre un PDF. Usando Aspose.PDF for Python via the Facades API, el ejemplo muestra cómo vincular un documento, asignar una acción de evento de apertura y guardar el PDF actualizado.
---

Las acciones a nivel de documento le permiten definir comportamientos que se ejecutan automáticamente cuando ocurren ciertos eventos, como la apertura de un PDF. Con [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puede adjuntar código JavaScript a estos eventos. Esto puede usarse para notificaciones, lógica de validación o flujos de trabajo interactivos.

1. Crea el objeto PdfContentEditor.
1. Vincular el PDF de entrada.
1. Agregar acción a nivel de documento.
1. Guardar el documento actualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_document_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add JavaScript action for document open event
    content_editor.add_document_additional_action(
        content_editor.DOCUMENT_OPEN,
        "app.alert('Document opened with PdfContentEditor action');",
    )
    # Save updated document
    content_editor.save(outfile)
```
