---
title: Adicionar Anotação de Curva
type: docs
weight: 20
url: /pt/python-net/add-curve-annotation/
description: Este exemplo vincula um PDF de entrada, desenha uma curva tracejada na primeira página e salva o documento modificado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar Anotação de Curva a um PDF Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como adicionar uma anotação de curva a um documento PDF usando Aspose.PDF for Python via a API Facades. Ele mostra como definir os vértices da curva, o estilo da borda, os limites da anotação, o conteúdo de texto e salvar o documento atualizado.
---

Anotações de curva são usadas para destacar caminhos ou formas irregulares em um PDF, proporcionando ênfase visual ou marcando áreas importantes. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode desenhar curvas especificando uma sequência de vértices, estilo de borda, visibilidade, retângulo da anotação e texto descritivo.

1. Crie o objeto PdfContentEditor.
1. Vincular o PDF onput.
1. Configure as propriedades da Curve.
1. Desenhe a anotação Curve.
1. Salvar o Document atualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_curve_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 1  # 1 - Dashed
    line_info.vertice_coordinate = [120, 520, 160, 560, 220, 540, 280, 580]
    line_info.visibility = True
    content_editor.draw_curve(
        line_info,
        1,
        apd.Rectangle(110, 510, 220, 100),
        "This is curve annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
