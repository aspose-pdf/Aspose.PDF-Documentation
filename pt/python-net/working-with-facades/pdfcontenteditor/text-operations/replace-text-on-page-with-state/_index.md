---
title: Substituir Texto na Página com Estado
type: docs
weight: 20
url: /pt/python-net/replace-text-on-page-with-state/
description: Neste exemplo, todas as ocorrências da palavra "software" na página 1 são substituídas por "SOFTWARE PAGE 1", usando texto vermelho com tamanho de fonte 12.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Substituir Texto com Formatação Personalizada em uma Página Específica Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como substituir texto em uma página específica de um PDF enquanto aplica formatação personalizada usando Aspose.PDF for Python via the Facades API. Ele mostra como controlar o tamanho da fonte e a cor durante a substituição de texto.
---

Às vezes, substituir texto em um PDF também requer alterações de formatação, como cor ou tamanho da fonte. Usando TextState, você pode definir propriedades de estilo e aplicá-las durante a substituição. Isso permite realçar o texto modificado ou impor formatação consistente em todos os documentos.

1. Criar um [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instância.
1. Vincule o documento PDF de entrada.
1. Defina um TextState com formatação personalizada.
1. Configure a estratégia de substituição.
1. Substitua texto em uma página específica.
1. Salve o documento PDF atualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_on_page_with_state(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.red
    text_state.font_size = 12

    # Replace text on a specific page with explicit text formatting
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("software", 1, "SOFTWARE PAGE 1", text_state)
    # Save updated document
    content_editor.save(outfile)
```
