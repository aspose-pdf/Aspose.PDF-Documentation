---
title: Substituir Texto com Regex
type: docs
weight: 30
url: /pt/python-net/replace-text-regex/
description: Neste exemplo, todos os números de quatro dígitos no documento são substituídos pelo placeholder "[NUMBER]". Isso é útil para mascarar dados sensíveis, normalizar o conteúdo ou anonimizar documentos.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Substituir Texto Usando Expressões Regulares com PdfContentEditor em Python
Abstract: Este exemplo demonstra como substituir texto em um PDF usando expressões regulares com Aspose.PDF for Python via a API Facades. Ele mostra como buscar padrões e substituir todas as correspondências ao longo do documento.
---

Expressões regulares permitem substituição flexível de texto baseada em padrões em vez de cadeias fixas. Ao habilitar o suporte a regex em 'replace_text_strategy', você pode corresponder conteúdo dinâmico, como números, datas ou strings formatadas.

1. Criar um [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instância.
1. Vincule o documento PDF de entrada.
1. Configure a estratégia de substituição para usar regex.
1. Substitua padrões correspondentes em todo o documento.
1. Salve o documento PDF atualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_regex(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text in the whole document
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text_strategy.is_regular_expression_used = True
    content_editor.replace_text(r"\d{4}", "[NUMBER]")
    # Save updated document
    content_editor.save(outfile)
```
