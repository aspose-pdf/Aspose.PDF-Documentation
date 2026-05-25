---
title: Concatenar vários arquivos PDF
type: docs
weight: 20
url: /pt/python-net/concatenate-pdf-files/
description: Combine vários arquivos PDF em um único documento usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mesclar vários arquivos PDF em um PDF único em Python
Abstract: Aprenda como combinar vários arquivos PDF em um único documento usando Aspose.PDF for Python. Este exemplo demonstra como usar o método concatenate para mesclar vários PDFs sem interrupções, preservando seu conteúdo e formatação.
---

Mesclar arquivos PDF é uma tarefa comum na gestão de documentos, relatórios e fluxos de trabalho automatizados. Usando Aspose.PDF for Python, os desenvolvedores podem combinar facilmente vários arquivos PDF em um único documento consolidado. O método concatenate da [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe garante que todas as páginas dos arquivos de entrada sejam preservadas na saída final, mantendo seu layout e conteúdo originais. Essa abordagem é útil para criar relatórios abrangentes, combinar formulários ou arquivar vários documentos de forma eficiente.

1. Crie um objeto PdfFileEditor.
1. Mesclar Vários Arquivos PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge, output_file)
```
