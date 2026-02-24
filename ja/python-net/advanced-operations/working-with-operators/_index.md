---
title: Python を使用した演算子の操作
linktitle: 演算子の操作
type: docs
weight: 90
url: /ja/python-net/working-with-operators/
description: このトピックでは、Aspose.PDF for Python via .NET で演算子を使用する方法を説明します。演算子クラスは PDF 操作のための優れた機能を提供します。
lastmod: "2025-05-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Python via .NET で PDF の演算子を使用する方法
Abstract: この記事では、PDF 演算子とそれらを使用した PDF コンテンツストリームの操作について詳しく解説します。演算子は PDF 内の特定のアクションを指示するキーワードで、ページ上にグラフィカル要素を描画するなどの操作を行い、コンテンツストリーム内でのみ有効です。記事では、低レベルのグラフィック演算子を直接操作してコンテンツストリームを制御することで、PDF 内の画像配置を正確に行う方法を示します。この手法は、透かしの追加、オーバーレイの整列、カスタムレイアウトの作成など、正確な画像位置決めが必要なタスクに有益です。特に GSave、ConcatenateMatrix、Do、GRestore といった演算子が、グラフィック状態と変換を管理し、他のページコンテンツに影響を与えることなく正確な描画を実現する点が強調されています。
---

## PDF 演算子の概要と使用方法

演算子は、ページ上にグラフィカルな形状を描画するなど、実行すべきアクションを指定する PDF キーワードです。演算子キーワードは、先頭にスラッシュ文字 (2Fh) がないことで名前付きオブジェクトと区別されます。演算子はコンテンツストリーム内でのみ意味を持ちます。

