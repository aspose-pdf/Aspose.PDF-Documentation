---
title: Concatenar grande número de arquivos PDF
type: docs
weight: 10
url: /pt/python-net/concatenate-large-number-files/
description: Mescle um grande número de arquivos PDF de forma eficiente usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Concatenar arquivos PDF grandes em Python usando buffering de disco
Abstract: Aprenda como mesclar um grande número de arquivos PDF de forma eficiente usando Aspose.PDF for Python. Este exemplo demonstra como habilitar o buffering de disco para lidar com PDFs grandes sem esgotar a memória do sistema, garantindo uma concatenação suave de muitos arquivos.
---

Ao trabalhar com grandes coleções de arquivos PDF, o consumo de memória pode se tornar um gargalo durante a concatenação. Usando Aspose.PDF for Python, você pode habilitar o buffering de disco no [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe para mesclar muitos PDFs de forma eficiente. O método concatenate combina os arquivos de entrada em um único PDF enquanto o buffer de disco evita alto uso de memória. Esta abordagem é ideal para processar documentos em massa, geração automática de relatórios ou consolidação de grandes arquivos PDF.

1. Crie um objeto PdfFileEditor.
1. Mesclar vários arquivos PDF.

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
