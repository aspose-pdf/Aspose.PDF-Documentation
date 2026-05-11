---
title: Obtener versión del PDF
type: docs
weight: 20
url: /es/python-net/get-pdf-version/
description: Aprenda cómo determinar programáticamente la versión de un documento PDF usando Aspose.PDF for Python. Este tutorial demuestra cómo usar la clase PdfFileInfo para comprobar la versión PDF de un archivo.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recuperar versión de PDF usando Aspose.PDF for Python
Abstract: Los documentos PDF tienen números de versión que indican las características y especificaciones que soportan (p. ej., 1.4, 1.7, 2.0). Conocer la versión del PDF es importante para la compatibilidad, el soporte de funcionalidades y los flujos de trabajo de procesamiento de documentos. En esta guía, aprenderá cómo recuperar la versión del PDF programáticamente usando la clase PdfFileInfo en Aspose.PDF for Python.
---

Las versiones de PDF definen las características y capacidades admitidas en un documento, incluidos los campos de formulario, el cifrado, las anotaciones y la compresión. Para los desarrolladores que trabajan con múltiples PDFs, comprobar la versión garantiza la compatibilidad con herramientas, bibliotecas o flujos de trabajo que procesan estos archivos.

Usando Aspose.PDF for Python, puede inspeccionar fácilmente la versión del PDF con el [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) clase.

1. Cargar un documento PDF.
1. Obtener su versión PDF.
1. Mostrar la versión en la consola.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_version(input_file_name):

    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)
    version = pdf_metadata.get_pdf_version()
    print(f"\nPDF Version: {version}")
```
