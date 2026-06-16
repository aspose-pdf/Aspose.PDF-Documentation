---
title: Python でベクターグラフィックスを操作する
linktitle: ベクターグラフィックの操作
type: docs
weight: 100
url: /ja/python-net/working-with-vector-graphics/
description: Python の GraphicsAbsorber を使用して PDF ページ間でベクターグラフィックを抽出、移動、削除、およびコピーする方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: グラフィックスアブソーバーを使用して Python で PDF ベクターグラフィックを検査および操作する
Abstract: この記事では、GraphicsAbsorber クラスを使用して、.NET 経由で Aspose.PDF for Python のベクターグラフィックを操作する方法について説明します。Python ワークフローで、PDF ページからベクター要素を抽出し、それらを移動または削除し、ページ間でグラフィックをコピーする方法を低レベルで制御する方法を学びましょう。
---

[Aspose.PDF for Python (.NET 経由)](/pdf/ja/python-net/) 提供する [グラフィックアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) PDF ページにすでに存在するベクターグラフィックにアクセスして操作するためのクラスです。itsと呼んでください。 `visit` 任意のページのメソッドを使用して、パス、図形、その他のグラフィカル演算子を抽出し、必要に応じてそれらの要素を移動、削除、またはコピーできます。

このページは、新しい図形を一から描くのではなく、既存のPDFに埋め込まれているベクター描画要素を調べたり変更したりする必要がある場合に使用します。

## グラフィックの抽出

抽出はすべてのベクターグラフィックスタスクの出発点です。 `GraphicsAbsorber` ページのコンテンツストリームを読み取り、ページ参照、位置、未処理演算子を使用して各グラフィック要素を公開します。

1. PDF ドキュメントを開きます。
1. を作成 [グラフィックアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) インスタンス。
1. コール `visit` ターゲットページに入力する `elements`.
1. 反復処理 `elements` 位置とオペレーター数を検査します。

```python
import aspose.pdf as ap
import sys
from os import path

def using_graphics_absorber(infile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")
```

`GraphicsAbsorber` の一部です `aspose.pdf.vector` 名前空間であり、PDF コンテンツストリームのベクターグラフィックと相互作用するように特別に設計されています。

## グラフィックの移動

抽出後、新しい設定を行います `position` 各要素で同じページに再配置します。更新内容をまとめてください `suppress_update` / `resume_update` バッチコンテンツストリーム書き込みの呼び出しを 1 回の操作にまとめ、重複した再描画を回避します。

1. PDF ドキュメントを開きます。
1. を作成 `GraphicsAbsorber` そして電話 `visit` ターゲットページに。
1. コール `suppress_update` コンテンツストリームの書き込みを一時停止します。
1. を更新 `position` 各要素の。
1. コール `resume_update` すべての変更を一度にコミットできます。
1. 変更した文書を保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def move_graphics(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                position = element.position
                element.position = ap.Point(position.x + 150, position.y - 10)
            graphics_absorber.resume_update()
        document.save(outfile)
```

## グラフィックを削除する

ページから特定のベクター要素を削除するには、位置または境界矩形でフィルタリングしてから削除します。Aspose.PDF for Python には、要素をインラインで削除するか、先に収集するかに応じて 2 つの方法があります。

### 方法 1: 長方形の境界を使用してインラインを削除する

このアプローチでは、各要素の位置を長方形と照合し、以下を呼び出します。 `element.remove()` ループのすぐ内側にあります。簡潔なコードが必要で、削除したセットを後で調べる必要がない場合に使用します。

1. PDF ドキュメントを開きます。
1. を作成 `GraphicsAbsorber` そして電話 `visit` ターゲットページに。
1. ターゲットを定義 [四角形](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
1. コール `suppress_update` コンテンツストリームの書き込みを一時停止します。
1. 繰り返し `elements`、呼び出し `remove()` 位置が長方形の内側にある各要素について。
1. コール `resume_update` 削除をコミットします。
1. 変更した文書を保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    element.remove()
            graphics_absorber.resume_update()
        document.save(outfile)
```

### 方法 2: 最初に要素を集めてから削除する

この方法では、一致する要素が a に集められます。 [グラフィック要素コレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicelementcollection/) コレクションをに渡します `page.delete_graphics`。削除を実行する前に、削除する内容を確認したり記録したりする必要がある場合に使用します。

1. PDF ドキュメントを開きます。
1. を作成 `GraphicsAbsorber` そして電話 `visit` ターゲットページに。
1. ターゲットの長方形を定義します。
1. 繰り返し `elements` そして、一致する要素を a に追加します `GraphicElementCollection`.
1. コール `page.contents.suppress_update` コンテンツストリームの書き込みを一時停止します。
1. コール `page.delete_graphics` コレクションと一緒に。
1. コール `page.contents.resume_update` 削除をコミットします。
1. 変更した文書を保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.visit(page)
            removed_elements_collection = ap.vector.GraphicElementCollection()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    removed_elements_collection.add(element)
            page.contents.suppress_update()
            page.delete_graphics(removed_elements_collection)
            page.contents.resume_update()
        document.save(outfile)
```

## 別のページへのグラフィックの追加

あるページから抽出されたベクター要素は、同じドキュメントの他のページに配置できます。要素を 1 つずつ追加する方法と、コレクション全体を 1 回の呼び出しで渡す方法の 2 つがあります。

### 方法 1: 要素を個別に追加する

このメソッドは、目的のページに配置する前に個々の要素をフィルタリングしたり変換したりするなど、要素ごとに制御する必要がある場合に使用します。

1. PDF ドキュメントを開きます。
1. を作成 `GraphicsAbsorber` そして電話 `visit` ソースページにあります。
1. ドキュメントに新しい宛先ページを追加します。
1. コール `page_2.contents.suppress_update` コンテンツストリームの書き込みを一時停止します。
1. コール `element.add_on_page(page_2)` 各要素について。
1. コール `page_2.contents.resume_update` すべての追加をコミットします。
1. 変更した文書を保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            for element in graphics_absorber.elements:
                element.add_on_page(page_2)
            page_2.contents.resume_update()
        document.save(outfile)
```

### 方法 2: コレクション全体を一度に追加する

この方法は、手動で繰り返すことなく、抽出されたすべての要素を 1 回の操作でページにコピーする場合に使用します。

1. PDF ドキュメントを開きます。
1. を作成 `GraphicsAbsorber` そして電話 `visit` ソースページにあります。
1. ドキュメントに新しい宛先ページを追加します。
1. コール `page_2.contents.suppress_update` コンテンツストリームの書き込みを一時停止します。
1. コール `page_2.add_graphics` フルで `elements` コレクション。
1. コール `page_2.contents.resume_update` すべての追加をコミットします。
1. 変更した文書を保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            page_2.add_graphics(graphics_absorber.elements, None)
            page_2.contents.resume_update()
        document.save(outfile)
```

## 関連トピック

- [Python での高度な PDF 操作](/pdf/ja/python-net/advanced-operations/)
- [Python で PDF グラフを操作する](/pdf/ja/python-net/working-with-graphs/)
- [Python で PDF オペレータを操作する](/pdf/ja/python-net/working-with-operators/)
- [Python で PDF ページを操作する](/pdf/ja/python-net/working-with-pages/)
