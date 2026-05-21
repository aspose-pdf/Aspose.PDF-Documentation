---
title: Concatenar Dois Arquivos PDF
type: docs
weight: 60
url: /pt/python-net/concatenate-two-files/
description: Concatenar dois arquivos PDF em um único documento usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mesclar Dois Arquivos PDF em um PDF Único no Python
Abstract: Aprenda como concatenar dois arquivos PDF em um único documento usando Aspose.PDF for Python. Este exemplo demonstra como mesclar dois PDFs de forma contínua, preservando seu conteúdo e formatação originais.
---

Combinar dois arquivos PDF é uma tarefa comum ao consolidar relatórios, contratos ou formulários. Usando Aspose.PDF for Python, você pode mesclar programaticamente dois PDFs em um único documento usando o método concatenate da [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe. Isso garante que todas as páginas de ambos os arquivos sejam incluídas no PDF de saída, mantendo o layout, conteúdo e estrutura originais.

1. Crie um objeto PdfFileEditor.
1. Mesclar dois arquivos PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge[0], files_to_merge[1], output_file)
```
