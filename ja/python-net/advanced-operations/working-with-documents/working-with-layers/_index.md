---
title: Python を使用した PDF レイヤーの操作
linktitle: PDF レイヤーの操作
type: docs
weight: 50
url: /ja/python-net/working-with-pdf-layers/
description: 次のタスクでは、PDF レイヤーのロック、PDF レイヤー要素の抽出、レイヤー化された PDF のフラット化、そして PDF 内のすべてのレイヤーを1つに統合する方法を説明します。
lastmod: "2025-11-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF レイヤーを操作する
Abstract: 本ガイドでは、Aspose.PDF for Python via .NET ライブラリを使用して PDF レイヤーを管理および操作する方法について包括的に解説します。PDF レイヤーはオプショナルコンテンツグループ（OCG）とも呼ばれ、コンテンツを個別のビジュアル要素に分割し、オン・オフを切り替えることができます。
---

PDF レイヤーは、単一の PDF ファイル内でコンテンツを柔軟に整理・表示する強力な手段であり、ユーザーは必要に応じて異なる部分を表示または非表示にできます。

**Aspose.PDF for Python via .NET** を使用すると、次のことができます:

- レイヤーをロック/アンロックして表示を制御する。
- レイヤーを別々のファイルまたはストリームに抽出する。
- レイヤーをフラット化して永続化する。
- レイヤーを単一の統合レイヤーに結合する。

## PDF にレイヤーを追加する

この例では、Aspose.PDF for Python via .NET を使用して PDF ドキュメントに複数のレイヤーを作成および追加する方法を示します。各レイヤーはカラーラインなどの個別のグラフィックコンテンツを含み、レイヤー対応の PDF ビューアでオン・オフを切り替えることができます。

1. 新しい PDF ドキュメントを作成し、ページを追加する。
1. 赤色レイヤーを作成して追加する。
1. 緑色レイヤーを作成して追加する。
1. 青色レイヤーを作成して追加する。
1. PDF ドキュメントを保存する。

生成された PDF は、赤線、緑線、青線という 3 つの個別のレイヤーを含みます。各レイヤーは、レイヤー対応の PDF リーダーでオンまたはオフを切り替えることができます。

```python

import aspose.pdf as ap
from os import path

def add_colored_layers(outfile: str, data_dir: str) -> None:
    """
    Creates a PDF with three layers (Red, Green, Blue lines).
    
    Args:
        outfile (str): Name of the output PDF file.
        data_dir (str): Directory path to save the file.
    """
    path_outfile = path.join(data_dir, outfile)

    try:
        # Create a new PDF document and add a blank page
        document = ap.Document()
        page = document.pages.add()

        # Helper function to add a colored line layer
        def add_layer(layer_id: str, layer_name: str, color: tuple, y_position: int):
            layer = ap.Layer(layer_id, layer_name)
            layer.contents.append(ap.operators.SetRGBColorStroke(*color))
            layer.contents.append(ap.operators.MoveTo(500, y_position))
            layer.contents.append(ap.operators.LineTo(400, y_position))
            layer.contents.append(ap.operators.Stroke())
            page.layers.append(layer)

        # Add Red, Green, and Blue layers
        add_layer("oc1", "Red Line", (1, 0, 0), 700)
        add_layer("oc2", "Green Line", (0, 1, 0), 750)
        add_layer("oc3", "Blue Line", (0, 0, 1), 800)

        # Save the document
        document.save(path_outfile)
        print(f"\nLayers added successfully.\nFile saved at: {path_outfile}")

    except Exception as e:
        print(f"Error adding layers: {e}")
```

## PDF レイヤーをロックする

Aspose.PDF for Python via .NET を使用すると、PDF を開き、1 ページ目の特定のレイヤーをロックし、変更を加えたドキュメントを保存できます。

この例では、Aspose.PDF for Python via .NET を使用して PDF ドキュメント内のレイヤー（オプショナルコンテンツグループ、OCG）をロックする方法を示します。ロックにより、PDF ビューアでユーザーがレイヤーの表示状態を変更できなくなり、ドキュメントで定義された通りにコンテンツが常に表示（または非表示）されるようになります。

