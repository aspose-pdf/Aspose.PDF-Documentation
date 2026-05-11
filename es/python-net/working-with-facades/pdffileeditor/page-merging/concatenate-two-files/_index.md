---
title: Concatenar dos archivos PDF
type: docs
weight: 60
url: /es/python-net/concatenate-two-files/
description: Concatenar dos archivos PDF en un solo documento usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fusionar dos archivos PDF en un único PDF en Python
Abstract: Aprenda cómo concatenar dos archivos PDF en un solo documento usando Aspose.PDF for Python. Este ejemplo demuestra cómo fusionar dos PDFs sin problemas mientras se preserva su contenido y formato original.
---

Combinar dos archivos PDF es una tarea común al consolidar informes, contratos o formularios. Usando Aspose.PDF for Python, puede fusionar programáticamente dos PDFs en un solo documento usando el método concatenate de la [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) clase. Esto asegura que todas las páginas de ambos archivos se incluyan en el PDF de salida mientras se mantiene el diseño, contenido y estructura originales.

1. Crear un objeto PdfFileEditor.
1. Combinar dos archivos PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge[0], files_to_merge[1], output_file)
```
