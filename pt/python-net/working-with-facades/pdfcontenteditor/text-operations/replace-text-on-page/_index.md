---
title: Substituir Texto na Página
type: docs
weight: 10
url: /pt/python-net/replace-text-on-page/
description: Neste exemplo, a primeira ocorrência da palavra "PDF" é substituída por "Texto Substituído da Página 1" usando um tamanho de fonte especificado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Substituir Texto em uma Página Específica Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como substituir texto em um documento PDF usando Aspose.PDF for Python via a API Facades. Ele mostra como substituir a primeira ocorrência de texto em uma página e salvar o documento atualizado.
---

A substituição de texto é uma necessidade comum ao atualizar documentos PDF. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode pesquisar texto específico e substituí-lo por novo conteúdo. A propriedade ‘replace_text_strategy’ permite controlar quantas ocorrências são substituídas.

1. Crie uma instância de PdfContentEditor.
1. Vincule o documento PDF de entrada.
1. Configure a estratégia de substituição de texto.
1. Substitua o texto alvo.
1. Salve o documento PDF atualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_on_page(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text on page 1
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_FIRST
    )
    content_editor.replace_text("PDF", "Page 1 Replaced Text", 14)
    # Save updated document
    content_editor.save(outfile)
```
