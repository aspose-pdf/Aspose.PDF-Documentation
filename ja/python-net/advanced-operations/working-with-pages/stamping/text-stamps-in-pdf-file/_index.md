---
title: PythonでPDFにテキストスタンプを追加する
linktitle: PDFファイルのテキストスタンプ
type: docs
weight: 20
url: /ja/python-net/text-stamps-in-the-pdf-file/
description: Aspose.PDF for Python ライブラリの TextStamp クラスを使用して、PDF ドキュメントにテキストスタンプを追加します。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pythonを使用してPDFにテキストスタンプを追加する方法
Abstract: この記事では、Aspose.PDF for Python ライブラリを使用して PDF ファイルにテキストスタンプを追加する包括的なガイドを提供します。フォントサイズ、スタイル、色、配置などのプロパティを持つカスタマイズ可能なテキストスタンプを作成するための `TextStamp` クラスの使用方法を概説します。記事には、シンプルなテキストスタンプの追加、テキスト配置の設定、塗りつぶしストロークテキストのような高度な描画モードの適用方法を示すコードスニペットが含まれています。最初のセクションでは、`Document` と `TextStamp` オブジェクトの作成、テキストプロパティの設定、特定のページへのスタンプの追加について説明します。第二のセクションでは、`text_alignment` プロパティを紹介し、テキストを水平・垂直に配置する方法を示し、PDF ページの中央にテキストを配置するコード例を提供します。最後のセクションでは、描画モードについて説明し、`TextState` オブジェクトを使用してストローク色と描画モードを設定し、スタンプにバインドする前に塗りつぶしストロークテキストを追加する方法を示します。各セクションには、理解と実装を容易にする実用的な例が添えられています。
---

## Pythonでテキストスタンプを追加する

PDF ファイルにテキストスタンプを追加するには、[TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) クラスを使用できます。[TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) クラスは、フォントサイズ、フォントスタイル、フォントカラーなど、テキストベースのスタンプを作成するために必要なプロパティを提供します。テキストスタンプを追加するには、必要なプロパティを指定して Document オブジェクトと TextStamp オブジェクトを作成する必要があります。その後、Page の [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) メソッドを呼び出して PDF にスタンプを追加できます。以下のコードスニペットは、PDF ファイルにテキストスタンプを追加する方法を示しています。これは、PDF ページに注釈、透かし、またはラベルを追加する際に便利です。

1. PDF ドキュメントを開く。
1. TextStamp オブジェクトを作成する。
1. スタンプの背景動作を設定する。
1. ページ上にスタンプを配置する。
1. 必要に応じてスタンプを回転させる。
1. テキストプロパティを設定する。
1. ページにスタンプを追加する。
1. 変更された PDF ドキュメントを保存する。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_stamp(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Create text stamp
    text_stamp = ap.TextStamp("Sample Stamp")
    # Set whether stamp is background
    text_stamp.background = True
    # Set origin
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # Rotate stamp
    text_stamp.rotate = ap.Rotation.ON90
    # Set text properties
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    text_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    text_stamp.text_state.foreground_color = ap.Color.dark_green
    # Add stamp to particular page
    document.pages[1].add_stamp(text_stamp)

    document.save(output_file_name)
```

