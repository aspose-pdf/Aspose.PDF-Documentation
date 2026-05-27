---
title: Adicionar Anotação Quadrada
type: docs
weight: 60
url: /pt/python-net/add-square-annotation/
description: Este exemplo associa um PDF de entrada, adiciona uma anotação quadrada azul preenchida na primeira página e salva o documento modificado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar Anotação Quadrada a um PDF Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como adicionar uma anotação quadrada a um documento PDF usando Aspose.PDF for Python via a Facades API. Ele mostra como definir o retângulo da anotação, o conteúdo de texto, a cor, as opções de preenchimento e salvar o documento atualizado.
---

Anotações quadradas são comumente usadas para destacar áreas de interesse, marcar seções importantes ou fornecer pistas visuais em um documento PDF. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode criar anotações quadradas (ou circulares) especificando o retângulo delimitador, o texto de conteúdo, a cor da borda, a opção de preenchimento, o número da página e a espessura da borda.

1. Crie o objeto PdfContentEditor.
1. Vincular o PDF de entrada.
1. Defina a anotação Square.
1. Adicione a anotação Square.
1. Salvar o Document atualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_square_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create SquareAnnotation object
    rect = apd.Rectangle(100, 300, 200, 400)
    contents = "This is square annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, True, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```
