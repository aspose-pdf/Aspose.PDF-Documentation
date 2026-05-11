---
title: Concatenar gran número de archivos PDF
type: docs
weight: 10
url: /es/python-net/concatenate-large-number-files/
description: Combinar un gran número de archivos PDF de manera eficiente usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Concatenar archivos PDF grandes en Python usando buffer de disco
Abstract: Aprenda cómo combinar un gran número de archivos PDF de manera eficiente usando Aspose.PDF for Python. Este ejemplo demuestra cómo habilitar el buffer de disco para manejar PDFs grandes sin agotar la memoria del sistema, asegurando una concatenación fluida de muchos archivos.
---

Al trabajar con colecciones grandes de archivos PDF, el consumo de memoria puede convertirse en un cuello de botella durante la concatenación. Usando Aspose.PDF for Python, puedes habilitar el buffer de disco en el [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) clase para combinar muchos PDFs de manera eficiente. El método concatenate combina los archivos de entrada en un único PDF mientras que el buffer de disco evita un uso elevado de memoria. Este enfoque es ideal para procesar documentos en masa, generación automática de informes o consolidar archivos PDF grandes.

1. Crear un objeto PdfFileEditor.
1. Combina varios archivos PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_large_number_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.use_disk_buffer = True  # Enable disk buffering for large files
    pdf_editor.concatenate(files_to_merge, output_file)
```
