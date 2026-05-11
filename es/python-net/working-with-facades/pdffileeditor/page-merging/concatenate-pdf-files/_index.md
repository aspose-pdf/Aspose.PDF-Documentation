---
title: Concatenar varios archivos PDF
type: docs
weight: 20
url: /es/python-net/concatenate-pdf-files/
description: Combina varios archivos PDF en un solo documento usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fusionar varios archivos PDF en un solo PDF en Python
Abstract: Aprende cómo combinar varios archivos PDF en un solo documento usando Aspose.PDF for Python. Este ejemplo muestra cómo usar el método concatenate para fusionar varios PDFs sin problemas mientras se preservan su contenido y formato.
---

Fusionar archivos PDF es una tarea común en la gestión de documentos, la generación de informes y los flujos de trabajo automatizados. Usando Aspose.PDF for Python, los desarrolladores pueden combinar fácilmente varios archivos PDF en un documento consolidado único. El método concatenate de la [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) clase garantiza que todas las páginas de los archivos de entrada se conserven en el resultado final, manteniendo su diseño y contenido original. Este enfoque es útil para crear informes completos, combinar formularios o archivar varios documentos de manera eficiente.

1. Crear un objeto PdfFileEditor.
1. Combinar varios archivos PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge, output_file)
```
