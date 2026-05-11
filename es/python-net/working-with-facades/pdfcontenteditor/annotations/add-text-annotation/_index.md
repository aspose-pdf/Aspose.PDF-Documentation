---
title: Agregar anotaciones de texto
linktitle: Agregar anotaciones de texto
type: docs
weight: 50
url: /es/python-net/add-text-annotation/
description: Agregar anotaciones de texto a un documento PDF utilizando la clase PdfContentEditor en Aspose.PDF for Python via .NET.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar anotaciones de texto en Python
Abstract: Aprenda cómo agregar anotaciones de texto a un documento PDF utilizando la clase PdfContentEditor en Aspose.PDF for Python via .NET. Este ejemplo muestra cómo colocar una anotación de texto en una posición específica, definir su título y contenidos, y guardar el archivo PDF actualizado.
---

Este artículo muestra cómo agregar una anotación de texto a un documento PDF utilizando la [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) clase en Aspose.PDF.

Las anotaciones de texto le permiten adjuntar comentarios, notas o información adicional a partes específicas de una página PDF. Estas anotaciones pueden aparecer como íconos y ser ampliadas por los usuarios al ver el documento.

En este ejemplo:

- Se carga un documento PDF en el PdfContentEditor.
- Se agrega una anotación de texto en una posición específica de la página.
- La anotación incluye un título, contenido, tipo de ícono y configuraciones de visibilidad.
- El documento modificado se guarda en un nuevo archivo.

1. Crear un objeto PdfContentEditor.
1. Vincular el documento PDF de entrada.
1. Definir la posición de la anotación.
1. Agregar anotación de texto.
1. Guardar el PDF actualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add text annotation to page 1
    content_editor.create_text(
        apd.Rectangle(100, 400, 50, 50),
        "Text Annotation",
        "This is a text annotation",
        True,
        "Insert",
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```
