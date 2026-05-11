---
title: Establecer metadatos PDF
type: docs
weight: 50
url: /es/python-net/set-pdf-metadata/
description: Modificar y guardar metadatos en documentos PDF usando Aspose.PDF for Python via .NET.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Actualizando metadatos PDF usando Aspose.PDF for Python
Abstract: Esta guía explica cómo modificar y guardar metadatos en documentos PDF usando Aspose.PDF for Python via .NET. Demuestra cómo actualizar propiedades estándar de PDF como título, asunto, palabras clave y creador, así como campos de metadatos personalizados. Al final, podrás actualizar programáticamente los metadatos PDF y guardar los cambios.
---

Los documentos PDF pueden contener tanto metadatos estándar (Title, Subject, Keywords, Creator, Author) como metadatos personalizados almacenados como propiedades XMP. Aspose.PDF proporciona una API simple para modificar estas propiedades en Python. Esta guía cubre cómo actualizar estos campos y guardar el archivo PDF modificado usando el [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) clase.

1. Cargue el archivo PDF.
1. Actualizar metadatos estándar.
1. Agregar o actualizar metadatos personalizados.
1. Guardar los metadatos actualizados.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Set PDF metadata
    pdf_info.subject = "Aspose PDF for Python via .NET"
    pdf_info.title = "Aspose PDF for Python via .NET"
    pdf_info.keywords = "Aspose, PDF, Python, .NET"
    pdf_info.creator = "Aspose Team"

    pdf_info.set_meta_info("CustomKey", "CustomValue")

    # pdf_info.save_new_info(outfile)
    # Is obsolete, use save() method instead

    # Save updated metadata
    pdf_info.save(outfile)
```
