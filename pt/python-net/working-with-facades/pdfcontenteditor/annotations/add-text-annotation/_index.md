---
title: Adicionar Anotações de Texto
type: docs
weight: 50
url: /pt/python-net/add-text-annotation/
description: Adicionar anotações de texto a um documento PDF usando a classe PdfContentEditor no Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar Anotações de Texto em Python
Abstract: Aprenda como adicionar anotações de texto a um documento PDF usando a classe PdfContentEditor no Aspose.PDF for Python via .NET. Este exemplo mostra como posicionar uma anotação de texto em uma posição específica, definir seu título e conteúdo, e salvar o arquivo PDF atualizado.
---

Este artigo mostra como adicionar uma anotação de texto a um documento PDF usando o [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) classe no Aspose.PDF.

Anotações de texto permitem que você anexe comentários, notas ou informações extra a partes específicas de uma página de PDF. Essas anotações podem aparecer como ícones e ser expandidas pelos usuários ao visualizar o documento.

Neste exemplo:

- Um documento PDF é carregado no PdfContentEditor.
- Uma anotação de texto é adicionada em uma posição específica na página.
- A anotação inclui um título, conteúdo, tipo de ícone e configurações de visibilidade.
- O documento modificado é salvo em um novo arquivo.

1. Crie um objeto PdfContentEditor.
1. Vincule o Document PDF de entrada.
1. Defina a posição da anotação.
1. Adicione anotação de texto.
1. Salve o PDF atualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add text annotation to page 1
    content_editor.create_text(
        apd.Rectangle(100, 400, 50, 50),
        "Text Annotation",
        "This is a text annotation",
        True,
        "Insert",
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```
