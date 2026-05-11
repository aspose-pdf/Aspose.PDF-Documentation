---
title: Dividir PDF en páginas individuales
linktitle: Dividir PDF en páginas individuales
type: docs
weight: 30
url: /es/python-net/split-pdf-into-single-pages/
description: Divida el documento PDF en PDFs de una sola página usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dividir un PDF en páginas individuales en Python
Abstract: Aprenda cómo dividir un documento PDF en PDFs de una sola página usando Aspose.PDF for Python. Este método extrae cada página del PDF original y la guarda como un archivo separado para una gestión y procesamiento flexibles del documento.
---

Dividir un PDF en páginas individuales es útil para procesamiento a nivel de página, impresión o distribución de secciones de un documento individualmente. Usando Aspose.PDF for Python, el método 'split_to_pages' del [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) clase crea archivos PDF separados para cada página en el documento de origen. Este enfoque permite la extracción automatizada de páginas para archivado, revisión o compartición individual, mientras se conserva el diseño y contenido original.

1. Crear un objeto PdfFileEditor.
1. Dividir PDF en páginas individuales.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF into Single Pages
def split_pdf_into_single_pages(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_pages(input_pdf_path, output_pdf_path)
```
