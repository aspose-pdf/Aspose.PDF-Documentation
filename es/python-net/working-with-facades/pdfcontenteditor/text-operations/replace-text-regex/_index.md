---
title: Reemplazar texto Regex
linktitle: Reemplazar texto Regex
type: docs
weight: 30
url: /es/python-net/replace-text-regex/
description: En este ejemplo, todos los números de cuatro dígitos en el documento se reemplazan con el marcador "[NUMBER]". Esto es útil para ocultar datos sensibles, normalizar contenido o anonimizar documentos.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Reemplazar texto usando expresiones regulares con PdfContentEditor en Python
Abstract: Este ejemplo muestra cómo reemplazar texto en un PDF usando expresiones regulares con Aspose.PDF for Python a través de la API Facades. Demuestra cómo buscar patrones y reemplazar todas las coincidencias en todo el documento.
---

Las expresiones regulares permiten un reemplazo de texto flexible basado en patrones en lugar de cadenas fijas. Al habilitar el soporte de regex en 'replace_text_strategy', puedes coincidir contenido dinámico como números, fechas o cadenas formateadas.

1. Crear un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instancia.
1. Enlace el documento PDF de entrada.
1. Configura la estrategia de reemplazo para usar regex.
1. Reemplazar patrones coincidentes en todo el documento.
1. Guarde el documento PDF actualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_regex(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text in the whole document
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text_strategy.is_regular_expression_used = True
    content_editor.replace_text(r"\d{4}", "[NUMBER]")
    # Save updated document
    content_editor.save(outfile)
```
