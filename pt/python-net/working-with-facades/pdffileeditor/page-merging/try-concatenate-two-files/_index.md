---
title: Tente Concatenar Dois Arquivos PDF
type: docs
weight: 90
url: /pt/python-net/try-concatenate-two-files/
description: Concatene dois arquivos PDF usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mesclar Dois Arquivos PDF com Segurança em Python sem Exceções
Abstract: Aprenda como concatenar dois arquivos PDF com segurança usando Aspose.PDF for Python. O método try_concatenate mescla os arquivos sem gerar exceções, permitindo um tratamento de erro elegante caso a operação falhe.
---

A fusão de dois arquivos PDF pode às vezes falhar devido a corrupção de arquivos, formatos incompatíveis ou outros problemas. Usando Aspose.PDF for Python, o método try_concatenate da classe PdfFileEditor permite tentar mesclar dois PDFs com segurança. Se a operação falhar, ele retorna False em vez de gerar uma exceção, proporcionando controle total sobre o tratamento de erros em fluxos de trabalho automatizados ou processamento em lotes.

1. Crie um objeto PdfFileEditor.
1. Tente Mesclar Dois Arquivos PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def try_concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    if not pdf_editor.try_concatenate(
        files_to_merge[0], files_to_merge[1], output_file
    ):
        print("Concatenation failed for the provided files.")
```
