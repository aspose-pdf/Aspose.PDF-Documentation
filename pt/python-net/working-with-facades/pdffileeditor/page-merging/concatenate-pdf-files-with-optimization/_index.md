---
title: Concatenar arquivos PDF com otimização
type: docs
weight: 30
url: /pt/python-net/concatenate-pdf-files-with-optimization/
description: Concatenar vários arquivos PDF em um único PDF otimizado usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mesclar arquivos PDF com saída otimizada em Python
Abstract: Aprenda como concatenar vários arquivos PDF em um único PDF otimizado usando Aspose.PDF for Python. Este exemplo demonstra como habilitar a otimização de tamanho para reduzir o tamanho do arquivo de saída, preservando o conteúdo e a formatação.
---

Ao mesclar vários PDFs, o arquivo resultante pode ficar grande, especialmente se contiver imagens ou conteúdo complexo. Usando Aspose.PDF for Python, os desenvolvedores podem habilitar a otimização durante a concatenação para reduzir o tamanho do arquivo sem perder qualidade. A propriedade optimize_size na [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe garante que o PDF mesclado seja compacto e eficiente, tornando-o adequado para compartilhamento, armazenamento ou arquivamento.

1. Crie um objeto PdfFileEditor e habilite a otimização.
1. Mescle arquivos PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files_with_optimization(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.optimize_size = True  # Enable optimization for smaller output file size
    pdf_editor.concatenate(files_to_merge, output_file)
```
