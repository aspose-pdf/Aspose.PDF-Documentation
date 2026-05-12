---
title: Reemplazar texto con estado
linktitle: Reemplazar texto con estado
type: docs
weight: 50
url: /es/python-net/replace-text-with-state/
description: En este ejemplo, todas las ocurrencias de "software" se reemplazan por "SOFTWARE" y se formatean en azul con un tamaño de fuente de 14.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Reemplazar texto con formato personalizado en un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo demuestra cómo reemplazar texto en un documento PDF mientras se aplica formato personalizado usando Aspose.PDF for Python a través de la API Facades. Muestra cómo controlar el color del texto y el tamaño de fuente durante el reemplazo.
---

Al actualizar texto en un PDF, puede que desees que el contenido de reemplazo destaque. Usando un objeto TextState, puedes definir estilos como el color y el tamaño de fuente, y luego aplicarlos a todo el texto reemplazado.

1. Crear un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)  instancia.
1. Enlace el documento PDF de entrada.
1. Define un TextState con formato personalizado.
1. Configurar el alcance del reemplazo.
1. Reemplazar texto en todo el documento.
1. Guarde el documento PDF actualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_with_state(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 14

    # Replace text with explicit text formatting
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("software", "SOFTWARE", text_state)
    # Save updated document
    content_editor.save(outfile)
```
