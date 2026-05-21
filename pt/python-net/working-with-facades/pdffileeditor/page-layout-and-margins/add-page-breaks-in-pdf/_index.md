---
title: Adicionar quebras de página em PDF
type: docs
weight: 20
url: /pt/python-net/add-page-breaks-in-pdf/
description: Inserir quebras de página em um documento PDF usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar quebras de página às páginas PDF programaticamente em Python
Abstract: Saiba como inserir quebras de página em um documento PDF usando Aspose.PDF for Python. Este exemplo demonstra como dividir uma página em uma posição vertical especificada, permitindo que os desenvolvedores reorganizem o conteúdo e criem páginas adicionais dinamicamente.
---

Quebras de página são úteis quando você precisa dividir páginas PDF longas em várias páginas ou controlar como o conteúdo é distribuído em um documento. Usando Aspose.PDF for Python, os desenvolvedores podem inserir quebras de página em posições específicas sem editar manualmente o PDF.

Este artigo mostra como usar o método 'add_page_break' de [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe para inserir uma quebra de página em uma coordenada vertical definida em uma página selecionada. O método cria uma nova página e move o conteúdo abaixo do ponto de quebra para essa página.

1. Crie um objeto PdfFileEditor.
1. Defina a posição da quebra de página.
1. Insira a quebra de página.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Page Breaks in PDF
def add_page_breaks_in_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.add_page_break(
        infile,
        outfile,
        [
            pdf_facades.PdfFileEditor.PageBreak(1, 400),
        ],
    )
```
