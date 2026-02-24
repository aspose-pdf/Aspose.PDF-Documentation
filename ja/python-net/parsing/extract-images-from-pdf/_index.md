---
title: Python を使用して PDF から画像を抽出する
linktitle: PDF から画像を抽出
type: docs
weight: 20
url: /ja/python-net/extract-images-from-the-pdf-file/
description: Aspose.PDF for Python を使用して PDF から画像の一部を抽出する方法
lastmod: "2023-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python 経由で PDF から画像を抽出する方法
Abstract: 本記事では、Python を使用して PDF ドキュメントから埋め込み画像を抽出するための簡潔なガイドを提供します。プロセスは主に3つのステップで構成されます。PDF ドキュメントの読み込み、画像リソースへのアクセス、そして画像をファイルに保存することです。コードスニペットは Aspose.PDF ライブラリを活用してこれらの操作を簡素化します。最初に、指定されたパスから PDF ドキュメントを読み込み、最初のページのリソースから目的の画像へアクセスします。最後に、ファイル I/O 操作を使用して指定された出力ファイルに画像を保存し、さらに分析、編集、または他のドキュメントでの再利用が可能になります。
---

このコードスニペットは、PDF ドキュメントから埋め込み画像を抽出し、別途分析、編集、または他のドキュメントでの再利用ができるようにします。

1. PDF ドキュメントを読み込む
1. 画像リソースにアクセスする
1. 画像をファイルに保存する

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```

