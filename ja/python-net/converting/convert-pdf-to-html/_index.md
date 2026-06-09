---
title: Python で PDF を HTML に変換
linktitle: PDF ファイルを HTML フォーマットに変換
type: docs
weight: 50
url: /ja/python-net/convert-pdf-to-html/
lastmod: "2026-06-09"
description: マルチページ出力、外部イメージ、SVG 処理、階層化された HTML レンダリングなど、.NET 経由で Aspose.PDF for Python を使用して PDF を HTML に変換する方法を学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Python で PDF を HTML に変換する方法
Abstract: この記事では、Python を使用して PDF ファイルを HTML に変換するための包括的なガイドを提供します。特に、.NET ライブラリ経由の Aspose.PDF for Python を使用してください。この変換をプログラムで行うために必要な手順の概要を説明し、ソース PDF から「ドキュメント」オブジェクトを作成する方法と、「HTMLSaveOptions」を使用してドキュメントを HTML 形式で保存する方法に焦点を当てています。この記事には、変換プロセスを説明する簡潔な Python コードスニペットが含まれています。さらに、Aspose.PDF の「PDF to HTML」アプリケーションというオンラインツールも紹介しています。このツールを使うと、ユーザーは変換の機能と品質を調べることができます。この記事は、PDF から HTML への変換に Python を使用する方法を完全に理解できるように、さまざまな関連トピックに対応できるように構成されています。
---

## PDF ファイルを HTML 形式に変換

**.NET 経由の Python 用 Aspose.pdf ** には、さまざまなファイル形式を PDF ドキュメントに変換したり、PDF ファイルをさまざまな出力形式に変換したりするための多くの機能があります。この記事では、PDF ファイルを PDF に変換する方法について説明します。 <abbr title="HyperText Markup Language">HTML</abbr>。PDF から HTML への変換には Python のコードをほんの数行だけ使用できます。Web サイトを作成したり、オンラインフォーラムにコンテンツを追加したりする場合は、PDF を HTML に変換する必要がある場合があります。PDF を HTML に変換する方法の 1 つは、プログラムで Python を使用することです。

{{% alert color="success" %}}
**オンラインでPDFをHTMLに変換してみてください**

