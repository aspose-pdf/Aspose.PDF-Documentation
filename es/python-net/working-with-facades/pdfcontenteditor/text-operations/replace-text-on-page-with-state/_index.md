---
title: Reemplazar texto en la página con estado
type: docs
weight: 20
url: /es/python-net/replace-text-on-page-with-state/
description: En este ejemplo, todas las apariciones de la palabra "software" en la página 1 se reemplazan por "SOFTWARE PAGE 1", usando texto rojo con un tamaño de fuente de 12.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Reemplazar texto con formato personalizado en una página específica usando PdfContentEditor en Python
Abstract: Este ejemplo muestra cómo reemplazar texto en una página específica de un PDF mientras se aplica formato personalizado usando Aspose.PDF for Python via the Facades API. Muestra cómo controlar el tamaño y el color de la fuente durante el reemplazo de texto.
---

A veces, reemplazar texto en un PDF también requiere cambios de formato como color o tamaño de fuente. Usando TextState, puedes definir propiedades de estilo y aplicarlas durante el reemplazo. Esto te permite resaltar el texto modificado o imponer un formato consistente en los documentos.

1. Crear un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instancia.
1. Vincula el documento PDF de entrada.
1. Define un TextState con formato personalizado.
1. Configura la estrategia de reemplazo.
1. Reemplaza texto en una página específica.
1. Guarda el documento PDF actualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_on_page_with_state(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.red
    text_state.font_size = 12

    # Replace text on a specific page with explicit text formatting
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("software", 1, "SOFTWARE PAGE 1", text_state)
    # Save updated document
    content_editor.save(outfile)
```
