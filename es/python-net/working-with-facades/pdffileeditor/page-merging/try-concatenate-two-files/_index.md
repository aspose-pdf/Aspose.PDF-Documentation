---
title: Intente concatenar dos archivos PDF
type: docs
weight: 90
url: /es/python-net/try-concatenate-two-files/
description: Concatene dos archivos PDF usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fusionar de forma segura dos archivos PDF en Python sin excepciones
Abstract: Aprenda cómo concatenar de forma segura dos archivos PDF usando Aspose.PDF for Python. El método try_concatenate une los archivos sin generar excepciones, lo que permite un manejo de errores elegante en caso de que la operación falle.
---

Fusionar dos archivos PDF a veces puede fallar debido a corrupción del archivo, formatos incompatibles u otros problemas. Usando Aspose.PDF for Python, el método try_concatenate de la clase PdfFileEditor le permite intentar fusionar dos PDF de forma segura. Si la operación falla, devuelve False en lugar de lanzar una excepción, dándole control total sobre el manejo de errores en flujos de trabajo automatizados o procesamiento por lotes.

1. Crear un objeto PdfFileEditor.
1. Intente fusionar dos archivos PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def try_concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    if not pdf_editor.try_concatenate(
        files_to_merge[0], files_to_merge[1], output_file
    ):
        print("Concatenation failed for the provided files.")
```
