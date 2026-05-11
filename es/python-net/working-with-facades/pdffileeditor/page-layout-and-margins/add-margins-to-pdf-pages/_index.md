---
title: Agregar márgenes a las páginas PDF
linktitle: Agregar márgenes a las páginas PDF
type: docs
weight: 10
url: /es/python-net/add-margins-to-pdf-pages/
description: Agregar márgenes personalizados a páginas seleccionadas de un PDF usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar márgenes personalizados a páginas PDF específicas en Python
Abstract: Aprenda cómo agregar márgenes personalizados a páginas seleccionadas de un PDF usando Aspose.PDF for Python. Este ejemplo muestra cómo expandir los límites de la página especificando márgenes superior, inferior, izquierdo y derecho para páginas individuales, haciendo que los PDFs sean más imprimibles o visualmente consistentes.
---

Agregar márgenes a las páginas PDF puede mejorar la legibilidad, preparar documentos para impresión o asignar espacio para anotaciones. Usando Aspose.PDF for Python, los desarrolladores pueden agregar márgenes a páginas específicas de un PDF de forma programática sin modificar el diseño del contenido.

En este fragmento de código, el [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class se usa para añadir márgenes de 0.5 pulgadas a las páginas 1 y 3 del documento de entrada. Los márgenes se definen en puntos (1 pulgada = 72 puntos) y se aplican individualmente a la izquierda, derecha, arriba y abajo de cada página.

1. Abra el documento PDF de origen.
1. Cree una instancia de 'PdfFileEditor'.
1. Defina los márgenes y las páginas a modificar.
1. Aplique los márgenes usando el método 'add_margins'.
1. Guarde el PDF actualizado en el archivo de salida.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Margins to PDF Pages
def add_margins_to_pdf_pages(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Define the margins to be added (in points)
    left_margin = 36  # 0.5 inch
    right_margin = 36  # 0.5 inch
    top_margin = 36  # 0.5 inch
    bottom_margin = 36  # 0.5 inch

    pdf_editor.add_margins(
        infile, outfile, [1, 3], left_margin, right_margin, top_margin, bottom_margin
    )
```
