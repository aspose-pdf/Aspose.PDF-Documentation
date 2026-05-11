---
title: Agregar saltos de página en PDF
type: docs
weight: 20
url: /es/python-net/add-page-breaks-in-pdf/
description: Insertar saltos de página en un documento PDF usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar saltos de página a páginas PDF programáticamente en Python
Abstract: Aprenda cómo insertar saltos de página en un documento PDF usando Aspose.PDF for Python. Este ejemplo demuestra cómo dividir una página en una posición vertical especificada, permitiendo a los desarrolladores reorganizar el contenido y crear páginas adicionales de forma dinámica.
---

Los saltos de página son útiles cuando necesita dividir páginas PDF largas en varias páginas o controlar cómo se distribuye el contenido a lo largo de un documento. Usando Aspose.PDF for Python, los desarrolladores pueden insertar saltos de página en posiciones específicas sin editar manualmente el PDF.

Este artículo muestra cómo usar el método 'add_page_break' de [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) clase para insertar un salto de página en una coordenada vertical definida en una página seleccionada. El método crea una nueva página y mueve el contenido que está debajo del punto de salto a esa página.

1. Crear un objeto PdfFileEditor.
1. Definir la posición del salto de página.
1. Insertar el salto de página.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Page Breaks in PDF
def add_page_breaks_in_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.add_page_break(
        infile,
        outfile,
        [
            pdf_facades.PdfFileEditor.PageBreak(1, 400),
        ],
    )
```
