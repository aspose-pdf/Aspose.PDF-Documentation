---
title: Listar Sellos
linktitle: Listar Sellos
type: docs
weight: 70
url: /es/python-net/list-stamps/
description: Este ejemplo carga un PDF, recupera todos los sellos de la página 1, los imprime y muestra un mensaje si no se encuentran sellos.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Listar anotaciones de sellos de goma en un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo muestra cómo recuperar y listar anotaciones de sellos de goma de un documento PDF usando Aspose.PDF for Python a través de la API Facades. Demuestra cómo acceder a los sellos en una página específica y mostrar sus detalles.
---

Cuando se trabaja con PDFs anotados, puede ser necesario inspeccionar los sellos de goma existentes antes de modificarlos o eliminarlos. El método 'get_stamps()' permite recuperar todos los sellos colocados en una página determinada. Luego puede iterar a través de los resultados y procesarlos programáticamente.

1. Crear un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instancia.
1. Vincula el documento PDF de entrada.
1. Recuperar todos los sellos de la página 1.
1. Iterar a través de la colección de sellos.
1. Imprimir cada sello.
1. Mostrar un mensaje si no existen sellos.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def list_stamps(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # List all stamps on page 1
    stamps = content_editor.get_stamps(1)

    count = 0
    for stamp in stamps:
        count += 1
        print(f"Stamp {count}: {stamp}")

    if count == 0:
        print("No stamps found")
```
