---
title: Adicionar Anotação de Círculo
type: docs
weight: 10
url: /pt/python-net/add-circle-annotation/
description: Este exemplo vincula um PDF de entrada, cria uma anotação de círculo na primeira página e salva o documento modificado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar Anotação de Círculo a um PDF Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como adicionar uma anotação de círculo a um documento PDF usando Aspose.PDF for Python via a API Facades. Ele mostra como definir os limites da anotação, definir o texto de conteúdo, configurar a cor e a aparência, e salvar o documento atualizado.
---

Anotações de círculo são úteis para destacar áreas de interesse em um documento PDF. Com [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode criar formas circulares especificando o retângulo que define os limites do círculo, juntamente com o texto da anotação, cor, opções de preenchimento, número da página e largura da borda.

1. Crie o objeto PdfContentEditor.
1. Vincular o PDF de entrada.
1. Defina os limites do círculo.
1. Adicione a anotação de círculo.
1. Salvar o Document atualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_circle_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create CircleAnnotation object
    rect = apd.Rectangle(300, 300, 400, 400)
    contents = "This is circle annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, False, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```
