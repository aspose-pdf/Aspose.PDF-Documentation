---
title: Agregar páginas al PDF
type: docs
weight: 10
url: /es/python-net/append-pages-to-pdf/
description: Agregar páginas de un documento PDF a otro usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar páginas de un PDF a otro en Python
Abstract: Aprenda cómo agregar páginas de un documento PDF a otro usando Aspose.PDF for Python. Este ejemplo demuestra cómo usar la clase PdfFileEditor para combinar páginas de varios PDFs y crear un documento de salida único.
---

Combinar páginas de diferentes documentos PDF es un requisito común en los flujos de trabajo de procesamiento de documentos. Usando Aspose.PDF for Python, los desarrolladores pueden agregar fácilmente páginas de uno o más archivos PDF a un documento existente.

Este fragmento de código muestra cómo usar el método append de [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) clase para agregar páginas seleccionadas de otro archivo PDF al final de un PDF de origen. Al especificar el rango de páginas, los desarrolladores pueden controlar exactamente qué páginas se incluyen en el documento final.

1. Crear un objeto PdfFileEditor.
1. Agregar páginas de otro PDF.

Las páginas especificadas del documento PDF secundario se añaden al final del PDF original, creando un archivo de salida combinado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Append Pages to PDF
def append_pages_to_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Append pages from the specified PDF document to the end of the source PDF document
    pdf_editor.append(infile, [sample_file], 1, 2, outfile)
```
