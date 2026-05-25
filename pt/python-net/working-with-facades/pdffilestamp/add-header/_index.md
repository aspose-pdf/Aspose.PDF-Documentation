---
title: Adicionar cabeçalho ao PDF
type: docs
weight: 20
url: /pt/python-net/add-header/
description: Saiba como adicionar cabeçalhos de texto e imagem às páginas PDF usando PdfFileStamp em Python.
lastmod: "2026-05-18"
TechArticle: true
AlternativeHeadline: Adicionar cabeçalhos de texto e imagem ao PDF em Python
Abstract: Este artigo explica como adicionar conteúdo de cabeçalho a documentos PDF com Aspose.PDF for Python via .NET usando a fachada PdfFileStamp. Ele mostra como adicionar um cabeçalho de texto, inserir um cabeçalho de imagem e aplicar margens de cabeçalho personalizadas antes de salvar o PDF atualizado.
---

Aspose.PDF for Python via .NET fornece o [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) fachada para adicionar conteúdo repetido às páginas PDF. Você pode usá-la para colocar texto de cabeçalho ou imagens no topo de cada página e ajustar as margens do cabeçalho para controlar a posição.

## Adicionar um cabeçalho de texto

Usar `add_header()` com um `FormattedText` objeto quando você quer colocar o mesmo texto de cabeçalho em cada página do PDF. O segundo argumento define a margem superior para o cabeçalho.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_text_header(infile: str, outfile: str) -> None:
    """Add a text header with a top margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("Sample Header")
        pdf_stamper.add_header(text, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Adicionar um cabeçalho de imagem

Usar `add_header()` com um arquivo de imagem ou fluxo de imagem quando o cabeçalho deve exibir um logo ou outro gráfico. Isso é útil para layouts de documentos com marca.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_image_header(infile: str, image_file: str, outfile: str) -> None:
    """Add an image header with a top margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_header(image_file, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Adicionar um cabeçalho com margens personalizadas

Use a sobrecarga com três valores de margem quando precisar de mais controle sobre a posição do cabeçalho. Neste exemplo, o cabeçalho é adicionado com margens superiores, esquerda e direita personalizadas.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_header_with_margins(infile: str, outfile: str) -> None:
    """Add a text header with top, left, and right margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText(
            text="Sample Header",
            text_color=ap_pydrawing.Color.blue,
            font_name="Arial",
            text_encoding=pdf_facades.EncodingType.WINANSI,
            embedded=True,
            font_size=12.0,
        )
        pdf_stamper.add_header(text, 20, 20, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
