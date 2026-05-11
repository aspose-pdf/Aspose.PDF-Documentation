---
title: Reemplazar texto simple
type: docs
weight: 40
url: /es/python-net/replace-text-simple/
description: En este ejemplo, todas las apariciones de "23" se sustituyen por "XXXIII " en todo el documento. Esto demuestra un reemplazo de cadena sencillo sin formato personalizado ni expresiones regulares.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Reemplazar texto en todo un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo demuestra cómo reemplazar texto en todo un documento PDF utilizando Aspose.PDF for Python via the Facades API. Reemplaza todas las apariciones de una cadena especificada con texto nuevo.
---

El reemplazo de texto simple es útil al actualizar valores repetidos en un documento. Con [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puedes definir un alcance de reemplazo y sustituir texto globalmente en todas las páginas.

1. Crear un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instancia.
1. Enlace el documento PDF de entrada.
1. Configura el alcance de reemplazo para todas las ocurrencias.
1. Reemplazar el texto objetivo.
1. Guarde el documento PDF actualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_simple(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text in the whole document
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("33", "XXXIII ")
    # Save updated document
    content_editor.save(outfile)
```
