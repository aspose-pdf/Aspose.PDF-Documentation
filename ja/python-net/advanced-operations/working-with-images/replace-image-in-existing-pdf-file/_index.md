---
title: Python を使用して既存の PDF ファイルの画像を置き換える
linktitle: 画像を置き換える
type: docs
weight: 70
url: /ja/python-net/replace-image-in-existing-pdf-file/
description: このセクションでは、Python ライブラリを使用して既存の PDF ファイルの画像を置き換える方法について説明します。
lastmod: "2025-09-17"
TechArticle: true
AlternativeHeadline: PDF の画像を置き換える
Abstract: Aspose.PDF for Python via .NET のドキュメントは、既存の PDF ファイル内の画像を置き換えるための包括的なガイドを提供しています。この機能は、テキストコンテンツを変更せずに、PDF ドキュメントのロゴ、グラフィック、その他の視覚要素を更新する際に不可欠です。
---

## PDF の画像を置き換える

PDF ページ上の既存の画像を新しい画像に置き換える方法は？Aspose.PDF for Python via .NET を使用して実装します。

1. 必要なモジュール（aspose.pdf、os.path、FileIO）をインポートします。
1. パスを定義します：
- 入力 PDF（infile）
- 新しい画像ファイル（image_file）
- 出力 PDF（outfile）
1. 'apdf.Document(path_infile)' を使用して PDF ドキュメントをロードします。
1. 新しい画像ファイルをバイナリ読み取りモードで開きます。
1. 最初のページの最初の画像を置き換えます：
- 'document.pages[1].resources.images.replace(1, image_stream)'
1. 更新された PDF を 'path_outfile' に保存します。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, outfile)

    document = apdf.Document(path_infile)

    with FileIO(path_image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(path_outfile)
```

## 特定の画像を置き換える

この例では、画像配置検出により PDF ページ上の特定の画像を特定して置き換える方法を示しています。

1. 'apdf.Document()' を使用して PDF をロードします。
1. ページ上のすべての画像配置を収集するために 'ImagePlacementAbsorber' を作成します。
1. 最初のページで吸収器を受け入れます（'document.pages[1].accept(absorber)'）。
1. ページに画像配置が存在するか確認します。
1. 最初の画像配置（absorber.image_placements[1]）を選択し、置き換えます。
1. 変更された PDF を 'path_outfile' に保存します。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, outfile)

    document = apdf.Document(path_infile)

    # Create ImagePlacementAbsorber to find image placements
    absorber = apdf.ImagePlacementAbsorber()

    # Accept the absorber for the first page
    document.pages[1].accept(absorber)

    # Replace the first image placement found
    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(path_image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(path_outfile)
```
