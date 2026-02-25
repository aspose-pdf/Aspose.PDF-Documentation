---
title: PythonでPDFにページ番号を追加する
linktitle: ページ番号の追加
type: docs
weight: 30
url: /ja/python-net/add-page-number/
description: Aspose.PDF for Python via .NET を使用すると、PageNumber スタンプクラスを使用して PDF ファイルにページ番号スタンプを追加できます。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pythonを使用してPDFにページ番号を追加する方法
Abstract: この記事では、文書にページ番号を追加することの重要性と、PDF ファイルでこれを実現するためのツールとして Aspose.PDF for Python via .NET ライブラリを紹介します。このライブラリは PageNumberStamp クラスを利用しており、フォーマット、余白、配置、開始番号など、ページ番号スタンプをカスタマイズするためのプロパティを提供します。手順は Document オブジェクトと PageNumberStamp オブジェクトを作成し、必要なプロパティを設定した後、add_stamp() メソッドを使用して PDF ページにスタンプを適用することです。この記事では、カスタマイズ可能なフォント属性を使用してページ番号スタンプを設定および適用する Python コード例を提供しています。
---

すべての文書にはページ番号が必要です。ページ番号は、読者が文書のさまざまな部分を見つけやすくします。

**Aspose.PDF for Python via .NET** は、[PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) を使用してページ番号を追加できるようにします。

## PDFへのページ番号スタンプの追加

Aspose.PDF for Python を使用して PDF の [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) に動的なページ番号スタンプを追加します。[`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) オブジェクトを使用すると、現在のページ番号と総ページ数を自動的に表示できます。例では、ページ番号スタンプを作成し、[`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) を使用して外観（フォント、サイズ、スタイル、色、配置、余白）をカスタマイズし、[`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) の特定のページに [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) メソッドで適用する方法を示しています。配置値は [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) 列挙体から取得でき、色・フォント・スタイルは [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) と [`FontStyles`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontstyles/)（フォントは [`FontRepository.find_font()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontrepository/#methods) で検索）で利用できます。この機能は、プロフェッショナルなページ番号付き文書の作成や PDF ワークフローでのページ付け自動化に役立ちます。

1. PDF ドキュメントを開く。
1. ページ番号スタンプを作成する。
1. スタンプのプロパティを設定する。
1. テキストスタイルをカスタマイズする。
1. スタンプをページに適用する。
1. 変更された PDF を保存する。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

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
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    document.pages[1].add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## PDFにローマ数字ページ番号を追加する

PDF ドキュメントのすべてのページにローマ数字形式でページ番号を追加します。ページ番号は [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) を使用してスタンプとして追加され、フォント、サイズ、スタイル、色、配置をカスタマイズできます。[`NumberingStyle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/) 列挙体を使用してローマ数字やその他の番号付け方式を選択できます。番号付けは任意の開始値から開始することも可能です。

1. PDF ドキュメントを開く。
1. ページ番号スタンプを作成する。
1. スタンプのプロパティを構成する。
1. テキストの外観を設定する。
1. すべてのページにスタンプを適用する。
1. 変更された PDF を保存する。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

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

## ライブ例

[Add PDF page numbers](https://products.aspose.app/pdf/page-number) は、ページ番号追加機能の動作を調べることができるオンラインの無料ウェブアプリケーションです。

[![PythonでPDFにページ番号を追加する方法](page_number.png)](https://products.aspose.app/pdf/page-number)


