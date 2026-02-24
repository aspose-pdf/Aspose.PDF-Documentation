---
title: Python を使用した PDF への画像追加
linktitle: 画像を追加
type: docs
weight: 10
url: /ja/python-net/add-image-to-existing-pdf-file/
description: このセクションでは、Python ライブラリを使用して既存の PDF ファイルに画像を追加する方法を説明します。
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: Python を使用して PDF に画像を追加する方法
Abstract: この記事では、Aspose.PDF ライブラリを使用した Python による既存の PDF ファイルへの画像追加方法を解説します。これを実現するための2つの方法が示されています。最初の方法は Aspose.PDF の `Document` クラスを使用し、PDF を読み込みページ番号を指定し、`Page` クラスの `add_image` メソッドで画像の位置を設定します。その後、`save()` メソッドで文書を保存します。2つ目の方法は Aspose.PDF.Facades 名前空間の `PdfFileMend` クラスを利用し、よりシンプルなインターフェースを提供します。この場合、`add_image()` メソッドを呼び出して指定ページと座標に画像を追加し、更新された PDF を保存し、`PdfFileMend` オブジェクトを閉じます。両方の方法のコードスニペットがプロセスの実例として提供されています。
---

## 既存の PDF ファイルに画像を追加

この例では、.NET 経由で Python 用 Aspose.PDF を使用して PDF ページの特定位置に画像を挿入する方法を示します。

1. 'ap.Document' で PDF ドキュメントをロードします。
1. 対象ページ '(document.pages[1]' を選択します（最初のページ）。
1. 'page.add_image()' を使用して画像を配置します：
- 画像のファイルパス。
- 画像の座標を定義する 'Rectangle' オブジェクト（left=20, bottom=730, right=120, top=830）。
1. 更新された PDF を保存します。

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    page = document.pages[1]
    page.add_image(
        path.join(self.data_dir, image_file),
        ap.Rectangle(20, 730, 120, 830, True),
    )
    document.save(path_outfile)
```

## 演算子を使用して画像を追加

次のコードスニペットは、上位レベルのヘルパーメソッドではなく、PDF 演算子を手動で操作する低レベルのアプローチで PDF ページに画像を追加する方法を示しています。

手順：

1. 新しい空白の 'Document' を作成します。
1. ページを追加し、サイズを設定します（842 × 595 - 横向き A4）。
1. ページの画像リソース (page.resources.images) にアクセスします。
1. 画像ファイルをストリームに読み込み、リソースに追加します。
- メソッドは 'image_id' を返します。
- 新しく追加された画像オブジェクトがリソースから取得されます。
1. 画像のアスペクト比を維持する矩形を定義します：
1. 演算子シーケンスを構築します：
- 'GSave()' - 現在のグラフィックス状態を保存します。
- 'ConcatenateMatrix(matrix)' - 変換を適用します（スケールとページ上で画像を垂直にセンタリング）。
- 'Do(image_id)' - 画像を描画します。
- 'GRestore()' - グラフィックス状態を復元します。
1. 演算子シーケンスを 'page.contents' に追加します。
1. 結果の PDF を保存します。

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842,595)

    # Get page resources
    resources_images = page.resources.images

    # Add image to resources
    image_stream = FileIO(path.join(self.data_dir, path_infile), "rb")
    image_id = resources_images.add(image_stream)

    x_image = list(resources_images)[-1]

    rectangle = ap.Rectangle(
        0,
        0,
        page.media_box.width,
        (page.media_box.width * x_image.height) / x_image.width,
        True,
    )

    # Create operator sequence for adding image
    operators = []

    # Save graphics state
    operators.append(ap.operators.GSave())

    # Set transformation matrix (position and size)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.llx + (page.media_box.height - rectangle.height) / 2,
    )
    operators.append(ap.operators.ConcatenateMatrix(matrix))

    # Draw the image
    operators.append(ap.operators.Do(image_id))

    # Restore graphics state
    operators.append(ap.operators.GRestore())

    # Add operators to page contents
    page.contents.add(operators)

    document.save(path_outfile)
```

## 代替テキスト付きで画像を追加

この例では、PDF ページに画像を追加し、アクセシビリティ準拠（PDF/UA など）のために代替テキスト（alt text）を割り当てる方法を示します。

1. 新しい 'Document' を作成し、ページを追加します（842 × 595、横向き A4）。
1. 'page.add_image()' を使用し、ページ全体に広がる矩形で画像を配置します。
1. ページの画像リソース ('page.resources.images') にアクセスします。
1. 代替テキスト文字列を定義します（例：'Alternative text for image'）。
1. リソースから最初の画像オブジェクトを取得します（'x_image = resources_images[1]'）。
1. 'try_set_alternative_text(alt_text, page)' を使用して画像に代替テキストを割り当てます。
1. 結果の PDF を保存します。

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842,595)

    page.add_image(
        path_image_file,
        ap.Rectangle(0, 0, 842, 595, True),
    )

    resources_images = page.resources.images
    alt_text = "Alternative text for image"
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text(alt_text, page)

    # If set is successful, then get the alternative text for the image
    if (result):
        print ("Text has been added successfuly")
    document.save(path_outfile)
```
