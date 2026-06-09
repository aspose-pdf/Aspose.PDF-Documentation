---
title: Python で PDF オペレータを操作する
linktitle: オペレーターとの連携
type: docs
weight: 90
url: /ja/python-net/working-with-operators/
description: Python で低レベル PDF 演算子を使用して、コンテンツストリームの正確な操作とグラフィック制御を行う方法を学びます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python のコンテンツストリーム制御に低レベルの PDF 演算子を使用する
Abstract: この記事では、.NET 経由で Aspose.PDF for Python で低レベル PDF オペレータを操作する方法について説明します。Python ワークフローで、コンテンツストリームを直接操作する方法、演算子クラスを使用してグラフィックを正確に配置する方法、PDF ページから描画されたオブジェクトを削除する方法を学びます。
---

## PDF 演算子とその使用法の紹介

演算子は、ページ上にグラフィカルな図形を描くなど、実行するアクションを指定するPDFキーワードです。演算子キーワードは、最初の固相文字 (2Fh) がないことで名前付きオブジェクトと区別されます。演算子はコンテンツストリーム内でのみ意味があります。

コンテンツストリームは PDF ストリームオブジェクトで、そのデータはページ上に描画されるグラフィック要素を説明する命令で構成されています。PDF 演算子の詳細については、を参照してください。 [PDF スペシフィケーション](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

このページは、Python で PDF コンテンツストリームを直接制御する必要がある場合に使用します。たとえば、グラフィックを正確な座標に配置したり、グラフィックの状態の変更をラップしたり、特定の描画演算子をページから削除したりする場合などです。

## オペレータクラスによる画像の追加

高レベルのレイアウト抽象化に頼らずに、画像コンテンツを PDF ページストリームに非常に正確に配置する必要がある場合は、低レベルの演算子クラスを使用してください。

この方法では、低レベルのグラフィック演算子を使用してコンテンツストリームを直接操作することで、PDF 内の画像の配置をきめ細かく制御できます。これは特に、次のような画像の正確な配置と変換が必要な場合に便利です。

- 特定の場所にウォーターマークやロゴを追加します。
- 既存のコンテンツに画像を正確に配置してオーバーレイします。
- 高レベルの抽象化では実現できないカスタムレイアウトを実装します。

GSave、ConcatenateMatrix、Do、GREStoreなどの演算子を使用することで、開発者は画像が正確にレンダリングされ、他のページコンテンツに意図しない副作用が生じないようにすることができます。

- ザの [GSave](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/gsave/) オペレータは PDF の現在のグラフィック状態を保存します。
- ザの [連結マトリックス](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/concatenatematrix/) （連結行列）演算子は、PDFページへの画像の配置方法を定義するために使用されます。
- ザの [行う](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/do/) オペレータはページに画像を描画します。
- ザの [GREStore](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/grestore/) オペレータはグラフィカルな状態を復元します。

PDF ファイルに画像を追加するには:

1. PDF ドキュメントを開く
1. 画像配置座標の定義
1. ターゲットページにアクセスする
1. ストリームに画像を読み込む
1. 現在のグラフィックステートの保存
1. 長方形と変換マトリックスの作成
1. 変換マトリックスの適用
1. 画像を描く
1. 以前のグラフィック状態を復元
1. 変更した PDF ドキュメントを保存する

次のコードスニペットは、PDF 演算子の使用方法を示しています。

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_using_pdf_operators(infile, imagefile, outfile):
    with ap.Document(infile) as document:
        lower_left_x = 100
        lower_left_y = 100
        upper_right_x = 200
        upper_right_y = 200

        page = document.pages[1]

        with open(imagefile, "rb") as image_stream:
            page.resources.images.add(image_stream)

        page.contents.append(ap.operators.GSave())

        rectangle = ap.Rectangle(
            lower_left_x, lower_left_y, upper_right_x, upper_right_y, True
        )
        matrix = ap.Matrix(
            [
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            ]
        )

        page.contents.append(ap.operators.ConcatenateMatrix(matrix))

        x_image = page.resources.images[len(page.resources.images)]

        page.contents.append(ap.operators.Do(x_image.name))

        page.contents.append(ap.operators.GRestore())

        document.save(outfile)
```

## オペレータを使用してページに XForm を描画する

この例では、XForms とグラフィックオペレータの機能を活用して、PDF 内のグラフィックコンテンツを効率的に再利用しました。画像を XForm にカプセル化することで、画像データを複製せずに複数回描画できるため、ファイルサイズが小さくなり、パフォーマンスが向上します。このアプローチは、以下の場合に特に役立ちます。

- 同じ画像またはグラフィックを 1 つの文書に複数回表示する必要があります。

- グラフィックの配置と変形を正確に制御する必要があります。

- PDF のパフォーマンスとサイズを最適化することが優先事項です。

GSave と GREStoreでグラフィックの状態を管理し、ConcatenateMatrixで変換行列を使用することにより、この手法では各グラフィックが正しく独立してレンダリングされます。

```python
import sys
import aspose.pdf as ap
from os import path

def draw_xform_on_page(infile, imagefile, outfile):
    with ap.Document(infile) as document:
        page_contents = document.pages[1].contents

        page_contents.insert(1, ap.operators.GSave())
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GSave())

        form = ap.XForm.create_new_form(document.pages[1], document)
        document.pages[1].resources.forms.append(form)

        form.contents.append(ap.operators.GSave())
        form.contents.append(ap.operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0))

        with open(imagefile, "rb") as image_stream:
            form.resources.images.add(image_stream)

        x_image = form.resources.images[len(form.resources.images)]
        form.contents.append(ap.operators.Do(x_image.name))
        form.contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 500)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 300)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GRestore())

        document.save(outfile)
```

## 演算子クラスを使用してグラフィックスオブジェクトを削除する

次のコードスニペットは、グラフィックを削除する方法を示しています。PDF ファイルにグラフィックのテキストラベルが含まれている場合、この方法では PDF ファイル内に残る可能性があることに注意してください。そのため、このような画像を削除する別の方法をグラフィックオペレータで探してください。

```python
import sys
import aspose.pdf as ap
from os import path

def remove_graphics_objects(infile, outfile):
    with ap.Document(infile) as document:
        page = document.pages[1]
        # Collect operators to remove in single pass
        # Operator codes: S=Stroke, h=ClosePathStroke, f=Fill'
        graphics_operators = {"S", "h", "f"}
        operators_to_remove = [
            op for op in page.contents if str(op) in graphics_operators
        ]

        page.contents.delete(operators_to_remove)
        document.save(outfile)
```

## 関連トピック

- [Python での高度な PDF 操作](/pdf/ja/python-net/advanced-operations/)
- [Python で PDF ページを操作する](/pdf/ja/python-net/working-with-pages/)
- [Python を使用して PDF 内の画像を操作する](/pdf/ja/python-net/working-with-images/)
- [Python で PDF グラフを操作する](/pdf/ja/python-net/working-with-graphs/)
