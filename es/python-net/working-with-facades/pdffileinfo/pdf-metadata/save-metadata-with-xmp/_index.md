---
title: Guardar metadatos con XMP
type: docs
weight: 30
url: /es/python-net/save-metadata-with-xmp/
description: Guardar metadatos PDF usando XMP con Aspose.PDF for Python via .NET
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guardar metadatos PDF con XMP usando Aspose.PDF for Python
Abstract: Esta guía demuestra cómo guardar metadatos PDF usando XMP (Extensible Metadata Platform) con Aspose.PDF for Python via .NET. XMP garantiza que tanto los metadatos estándar como los personalizados se incrusten en un formato XML estandarizado dentro del PDF, mejorando la compatibilidad entre aplicaciones y flujos de trabajo.
---

Los metadatos PDF pueden almacenarse de múltiples maneras, y XMP es el método moderno y estandarizado para incrustar metadatos dentro de un archivo PDF. Usando Aspose.PDF, puedes actualizar campos estándar como Title, Subject, Keywords y Creator, y luego guardarlos en formato XMP para garantizar una mayor compatibilidad y una preparación para el futuro. Este método se recomienda sobre los métodos heredados de almacenamiento de metadatos.

1. Cargue el archivo PDF.
1. Establecer campos de metadatos estándar.
1. Guardar metadatos en formato XMP.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def save_info_with_xmp(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Set PDF metadata
    pdf_info.subject = "Aspose PDF for Python via .NET"
    pdf_info.title = "Aspose PDF for Python via .NET"
    pdf_info.keywords = "Aspose, PDF, Python, .NET"
    pdf_info.creator = "Aspose Team"

    # Save updated metadata
    pdf_info.save_new_info_with_xmp(outfile)
```