コンテンツストリームは、ページ上に描画されるべきグラフィック要素を記述した命令からなるデータを保持する PDF ストリームオブジェクトです。PDF 演算子の詳細は、[PDF 仕様](https://opensource.adobe.com/dc-acrobat-sdk-docs/)をご参照ください。

### 実装の詳細

この手法は、低レベルのグラフィック演算子を使用してコンテンツストリームを直接操作することで、PDF 内の画像配置を細かく制御します。画像の正確な位置決めや変換が必要な場合に特に有用で、例えば以下のようなケースです。

- 特定の位置に透かしやロゴを追加する。

- 既存コンテンツに正確に合わせて画像をオーバーレイする。

- 上位レベルの抽象化では実現できないカスタムレイアウトを実装する。

GSave、ConcatenateMatrix、Do、GRestore などの演算子を使用することで、画像が正確に描画され、他のページコンテンツに予期せぬ影響を与えることなくグラフィック状態や変換を管理できます。

- [GSave](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/gsave/) 演算子は PDF の現在のグラフィック状態を保存します。
- [ConcatenateMatrix](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/concatenatematrix/) (concatenate matrix) 演算子は、画像を PDF ページ上のどこに配置するかを定義するために使用されます。
- [Do](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/do/) 演算子はページ上に画像を描画します。
- [GRestore](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/grestore/) 演算子はグラフィック状態を復元します。

PDF ファイルに画像を追加する手順:

1. PDF ドキュメントを開く
1. 画像配置座標を定義する
1. 対象ページにアクセスする
1. 画像をストリームに読み込む
1. 現在のグラフィック状態を保存する
1. 矩形と変換行列を作成する
1. 変換行列を適用する
1. 画像を描画する
1. 前のグラフィック状態を復元する
1. 変更された PDF ドキュメントを保存する

以下のコードスニペットは、PDF 演算子の使用方法を示しています。

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Set coordinates for the image placement
        lower_left_x = 100
        lower_left_y = 100
        upper_right_x = 200
        upper_right_y = 200

        # Get the page where the image needs to be added
        page = document.pages[1]

        # Load the image into a file stream
        with open(path_imagefile, "rb") as image_stream:
            # Add the image to the page's Resources collection
            page.resources.images.add(image_stream)

        # Save the current graphics state using the GSave operator
        page.contents.add(ap.operators.GSave())

        # Create a rectangle and matrix for positioning the image
        rectangle = ap.Rectangle(lower_left_x, lower_left_y, upper_right_x, upper_right_y)
        matrix = ap.Matrix([
            rectangle.urx - rectangle.llx, 0,
            0, rectangle.ury - rectangle.lly,
            rectangle.llx, rectangle.lly
        ])

        # Define how the image must be placed using the ConcatenateMatrix operator
        page.contents.add(ap.operators.ConcatenateMatrix(matrix))

        # Get the image from the Resources collection
        x_image = page.resources.images[page.resources.images.count]

        # Draw the image using the Do operator
        page.contents.add(ap.operators.Do(x_image.name))

        # Restore the graphics state using the GRestore operator
        page.contents.add(ap.operators.GRestore())

        # Save PDF document
        document.save(path_outfile)
```

## 演算子を使用してページに XForm を描画する

この例では、XForm とグラフィック演算子の力を活用して、PDF 内でグラフィックコンテンツを効率的に再利用しています。画像を XForm にカプセル化することで、画像データを重複させることなく複数回描画でき、ファイルサイズが小さくなりパフォーマンスが向上します。このアプローチは、特に以下の場合に有益です。

- 同じ画像またはグラフィックを文書内で複数回表示する必要がある場合。

- グラフィックの配置と変換を正確に制御する必要がある場合。

- PDF のパフォーマンスとサイズの最適化が優先される場合。

GSave と GRestore でグラフィック状態を管理し、ConcatenateMatrix で変換行列を使用することにより、この手法は各グラフィックが正しくかつ独立して描画されることを保証します。

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        page_contents = document.pages[1].contents

        # Wrap existing contents with GSave/GRestore operators to preserve graphics state
        page_contents.insert(1, ap.operators.GSave())
        page_contents.add(ap.operators.GRestore())

        # Add GSave operator to start new graphics state
        page_contents.add(ap.operators.GSave())

        # Create an XForm
        form = ap.XForm.create_new_form(document.pages[1], document)
        document.pages[1].resources.forms.add(form)

        form.contents.add(ap.operators.GSave())
        # Define image width and height
        form.contents.add(ap.operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0))

        # Load image into stream
        with open(path_imagefile, 'rb') as image_stream:
            # Add the image to the XForm's resources
            form.resources.images.add(image_stream)

        x_image = form.resources.images[form.resources.images.count]
        # Draw the image on the XForm
        form.contents.add(ap.operators.Do(x_image.name))
        form.contents.add(ap.operators.GRestore())

        # Place and draw the XForm at two different coordinates

        # Draw the XForm at (100, 500)
        page_contents.add(ap.operators.GSave())
        page_contents.add(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500))
        page_contents.add(ap.operators.Do(form.name))
        page_contents.add(ap.operators.GRestore())

        # Draw the XForm at (100, 300)
        page_contents.add(ap.operators.GSave())
        page_contents.add(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300))
        page_contents.add(ap.operators.Do(form.name))
        page_contents.add(ap.operators.GRestore())

        # Restore graphics state
        page_contents.add(ap.operators.GRestore())

        # Save PDF document
        document.save(path_outfile)
```

## 演算子クラスを使用してグラフィックオブジェクトを削除する

以下のコードスニペットはグラフィックの削除方法を示します。PDF ファイルにグラフィック用のテキストラベルが含まれている場合、このアプローチではそれらが残る可能性があることに注意してください。したがって、画像を削除する代替手段として、グラフィック演算子を検索する必要があります。

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Get the specific page (page 2 in this case)
        page = document.pages[2]

        # Get the operator collection from the page contents
        operator_collection = page.contents

        # Define the path-painting operators to be removed
        operators_to_remove = [
            ap.operators.Stroke(),
            ap.operators.ClosePathStroke(),
            ap.operators.Fill()
        ]

        # Delete the specified operators from the page contents
        operator_collection.delete(operators_to_remove)

        # Save PDF document
        document.save(path_outfile)
```


