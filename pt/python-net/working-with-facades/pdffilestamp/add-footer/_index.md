---
title: Adicionar rodapé ao PDF
type: docs
weight: 10
url: /pt/python-net/add-footer/
description: Aprenda como adicionar rodapés de texto e imagem às páginas PDF usando PdfFileStamp em Python.
lastmod: "2026-05-18"
TechArticle: true
AlternativeHeadline: Adicionar rodapés de texto e imagem ao PDF em Python
Abstract: Este artigo explica como adicionar conteúdo de rodapé a documentos PDF com Aspose.PDF for Python via .NET usando a fachada PdfFileStamp. Ele mostra como adicionar um rodapé de texto, inserir um rodapé de imagem e aplicar margens de rodapé personalizadas antes de salvar o PDF atualizado.
---

Aspose.PDF for Python via .NET fornece o [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) fachada para adicionar conteúdo repetido a páginas PDF. Você pode usá-la para colocar texto ou imagens de rodapé na parte inferior de cada página e ajustar as margens do rodapé para controlar a localização.

## Adicionar um rodapé de texto

Usar `add_footer()` com um `FormattedText` objeto quando você deseja colocar o mesmo rodapé de texto em cada página do PDF. O segundo argumento define a margem inferior usada para a colocação do rodapé.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_text_footer(infile: str, outfile: str) -> None:
    """Add a text footer with a bottom margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("Sample Footer")
        pdf_stamper.add_footer(text, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Adicionar um rodapé de imagem

Usar `add_footer()` com um fluxo de imagem quando o rodapé deve exibir um logotipo ou outra imagem em vez de texto. O exemplo abre o arquivo de imagem como um fluxo binário e o coloca na parte inferior de cada página.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_image_footer(infile: str, image_file: str, outfile: str) -> None:
    """Add an image footer with a bottom margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_footer(image_file, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Adicione um rodapé com margens personalizadas

Use a sobrecarga com três valores de margem quando precisar de mais controle sobre a posição do rodapé. Neste exemplo, o rodapé é adicionado com margens personalizadas inferior, esquerda e direita.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_footer_with_margins(infile: str, outfile: str) -> None:
    """Add a text footer with bottom, left, and right margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("This footer has margins on all sides.")
        pdf_stamper.add_footer(text, 20, 20, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
