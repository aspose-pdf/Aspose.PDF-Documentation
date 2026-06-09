---
title: Python で HTML を PDF に変換
linktitle: HTML ファイルを PDF ファイルに変換する
type: docs
weight: 40
url: /ja/python-net/convert-html-to-pdf/
lastmod: "2026-06-09"
description: CSS メディア設定、埋め込みフォント、タグ付き PDF 出力など、.NET 経由の Aspose.PDF を使用して Python で HTML と MHTML を PDF に変換する方法を学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Aspose.PDF を使って Python で HTML を PDF に変換する方法
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して HTML ファイルと MHTML ファイルを PDF に変換する方法について説明します。HTML から PDF への基本的なワークフローについて説明し、メディアタイプによるレンダリングの制御方法、CSS ページルールの優先順位、埋め込みフォント、単一ページ出力、およびアクセシブルなタグ付き PDF の論理構造生成について説明します。
---

## Python HTML から PDF への変換

**.NET 経由の Python 用 Aspose.pdf **を使用すると、既存のHTMLドキュメントを柔軟なレンダリングオプションを使用してPDFに変換できます。レイアウト、スタイル、アクセシビリティ、アーカイブ要件に合わせて、出力の生成方法を微調整できます。

## HTML ファイルを PDF に変換

次の Python の例は、HTML ドキュメントを PDF に変換するための基本的なワークフローを示しています。

1. のインスタンスを作成する [HTML ロードオプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) クラス。
1. を初期化 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) ソース HTML ファイルを含むオブジェクト。
1. 呼び出して出力 PDF ドキュメントを保存します `document.save()`.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## 関連コンバージョン

- [PDF ファイルを HTML 形式に変換](/pdf/ja/python-net/convert-pdf-to-html/) 既存の PDF ファイルから Web 対応の出力が必要な場合。
- [他のファイル形式を PDF に変換](/pdf/ja/python-net/convert-other-files-to-pdf/) EPUB、XPS、テキスト、およびポストスクリプト変換ワークフロー用。
- [画像を PDF に変換](/pdf/ja/python-net/convert-images-format-to-pdf/) ソースコンテンツが HTML マークアップではなく画像ベースの場合。

{{% alert color="success" %}}
**オンラインでHTMLをPDFに変換してみてください**

Asposeがオンライン申請書を提示します [「HTML から PDF へ」](https://products.aspose.app/html/en/conversion/html-to-pdf)ここで、変換品質と出力をテストできます。

[![Aspose.PDF アプリを使用して HTML を PDF に変換](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## メディアタイプを使用して HTML を PDF に変換

この例は、特定のレンダリングオプションを使用して HTML ファイルを PDF に変換する方法を示しています。

1. のインスタンスを作成する [HTML ロードオプション ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) クラス。
1. セット `html_media_type` 画面レイアウトまたは印刷レイアウト用の CSS ルールを適用する。例: `HtmlMediaType.SCREEN` または `HtmlMediaType.PRINT`.
1. HTML をに読み込む `ap.Document` ロードオプションを使用する。
1. 文書を PDF として保存します。

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.html_media_type = ap.HtmlMediaType.SCREEN
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## CSS に優先順位を付ける `@page` HTML から PDF への変換中のルール

一部の文書は以下を使用します [その `@page` ルール](https://developer.mozilla.org/en-US/docs/Web/CSS/@page) ページレイアウト用。これらのスタイルが他の設定と矛盾する場合は、次の方法で優先順位を制御できます。 `is_priority_css_page_rule`.

1. のインスタンスを作成する [HTML ロードオプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) クラス。
1. セット `is_priority_css_page_rule = False` 他のスタイルを優先させる `@page` ルール。
1. HTML をに読み込む `ap.Document` 設定済みのオプションを使用します。
1. 文書を PDF として保存します。

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
# load_options.is_priority_css_page_rule = False
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## フォントが埋め込まれた HTML を PDF に変換

この例は、フォントの埋め込み中に HTML ファイルを PDF に変換する方法を示しています。出力 PDF で元のタイポグラフィを保存する必要がある場合は、次のように設定します。 `is_embed_fonts` に `True`.

1. 作成 `HtmlLoadOptions()` HTML から PDF への変換を設定します。
1. セット `is_embed_fonts = True` HTML で使用されているフォントを PDF に直接埋め込むことができます。
1. HTML をに読み込む `ap.Document` これらのオプションで。
1. 文書を PDF として保存します。

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.is_embed_fonts = True
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## 単一の PDF ページに HTML コンテンツをレンダリングする

この例は、.NET 経由で Aspose.PDF for Python を使用して HTML ファイルを 1 ページの PDF に変換する方法を示しています。を使用してください。 `is_render_to_single_page` HTML コンテンツ全体を 1 つの連続したページにレンダリングしたい場合にプロパティを指定します。

1. のインスタンスを作成 `HtmlLoadOptions()` 変換プロセスを設定します。
1. 有効にする `is_render_to_single_page` HTML コンテンツ全体を 1 ページにレンダリングします。
1. 設定したオプションを含むドキュメントを、にロードします `ap.Document`.
1. 結果を PDF ファイルとして保存します。

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

options = ap.HtmlLoadOptions()
options.is_render_to_single_page = True

doc = ap.Document(path_infile, options)
doc.save(path_outfile)
```

## HTML タグから論理構造を作成

タグ付き PDF とも呼ばれる論理構造では、見出し、段落、リストなど、元の HTML の意味階層が保持されます。これにより、作成された PDF がよりアクセスしやすく、検索しやすくなり、構造化文書のワークフローに適したものになります。

変換時に論理構造を有効にすることで、HTML DOM はビジュアルコンテンツとしてのみレンダリングされるのではなく、PDF タグツリーにマップされます。

アクセシビリティ要件を満たすには、読み上げ順序を定義し、スクリーンリーダーに代替テキストを提供し、コンテンツの階層を維持する論理構造要素を PDF に含める必要があります。

> 出力 PDF の論理構造の品質は、元の HTML マークアップの品質に直接依存します。HTML の構造が不十分だったり無効だったりすると、変換された PDF のタグ付けが不完全または不正確になる可能性があります。

1. HTMLLoadOptions インスタンスを作成して、HTML の変換方法を制御します。
1. セマンティックタグを有効にして、PDF に構造化された要素が含まれるようにします。
1. 設定したオプションを使用して HTML ファイルを開きます。
1. 構造化された PDF を保存します。

```python
import aspose.pdf as ap

# Path to the source HTML
input_html_path = "input.html"
# Path for the Logical Structure PDF
output_pdf_path = "output_logical_structure.pdf"
# Initialize HtmlLoadOptions
options = ap.HtmlLoadOptions()
# Convert HTML markup to PDF logical structure elements
options.create_logical_structure = True
# Open PDF document
with ap.Document(input_html_path, options) as document:
    # Save PDF document
    document.save(output_pdf_path)
```

## MHTML ファイルを PDF ファイルに変換します

この例は、.NET 経由で Aspose.PDF for Python を使用し、特定のページサイズで MHT または MHTML ファイルを PDF ドキュメントに変換する方法を示しています。

1. のインスタンスを作成 `ap.MhtLoadOptions()` MHTML ファイル処理を設定します。
1. ページサイズなど、さまざまなパラメータを設定します。
1. 入力ファイルと設定されたロードオプションを使用してドキュメントを初期化します。
1. 結果の文書を PDF として保存します。

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
load_options = ap.MhtLoadOptions()
load_options.page_info.width = 842
load_options.page_info.height = 1191
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```
