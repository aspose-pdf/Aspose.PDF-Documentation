---
title: Agregar anotación de película
linktitle: Agregar anotación de película
type: docs
weight: 10
url: /es/python-net/add-movie-annotation/
description: Este ejemplo enlaza un PDF de entrada, agrega una anotación de película en la página 1 y guarda el PDF actualizado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar una anotación de película a un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo muestra cómo incrustar una película (video) en un documento PDF usando Aspose.PDF para Python a través de la API Facades. Demuestra cómo agregar una anotación clicable que reproduce un video directamente dentro del PDF.
---

Las anotaciones de película en los PDF le permiten incrustar contenido multimedia, como videos, en sus documentos. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puede definir un rectángulo en una página donde aparecerá el video. Al hacer clic, el video puede reproducirse directamente desde el PDF, haciendo sus documentos más interactivos y atractivos.

1. Crea una instancia de PdfContentEditor.
1. Vincula el documento PDF de entrada.
1. Definir un rectángulo para la anotación de película.
1. Especificar el archivo de video para incrustar.
1. Asignar el número de página para la anotación.
1. Guarda el documento PDF actualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_movie_annotation(infile, movie_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add movie annotation to page 1
    content_editor.create_movie(apd.Rectangle(80, 500, 220, 120), movie_file, 1)
    # Save updated document
    content_editor.save(outfile)
```
