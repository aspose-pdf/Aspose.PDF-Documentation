---
title: Python で既存の PDF にイメージを追加する方法
linktitle: PDF に画像を追加
type: docs
weight: 10
url: /ja/python-net/add-image-to-existing-pdf-file/
description: Python で既存の PDF ファイルに画像を追加する方法、固定座標に配置する方法、代替テキストを設定する方法、画像圧縮を使用する方法について説明します。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Python を使用して既存の PDF ファイルに画像を追加する
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントに画像を追加する方法を説明します。固定座標への画像の配置、低レベルの PDF 演算子による画像の描画、アクセシビリティのための代替テキストの割り当て、Flate 圧縮による画像の埋め込みについて説明します。
---

## Python で既存の PDF ファイルにイメージを追加する方法

この例は、.NET 経由の Aspose.PDF for Python を使用して、既存の PDF ページの固定位置に画像を配置する方法を示しています。

既存のPDFレイアウトにロゴ、写真、スタンプ、グラフ、その他のグラフィックを追加する必要がある場合は、これらの例を使用してください。ページ座標を使用して画像を配置したり、演算子を使用して描画したり、アクセシビリティテキストを追加したり、画像圧縮を制御したりできます。

1. で既存の PDF を読み込む `ap.Document(infile)`.
1. ターゲットページを選択してください (`document.pages[1]` 最初のページ用）。
1. コール `page.add_image()` と:
    -画像ファイルのパス。
    -A `Rectangle` 配置座標の定義
1. 更新した PDF を保存します。

```python
import aspose.pdf as ap


def add_image(infile, image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))
    document.save(outfile)
```

## 演算子を使用して PDF に画像を追加する

この方法では、高レベルのPDF演算子ではなく低レベルのPDF演算子を含む画像が追加されます。 `add_image()` ヘルパー。

1. 新規作成 `Document` そしてページを追加します。
1. ページリソースに画像を追加する (`page.resources.images`).
1. 変換演算子の作成 (`GSave`, `ConcatenateMatrix`, `Do`, `GRestore`).
1. ページコンテンツに演算子を追加します。
1. 結果の PDF を保存します。

```python
import aspose.pdf as ap
from io import FileIO


def add_image_using_operators(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream)

    rectangle = ap.Rectangle(0, 0, page.media_box.width, page.media_box.height, True)

    operators = [
        ap.operators.GSave(),
        ap.operators.ConcatenateMatrix(
            ap.Matrix(
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            )
        ),
        ap.operators.Do(image_id),
        ap.operators.GRestore(),
    ]

    page.contents.add(operators)
    document.save(outfile)
```

## 代替テキスト付きの PDF への画像の追加

この例では、アクセシビリティのために画像を追加し、代替テキストを割り当てています。

1. 新規作成 `Document` そしてページを追加します。
1. を使用してページに画像を追加します `page.add_image()`.
1. から画像リソースを取得 `page.resources.images`.
1. 代替テキストを使用して設定 `try_set_alternative_text()`.
1. 結果の PDF を保存します。

```python
import aspose.pdf as ap


def add_image_set_alternative_text(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)

    page.add_image(image_file, ap.Rectangle(0, 0, 842, 595, True))
    resources_images = page.resources.images
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text("Alternative text for image", page)

    if result:
        print("Alternative text has been added successfully")

    document.save(outfile)
```

## フレート圧縮による PDF への画像の追加

この例では、を使用して画像を埋め込みます `ImageFilterType.FLATE` 圧縮。

1. 新規作成 `Document` そしてページを追加します。
1. Flate圧縮を使用して画像をページリソースに追加します。
1. 行列演算子を使用して画像を配置および描画します。
1. 文書を保存します。

```python
import aspose.pdf as ap
from io import FileIO


def add_image_to_pdf_with_flate_compression(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream, ap.ImageFilterType.FLATE)

    rectangle = ap.Rectangle(0, 0, 600, 600, True)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.lly,
    )

    page.contents.add([ap.operators.GSave()])
    page.contents.add([ap.operators.ConcatenateMatrix(matrix)])
    page.contents.add([ap.operators.Do(image_id)])
    page.contents.add([ap.operators.GRestore()])

    document.save(outfile)
```

## 関連画像トピック

- [Python を使用して PDF 内の画像を操作する](/pdf/ja/python-net/working-with-images/)
- [既存の PDF ファイル内の画像の置換](/pdf/ja/python-net/replace-image-in-existing-pdf-file/)
- [PDF ファイルからの画像の削除](/pdf/ja/python-net/delete-images-from-pdf-file/)
- [PDF ファイルからの画像の抽出](/pdf/ja/python-net/extract-images-from-pdf-file/)
