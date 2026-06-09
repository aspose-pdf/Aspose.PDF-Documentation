---
title: Python を使用して PDF ファイルから画像を抽出する
linktitle: 画像を抽出
type: docs
weight: 30
url: /ja/python-net/extract-images-from-pdf-file/
description: Python で PDF ファイルから埋め込み画像を抽出する方法を学びましょう。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Python を使用して PDF ファイルから画像を抽出する
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントから画像を抽出する方法を説明します。埋め込まれた 1 つの画像を抽出する方法と、ページ上の特定の四角形領域内にある画像をエクスポートする方法について説明しています。
---

このページは、埋め込まれたグラフィックを再利用したり、画像アセットをアーカイブしたり、PDF 以外の画像コンテンツを処理したりする必要がある場合に使用します。

1. ソース PDF を以下のようにロードします。 `ap.Document(infile)`.
1. ターゲットページとイメージリソースインデックスを選択します。
1. イメージオブジェクトを出力ストリームに保存します。

```python
import aspose.pdf as ap
from io import FileIO


def extract_image(infile, outfile):
    document = ap.Document(infile)
    x_image = document.pages[1].resources.images[1]
    with FileIO(outfile, "wb") as output_image:
        x_image.save(output_image)
```

## PDF の特定の領域から画像を抽出

この例は、PDF ページの指定された矩形領域内にある画像を抽出し、それらを個別のファイルとして保存します。

1. ソース PDF をロードします。
1. 作成 `ImagePlacementAbsorber` ターゲットページで受け入れてください。
1. ターゲットの長方形を定義します。
1. 画像の配置を繰り返して、各画像の境界が領域に収まるかどうかを確認します。
1. 一致した画像を出力ファイルに保存します。

```python
import aspose.pdf as ap
from io import FileIO


def extract_image_from_specific_region(infile, outfile):
    document = ap.Document(infile)
    rectangle = ap.Rectangle(0, 0, 590, 590, True)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(image_placement.rectangle.llx, image_placement.rectangle.lly)
        point2 = ap.Point(image_placement.rectangle.urx, image_placement.rectangle.ury)

        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(outfile.replace("index", str(index)), "wb") as output_image:
                image_placement.image.save(output_image)
            index += 1
```

## 関連画像トピック

- [Python を使用して PDF 内の画像を操作する](/pdf/ja/python-net/working-with-images/)
- [既存の PDF ファイル内の画像の置換](/pdf/ja/python-net/replace-image-in-existing-pdf-file/)
- [PDF ファイルからの画像の削除](/pdf/ja/python-net/delete-images-from-pdf-file/)
- [既存の PDF ファイルへの画像の追加](/pdf/ja/python-net/add-image-to-existing-pdf-file/)
