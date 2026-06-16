---
title: Python を使用して PDF レイヤーを操作する
linktitle: PDF レイヤーの操作
type: docs
weight: 50
url: /ja/python-net/working-with-pdf-layers/
description: Python で PDF レイヤーを追加、ロック、抽出、フラット化、結合する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python による PDF レイヤーの管理
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF レイヤー (オプションコンテンツグループ) を操作する方法について説明します。レイヤーの追加、レイヤー表示のロック、レイヤーコンテンツの抽出、レイヤーコンテンツのフラット化、レイヤーを 1 つのレイヤーに結合する方法について説明します。
---

PDF レイヤーはオプションコンテンツグループ（OCG）とも呼ばれ、コンテンツを個別のビジュアルグループに整理して、互換性のある PDF ビューアで表示または非表示にすることができます。Aspose.PDF では、レイヤー操作は次の点を中心に構築されています。 [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) アピ。

.NET 経由の Python 用 Aspose.PDF を使用すると、次のことが可能になります。

- ページに複数のレイヤーを追加します。
- レイヤーをロックまたはロック解除して可視性動作を制御します。
- レイヤーを別々のファイルまたはストリームに抽出します。
- 階層化されたコンテンツをページにフラット化します。
- 複数のレイヤーを 1 つのレイヤーに結合します。

## PDF へのレイヤーの追加

この例では、3 つのレイヤーを含む PDF を作成します。この例ではを使用します。 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)、を追加します [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)、および追加 [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) そのページへのオブジェクト

1. 新規作成 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) そして追加 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. 赤いレイヤーを作成して追加します。
1. 緑のレイヤーを作成して追加します。
1. 青いレイヤーを作成して追加します。
1. PDF ドキュメントを保存します。

作成された PDF には、赤線、緑線、青線の 3 つのレイヤーが含まれます。レイヤーコンテンツをサポートする PDF リーダーでは、それぞれのオンとオフを切り替えることができます。

```python
import aspose.pdf as ap

def add_layers(outfile: str) -> None:
    document = ap.Document()
    page = document.pages.add()

    # Red layer
    layer = ap.Layer("oc1", "Red Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(1, 0, 0))
    layer.contents.append(ap.operators.MoveTo(500, 700))
    layer.contents.append(ap.operators.LineTo(400, 700))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    # Green layer
    layer = ap.Layer("oc2", "Green Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(0, 1, 0))
    layer.contents.append(ap.operators.MoveTo(500, 750))
    layer.contents.append(ap.operators.LineTo(400, 750))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    # Blue layer
    layer = ap.Layer("oc3", "Blue Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(0, 0, 1))
    layer.contents.append(ap.operators.MoveTo(500, 800))
    layer.contents.append(ap.operators.LineTo(400, 800))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    document.save(outfile)
    print(f"Layers added successfully. File saved at {outfile}")
```

## PDF レイヤーをロックする

この例では、PDF を開き、最初のページの特定のレイヤーをロックして、更新したファイルを保存します。

レイヤーをロックすると、サポートされている PDF ビューアでユーザーはそのレイヤーの表示状態を変更できなくなります。レイヤーはページからアクセスされ、ページのレイヤーコレクションを通じて管理されます。

使用可能なメソッドとプロパティ:

- [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) レイヤーをロックします。
- [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) レイヤーのロックを解除します。
- [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties) 現在のロック状態を返します。

1. PDF ドキュメントを開きます。
1. PDF の最初のページにアクセスします。
1. ページにレイヤーがあるかどうかを確認します。
1. 最初のレイヤーを取得してロックします。
1. 更新した PDF を保存します。

PDF にレイヤーが含まれている場合、最初のレイヤーはロックされ、ユーザーがその表示状態を変更できないようにします。レイヤーが見つからない場合は、代わりにメッセージが印刷されます。

```python
import aspose.pdf as ap

def lock_layer(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) > 0:
        layer = page.layers[0]
        layer.lock()
        document.save(outfile)
        print(f"Layer locked successfully. File saved at {outfile}")
    else:
        print("No layers found in the document.")
```

## PDF レイヤー要素の抽出

この例では、Aspose.PDF for Python via .NET ライブラリを使用して PDF ドキュメントの最初のページから個々のレイヤーを抽出し、以下を使用して各レイヤーを個別の PDF ファイルとして保存します。 [`Layer.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

レイヤーから新しい PDF を作成するには、次のコードスニペットを使用できます。

1. PDF を読み込む [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 1 ページ目からページ目までのレイヤーにアクセスする [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. レイヤーが存在するかどうかを確認してください。
1. レイヤーを繰り返し処理し、それぞれを保存します。

```python
import aspose.pdf as ap

def extract_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    index = 1
    for layer in layers:
        output_file = outfile.replace(".pdf", f"{index}.pdf")
        layer.save(output_file)
        print(f"Layer {index} saved to {output_file}")
        index += 1
```

PDF レイヤー要素を抽出して、新しい PDF ファイルストリームに保存することができます。

```python
from io import FileIO
import aspose.pdf as ap

def extract_layers_stream(infile: str, outfile: str) -> None:
    document = ap.Document(infile)

    if len(document.pages[1].layers) == 0:
        print("No layers found in the document.")
        return

    layer = document.pages[1].layers[0]

    with FileIO(outfile, "wb") as output_layer:
        layer.save(output_layer)
    print(f"Layer extracted to stream: {outfile}")
```

## レイヤード PDF をフラット化

このスクリプトは、.NET 経由の Python Aspose.PDF を使用して PDF ドキュメントの最初のページのすべてのレイヤーをフラット化します。フラット化を行うと、各レイヤーのビジュアルコンテンツが 1 つの統合レイヤーに結合され、視覚的な忠実度やレイヤー固有のデータを失うことなく、印刷、共有、アーカイブが容易になります。この操作は次の方法で実行されます。 [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

1. PDF ドキュメントをロードします。
1. 1 ページ目のレイヤーにアクセスします。
1. レイヤーが存在するかどうかを確認してください。
1. 各レイヤーを平坦化します `layer.flatten(True)`.
1. 変更した文書を保存します。

```python
import aspose.pdf as ap

def flatten_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    for layer in layers:
        layer.flatten(True)

    document.save(outfile)
    print(f"Layers flattened successfully. File saved at {outfile}")
```

## PDF 内のすべてのレイヤーを 1 つに結合

このコードスニペットでは、Aspose.PDF を使用して PDF の最初のページのすべてのレイヤーをカスタム名のある 1 つの統合レイヤーに結合します。 [`Page.merge_layers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods).

1. PDF ドキュメントをロードします。
1. ページ 1 にアクセスし、そのレイヤーを取得します。
1. レイヤーが存在するかどうかを確認してください。
1. 新しいレイヤー名を定義します。
1. レイヤーを 1 つに結合します。
1. 文書を保存します。

```python
import aspose.pdf as ap

def merge_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) == 0:
        print("No layers found in the document.")
        return

    new_layer_name = "LayerNew"
    page.merge_layers(new_layer_name)
    document.save(outfile)
    print(f"Layers merged successfully. File saved at {outfile}")
```

## 関連するレイヤートピックス

- [Python で PDF ページを操作する](/pdf/ja/python-net/working-with-pages/)
- [Python を使用して PDF 内のテーブルを操作する](/pdf/ja/python-net/working-with-tables/)
- [Python で PDF ページを追加する](/pdf/ja/python-net/add-pages/)
