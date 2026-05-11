---
title: Extraer páginas de PDF
linktitle: Extraer páginas de PDF
type: docs
weight: 30
url: /es/python-net/extract-pages-from-pdf/
description: Extraer páginas seleccionadas de un documento PDF usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraer páginas específicas de un documento PDF en Python
Abstract: Aprende cómo extraer páginas seleccionadas de un documento PDF usando Aspose.PDF for Python. Este ejemplo muestra cómo crear un nuevo PDF que contenga solo las páginas que necesitas, habilitando la creación personalizada de documentos y la manipulación a nivel de página.
---

Extraer páginas de un PDF es útil cuando necesitas crear un subconjunto de un documento, compartir solo contenido específico o reorganizar PDFs para presentaciones, informes o impresión. Usando Aspose.PDF for Python, los desarrolladores pueden extraer programáticamente páginas de un archivo PDF y guardarlas como un nuevo documento.

Aprende cómo usar el método extract de la [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) clase. Al especificar una lista de páginas a extraer, puedes generar un nuevo PDF que contenga solo las páginas seleccionadas mientras se preserva el contenido y el formato original.

1. Crear un objeto PdfFileEditor.
1. Definir páginas a extraer.
1. Extraer las páginas.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Extract Pages from PDF
def extract_pages_from_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page numbers to be extracted (1-based index)
    pages_to_extract = [1, 4, 3]

    # Extract the specified pages from the PDF document and save to a new PDF document
    pdf_editor.extract(infile, pages_to_extract, outfile)
```
