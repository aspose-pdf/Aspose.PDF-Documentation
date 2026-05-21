---
title: Dividir PDF em Páginas Únicas
type: docs
weight: 30
url: /pt/python-net/split-pdf-into-single-pages/
description: Divida o documento PDF em PDFs de página única usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dividir um PDF em Páginas Individuais em Python
Abstract: Saiba como dividir um documento PDF em PDFs de página única usando Aspose.PDF for Python. Este método extrai cada página do PDF original e a salva como um arquivo separado para gerenciamento e processamento flexíveis de documentos.
---

Dividir um PDF em páginas individuais é útil para processamento ao nível de página, impressão ou distribuição de seções de um documento individualmente. Usando Aspose.PDF for Python, o método 'split_to_pages' da [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe cria arquivos PDF separados para cada página no documento de origem. Essa abordagem permite a extração automatizada de páginas para arquivamento, revisão ou compartilhamento individual, preservando o layout e o conteúdo originais.

1. Crie um objeto PdfFileEditor.
1. Dividir PDF em páginas individuais.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF into Single Pages
def split_pdf_into_single_pages(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_pages(input_pdf_path, output_pdf_path)
```
