---
title: Adicionar Anotação de Caret
type: docs
weight: 10
url: /pt/python-net/add-caret-annotation/
description: Este exemplo carrega um PDF existente, adiciona uma anotação de caret à primeira página e salva o documento modificado. A anotação inclui um símbolo de caret vermelho e texto de comentário descritivo.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar Anotação de Caret a um PDF Usando Python
Abstract: Este exemplo demonstra como adicionar uma anotação de caret a um documento PDF usando Aspose.PDF for Python via a API Facades. O exemplo mostra como vincular um arquivo PDF, definir a posição da anotação usando retângulos, configurar as propriedades do caret e salvar o documento atualizado.
---

Anotações de caret são comumente usadas para indicar inserções de texto ou comentários editoriais em um documento. Com o PdfContentEditor, você pode adicionar anotações de caret programaticamente, especificando o número da página, os limites da anotação, a área de chamada, o símbolo, o texto da nota e a cor.

1. Criar o [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objeto.
1. Vincular o PDF de entrada.
1. Definir parâmetros da Anotação Caret:
  - Número da página onde a anotação será adicionada
  - Retângulo Caret (posição da anotação)
  - Retângulo de chamada (área de texto)
  - Símbolo (por exemplo "P")
  - Texto da anotação
  - Cor da anotação
1. Adicionar a anotação de cursor.
1. Salvar o Document atualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_caret_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add caret annotation to page 1
    content_editor.create_caret(
        1,
        apd.Rectangle(350, 400, 10, 10),
        apd.Rectangle(300, 380, 115, 15),
        "P",
        "This is a caret annotation",
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```
