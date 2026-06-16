---
title: PDF にフッターを追加
type: docs
weight: 10
url: /ja/python-net/add-footer/
description: Python の PDFFileStamp を使用して PDF ページにテキストと画像のフッターを追加する方法を学びましょう。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Python でテキストフッターと画像フッターを PDF に追加する方法
Abstract: この記事では、PDFFileStamp ファサードを使用して、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントにフッターコンテンツを追加する方法について説明します。更新された PDF を保存する前に、テキストフッターを追加する方法、画像フッターを配置する方法、カスタムフッターマージンを適用する方法を示します。
---

.NET 経由の Python 用 Aspose.PDF は [PDF ファイルスタンプ](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) PDF ページに繰り返しコンテンツを追加するためのファサード。これを使用して、各ページの下部にフッターテキストまたは画像を配置したり、フッターの余白を調整して配置を制御したりできます。

## テキストフッターを追加する

使用 `add_footer()` と `FormattedText` PDF のすべてのページに同じテキストフッターを配置する場合にオブジェクトを指定します。2 番目の引数は、フッターの配置に使用する下余白を設定します。

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

## 画像フッターの追加

使用 `add_footer()` フッターにテキストの代わりにロゴまたは別の画像を表示する必要がある場合は、画像ストリームを使用します。この例では、イメージファイルをバイナリストリームとして開き、各ページの下部に配置します。

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

## カスタム余白付きフッターの追加

フッターの配置をより細かく制御する必要がある場合は、3 つのマージン値を持つオーバーロードを使用してください。この例では、フッターにカスタムの下、左、右の余白が追加されています。

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
