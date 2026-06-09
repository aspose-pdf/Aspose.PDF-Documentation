---
title: PDF にページ番号を追加
type: docs
weight: 30
url: /ja/python-net/page-number/
description: Python の PDFFileStamp を使用して PDF ドキュメントにページ番号を追加する方法を学びましょう。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Python で PDF にページ番号を追加する方法
Abstract: この記事では、PDFFileStamp ファサードを使用して、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントにページ番号を追加する方法について説明します。デフォルトの配置でページ番号を追加する方法、カスタム座標に配置する方法、および配置と余白を制御する方法を示します。
---

.NET 経由の Python 用 Aspose.PDF は [PDF ファイルスタンプ](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) PDF ページに繰り返しコンテンツを追加するためのファサード。これを使用して、ページ番号をデフォルトの位置で挿入したり、特定の座標に配置したり、配置や余白を制御したりできます。

## ページ番号を既定の配置で追加

使用 `add_page_number()` ページ番号をデフォルトの場所に追加したい場合、追加の位置引数は必要ありません。これは文書内の各ページに番号を付ける最も簡単な方法です。

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

## カスタム座標にページ番号を追加

各ページの特定の X および Y 位置にページ番号を表示する必要がある場合は、座標ベースのオーバーロードを使用してください。この方法は、文書レイアウトにカスタム配置が必要な場合に便利です。

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

## 配置と余白を含むページ番号の追加

ページ番号が表示される場所をより細かく制御する必要がある場合は、position 引数と margin 引数付きのオーバーロードを使用してください。この例では、数字はページの右上の領域に揃えられ、余白が明記されています。

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

## ページ番号をローマ字スタイルで追加

「add_page_numbers_with_roman_style」関数は、大文字のローマ数字を使用してページ番号を追加することによってPDF文書を拡張する方法を示します。Aspose.PDF の PDFFileStamp クラスを利用して、すべてのページに一貫した番号付けを適用します。

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
