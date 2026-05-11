---
title: Reemplazar texto en la página
type: docs
weight: 10
url: /es/python-net/replace-text-on-page/
description: En este ejemplo, la primera aparición de la palabra "PDF" se reemplaza con "Page 1 Replaced Text" utilizando un tamaño de fuente especificado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Reemplazar texto en una página específica usando PdfContentEditor en Python
Abstract: Este ejemplo demuestra cómo reemplazar texto en un documento PDF usando Aspose.PDF for Python a través de la API de Facades. Muestra cómo reemplazar la primera aparición de texto en una página y guardar el documento actualizado.
---

El reemplazo de texto es un requisito común al actualizar documentos PDF. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puedes buscar texto específico y reemplazarlo con contenido nuevo. La propiedad 'replace_text_strategy' permite controlar cuántas apariciones se reemplazan.

1. Crea una instancia de PdfContentEditor.
1. Vincula el documento PDF de entrada.
1. Configurar la estrategia de reemplazo de texto.
1. Reemplazar el texto objetivo.
1. Guarda el documento PDF actualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_on_page(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text on page 1
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_FIRST
    )
    content_editor.replace_text("PDF", "Page 1 Replaced Text", 14)
    # Save updated document
    content_editor.save(outfile)
```
