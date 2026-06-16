---
title: PDF 内の画像の取得と検索
linktitle: 画像の取得と検索
type: docs
weight: 40
url: /ja/python-net/search-and-get-images-from-pdf-document/
description: Python で PDF 文書内の画像を検索して調べる方法を学びます。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Python を使用して PDF ファイル内の画像を検索して検査する
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内の画像を検索および検査する方法を説明します。ImagePlacementAbsorber を使用してイメージの配置、サイズ、解像度、代替テキストを分析する方法について説明します。
---

## PDF ページの画像配置プロパティの検査

この例は、.NET 経由の Aspose.PDF for Python を使用して、特定の PDF ページのすべての画像のプロパティを分析および表示する方法を示しています。

このページは、画像の配置を監査したり、画像の解像度を検査したり、PDF ページに埋め込まれている画像オブジェクトを特定したりする必要がある場合に使用します。

1. 「画像配置アブソーバー」を作成して、ページ上のすべての画像を収集します。
1. 'document.pages [1] .accept (アブソーバー) 'を呼び出して、最初のページの画像の配置を分析します。
1. 「absorber.image_placements」を繰り返し処理して、各画像の主要なプロパティを表示します。
    -幅と高さ (ポイント)。
    -左下の X (LLX) 座標と左下の Y (LLY) 座標。
    -水平 (X) および垂直 (Y) 解像度 (DPI)。

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_params(infile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))
```

## PDF 内の画像タイプの抽出とカウント

この関数は、PDF の最初のページのすべての画像を解析し、グレースケール画像と RGB 画像の数をカウントします。

1. 「画像配置アブソーバー」を作成して、ページ上のすべての画像を収集します。
1. グレースケールおよび RGB 画像のカウンターを初期化します。
1. 'document.pages [1] .accept (アブソーバー) 'を呼び出して、画像の配置を分析してください。
1. 見つかった画像の総数を印刷します。
1. 「absorber.image_placements」の各画像を繰り返し処理します。
    -'image_placement.image.get_color_type () 'を使用して画像のカラータイプを取得します。
    -対応するカウンタ (グレースケールまたは RGB) をインクリメントします。
    -グレースケールか RGB かを示すメッセージを各画像に印刷します。

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_types_from_pdf(infile):
    """
    Extract and count image types (grayscale/RGB) with resolution analysis.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_image_types_from_pdf("sample_extr.pdf")

    Note:
        Prints total images count, color type for each image, and resolution info.
    """

    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()

    # Counters for grayscale and RGB images
    grayscaled = 0
    rgb = 0

    document.pages[1].accept(absorber)

    print("--------------------------------")
    print("Total Images = " + str(len(absorber.image_placements)))

    image_counter = 1

    for image_placement in absorber.image_placements:
        # Determine the color type of the image
        colorType = image_placement.image.get_color_type()
        if colorType == ap.ColorType.GRAYSCALE:
            grayscaled += 1
            print(f"Image {image_counter} is Grayscale...")
        elif colorType == ap.ColorType.RGB:
            rgb += 1
            print(f"Image {image_counter} is RGB...")
        image_counter += 1

    print("--------------------------------")
    print("Grayscale Images = " + str(grayscaled))
    print("RGB Images = " + str(rgb))
```

## PDF から詳細な画像情報を抽出

この関数は、PDFの最初のページのすべての画像を分析し、ページのグラフィック変換に基づいて拡大縮小されたサイズと有効解像度を計算します。

1. PDF の読み込みと変数の初期化
1. 画像リソースの収集
1. プロセスページコンテンツオペレータ:
    -'GSave'-現在の CTM をスタックにプッシュします。
    -'GREStore'-スタックから最後の CTM をポップします。
    -'ConcatenateMatrix'-オペレーターのマトリックスを乗算して現在の CTM を更新します。
1. 画像名、拡大縮小後のサイズ、計算された解像度を印刷します。

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_information_from_pdf(infile):
    with ap.Document(infile) as document:
        default_resolution = 72
        graphics_state = []

        image_names = list(document.pages[1].resources.images.names)

        graphics_state.append(
            drawing.drawing2d.Matrix(
                float(1), float(0), float(0), float(1), float(0), float(0)
            )
        )

        for op in document.pages[1].contents:
            if is_assignable(op, ap.operators.GSave):
                graphics_state.append(
                    cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone()
                )

            elif is_assignable(op, ap.operators.GRestore):
                graphics_state.pop()

            elif is_assignable(op, ap.operators.ConcatenateMatrix):
                op_cm = cast(ap.operators.ConcatenateMatrix, op)
                cm = drawing.drawing2d.Matrix(
                    float(op_cm.matrix.a),
                    float(op_cm.matrix.b),
                    float(op_cm.matrix.c),
                    float(op_cm.matrix.d),
                    float(op_cm.matrix.e),
                    float(op_cm.matrix.f),
                )

                graphics_state[-1].multiply(cm)
                continue

            elif is_assignable(op, ap.operators.Do):
                op_do = cast(ap.operators.Do, op)
                if op_do.name in image_names:
                    last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                    index = image_names.index(op_do.name) + 1
                    image = document.pages[1].resources.images[index]

                    scaled_width = math.sqrt(
                        last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2
                    )
                    scaled_height = math.sqrt(
                        last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2
                    )

                    original_width = image.width
                    original_height = image.height

                    res_horizontal = (
                        original_width * default_resolution / scaled_width
                    )
                    res_vertical = (
                        original_height * default_resolution / scaled_height
                    )

                    info = (
                        f"{infile} image {op_do.name} "
                        f"({scaled_width:.2f}:{scaled_height:.2f}): "
                        f"res {res_horizontal:.2f} x {res_vertical:.2f}\n"
                    )
                    print(info.rstrip())
```

## PDF 内の画像から代替テキストを抽出

この関数は、PDF の最初のページのすべての画像から代替テキスト（代替テキスト）を取得します。これは、アクセシビリティと PDF/UA のコンプライアンスチェックに役立ちます。

1. 「AP.Document ()」を使用して PDF ドキュメントをロードします。
1. 「画像配置アブソーバー」を作成して、ページ上のすべての画像を収集します。
1. 最初のページでアブソーバーを受け入れます (page.accept (アブソーバー))。
1. 「absorber.image_placements」の各画像を繰り返し処理します。
    -ページのリソースコレクション (get_name_in_collection ()) 内のイメージの名前を出力します。
    -「get_alternative_text (ページ)」を使用して代替テキストを取得します。
    -代替テキストの最初の行を出力します。

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_alt_text(infile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: " + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])
```

## 関連画像トピック

- [Python を使用して PDF 内の画像を操作する](/pdf/ja/python-net/working-with-images/)
- [PDF ファイルからの画像の抽出](/pdf/ja/python-net/extract-images-from-pdf-file/)
- [既存の PDF ファイル内の画像の置換](/pdf/ja/python-net/replace-image-in-existing-pdf-file/)
- [既存の PDF ファイルへの画像の追加](/pdf/ja/python-net/add-image-to-existing-pdf-file/)
