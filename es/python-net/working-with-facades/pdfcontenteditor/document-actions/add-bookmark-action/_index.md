---
title: Agregar acción de marcador
linktitle: Agregar acción de marcador
type: docs
weight: 10
url: /es/python-net/add-bookmark-action/
description: Este ejemplo vincula un PDF de entrada, crea un marcador etiquetado "PdfContentEditor Bookmark" que navega a la página 1 y guarda el documento actualizado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crear un marcador con acción de navegación en un PDF usando Python
Abstract: Este ejemplo muestra cómo agregar un marcador con una acción de navegación a un documento PDF usando Aspose.PDF for Python via the Facades API. Muestra cómo configurar el texto del marcador, su apariencia y una acción que dirige a los usuarios a una página específica.
---

Los marcadores proporcionan una navegación rápida dentro de los documentos PDF. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puedes crear marcadores programáticamente y asignar acciones como navegar a una página. También puedes personalizar la apariencia del marcador, incluyendo opciones de color y estilo como negrita o cursiva.

1. Crea el objeto PdfContentEditor.
1. Vincular el PDF de entrada.
1. Definir propiedades del marcador.
1. Asignar acción al marcador.
1. Guardar el documento actualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_bookmark_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a bookmark action to navigate to page 1
    content_editor.create_bookmarks_action(
        "PdfContentEditor Bookmark",
        apd.Color.blue,
        True,
        False,
        "",
        "GoTo",
        "1",
    )
    # Save updated document
    content_editor.save(outfile)
```