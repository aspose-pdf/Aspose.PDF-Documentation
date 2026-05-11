---
title: Dividir PDF desde el comienzo
type: docs
weight: 10
url: /es/python-net/split-pdf-from-beginning/
description: Divida un documento PDF desde el principio utilizando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dividir PDF desde el Inicio en Python usando Aspose.PDF
Abstract: Aprenda cómo dividir un documento PDF desde el principio utilizando Aspose.PDF for Python. Este ejemplo demuestra la extracción de un número específico de páginas comenzando desde la primera página para crear un nuevo documento PDF.
---

Dividir PDFs desde el principio es útil cuando necesita las primeras páginas de un documento como un archivo separado. Usando Aspose.PDF for Python, el método split_from_first en el [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) La clase le permite extraer un número definido de páginas a partir de la página uno. Esta función es ideal para generar extractos, vistas previas o secciones más pequeñas de un PDF más grande sin editar manualmente el archivo original.

1. Crear un objeto PdfFileEditor.
1. Dividir PDF desde la primera página.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF from Beginning
def split_pdf_from_beginning(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_from_first(input_pdf_path, 3, output_pdf_path)
```
