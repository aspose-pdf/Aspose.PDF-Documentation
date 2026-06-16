---
title: Python 経由で PDF からフォントを抽出
linktitle: PDF からフォントを抽出
type: docs
weight: 30
url: /ja/python-net/extract-fonts-from-pdf/
description: Aspose.PDF for Python ライブラリを使用して、PDF ドキュメントからすべての埋め込みフォントを抽出します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF からフォントを抽出する方法
Abstract: この記事では、Aspose.PDF for Python を使用して PDF ドキュメントで使用されているフォントを検査する方法について説明します。Document クラスで PDF を開き、font_utilities.get_all_fonts () を呼び出して使用可能なフォントオブジェクトを取得し、結果を繰り返し処理して分析、監査、または文書処理ワークフローでフォント名を読み取る方法を説明します。
---

使用 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) PDF を開いて電話するには `font_utilities.get_all_fonts()` 利用可能なものをすべて取得するには [フォント](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/font/) ドキュメントが参照するオブジェクト。埋め込みフォントの監査、変換前のフォントの入手可否の確認、文書リソースの分析などに役立ちます。

1. ソース PDF をとして開きます `Document`.
1. コール `document.font_utilities.get_all_fonts()` フォントコレクションを取得します。
1. 返されたものを繰り返し処理する `Font` オブジェクト。
1. それぞれを読んで印刷する `font.font_name` 価値。

```python

    import aspose.pdf as apdf
    from os import path

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```
