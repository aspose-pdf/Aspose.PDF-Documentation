---
title: Agregar anotaciones de texto libre
type: docs
weight: 20
url: /es/python-net/add-free-text-annotation/
description: Este ejemplo carga un archivo PDF existente, agrega una anotación de texto libre a la primera página en una posición definida y guarda el documento modificado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar anotación de texto libre a un PDF usando Python
Abstract: Este ejemplo demuestra cómo insertar una anotación de texto libre en un documento PDF usando Aspose.PDF para Python a través de la API Facades. Muestra cómo vincular un PDF, definir la ubicación de la anotación, agregar texto personalizado y guardar el documento actualizado.
---

Las anotaciones de texto libre le permiten colocar texto visible directamente en una página PDF sin requerir comentarios emergentes. Usando PdfContentEditor, puede especificar el rectángulo de la anotación, el texto mostrado y la página objetivo.

1. Crear el [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objeto.
1. Vincular el PDF de entrada.
1. Defina la posición de la anotación.
1. Agregar la anotación de texto libre.
1. Guardar el documento actualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_free_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add free text annotation to page 1
    content_editor.create_free_text(
        apd.Rectangle(200, 480, 150, 25), "This is a free text annotation", 1
    )
    # Save updated document
    content_editor.save(outfile)
```
