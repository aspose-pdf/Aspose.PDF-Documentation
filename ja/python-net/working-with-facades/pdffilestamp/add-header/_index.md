---
title: PDF にヘッダーを追加
type: docs
weight: 20
url: /ja/python-net/add-header/
description: Python の PDFFileStamp を使用して PDF ページにテキストヘッダーと画像ヘッダーを追加する方法を学びましょう。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Python でテキストヘッダーと画像ヘッダーを PDF に追加する方法
Abstract: この記事では、PDFFileStamp ファサードを使用して、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントにヘッダーコンテンツを追加する方法について説明します。更新された PDF を保存する前に、テキストヘッダーを追加する方法、画像ヘッダーを配置する方法、カスタムヘッダーマージンを適用する方法を示します。
---

.NET 経由の Python 用 Aspose.PDF は [PDF ファイルスタンプ](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) PDF ページに繰り返しコンテンツを追加するためのファサード。これを使用して、各ページの上部にヘッダーテキストまたは画像を配置したり、ヘッダーの余白を調整して配置を制御したりできます。

## テキストヘッダーの追加

使用 `add_header()` と `FormattedText` PDF のすべてのページに同じヘッダーテキストを配置する場合にオブジェクトを指定します。2 番目の引数はヘッダーの上余白を定義します。

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

## 画像ヘッダーの追加

使用 `add_header()` ヘッダーにロゴまたは別のグラフィックを表示する必要がある場合は、画像ファイルまたは画像ストリームを使用します。これはブランド文書のレイアウトに便利です。

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

## カスタム余白付きのヘッダーの追加

ヘッダーの配置をより細かく制御する必要がある場合は、3 つのマージン値をもつオーバーロードを使用してください。この例では、ヘッダーにカスタムの上、左、右の余白が追加されています。

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
