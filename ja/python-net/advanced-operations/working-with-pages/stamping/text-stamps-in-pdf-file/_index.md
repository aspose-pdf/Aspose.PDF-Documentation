---
title: Python で PDF にテキストスタンプを追加する方法
linktitle: PDF ファイル内のテキストスタンプ
type: docs
weight: 20
url: /ja/python-net/text-stamps-in-the-pdf-file/
description: Python で PDF 文書にテキストスタンプを追加する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF にテキストスタンプを追加する方法
Abstract: この記事では、Python 用 Aspose.PDF ライブラリを使用して PDF ファイルにテキストスタンプを追加する方法を包括的に説明します。`TextStamp` クラスを使用して、フォントサイズ、スタイル、色、配置などのプロパティを持つカスタマイズ可能なテキストスタンプを作成する方法について概説しています。この記事には、簡単なテキストスタンプの追加方法、テキスト配置の設定方法、フィルストロークテキストなどの高度なレンダリングモードの適用方法を示すコードスニペットが含まれています。最初のセクションでは、「Document」オブジェクトと「TextStamp」オブジェクトの作成、テキストプロパティの設定、特定のページへのスタンプの追加について説明します。2 番目のセクションでは、テキストを水平方向と垂直方向に揃える `text_alignment` プロパティを紹介し、PDF ページのテキストを中央に配置するコード例を紹介します。最後のセクションではレンダリングモードについて説明し、スタンプにバインドする前に `TextState` オブジェクトを使用してストロークの色とレンダリングモードを設定してフィルストロークテキストを追加する方法を示します。各セクションには、理解と実装を容易にする実用的な例が添えられています。
---

## Python でテキストスタンプを追加する

使用できます [テキストスタンプ](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) PDF ファイルにテキストスタンプを追加するためのクラス。 [テキストスタンプ](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) クラスには、フォントサイズ、フォントスタイル、フォントの色など、テキストベースのスタンプの作成に必要なプロパティが用意されています。テキストスタンプを追加するには、必要なプロパティを使用して Document オブジェクトと TextStamp オブジェクトを作成する必要があります。その後、呼び出すことができます。 [add_stamp ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) PDF にスタンプを追加するページのメソッド。次のコードスニペットは、PDF ファイルにテキストスタンプを追加する方法を示しています。これは PDF ページに注釈、透かし、ラベルを追加する場合に便利です。

1. PDF ドキュメントを開きます。
1. TextStamp オブジェクトを作成します。
1. スタンプの背景動作を設定します。
1. スタンプをページに配置します。
1. 必要に応じてスタンプを回転させてください。
1. テキストプロパティを設定します。
1. スタンプをページに追加します。
1. 変更した PDF ドキュメントを保存します。

```python
import sys
import aspose.pdf as ap
from os import path

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
    text_stamp.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    text_stamp.text_state.foreground_color = ap.Color.dark_green
    # Add stamp to particular page
    document.pages[1].add_stamp(text_stamp)

    document.save(output_file_name)
```

## スタンピング関連トピック

- [Python で PDF ページにスタンプを付ける](/pdf/ja/python-net/stamping/)
- [Python で PDF にページスタンプを追加する方法](/pdf/ja/python-net/page-stamps-in-the-pdf-file/)
- [Python で PDF にイメージスタンプを追加する方法](/pdf/ja/python-net/image-stamps-in-pdf-page/)
- [Python で PDF にページ番号を追加する方法](/pdf/ja/python-net/add-page-number/)