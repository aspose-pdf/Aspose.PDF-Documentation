---
title: Python を使用して PDF ファイルから画像を抽出
linktitle: 画像を抽出
type: docs
weight: 30
url: /ja/python-net/extract-images-from-pdf-file/
description: このセクションでは、Python ライブラリを使用して PDF ファイルから画像を抽出する方法を示します。
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: Python を使って PDF から画像を抽出
Abstract: この記事では、Aspose.PDF for Python を使用して PDF ファイルから画像を抽出するプロセスについて説明します。管理、アーカイブ、分析、共有などの目的で画像を分離する有用性を強調しています。記事では、PDF 内の画像は各ページのリソースコレクション、特に XImage コレクションに格納されていることを説明しています。画像を抽出するには、特定のページにアクセスし、Images コレクションからインデックスを使用して画像を取得します。インデックスで返される XImage オブジェクトは、抽出した画像を保存するための `save()` メソッドを提供します。コードスニペットが示されており、PDF ドキュメントを開き、2 ページ目からインデックスで特定の画像を抽出し、ファイルに保存する手順をデモンストレーションしています。
---

PDF ファイルから画像を分離する必要がありますか？ ドキュメントの画像をより簡単に管理、アーカイブ、分析、共有するために、**Aspose.PDF for Python** を使用して PDF ファイルから画像を抽出しましょう。

1. 'ap.Document()' で PDF ドキュメントをロードします。
1. 文書の目的のページにアクセスします (document.pages[1])。
1. ページのリソースから画像を選択します（例: resources.images[1]）。
1. 対象ファイル用に出力ストリーム（FileIO）を作成します。
1. 'xImage.save(output_image)' を使用して抽出した画像を保存します。

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    document = ap.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```

## PDF の特定領域から画像を抽出

この例では、PDF ページ上の指定された矩形領域内にある画像を抽出し、個別のファイルとして保存します。

1. 'ap.Document' を使用して PDF ドキュメントをロードします。
1. 最初のページのすべての画像を収集するために 'ImagePlacementAbsorber' を作成します。
1. 画像配置を解析するために 'document.pages[1].accept(absorber)' を呼び出します。
1. 'absorber.image_placements' のすべての画像を反復処理します：
- 画像のバウンディングボックス (llx, lly, urx, ury) を取得します。
- 画像矩形の両角が対象矩形の内部にあるかどうか (rectangle.contains()) を確認します。
- もし条件が真であれば、FileIO を使用して画像をファイルに保存し、ファイル名の 'index' を連番に置き換えます。
1. 保存した各画像に対してインデックスを増やします。

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    rectangle = ap.Rectangle(0, 0, 590, 590, True)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)
    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(
            image_placement.rectangle.llx, image_placement.rectangle.lly
        )
        point2 = ap.Point(
            image_placement.rectangle.urx, image_placement.rectangle.urx
        )
        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(path_outfile.replace("index", str(index)), "w") as output_image:
                image_placement.image.save(output_image)
            index = index + 1
```

## PDF から画像情報を抽出

以下の例は、PDF ページに埋め込まれた画像を分析し、実効解像度を計算する方法を示しています。

1. 'ap.Document' で PDF を開きます。
1. ページ内容を読み取る際にグラフィックス状態を追跡します。
1. 演算子を処理します：
- 'GSave'/'GRestore' - 行列をプッシュ/ポップします。
- 'ConcatenateMatrix' - 変換を更新します。
- 'Do' - 画像の場合、サイズを取得し変換を適用します。
1. 実効 DPI を計算します。
1. 画像名、スケールされたサイズ、DPI を出力します。

```python

    import aspose.pdf as ap
    from io import FileIO
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
