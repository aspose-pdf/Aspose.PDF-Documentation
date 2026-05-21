---
title: Adicionar número de página ao PDF
type: docs
weight: 30
url: /pt/python-net/page-number/
description: Saiba como adicionar números de página a documentos PDF usando PdfFileStamp em Python.
lastmod: "2026-05-18"
TechArticle: true
AlternativeHeadline: Adicionar números de página ao PDF em Python
Abstract: Este artigo explica como adicionar números de página a documentos PDF com Aspose.PDF for Python via .NET usando a fachada PdfFileStamp. Ele mostra como adicionar números de página com o posicionamento padrão, posicioná‑los em coordenadas personalizadas e controlar o alinhamento e as margens.
---

Aspose.PDF for Python via .NET fornece o [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) fachada para adicionar conteúdo repetido às páginas PDF. Você pode usá-la para inserir números de página com posicionamento padrão, posicioná‑los em coordenadas específicas ou controlar seu alinhamento e margens.

## Adicionar números de página com o posicionamento padrão

Usar `add_page_number()` sem argumentos de posição adicionais quando você deseja que os números de página sejam adicionados na localização padrão. Esta é a maneira mais simples de numerar cada página do documento.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_default(infile: str, outfile: str) -> None:
    """Add centered page numbers to the bottom of each page."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number("Page #")
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Adicionar números de página em coordenadas personalizadas

Use a sobrecarga baseada em coordenadas quando precisar que os números de página apareçam em uma posição X e Y específicas em cada página. Essa abordagem é útil quando o layout do documento requer um posicionamento personalizado.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_at_coordinates(infile: str, outfile: str) -> None:
    """Add page numbers at explicit X/Y coordinates."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number("Page #", 300, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Adicionar números de página com alinhamento e margens

Use a sobrecarga com argumentos de posição e margem quando precisar de mais controle sobre onde os números de página aparecem. Neste exemplo, os números são alinhados à área superior‑direita da página com margens explícitas.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_with_position_and_margins(infile: str, outfile: str) -> None:
    """Add page numbers using a predefined position and page margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number(
            "Page #",
            pdf_facades.PdfFileStamp.POS_BOTTOM_RIGHT,
            10,
            10,
            10,
            10,
        )
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Adicionar numeração de páginas no estilo romano

A função 'add_page_numbers_with_roman_style' mostra como aprimorar um documento PDF adicionando numeração de páginas usando numerais romanos maiúsculos. Ela utiliza a classe PdfFileStamp da Aspose.PDF para aplicar numeração consistente em todas as páginas.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_with_roman_style(infile: str, outfile: str) -> None:
    """Add page numbers with a custom start value and Roman numbering."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.numbering_style = ap.NumberingStyle.NUMERALS_ROMAN_UPPERCASE
        pdf_stamper.starting_number = 42
        pdf_stamper.add_page_number("Page #", pdf_facades.PdfFileStamp.POS_UPPER_RIGHT)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
