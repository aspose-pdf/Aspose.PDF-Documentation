---
title: Python で PDF にページ番号を追加する方法
linktitle: ページ番号の追加
type: docs
weight: 30
url: /ja/python-net/add-page-number/
description: Python で PDF 文書にページ番号スタンプを追加する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF にページ番号を追加する方法
Abstract: この記事では、文書にページ番号を追加してナビゲーションを容易にすることの重要性について説明し、PDF ファイルでページ番号を追加するためのツールとして Aspose.PDF for Python (.NET ライブラリ経由) を紹介します。このライブラリでは PageNumberStamp クラスを使用します。このクラスには、フォーマット、余白、配置、開始番号など、ページ番号スタンプをカスタマイズするためのプロパティが用意されています。このプロセスでは、Document オブジェクトと PageNumberStamp オブジェクトを作成し、必要なプロパティを設定し、add_stamp () メソッドを使用して PDF ページにスタンプを適用します。この記事では、カスタマイズ可能なフォント属性を使用してページ番号スタンプを設定して適用する方法を示す Python コード例を紹介します。
---

すべての文書にはページ番号が含まれている必要があります。ページ番号があると、読者は文書のさまざまな部分を見つけやすくなります。

**.NET 経由の Python 用 Aspose.pdf **では、次のようにページ番号を追加できます [ページ番号スタンプ](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

## PDF へのページ番号スタンプの追加

PDF への動的ページ番号スタンプの追加 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Python 用の Aspose.PDF を使う。は [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) オブジェクトを使用すると、現在のページ番号と合計ページ数を自動的に表示できます。この例は、ページ番号スタンプを作成し、その外観 (フォント、サイズ、スタイル、色、配置、余白) をカスタマイズする方法を示しています。 [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/)そしてそれを特定のものに適用する [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) PDFでご覧になるには [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) 方法。アライメント値は次の式から取得されます。 [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) enum、および色/フォント/スタイルは次の方法で入手できます。 [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) そして [`FontStyles`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontstyles/) (経由で検出されたフォント [`FontRepository.find_font()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontrepository/#methods))。この機能は、プロフェッショナルな番号付き文書を生成したり、PDF ワークフローのページネーションを自動化したりするのに役立ちます。

1. PDF ドキュメントを開きます。
1. ページ番号スタンプを作成します。
1. スタンプのプロパティを設定します。
1. テキストスタイルをカスタマイズします。
1. スタンプをページに適用します。
1. 変更した PDF を保存します。

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_num_stamp(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.format = "Page # of " + str(len(document.pages))
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 1
    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    document.pages[1].add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## PDF へのローマ数字のページ番号の追加

PDF 文書のすべてのページにローマ数字形式のページ番号を追加します。ページ番号は、を使用してスタンプとして追加されます。 [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/)、フォント、サイズ、スタイル、色、配置をカスタマイズできます。を使用してください。 [`NumberingStyle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/) enum を使用してローマ数字やその他の番号付けスキームを選択します。番号付けは任意の指定値から開始することもできます。

1. PDF ドキュメントを開きます。
1. ページ番号スタンプを作成します。
1. スタンプのプロパティを設定します。
1. テキストの外観を設定します。
1. スタンプをすべてのページに適用します。
1. 変更した PDF を保存します。

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_num_stamp_roman(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 42
    page_number_stamp.numbering_style = ap.NumberingStyle.NUMERALS_ROMAN_UPPERCASE

    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    for page in document.pages:
        page.add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## ライブサンプル

[PDF ページ番号の追加](https://products.aspose.app/pdf/page-number) は、ページ番号の追加機能の仕組みを調べることができる無料のオンラインWebアプリケーションです。

[![Pythonを使用してPDFにページ番号を追加する方法](page_number.png)](https://products.aspose.app/pdf/page-number)

## スタンピング関連トピック

- [Python で PDF ページにスタンプを付ける](/pdf/ja/python-net/stamping/)
- [Python で PDF にページスタンプを追加する方法](/pdf/ja/python-net/page-stamps-in-the-pdf-file/)
- [Python で PDF にイメージスタンプを追加する方法](/pdf/ja/python-net/image-stamps-in-pdf-page/)
- [Python で PDF にテキストスタンプを追加する方法](/pdf/ja/python-net/text-stamps-in-the-pdf-file/)