Python 用の Aspose.PDF はオンラインアプリケーションを提供します [「PDF から HTML へ」](https://products.aspose.app/pdf/conversion/pdf-to-html)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリで PDF を HTML に変換](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

手順:Python で PDF を HTML に変換する

1. のインスタンスを作成 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) ソース PDF ドキュメントを含むオブジェクト。
1. 保存先 [HTML 保存オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) 電話して [保存 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## 関連コンバージョン

- [HTML ファイルを PDF に変換](/pdf/ja/python-net/convert-html-to-pdf/) Web からドキュメントへのリバースワークフローが必要な場合
- [PDF をワードに変換](/pdf/ja/python-net/convert-pdf-to-word/) 編集可能なドキュメント出力がHTMLよりも便利な場合。
- [PDF を画像形式に変換](/pdf/ja/python-net/convert-pdf-to-images-format/) ラスタエクスポートシナリオ用。

### 指定したフォルダに画像を保存してPDFをHTMLに変換

この関数は、.NET 経由の Python 用 Aspose.PDF を使用して PDF ファイルを HTML フォーマットに変換します。抽出されたすべての画像は、HTML ファイルに埋め込まれるのではなく、指定されたフォルダーに保存されます。

1. HTML 保存オプションを設定します。
1. 外部画像を含む HTML として保存します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_storing_images(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "images")
    save_options.special_folder_for_all_images = images_path
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### PDF をマルチページの HTML 形式に変換

この関数は、PDF ファイルを複数ページの HTML に変換し、各 PDF ページが個別の HTML ファイルとしてエクスポートされます。これにより、出力の操作が容易になり、サイズの大きい PDF の読み込み時間が短縮されます。

1. 「AP.ドキュメント」を使用してソースPDFをロードします。
1. 「HTML 保存オプション」を作成し、「ページに分割する」を設定します。
1. 文書を HTML として保存し、ページを別々のファイルに分割します。
1. 確認メッセージを印刷します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_multi_page(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.split_into_pages = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 指定したフォルダにSVG画像を保存してPDFをHTMLに変換

この関数は、すべての画像を HTML に直接埋め込むのではなく、指定されたフォルダーに SVG ファイルとして保存しながら、PDF を HTML 形式に変換します。

1. 「AP.ドキュメント」を使用してソースPDFをロードします。
1. 「HTMLSaveOptions」を作成し、「special_folder_for_svg_images」をターゲットフォルダーに設定します。
1. ドキュメントを外部 SVG 画像を含む HTML として保存します。
1. 確認メッセージを印刷します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_storing_svg(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "svg_images")
    save_options.special_folder_for_svg_images = images_path
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### PDF を HTML に変換し、圧縮された SVG イメージを保存する

このスニペットは PDF を HTML 形式に変換し、すべての画像を指定されたフォルダーに SVG ファイルとして保存し、圧縮してファイルサイズを小さくします。

1. 「AP.ドキュメント」を使用してPDFドキュメントをロードします。
1. 「HTML 保存オプション」を作成し、
   - SVG イメージを外部に保存するには、'special_folder_for_svg_images' を設定します。
   - SVG 画像を圧縮するには、「compress_svg_graphics_if_any」を有効にします。
1. 文書を圧縮された外部 SVG 画像を含む HTML として保存します。
1. 確認メッセージを印刷します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_compress_svg(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "svg_images")
    save_options.special_folder_for_svg_images = images_path
    save_options.compress_svg_graphics_if_any = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 埋め込まれたラスター画像の制御による PDF から HTML への変換

このスニペットは PDF を HTML 形式に変換し、ラスター画像を PNG ページの背景として埋め込みます。この方法では、HTML 内の画質とページレイアウトが維持されます。

1. 「AP.ドキュメント」を使用してPDFドキュメントをロードします。
1. 「HTMLSaveOptions」と「raster_images_saving_mode に設定」を「AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND' に設定」を作成します。
1. ラスター画像が埋め込まれた HTML として文書を保存します。
1. 確認メッセージを印刷します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_PNG_background(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.raster_images_saving_mode = ap.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### PDF を本文のみのコンテンツ HTML ページに変換

この関数は PDF を HTML 形式に変換し、余分な「html」または「head」タグなしで「本文のみ」のコンテンツを生成し、出力を個別のページに分割します。

1. 「AP.ドキュメント」を使用してPDFドキュメントをロードします。
1. 「HTML 保存オプション」を作成して以下を設定します。
   - 'html_markup_generation_mode = WRITE_ONLY_BODY_CONTENT' を指定すると、「本文」コンテンツのみが生成されます。
   - 「ページに分割する」を選択すると、PDF ページごとに個別の HTML ファイルが作成されます。
1. 指定したオプションを使用して文書を HTML として保存します。
1. 確認メッセージを印刷します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_body_content(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.html_markup_generation_mode = (
        ap.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
    )
    save_options.split_into_pages = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 透明テキストレンダリングによる PDF から HTML への変換

この関数は PDF を HTML 形式に変換し、影の付いたテキストを含むすべてのテキストを透明に表示します。これにより、出力 HTML で柔軟なスタイルを設定しながら、視覚的な忠実度を維持できます。

1. 「AP.ドキュメント」を使用してPDFドキュメントをロードします。
1. 「HTML 保存オプション」を作成して以下を設定します。
    -「save_transparent _texts」を押すと、通常のテキストが透明になります。
    -「save_shadowed_texts_as_transparent _text」を選択すると、シャドウ付きのテキストが透明でレンダリングされます。
1. 文書を透明テキストレンダリングの HTML として保存します。
1. 確認メッセージを印刷します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_transparent_text_rendering(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.save_transparent_texts = True
    save_options.save_shadowed_texts_as_transparent_texts = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### ドキュメントレイヤーレンダリングによる PDF から HTML への変換

この関数は PDF を HTML 形式に変換し、マークされたコンテンツを出力 HTML の個別のレイヤーに変換することでドキュメントレイヤーを保持します。これにより、レイヤー化された要素 (注釈、背景、オーバーレイなど) を正確にレンダリングできます。

1. 「AP.ドキュメント」を使用してPDFドキュメントをロードします。
1. 「HTML保存オプション」を作成し、「convert_marked_content_to_layers」を有効にしてレイヤーを保存します。
1. 文書を階層化されたコンテンツを含む HTML として保存します。
1. 確認メッセージを印刷します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_document_layers_rendering(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.convert_marked_content_to_layers = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

