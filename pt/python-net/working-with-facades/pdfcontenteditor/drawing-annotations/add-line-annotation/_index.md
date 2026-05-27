---
title: Adicionar Anotação de Linha
type: docs
weight: 30
url: /pt/python-net/add-line-annotation/
description: Este exemplo vincula um PDF de entrada, desenha uma anotação de linha vermelha com pontas de linha quadradas e salva o PDF modificado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar Anotação de Linha a um PDF Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como adicionar uma anotação de linha a um documento PDF usando Aspose.PDF for Python via a API Facades. Ele explica como definir os pontos inicial e final da linha, os limites do retângulo, as propriedades de aparência e salvar o documento atualizado.
---

Anotações de linha são úteis para enfatizar texto, destacar relacionamentos ou chamar a atenção para áreas específicas em um PDF. Com [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode criar programaticamente anotações de linha especificando os pontos inicial e final, o retângulo delimitador, a cor, o estilo da borda e as pontas da linha.

1. Crie o objeto PdfContentEditor.
1. Vincular o PDF de entrada.
1. Defina as propriedades da Anotação de Linha.
1. Adicione a anotação de Linha.
1. Salvar o Document atualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_line_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create LineAnnotation object
    rect = apd.Rectangle(100, 100, 200, 200)
    contents = "This is line annotation"
    content_editor.create_line(
        rect,
        contents,
        100,
        100,
        200,
        200,
        1,
        1,
        apd.Color.red,
        "Solid",
        [3, 2],
        ["Square"],
    )

    # Save output PDF file
    content_editor.save(outfile)
```
