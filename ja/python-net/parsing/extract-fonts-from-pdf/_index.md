---
title: PythonでPDFからフォントを抽出する
linktitle: PDFからフォントを抽出する
type: docs
weight: 30
url: /ja/python-net/extract-fonts-from-pdf/
description: Aspose.PDF for Python ライブラリを使用して、PDF ドキュメントに埋め込まれたすべてのフォントを抽出します。
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使って PDF からフォントを抽出する方法
Abstract: この記事では、Aspose.PDF ライブラリの特定のメソッドを使用して PDF ドキュメントからすべてのフォントを抽出する方法を解説します。`Document` クラスで利用できる `font_utilities.get_all_fonts()` メソッドを紹介し、フォント情報の取得を容易にします。記事には、必要なモジュールのインポート、PDF ドキュメントのオープン、フォントの反復処理、各フォント名の出力を示す Python コードスニペットが含まれています。このアプローチは、PDF ファイル内のフォントデータを分析または操作する必要がある開発者にとって有用です。
---

PDF ドキュメントからすべてのフォントを取得したい場合は、`Document` クラスで提供されている `font_utilities.get_all_fonts()` メソッドを使用できます。既存の PDF ドキュメントからすべてのフォントを取得するためのコードスニペットは次のとおりです:

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

