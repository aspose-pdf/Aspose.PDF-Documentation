---
title: Adicionar Anotação de Polígono
type: docs
weight: 40
url: /pt/python-net/add-polygon-annotation/
description: Este exemplo associa um PDF de entrada, desenha um polígono sólido na primeira página e salva o documento modificado com uma anotação.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar Anotação de Polígono a um PDF Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como adicionar uma anotação de polígono a um documento PDF usando Aspose.PDF for Python via the Facades API. Ele mostra como definir os vértices do polígono, o estilo da borda, os limites da anotação, texto descritivo e salvar o documento atualizado.
---

Anotações de polígonos são usadas para destacar áreas ou formas irregulares em um PDF, proporcionando ênfase visual ou marcando regiões específicas. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode criar polígonos especificando as coordenadas dos vértices, o estilo da borda, o número da página e o retângulo da anotação.

1. Crie o objeto PdfContentEditor.
1. Vincular o PDF de entrada.
1. Configure as propriedades do Polígono.
1. Adicione a anotação de Polígono.
1. Salvar o Document atualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_polygon_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0  # 0 - Solid
    line_info.vertice_coordinate = [100, 200, 150, 260, 220, 220, 200, 160]
    content_editor.create_polygon(
        line_info,
        1,
        apd.Rectangle(90, 150, 150, 120),
        "This is polygon annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
