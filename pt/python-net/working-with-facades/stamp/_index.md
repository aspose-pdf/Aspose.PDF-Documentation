---
title: Classe Stamp
type: docs
weight: 150
url: /pt/python-net/stamp-class/
description: Aprenda a trabalhar com a classe Stamp para adicionar carimbos de imagem, PDF e baseados em texto a documentos PDF em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Python via .NET fornece o [Carimbo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/stamp/) classe para colocar conteúdo visual reutilizável em páginas PDF. Uma marca pode ser baseada em texto, uma imagem ou até mesmo uma página de outro PDF, e pode ser posicionada, girada, estilizada e limitada a páginas específicas.

Este artigo demonstra vários fluxos de trabalho comuns de carimbo:

1. Criar recursos de texto reutilizáveis para carimbos baseados em texto.
1. Adicionar carimbos de imagem e de página PDF.
1. Adicionar carimbos de texto estilizados.
1. Limite um carimbo a páginas selecionadas.
1. Configure um carimbo de imagem de fundo.

O exemplo usa duas funções auxiliares: uma cria texto formatado para carimbos baseados em texto, e a outra cria um `TextState` objeto usado para estilizar carimbos de texto.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def _create_text_logo(text: str) -> pdf_facades.FormattedText:
    """Create formatted text for text stamp examples."""
    return pdf_facades.FormattedText(
        text,
        drawing.Color.blue,
        drawing.Color.light_gray,
        pdf_facades.FontStyle.HELVETICA_BOLD,
        pdf_facades.EncodingType.WINANSI,
        True,
        14,
    )


def _create_text_state() -> ap.text.TextState:
    """Create a text state used to style text stamps."""
    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.dark_blue
    text_state.font_size = 16
    text_state.font_style = ap.text.FontStyles.BOLD
    return text_state
```

## Adicionar um carimbo de imagem

Usar `bind_image()` quando o carimbo deve exibir uma imagem, como um logotipo, emblema ou ícone. Depois de vincular a imagem, você pode definir o ID do carimbo e a origem antes de adicioná-lo ao documento.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to the PDF."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.stamp_id = 1
        stamp.set_origin(36, 520)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Adicionar uma página PDF como carimbo

Usar `bind_pdf()` quando você deseja usar uma página de outro arquivo PDF como o conteúdo do selo. Isso é útil para sobreposições, como aprovações, modelos ou elementos visuais pré-construídos armazenados em um documento separado.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_pdf_page_as_stamp(infile: str, stamp_pdf: str, outfile: str) -> None:
    """Add the first page of another PDF as a stamp."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_pdf(stamp_pdf, 1)
        stamp.page_number = 1
        stamp.set_origin(36, 250)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Adicionar um carimbo de texto com estado de texto

Usar `bind_logo()` junto com `bind_text_state()` quando você deseja criar um selo baseado em texto com estilo de fonte personalizado. Esta abordagem é útil para marcas de aprovação, rótulos e anotações específicas de fluxo de trabalho.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_text_stamp_with_text_state(infile: str, outfile: str) -> None:
    """Add a text stamp and style it with a TextState object."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_logo(_create_text_logo("Approved by signing workflow"))
        stamp.bind_text_state(_create_text_state())
        stamp.set_origin(36, 700)
        stamp.rotation = 15.0

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Adicionar um carimbo a páginas específicas

Se o carimbo não deve aparecer em todas as páginas, atribua os números das páginas de destino a `pages` propriedade. Este exemplo adiciona um carimbo de imagem apenas na primeira página.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_stamp_to_specific_pages(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp only to the selected pages."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.pages = [1]
        stamp.set_origin(400, 40)
        stamp.set_image_size(120, 60)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Adicionar um carimbo de imagem de fundo

Use um carimbo de fundo quando a imagem deve aparecer atrás do conteúdo da página. Você também pode controlar a opacidade, rotação, qualidade, tamanho e posição do carimbo para criar efeitos no estilo de marca d'água.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_background_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add a rotated background image stamp with opacity and quality settings."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.is_background = True
        stamp.opacity = 0.35
        stamp.quality = 90
        stamp.rotation = 45.0
        stamp.set_image_size(160, 80)
        stamp.set_origin(200, 300)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Tópicos Relacionados a Facades

- [Trabalhando com Fachadas PDF em Python](/pdf/pt/python-net/working-with-facades/)
- [Adicione cabeçalhos, rodapés e carimbos com PdfFileStamp](/pdf/pt/python-net/pdffilestamp-class/)
- [Adicionar um carimbo de página a arquivos PDF em Python](/pdf/pt/python-net/add-stamp/)
