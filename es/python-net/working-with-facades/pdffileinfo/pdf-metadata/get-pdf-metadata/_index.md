---
title: Obtener metadatos de PDF
type: docs
weight: 20
url: /es/python-net/get-pdf-metadata/
description: Extraer y mostrar metadatos de documentos PDF usando Aspose.PDF for Python.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recuperar metadatos de PDF usando Aspose.PDF for Python.
Abstract: Esta guía muestra cómo extraer y mostrar metadatos de documentos PDF usando Aspose.PDF for Python. Aprenderá a acceder a propiedades estándar de PDF como título, autor, palabras clave, fechas de creación/modificación, así como a campos de metadatos personalizados. Además, la guía cubre verificaciones de la validez del PDF, encriptación y estado de portafolio.
---

Los documentos PDF a menudo contienen metadatos valiosos que describen el contenido del documento, la autoría y los permisos. Aspose.PDF proporciona una API conveniente para recuperar tanto propiedades de metadatos estándar como personalizadas. Este fragmento de código muestra cómo usar el [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) clase para inspeccionar archivos PDF programáticamente, incluyendo ejemplos paso a paso en Python.

1. Cargue el archivo PDF.
1. Recuperar metadatos estándar.
1. Verificar el estado y la seguridad del PDF.
1. Recuperar metadatos personalizados.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_metadata(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    print(f"Subject: {pdf_info.subject}")
    print(f"Title: {pdf_info.title}")
    print(f"Keywords: {pdf_info.keywords}")
    print(f"Creator: {pdf_info.creator}")
    print(f"Creation Date: {pdf_info.creation_date}")
    print(f"Modification Date: {pdf_info.mod_date}")

    # Check PDF status
    print(f"Is Valid PDF: {pdf_info.is_pdf_file}")
    print(f"Is Encrypted: {pdf_info.is_encrypted}")
    print(f"Has Open Password: {pdf_info.has_open_password}")
    print(f"Has Edit Password: {pdf_info.has_edit_password}")
    print(f"Is Portfolio: {pdf_info.has_collection}")

    # Retrieve and display a specific custom attribute
    reviewer = pdf_info.get_meta_info("Reviewer")
    print(f"Reviewer: {reviewer if reviewer else 'No Reviewer metadata found.'}")
```
