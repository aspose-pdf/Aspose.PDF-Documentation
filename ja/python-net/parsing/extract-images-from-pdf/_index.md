---
title: Python を使用して PDF から画像を抽出する
linktitle: PDF から画像を抽出
type: docs
weight: 20
url: /ja/python-net/extract-images-from-the-pdf-file/
description: Aspose.PDF for Python を使用して PDF ファイルから埋め込み画像を抽出する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pythonを使ってPDFから画像を抽出する方法
Abstract: この記事では、Aspose.PDF for Python を使用して PDF ドキュメントから埋め込み画像を抽出する方法について説明します。Document クラスを使用してソース PDF を開く方法、ページリソースコレクションから画像にアクセスする方法、抽出した XImage を再利用、検査、または下流処理用に外部ファイルに保存する方法について説明しています。
---

使用 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) PDF を開き、ページリソースにアクセスして PDF を取得します [XImage](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximage/) オブジェクトを作成し、別のファイルとして保存します。この方法は、画像を再利用したり、抽出したアセットを検査したり、PDF コンテンツから画像処理ワークフローを構築したりする必要がある場合に役立ちます。

1. PDF をとして開く `Document`.
1. ターゲットページから画像リソースにアクセスします。
1. 必要なものを取得する `XImage` ページ画像コレクションから。
1. 抽出したイメージを出力ファイルに保存します。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```
