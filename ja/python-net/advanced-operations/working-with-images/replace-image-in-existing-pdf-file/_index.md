---
title: Python を使用して既存の PDF ファイル内の画像を置き換える
linktitle: 画像を置換
type: docs
weight: 70
url: /ja/python-net/replace-image-in-existing-pdf-file/
description: Python で既存の PDF ファイルに埋め込まれた画像を置き換える方法を学びましょう。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 既存の PDF ファイル内の画像を Python で置き換える
Abstract: この記事では、PDF ドキュメント内の画像を .NET 経由で Python 用 Aspose.PDF に置き換える方法を説明します。リソースインデックスによる画像の置き換えと、ImagePlacementAbsorber で見つかった特定の画像の置き換えについて説明します。
---

## PDF 内の画像を置き換える

このページは、文書のレイアウトを再構築せずに、PDF に埋め込まれているロゴ、図、またはその他のグラフィックを更新する必要がある場合に使用します。

1. ソース PDF を以下のようにロードします。 `ap.Document(infile)`.
1. 置換イメージをバイナリストリームとして開きます。
1. 画像リソースをページのインデックスに置き換えます。
1. 更新した PDF を保存します。

```python
import aspose.pdf as ap
from io import FileIO


def replace_image(infile, image_file, outfile):
    document = ap.Document(infile)

    with FileIO(image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(outfile)
```

## 特定の画像を置き換える

この例は、以下で見つかった特定の画像配置を置き換えます `ImagePlacementAbsorber`.

1. ソース PDF をロードします。
1. 作成 `ImagePlacementAbsorber` そして、ページ上の画像の配置を収集します。
1. ページ上に画像の配置が存在するかどうかを確認します。
1. 選択した配置を新しいイメージストリームに置き換えます。
1. 更新した PDF を保存します。

```python
import aspose.pdf as ap
from io import FileIO


def replace_image_with_absorber(infile, image_file, outfile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(outfile)
```

## 関連画像トピック

- [Python を使用して PDF 内の画像を操作する](/pdf/ja/python-net/working-with-images/)
- [PDF ファイルからの画像の削除](/pdf/ja/python-net/delete-images-from-pdf-file/)
- [PDF ファイルからの画像の抽出](/pdf/ja/python-net/extract-images-from-pdf-file/)
- [既存の PDF ファイルへの画像の追加](/pdf/ja/python-net/add-image-to-existing-pdf-file/)
