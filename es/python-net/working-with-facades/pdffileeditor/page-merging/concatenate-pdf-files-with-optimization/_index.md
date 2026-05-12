---
title: Concatenar archivos PDF con optimización
linktitle: Concatenar archivos PDF con optimización
type: docs
weight: 30
url: /es/python-net/concatenate-pdf-files-with-optimization/
description: Concatenar varios archivos PDF en un único PDF optimizado usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combinar archivos PDF con salida optimizada en Python
Abstract: Aprenda cómo concatenar varios archivos PDF en un único PDF optimizado usando Aspose.PDF for Python. Este ejemplo muestra cómo habilitar la optimización de tamaño para reducir el tamaño del archivo de salida mientras se preserva el contenido y el formato.
---

Al combinar varios PDFs, el archivo resultante puede volverse grande, especialmente si contiene imágenes o contenido complejo. Usando Aspose.PDF for Python, los desarrolladores pueden habilitar la optimización durante la concatenación para reducir el tamaño del archivo sin perder calidad. La propiedad optimize_size en el [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) clase garantiza que el PDF combinado sea compacto y eficiente, haciéndolo adecuado para compartir, almacenar o archivar.

1. Crear un objeto PdfFileEditor y habilitar la optimización.
1. Combinar archivos PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files_with_optimization(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.optimize_size = True  # Enable optimization for smaller output file size
    pdf_editor.concatenate(files_to_merge, output_file)
```
