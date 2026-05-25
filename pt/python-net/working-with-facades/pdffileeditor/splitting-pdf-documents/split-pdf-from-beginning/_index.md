---
title: Dividir PDF a partir do Início
type: docs
weight: 10
url: /pt/python-net/split-pdf-from-beginning/
description: Divida um documento PDF a partir do início usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Divida PDF a partir do Início em Python Usando Aspose.PDF
Abstract: Aprenda como dividir um documento PDF a partir do início usando Aspose.PDF for Python. Este exemplo demonstra a extração de um número específico de páginas a partir da primeira página para criar um novo documento PDF.
---

Dividir PDFs a partir do início é útil quando você precisa das primeiras páginas de um documento como um arquivo separado. Usando Aspose.PDF for Python, o método split_from_first na [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe permite extrair um número definido de páginas a partir da página um. Esse recurso é ideal para gerar trechos, visualizações ou seções menores de um PDF maior sem editar manualmente o arquivo original.

1. Crie um objeto PdfFileEditor.
1. Dividir PDF a partir da primeira página.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF from Beginning
def split_pdf_from_beginning(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_from_first(input_pdf_path, 3, output_pdf_path)
```
