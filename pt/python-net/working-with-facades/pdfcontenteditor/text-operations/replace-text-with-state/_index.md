---
title: Substituir Texto com Estado
type: docs
weight: 50
url: /pt/python-net/replace-text-with-state/
description: Neste exemplo, todas as ocorrências de \u0022software\u0022 são substituídas por \u0022SOFTWARE\u0022 e formatadas em azul com tamanho de fonte 14.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Substituir Texto com Formatação Personalizada em um PDF Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como substituir texto em um documento PDF enquanto aplica formatação personalizada usando Aspose.PDF for Python via a API Facades. Ele mostra como controlar a cor do texto e o tamanho da fonte durante a substituição.
---

Ao atualizar texto em um PDF, você pode querer que o conteúdo substituído se destaque. Usando um objeto TextState, você pode definir estilo como cor e tamanho da fonte, e então aplicá-lo a todo o texto substituído.

1. Criar um [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)  instância.
1. Vincule o documento PDF de entrada.
1. Defina um TextState com formatação personalizada.
1. Configurar escopo de substituição.
1. Substituir texto em todo o documento.
1. Salve o documento PDF atualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_with_state(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 14

    # Replace text with explicit text formatting
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("software", "SOFTWARE", text_state)
    # Save updated document
    content_editor.save(outfile)
```
