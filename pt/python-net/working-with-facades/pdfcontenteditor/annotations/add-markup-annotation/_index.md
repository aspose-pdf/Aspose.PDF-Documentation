---
title: Adicionar Anotações de Marcação
type: docs
weight: 30
url: /pt/python-net/add-markup-annotation/
description: Este exemplo associa um PDF de entrada, adiciona quatro anotações de marcação diferentes na primeira página e salva o documento atualizado. Cada anotação demonstra um estilo de marcação e cor diferentes.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar Anotações de Marcação de Realce, Sublinhado, Tachado e Ondulado em um PDF Usando Python
Abstract: Este exemplo demonstra como adicionar múltiplas anotações de marcação—realce, sublinhado, tachado e ondulado—em um documento PDF usando Aspose.PDF for Python via the Facades API. O exemplo mostra como definir áreas de anotação, especificar tipos de marcação, aplicar cores e salvar o documento modificado.
---

Anotações de marcação são usadas para enfatizar ou revisar texto dentro de um PDF. Com PdfContentEditor, você pode aplicar programaticamente estilos de marcação diferentes especificando uma área retangular, texto de comentário, tipo de marcação, número da página e cor.

1. Criar o [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objeto.
1. Vincular o PDF de entrada.
1. Definir retângulos de anotação.
1. Adicionar Anotações de Marcação.
1. Salvar o Document atualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_markup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add markup annotation to page 1
    content_editor.create_markup(
        apd.Rectangle(120, 440, 200, 20),
        "This is a highlight annotation",
        0,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 542, 200, 20),
        "This is a underline annotation",
        1,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(120, 568, 200, 20),
        "This is a strikeout annotation",
        2,
        1,
        apd.Color.orange_red,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 598, 200, 20),
        "This is a squiggly annotation",
        3,
        1,
        apd.Color.dark_blue,
    )
    # Save updated document
    content_editor.save(outfile)
```
