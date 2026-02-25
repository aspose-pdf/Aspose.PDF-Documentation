---
title: PDFで画像を取得および検索
linktitle: 画像の取得と検索
type: docs
weight: 40
url: /ja/python-net/search-and-get-images-from-pdf-document/
description: Aspose.PDFを使用して、PythonでPDFドキュメントから画像を検索および取得する方法を学びます。
lastmod: "2025-09-17"
TechArticle: true
AlternativeHeadline: PDFから画像を検索および抽出する
Abstract: Aspose.PDF for Python via .NET ライブラリは、PDFドキュメントから画像を検索および抽出するための強力な機能を提供します。'ImagePlacementAbsorber' クラスを利用することで、開発者はPDFのすべてのページに埋め込まれた画像を効率的に検出し、アクセスできます。
---

## PDFページの画像配置プロパティの検査

この例では、Aspose.PDF for Python via .NET を使用して、特定のPDFページ上のすべての画像のプロパティを分析し表示する方法を示します。

1. ページ上のすべての画像を収集するために 'ImagePlacementAbsorber' を作成します。
1. 最初のページの画像配置を分析するために 'document.pages[1].accept(absorber)' を呼び出します。
1. 'absorber.image_placements' を反復処理し、各画像の主要なプロパティを表示します。
- 幅と高さ（ポイント）。
- 左下X（LLX）および左下Y（LLY）座標。
- 水平（X）および垂直（Y）解像度（DPI）。

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        # Display image placement properties for all placements
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))
```

## PDF内の画像タイプを抽出およびカウント

この関数はPDFの最初のページのすべての画像を分析し、グレースケール画像とRGB画像の数をカウントします。

1. ページ上のすべての画像を収集するために 'ImagePlacementAbsorber' を作成します。
1. グレースケール画像とRGB画像のカウンタを初期化します。
1. 画像配置を分析するために 'document.pages[1].accept(absorber)' を呼び出します。
1. 見つかった画像の総数を出力します。
1. 'absorber.image_placements' 内の各画像を反復処理します：
- 'image_placement.image.get_color_type()' を使用して画像の色タイプを取得します。
- 対応するカウンタ（グレースケールまたはRGB）をインクリメントします。
- 画像がグレースケールかRGBかを示すメッセージを各画像について出力します。

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
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
```

## PDFから詳細な画像情報を抽出

この関数はPDFの最初のページのすべての画像を分析し、ページのグラフィック変換に基づいてスケールされた寸法と実効解像度を計算します。

1. PDFをロードし変数を初期化します
1. 画像リソースを収集します
1. ページコンテンツ演算子を処理します：
- 'GSave' - 現在のCTMをスタックにプッシュします。
- 'GRestore' - スタックから最後のCTMをポップします。
- 'ConcatenateMatrix' - 演算子の行列と乗算して現在のCTMを更新します。
1. 画像名、スケールされた寸法、および計算された解像度を出力します。

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)

    default_resolution = 72
    graphics_state = []

    image_names = list(document.pages[1].resources.images.names)

    graphics_state.append(drawing.drawing2d.Matrix(float(1), float(0), float(0), float(1), float(0), float(0)))

    for op in document.pages[1].contents:
        if is_assignable(op, ap.operators.GSave):
            graphics_state.append(cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone())

        elif is_assignable(op, ap.operators.GRestore):
            graphics_state.pop()

        elif is_assignable(op, ap.operators.ConcatenateMatrix):
            opCM = cast(ap.operators.ConcatenateMatrix, op)
            cm = drawing.drawing2d.Matrix(
                float(opCM.matrix.a),
                float(opCM.matrix.b),
                float(opCM.matrix.c),
                float(opCM.matrix.d),
                float(opCM.matrix.e),
                float(opCM.matrix.f),
            )

            graphics_state[-1].multiply(cm)
            continue

        elif is_assignable(op, ap.operators.Do):
            opDo = cast(ap.operators.Do, op)
            if opDo.name in image_names:
                last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                index = image_names.index(opDo.name) + 1
                image = document.pages[1].resources.images[index]

                scaled_width = math.sqrt(last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2)
                scaled_height = math.sqrt(last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2)

                original_width = image.width
                original_height = image.height

                res_horizontal = original_width * default_resolution / scaled_width
                res_vertical = original_height * default_resolution / scaled_height

                print(
                    f"{self.data_dir}image {opDo.name} "
                    f"({scaled_width:.2f}:{scaled_height:.2f}): "
                    f"res {res_horizontal:.2f} x {res_vertical:.2f}"
                )
```

## PDF内の画像から代替テキストを抽出

この関数はPDFの最初のページにあるすべての画像から代替テキスト（altテキスト）を取得し、アクセシビリティやPDF/UA準拠チェックに役立ちます。

1. 'ap.Document()' を使用して PDF ドキュメントをロードします。
1. ページ上のすべての画像を収集するために 'ImagePlacementAbsorber' を作成します。
1. 最初のページで吸収器を受け入れます（page.accept(absorber)）。
1. 'absorber.image_placements' 内の各画像を反復処理します：
- ページのリソースコレクション内の画像名を出力します（get_name_in_collection()）。
- 'get_alternative_text(page)' を使用して代替テキストを取得します。
- 代替テキストの最初の行を出力します。

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: "
            + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])
```
