---
title: Pythonで既存のPDFに画像を追加する
linktitle: PDFに画像を追加する
type: docs
weight: 10
url: /ja/python-net/add-image-to-existing-pdf-file/
description: Pythonで既存のPDFファイルに画像を追加し、固定座標に配置し、代替テキストを設定し、画像圧縮を使用する方法を学びます。
lastmod: "2026-05-05"
TechArticle: true
AlternativeHeadline: Pythonを使用して既存のPDFファイルに画像を追加する
Abstract: この記事では、Aspose.PDF for Python via .NET を使用して PDF 文書に画像を追加する方法を示します。固定座標に画像を配置する方法、低レベルの PDF 演算子で画像を描画する方法、アクセシビリティのために代替テキストを割り当てる方法、そして Flate 圧縮で画像を埋め込む方法について説明します。
---

## Python で既存の PDF ファイルに画像を追加する

この例では、Aspose.PDF for Python via .NET を使用して、既存の PDF ページ上の固定位置に画像を配置する方法を示します。

ロゴ、写真、スタンプ、チャート、またはその他のグラフィックを既存の PDF レイアウトに追加する必要がある場合は、これらの例を使用してください。ページ座標で画像を配置したり、演算子で描画したり、アクセシビリティテキストを追加したり、画像圧縮を制御したりできます。

1. 既存の PDF を読み込む `ap.Document(infile)`.
1. 対象ページを選択 (`document.pages[1]` 最初のページ用に)
1. 呼び出す `page.add_image()` と:
    - 画像ファイルのパス。
    - A `Rectangle` 配置座標を定義する。
1. 更新された PDF を保存します。

```python
import aspose.pdf as ap


def add_image(infile, image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))
    document.save(outfile)
```

## 演算子を使用して PDF に画像を追加する

このアプローチは、高レベルの PDF オペレータの代わりに、低レベルの PDF オペレータで画像を追加します。 `add_image()` ヘルパー。

1. 新規作成 `Document` ページを追加します。
1. ページ リソースに画像を追加する（`page.resources.images`).
1. 変換オペレーターを作成する (`GSave`, `ConcatenateMatrix`, `Do`, `GRestore`).
1. ページコンテンツにオペレーターを追加します。
1. 結果として得られたPDFを保存します。

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

## 代替テキスト付きで画像をPDFに追加

この例では画像を追加し、アクセシビリティのために代替テキストを割り当てます。

1. 新規作成 `Document` ページを追加します。
1. 画像をページに追加する `page.add_image()`.
1. 画像リソースを取得 `page.resources.images`.
1. 代替テキストを設定する `try_set_alternative_text()`.
1. 結果として得られたPDFを保存します。

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

## Flate 圧縮で PDF に画像を追加する

この例では画像を埋め込みます `ImageFilterType.FLATE` 圧縮。

1. 新規作成 `Document` ページを追加します。
1. Flate 圧縮でページリソースに画像を追加する。
1. 行列演算子を使用して画像を配置し、描画する。
1. ドキュメントを保存します。

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

- [Python を使用して PDF の画像を操作する](/pdf/ja/python-net/working-with-images/)
- [既存の PDF ファイルの画像を置き換える](/pdf/ja/python-net/replace-image-in-existing-pdf-file/)
- [PDF ファイルから画像を削除する](/pdf/ja/python-net/delete-images-from-pdf-file/)
- [PDF ファイルから画像を抽出する](/pdf/ja/python-net/extract-images-from-pdf-file/)
