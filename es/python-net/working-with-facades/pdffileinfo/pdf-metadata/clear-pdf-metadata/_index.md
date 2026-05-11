---
title: Borrar metadatos de PDF
type: docs
weight: 10
url: /es/python-net/clear-pdf-metadata/
description: Eliminar todos los metadatos de un documento PDF usando Aspose.PDF para Python a través de .NET.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Borrado de metadatos PDF usando Aspose.PDF para Python
Abstract: Esta guía explica cómo eliminar todos los metadatos de un documento PDF usando Aspose.PDF para Python a través de .NET. Aprenderá a borrar tanto los campos de metadatos estándar como los personalizados y a guardar el PDF sanitizado. Esto es útil para la privacidad, la seguridad o la preparación de PDFs para su publicación.
---

Los PDF suelen contener metadatos como título, autor, palabras clave, fechas de creación y campos personalizados. En algunos escenarios, puede querer eliminar todos los metadatos de un PDF, por ejemplo antes de su distribución o archivado. Aspose.PDF proporciona el método clear_info() para eliminar todos los metadatos fácilmente. Después de la eliminación, puede guardar el PDF usando el método save().

1. Cargue el archivo PDF.
1. Borrar todos los metadatos.
1. Guardar el PDF limpio.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def clear_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Clear PDF metadata
    pdf_info.clear_info()

    # Save updated metadata
    pdf_info.save(outfile)
```
