---
title: Adicionar Anotação de Polilinha
type: docs
weight: 50
url: /pt/python-net/add-polyline-annotation/
description: O exemplo vincula um PDF de entrada, cria uma polilinha sólida na primeira página e salva o documento modificado com uma anotação.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar Anotação de Polilinha a um PDF Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como adicionar uma anotação de polilinha a um documento PDF usando Aspose.PDF for Python via a API Facades. Mostra como definir uma sequência de vértices, estilo de borda, retângulo da anotação, texto e salvar o documento atualizado.
---

Anotações de polilinha permitem que você destaque uma série de segmentos de linha conectados em um PDF. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode desenhar uma polilinha especificando as coordenadas dos vértices, o estilo da borda, o número da página e os limites da anotação. Isso é útil para representar visualmente caminhos, tendências ou conexões em diagramas e documentos.

1. Crie o objeto PdfContentEditor.
1. Vincular o PDF de entrada.
1. Configurar propriedades da Polilinha.
1. Adicionar a anotação de Polilinha.
1. Salvar o Document atualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_polyline_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0  # 0 - Solid
    line_info.vertice_coordinate = [120, 420, 180, 460, 230, 430, 290, 470]
    content_editor.create_poly_line(
        line_info,
        1,
        apd.Rectangle(110, 410, 200, 90),
        "This is polyline annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
