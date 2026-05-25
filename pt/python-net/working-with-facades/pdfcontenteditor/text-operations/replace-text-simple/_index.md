---
title: Substituir Texto Simples
type: docs
weight: 40
url: /pt/python-net/replace-text-simple/
description: Neste exemplo, todas as ocorrências de "33" são substituídas por "XXXIII " em todo o documento. Isso demonstra a substituição direta de strings sem formatação personalizada ou expressões regulares.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Substituir Texto em um PDF Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como substituir texto em todo um documento PDF usando Aspose.PDF for Python via a API Facades. Ele substitui todas as ocorrências de uma cadeia especificada por um novo texto.
---

A substituição simples de texto é útil ao atualizar valores repetidos em um documento. Com [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode definir um escopo de substituição e substituir o texto globalmente em todas as páginas.

1. Criar um [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instância.
1. Vincule o documento PDF de entrada.
1. Configure o escopo de substituição para todas as ocorrências.
1. Substitua o texto alvo.
1. Salve o documento PDF atualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_simple(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text in the whole document
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("33", "XXXIII ")
    # Save updated document
    content_editor.save(outfile)
```
