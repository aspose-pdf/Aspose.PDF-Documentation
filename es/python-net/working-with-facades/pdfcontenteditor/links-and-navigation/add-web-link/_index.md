---
title: Agregar enlace web
type: docs
weight: 60
url: /es/python-net/add-web-link/
description: Este ejemplo enlaza un PDF de entrada, agrega una anotación de enlace web azul en la página 1 que apunta a la página del producto PDF de Python de Aspose, y guarda el documento modificado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar un enlace web a un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo demuestra cómo agregar un enlace web a un documento PDF usando Aspose.PDF for Python a través de la API Facades. Muestra cómo crear un área clicable en una página que abre una URL especificada en un navegador web y guardar el documento actualizado.
---

Los enlaces web en los PDFs permiten a los usuarios navegar directamente a recursos en línea, sitios web o documentación. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puedes definir un área rectangular en una página PDF que, al hacer clic, abre una URL en el navegador web predeterminado.

1. Crea una instancia de PdfContentEditor.
1. Vincula el documento PDF de entrada.
1. Defina un rectángulo para el enlace web clicable.
1. Especifique la URL, el número de página y el color del enlace.
1. Guarda el documento PDF actualizado.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_web_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a web link annotation to page 1
    content_editor.create_web_link(
        apd.Rectangle(100, 650, 200, 20),
        "https://products.aspose.com/pdf/python-net/",
        1,
        apd.Color.blue,
    )
    # Save updated document
    content_editor.save(outfile)
```
