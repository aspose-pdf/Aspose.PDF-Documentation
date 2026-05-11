---
title: Agregar enlace de documento PDF
type: docs
weight: 50
url: /es/python-net/add-pdf-document-link/
description: Este ejemplo enlaza un PDF de entrada, agrega un enlace de color verde a una página en otro PDF y guarda el documento modificado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar un enlace de documento PDF usando PdfContentEditor en Python
Abstract: Este ejemplo muestra cómo agregar un enlace a otro documento PDF usando Aspose.PDF for Python via the Facades API. Muestra cómo crear un área clicable que abre un PDF diferente y guardar el documento actualizado.
---

Los enlaces de documentos PDF permiten a los usuarios navegar de un PDF a otro sin problemas. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puedes definir un rectángulo clicable que enlaza a una página en un archivo PDF diferente, haciendo que tus documentos sean interactivos y conectados.

1. Cree una instancia de PdfContentEditor.
1. Enlace el documento PDF de entrada.
1. Defina un rectángulo para el enlace clicable.
1. Especifique el archivo PDF vinculado, la página de origen y la página de destino.
1. Establezca el color del enlace.
1. Guarde el documento PDF actualizado.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_pdf_document_link(infile, linked_pdf, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add link to another PDF document
    content_editor.create_pdf_document_link(
        apd.Rectangle(140, 590, 240, 20),
        linked_pdf,
        1,
        1,
        apd.Color.green,
    )
    # Save updated document
    content_editor.save(outfile)
```
