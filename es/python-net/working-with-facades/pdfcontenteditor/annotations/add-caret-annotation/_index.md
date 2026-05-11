---
title: Agregar anotación de caret
type: docs
weight: 10
url: /es/python-net/add-caret-annotation/
description: Este ejemplo carga un PDF existente, agrega una anotación de caret a la primera página y guarda el documento modificado. La anotación incluye un símbolo de caret rojo y texto de comentario descriptivo.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar anotación de caret a un PDF usando Python
Abstract: Este ejemplo muestra cómo agregar una anotación de caret a un documento PDF usando Aspose.PDF for Python via the Facades API. El ejemplo muestra cómo enlazar un archivo PDF, definir la ubicación de la anotación usando rectángulos, configurar las propiedades del caret y guardar el documento actualizado.
---

Las anotaciones de caret se utilizan comúnmente para indicar inserciones de texto o comentarios editoriales en un documento. Con PdfContentEditor, puedes agregar anotaciones de caret de forma programática especificando el número de página, los límites de la anotación, el área de llamada, el símbolo, el texto de la nota y el color.

1. Crear el [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objeto.
1. Vincular el PDF de entrada.
1. Definir los parámetros de la anotación Caret:
  - Número de página donde se añadirá la anotación
  - Caret rectangle (posición de la anotación)
  - Rectángulo de llamada (área de texto)
  - Símbolo (por ejemplo "P")
  - Texto de anotación
  - Color de anotación
1. Agregar la anotación de cursor.
1. Guardar el documento actualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_caret_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add caret annotation to page 1
    content_editor.create_caret(
        1,
        apd.Rectangle(350, 400, 10, 10),
        apd.Rectangle(300, 380, 115, 15),
        "P",
        "This is a caret annotation",
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```
