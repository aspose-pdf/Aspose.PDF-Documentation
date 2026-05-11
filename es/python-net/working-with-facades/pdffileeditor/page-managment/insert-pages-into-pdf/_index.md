---
title: Insertar páginas en PDF
type: docs
weight: 40
url: /es/python-net/insert-pages-into-pdf/
description: Insertar páginas de un PDF a otro usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Insertar páginas de otro PDF en un PDF existente en Python
Abstract: Aprenda cómo insertar páginas de un PDF a otro usando Aspose.PDF for Python. Este ejemplo demuestra cómo agregar páginas seleccionadas de un PDF secundario en una posición específica del documento original, creando un PDF combinado con una colocación precisa de páginas.
---

Insertar páginas en un PDF existente es un requisito común al combinar documentos, agregar contenido o reorganizar informes. Usando Aspose.PDF for Python, los desarrolladores pueden insertar páginas de un PDF a otro de forma programática en una ubicación especificada.

Este artículo muestra cómo usar el método insert del [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) clase. Al especificar los números de página a insertar y la ubicación de destino, puedes combinar contenido de diferentes PDFs manteniendo el formato y la estructura originales.

1. Crear un objeto PdfFileEditor.
1. Define la posición de inserción y las páginas.
1. Insertar páginas.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Insert Pages into PDF
def insert_pages_into_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page number where new pages will be inserted (1-based index)
    insert_page_number = 2

    pdf_editor.insert(infile, insert_page_number, sample_file, [1, 2], outfile)
```
