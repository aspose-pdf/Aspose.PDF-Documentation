---
title: Dividir PDF hasta el final
linktitle: Dividir PDF hasta el final
type: docs
weight: 40
url: /es/python-net/split-pdf-to-end/
description: Divida un documento PDF desde una página dada hasta la última página usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Divida un PDF desde una página específica hasta el final en Python
Abstract: Aprenda cómo dividir un documento PDF desde una página dada hasta la última página usando Aspose.PDF for Python. Este ejemplo demuestra cómo extraer todas las páginas a partir de una página especificada para crear un nuevo archivo PDF.
---

Dividir un PDF desde una página específica hasta el final es útil cuando necesita la porción final de un documento como un archivo separado. Usando Aspose.PDF for Python, el método split_to_end de la [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) clase le permite extraer páginas comenzando desde cualquier número de página hasta la última página del documento. Esto es ideal para crear extractos, extraer capítulos o procesar partes de un PDF grande sin editarlo manualmente.

1. Crear un objeto PdfFileEditor.
1. Dividir PDF desde una página específica hasta el final.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF to End
def split_pdf_to_end(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_end(input_pdf_path, 2, output_pdf_path)
```
