---
title: スタンプクラス
type: docs
weight: 150
url: /ja/python-net/stamp-class/
description: Stamp クラスを使用して Python で PDF ドキュメントに画像、PDF、およびテキストベースのスタンプを追加する方法を学びます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

.NET 経由の Python 用 Aspose.PDF は [スタンプ](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/stamp/) 再利用可能なビジュアルコンテンツを PDF ページに配置するためのクラス。スタンプは、テキスト、画像、または別の PDF のページをもとにしたり、配置、回転、スタイルを設定したり、特定のページのみに限定したりできます。

この記事では、一般的なスタンプワークフローをいくつか紹介します。

1. テキストベースのスタンプ用に再利用可能なテキストリソースを作成します。
1. 画像と PDF ページのスタンプを追加します。
1. スタイル付きのテキストスタンプを追加します。
1. スタンプを選択したページに制限します。
1. 背景画像スタンプを設定します。

この例では 2 つの補助関数を使用しています。1 つはテキストベースのスタンプ用にフォーマットされたテキストを作成し、もう 1 つは `TextState` テキストスタンプのスタイル設定に使用されるオブジェクト。

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

## 画像スタンプの追加

使用 `bind_image()` スタンプにロゴ、バッジ、アイコンなどの画像を表示する必要がある場合。イメージをバインドしたら、ドキュメントに追加する前にスタンプ ID とオリジンを設定できます。

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

## PDF ページをスタンプとして追加

使用 `bind_pdf()` 別のPDFファイルのページをスタンプの内容として使用したい場合。これは、承認書、テンプレート、または別の文書に保存されている作成済みの視覚要素などのオーバーレイに役立ちます。

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

## テキストステート付きのテキストスタンプの追加

使用 `bind_logo()` と一緒に `bind_text_state()` カスタムフォントスタイルでテキストベースのスタンプを作成したいとき。この方法は、承認マーク、ラベル、およびワークフロー固有の注釈に役立ちます。

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

## 特定のページにスタンプを追加する

スタンプがすべてのページに表示されないようにするには、ターゲットページ番号をに割り当ててください `pages` 財産。この例では、最初のページにのみイメージスタンプを追加します。

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

## 背景画像スタンプの追加

ページコンテンツの背後に画像が表示される場合は、背景スタンプを使用してください。スタンプの不透明度、回転、品質、サイズ、位置を制御して、透かしのような効果を作成することもできます。

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

## 関連ファサードトピック

- [Python での PDF ファサードの操作](/pdf/ja/python-net/working-with-facades/)
- [PDFFileStampを使用してヘッダー、フッター、およびスタンプを追加します](/pdf/ja/python-net/pdffilestamp-class/)
- [Python で PDF ファイルにページスタンプを追加する方法](/pdf/ja/python-net/add-stamp/)
