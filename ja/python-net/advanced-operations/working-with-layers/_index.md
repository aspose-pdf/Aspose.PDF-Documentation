---
title: Python を使用した PDF レイヤーの操作
linktitle: PDF レイヤーの操作
type: docs
weight: 50
url: /ja/python-net/work-with-pdf-layers/
description: この記事では、PDF レイヤーをロックする方法、PDF レイヤーの要素を抽出する方法、レイヤー化された PDF をフラット化する方法、そして PDF 内のすべてのレイヤーを 1 つにマージする方法を説明します。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF レイヤーを管理、ロック、抽出、フラット化、マージする方法
Abstract: この記事では、Aspose.PDF for .NET を使用して Python で PDF レイヤーを操作する方法を説明します。レイヤーのロック、レイヤー要素の抽出、レイヤー化された PDF のフラット化、レイヤーのマージが含まれます。
---

PDF レイヤーを使用すると、文書に複数のコンテンツセットを含め、必要に応じて選択的に表示または非表示にできます。各レイヤーはテキスト、画像、またはグラフィックを含むことができ、ユーザーは必要に応じてオン/オフを切り替えることができます。レイヤーは、コンテンツを整理または分離する必要がある複雑な文書で特に便利です。以下の例では、[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) と [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API を使用し、ページの `layers` コレクションを介して [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) オブジェクトを操作します。

## PDF レイヤーをロックする

Aspose.PDF for Python via .NET を使用すると、PDF を開き（[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を参照）、最初の [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) の特定の [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) をロックし、変更を加えたドキュメントを保存できます。

[`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) オブジェクトで使用できるメソッドとプロパティ:

- `layer.lock()` – レイヤーをロックします。 (see [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods))
- `layer.unlock()` – レイヤーのロックを解除します。 (see [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods))
- `layer.locked` – 現在のロック状態を返します。 (see [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties))

1. PDF ドキュメントを開きます（[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を参照）。
1. ドキュメントの [`Pages`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) コレクションを使用して最初のページを取得します（[`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) を参照）。
1. `page.layers` からロックする [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) を選択します。
1. `layer.lock()` を呼び出して、ユーザーがレイヤーの表示を切り替えられないようにします。
1. [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) を使用して更新されたドキュメントを保存します。

```python

import aspose.pdf as ap

def lock_layer(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]
        layer = page.layers[0]

        # Lock the layer
        layer.lock()

        # Save updated PDF
        document.save(path_outfile)
```

## PDF レイヤー要素の抽出

Aspose.PDF を使用すると、各 [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) を [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) から抽出し、別々の PDF ファイルとして保存できます。

レイヤーから新しい PDF を作成するには、次のコードスニペットを使用できます（`layers` コレクションは `Page.layers` から取得します）。

```python

import aspose.pdf as ap

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF with a unique filename
        for i, layer in enumerate(layers):
            layer.save(f"{path_outfile}_layer_{i}.pdf")
```

レイヤーをストリームに保存することもできます：

```python

import aspose.pdf as ap
import io

def save_layers_to_stream(path_infile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        streams = []
        for layer in layers:
            layer_stream = io.BytesIO()
            layer.save(layer_stream)
            layer_stream.seek(0)
            streams.append(layer_stream)
        return streams
```

## レイヤー化された PDF のフラット化

フラット化により、ページ上の [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) が永続的になり、切り替え機能が削除されます。

```python

import aspose.pdf as ap

def flatten_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        # Flatten each layer
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

`cleanup_content_stream` パラメータは、オプションコンテンツグループマーカー（OCG マーカー）を削除するかどうかを制御します。これを `False` に設定するとフラット化が高速化されます。詳細は [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) メソッドをご覧ください。

## PDF 内のすべてのレイヤーを1つにマージする

すべてのレイヤー（または特定のレイヤー）を単一の新しい [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) にマージできます（マージ API は [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) オブジェクトにあります）。

`[`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)` オブジェクトのメソッド:

- `page.merge_layers(new_layer_name)` — すべてのレイヤーを新しいレイヤー名にマージします（[`Page.MergeLayers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) を参照）。
- `page.merge_layers(new_layer_name, new_optional_content_group_id)` — カスタムオプションコンテンツグループ ID を使用してマージします（[`Page.MergeLayers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) を参照）。

```python

import aspose.pdf as ap

def merge_layers(path_infile, path_outfile, new_layer_name, optional_group_id=None):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```