利用可能なメソッドとプロパティ:

- layer.lock() – レイヤーをロックします。
- layer.unlock() – レイヤーのロックを解除します。
- layer.locked – 現在のロック状態を返します。

1. PDF ドキュメントを開く。
1. PDF の最初のページにアクセスする。
1. ページにレイヤーがあるか確認する。
1. 最初のレイヤーを取得し、ロックする。
1. 更新された PDF を保存する。

PDF にレイヤーが含まれている場合、最初のレイヤーがロックされ、ユーザーが表示状態を変更できなくなります。レイヤーが見つからない場合は、代わりにメッセージが出力されます。

```python

import aspose.pdf as ap
from os import path

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

この例では、Aspose.PDF for Python via .NET ライブラリを使用して、PDF ドキュメントの最初のページから個別のレイヤーを抽出し、各レイヤーを別々の PDF ファイルとして保存します。

レイヤーから新しい PDF を作成するには、以下のコードスニペットを使用できます:

1. PDF ドキュメントをロードする。入力 PDF は Aspose.PDF.Document オブジェクトにロードされます。
1. ページ 1 のレイヤーにアクセスする。スクリプトは document.pages[1].layers を使用して最初のページからすべてのレイヤーを取得します。
1. レイヤーを確認する。レイヤーが見つからない場合、メッセージが出力され関数は終了します。
1. 各レイヤーを反復処理し、保存する。

```python

import aspose.pdf as ap
from os import path

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF
        for layer in layers:
            layer.save(path_outfile)
```

PDF レイヤー要素を抽出し、新しい PDF ファイルストリームに保存することが可能です:

```python

import aspose.pdf as ap
from os import path

def save_layers_to_stream(path_infile, output_stream):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        for layer in layers:
            layer.save(output_stream)
```

## レイヤー化された PDF のフラット化

このスクリプトは Aspose.PDF for Python via .NET を使用して、PDF ドキュメントの最初のページのすべてのレイヤーをフラット化します。フラット化により、各レイヤーの視覚コンテンツが単一の統合レイヤーに結合され、印刷、共有、アーカイブが容易になり、視覚的な忠実度やレイヤー固有のデータが失われません。

1. PDFドキュメントを読み込む。入力PDFはAspose.PDF.Documentオブジェクトにロードされます。
1. ページ1のレイヤーにアクセスする。スクリプトはdocument.pages[1].layersを使用して最初のページからすべてのレイヤーを取得します。
1. レイヤーの存在を確認する。レイヤーが見つからない場合、メッセージが表示され関数が終了します。
1. 各レイヤーをフラット化する。各レイヤーはlayer.flatten(True)を使用してフラット化され、内容がページに統合されます。
1. 変更されたドキュメントを保存する。

```python

import aspose.pdf as ap
from os import path

def flatten_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if not page.layers:
            print("No layers found in the document.")
            return
        # Flatten each layer
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

## PDF内のすべてのレイヤーを1つに統合する

このコードスニペットはAspose.PDFを使用して、PDFの最初のページのすべてのレイヤーをカスタム名の統合レイヤーにマージします。

1. PDFドキュメントを読み込む。PDFはAspose.PDF.Documentオブジェクトにロードされます。
1. ページとそのレイヤーにアクセスする。最初のページが選択され、そのレイヤーが取得されます。
1. レイヤーを確認する。レイヤーが存在しない場合、メッセージが表示されプロセスが終了します。
1. 新しいレイヤー名を定義する。マージされた結果のために新しいレイヤー名（"LayerNew"）が指定されます。
1. レイヤーをマージする。オプションのコンテンツグループIDが提供されている場合はそれを使用してマージします。提供されていない場合は、新しい名前だけでレイヤーがマージされます。
1. ドキュメントを保存する

```python

import aspose.pdf as ap
from os import path

def merge_layers(path_infile, path_outfile, new_layer_name, optional_group_id=None):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```
