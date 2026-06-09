---
title: Python で PDF を EPUB、テキスト、XPS などに変換する方法
linktitle: PDF を他の形式に変換
type: docs
weight: 90
url: /ja/python-net/convert-pdf-to-other-files/
lastmod: "2026-06-09"
description: .NET 経由で Aspose.PDF for Python を使用して、PDF ファイルを Python で EPUB、LaTeX、Markdown、テキスト、XPS、MobiXML に変換する方法を学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Python でPDFを他のフォーマットに変換する方法
Abstract: この記事では、Aspose.PDF for Python を使用して PDF ファイルをさまざまな形式に変換するための包括的なガイドを提供しています。PDF から EPUB、ラテックス/テックス、テキスト、XPS、および XML 形式への変換について説明しています。各セクションの冒頭には、PDFをそれぞれの形式に変換するためのAsposeが提供するオンラインアプリケーションを試すための招待状があり、これらのツールの使いやすさと品質が強調されています。
---

## PDF ファイルを EPUB に変換

{{% alert color="success" %}}
**オンラインでPDFをEPUBに変換してみてください**

Python 用の Aspose.PDF はオンラインアプリケーションを提供します [「PDF から EPUB へ」](https://products.aspose.app/pdf/conversion/pdf-to-epub)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリで PDF を EPUB に変換](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> は、国際デジタル出版フォーラム（IDPF）が提供する無料のオープン電子書籍標準です。ファイルの拡張子は.epub です。
EPUB はリフロー可能なコンテンツ向けに設計されています。つまり、EPUB リーダーは特定のディスプレイデバイスに合わせてテキストを最適化できます。EPUB は固定レイアウトのコンテンツもサポートしています。この形式は、出版社や変換会社が社内で使用できるだけでなく、配布や販売にも使用できる単一の形式として意図されています。オープン電子書籍の標準よりも優先されます。

Aspose.PDF for Python は PDF ドキュメントを EPUB 形式に変換する機能もサポートしています。Aspose.PDF for Python には 'EpubSaveOptions' という名前のクラスがあり、これをの 2 番目の引数として使用できます。 [ドキュメント.save ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使用して EPUB ファイルを生成します。
Python でこの要件を満たすには、次のコードスニペットを使用してみてください。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_EPUB(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = ap.EpubSaveOptions.RecognitionMode.FLOW
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## 関連コンバージョン

- [PDF をワードに変換](/pdf/ja/python-net/convert-pdf-to-word/) 編集可能なオフィス文書出力用。
- [PDF ファイルを HTML 形式に変換](/pdf/ja/python-net/convert-pdf-to-html/) ブラウザ指向の出力用。
- [PDF を PDF/A、PDF/E、および PDF/X に変換](/pdf/ja/python-net/convert-pdf-to-pdf_x/) アーカイブおよび標準準拠の変換ワークフロー用。

## PDF をラテックス/テックスに変換

**.NET 経由の Python 用 Aspose.pdf ** PDF からラテックス/テックスへの変換をサポートします。
LaTeXファイル形式は、特別なマークアップが付いたテキストファイル形式で、TeXベースの文書作成システムで高品質のタイプセットに使用されます。

{{% alert color="success" %}}
**オンラインでPDFをラテックス/テックスに変換してみてください**

Python 用の Aspose.PDF はオンラインアプリケーションを提供します [「PDF から LaTeX へ」](https://products.aspose.app/pdf/conversion/pdf-to-tex)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリで PDF をラテックス/テックスに変換](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

PDF ファイルを TeX に変換するには、Aspose.PDF には次のクラスがあります [ラテックス保存オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) これには、変換処理中に一時イメージを保存するための OutDirectoryPath プロパティが用意されています。

次のコードスニペットは、Python を使用して PDF ファイルを TEX 形式に変換するプロセスを示しています。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_TeX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.LaTeXSaveOptions()
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## PDF をテキストに変換

**Aspose.pdf for Python**は、PDFドキュメント全体と単一ページのテキストファイルへの変換をサポートしています。「TextDevice」クラスを使用して PDF ドキュメントを TXT ファイルに変換できます。次のコードスニペットでは、すべてのページからテキストを抽出する方法を説明しています。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_TXT(infile, outfile):
    document = ap.Document(infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**オンラインでPDFをテキストに変換してみてください**

Python 用の Aspose.PDF はオンラインアプリケーションを提供します [「PDF からテキストへ」](https://products.aspose.app/pdf/conversion/pdf-to-txt)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリで PDF をテキストに変換](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## PDF ファイルを XPS ファイルに変換

**Python用アスポースPDF**では、PDFファイルをXPSフォーマットに変換することができます。提示されたコードスニペットを使って Python で PDF ファイルを XPS フォーマットに変換してみましょう。

{{% alert color="success" %}}
**オンラインでPDFをXPSに変換してみてください**

Python 用の Aspose.PDF はオンラインアプリケーションを提供します [「PDF ファイルから XPS へ」](https://products.aspose.app/pdf/conversion/pdf-to-xps)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリで PDF を XPS に変換](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPSファイルタイプは、主にマイクロソフト社のXMLペーパー仕様に関連付けられています。XML Paper Specification (XPS) は、以前はMetro というコードネームで、次世代印刷パス (NGPP) のマーケティングコンセプトを取り入れていました。これは、ドキュメントの作成と表示を Windows オペレーティングシステムに統合するというマイクロソフトの取り組みです。

PDF ファイルを XPS に変換するには、Aspose.PDF には次のクラスがあります [XPS 保存オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) これは、の 2 番目の引数として使用されます [ドキュメント.save ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) XPS ファイルを生成する方法。

次のコードスニペットは、PDF ファイルを XPS 形式に変換するプロセスを示しています。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_XPS(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## PDF ファイルを MD ファイルに変換します

Aspose.PDF には「MarkDownSaveOptions ()」というクラスがあります。このクラスは、画像やリソースを保存したまま PDF ドキュメントを Markdown (MD) 形式に変換します。

1. 「AP.ドキュメント」を使用してソースPDFをロードします。
1. 「マークダウンセーブオプション」のインスタンスを作成します。
1. 'resources_directory_name'を 'images'に設定してください。抽出された画像はこのフォルダに保存されます。
1. 設定したオプションを使用して、変換された Markdown ドキュメントを保存します。
1. 変換後に確認メッセージを印刷します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_MD(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

指定された画像フォルダーに保存されているテキストとリンクされた画像を含むマークダウンファイル。

## PDF ファイルを MobiXML に変換

このメソッドは、PDF ドキュメントを Kindle 端末の電子書籍で一般的に使用されている MOBI (MobiXML) 形式に変換します。

1. 「AP.Document」を使用してソース PDF ドキュメントをロードします。
1. 「AP.SaveFormat.mobi_XML」の形式でドキュメントを保存します。
1. 変換が完了したら、確認メッセージを印刷します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_MobiXML(infile, outfile):
    document = ap.Document(infile)
    document.save(outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)
```
