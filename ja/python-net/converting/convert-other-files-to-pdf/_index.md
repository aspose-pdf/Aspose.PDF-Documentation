---
title: Python で他のファイル形式を PDF に変換する方法
linktitle: 他のファイル形式を PDF に変換
type: docs
weight: 80
url: /ja/python-net/convert-other-files-to-pdf/
lastmod: "2026-06-09"
description: .NET 経由の Aspose.PDF for Python を使用して、EPUB、Markdown、PCL、XPS、PostScript、XML、LaTeX ファイルを Python で PDF に変換する方法を学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Python で他のファイル形式を PDF に変換する方法
Abstract: この記事では、Python を使用してさまざまなファイル形式を PDF に変換し、.NET 経由で Aspose.PDF for Python の機能を活用する方法に関する包括的なガイドを提供します。このドキュメントでは、EPUB、マークダウン、PCL、テキスト、XPS、ポストスクリプト、XML、XSL-FO、ラテックス/テックスなど、いくつかの形式の変換プロセスの概要を説明しています。各セクションには、これらの変換を実装するための特定のコードスニペットと手順が記載されています。この記事では、正確で効率的な変換を実現するために、ファイルタイプごとに調整されたロードオプションなどの Aspose.PDF の機能の有用性を強調しています。さらに、ユーザーが機能を直接調べることができるオンライン変換アプリケーションの提供についても取り上げています。このガイドは、PDF 変換機能を Python アプリケーションに統合したいと考えている開発者にとって、実践的なリソースとして役立ちます。
---

この記事では、**Pythonを使用して他のさまざまなファイル形式をPDFに変換する方法**について説明します。以下のトピックを取り上げています。

## OFD ファイルを PDF ファイルに変換する

OFD はオープン固定レイアウトドキュメント (オープン固定ドキュメントフォーマットとも呼ばれます) の略です。これは電子文書に関する中国の国家規格 (GB/T 33190-2016) で、PDF の代替として導入されました。

Python で OFD を PDF に変換する手順:

1. OFDLoadOptions () を使用して OFD ロードオプションを設定します。
1. OFD ドキュメントをロードします。
1. PDF として保存します。

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_OFD_to_PDF(infile, outfile):
    load_options = ap.OfdLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## ラテックス/テックスを PDF に変換

LaTeXファイル形式は、TeXファミリーの言語から派生したLaTeX言語のマークアップを含むテキストファイル形式であり、LaTeXはTeXシステムの派生形式です。LaTeX (lah-letk/lay-tek または lah-tek) は文書準備システムおよび文書マークアップ言語です。数学、物理学、コンピューターサイエンスなど、多くの分野の科学文書の伝達と出版に広く使用されています。また、韓国語、日本語、漢字、アラビア語などの複雑な多言語資料を含む書籍や記事（特別版を含む）の作成と出版においても重要な役割を果たします。

LaTeX は出力の書式設定に TeX 組版プログラムを使用し、それ自体が TeX マクロ言語で記述されています。

{{% alert color="success" %}}
**LaTeX/TeXをオンラインでPDFに変換してみてください**

.NET 経由の Python 用 Aspose.PDF を使用するとオンラインアプリケーションが表示されます [「ラテックスからPDFへ」](https://products.aspose.app/pdf/conversion/tex-to-pdf)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリを使ってラテックス/テックスを PDF に変換](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Python で TEX を PDF に変換する手順:

1. LaTeX ロードオプション () を使用して LaTeX ロードオプションを設定します。
1. LaTeX ドキュメントをロードします。
1. PDF として保存します。

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_TEX_to_PDF(infile, outfile):
    load_options = ap.LatexLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## EPUB ファイルを PDF に変換

**.NET 経由の Python 用 Aspose.pdf ** を使用すると、EPUB ファイルを PDF 形式に簡単に変換できます。

EPUB（電子出版の略）は、国際デジタル出版フォーラム（IDPF）が提供する無料のオープン電子書籍標準です。ファイルの拡張子は.epub です。EPUB はリフロー型コンテンツ向けに設計されているため、EPUB リーダーは特定の表示デバイスに合わせてテキストを最適化できます。

<abbr title="electronic publication">EPUB</abbr> 固定レイアウトコンテンツもサポートしています。この形式は、出版社や変換会社が社内で使用できるだけでなく、配布や販売にも使用できる単一の形式として意図されています。これはオープン電子書籍標準に取って代わります。EPUB 3 バージョンは、コンテンツのパッケージングに関するベストプラクティス、研究、情報、イベントの標準化を行う大手書籍業界団体である書籍業界研究グループ (BISG) からも承認されています。

{{% alert color="success" %}}
**オンラインでEPUBをPDFに変換してみてください**

.NET 経由の Python 用 Aspose.PDF を使用するとオンラインアプリケーションが表示されます [「EPUB から PDF へ」](https://products.aspose.app/pdf/conversion/epub-to-pdf)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリで EPUB を PDF に変換](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

Python で EPUB を PDF に変換する手順:

1. EPUB ロードオプション () を使用して EPUB ドキュメントをロードします。
1. EPUB を PDF に変換します。
1. 確認書を印刷。

次のコードスニペットは、Pythonを使用してEPUBファイルをPDF形式に変換する方法を示しています。

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_EPUB_to_PDF(infile, outfile):
    load_options = ap.EpubLoadOptions()
    document = ap.Document(infile, load_options)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## マークダウンを PDF に変換

**この機能はバージョン19.6以降でサポートされています。**

{{% alert color="success" %}}
**マークダウンをオンラインでPDFに変換してみてください**

.NET 経由の Python 用 Aspose.PDF を使用するとオンラインアプリケーションが表示されます [「PDF へのマークダウン」](https://products.aspose.app/pdf/conversion/md-to-pdf)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリによる PDF へのマークダウンの変換](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

.NET 経由の Aspose.PDF for Python によるこのコードスニペットは、Markdown ファイルを PDF に変換するのに役立ちます。これにより、ドキュメントの共有、フォーマットの保存、印刷の互換性が向上します。o

次のコードスニペットは、Aspose.PDF ライブラリでこの機能を使用する方法を示しています。

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_MD_to_PDF(infile, outfile):
    load_options = ap.MdLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## PCL ファイルを PDF に変換

<abbr title="Printer Command Language">PCL</abbr> (プリンタコマンド言語) は、標準のプリンタ機能にアクセスするために開発された Hewlett-Packard プリンタ言語です。PCL レベル 1 から 5e/5c は、受信した順に処理および解釈される制御シーケンスを使用するコマンドベースの言語です。コンシューマーレベルでは、PCL データストリームはプリントドライバーによって生成されます。PCL 出力はカスタムアプリケーションでも簡単に生成できます。

{{% alert color="success" %}}
**オンラインでPCLをPDFに変換してみてください**

.NET 用の Aspose.PDF がオンラインアプリケーションを表示します [「PCL から PDF へ」](https://products.aspose.app/pdf/conversion/pcl-to-pdf)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリで PCL を PDF に変換](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

PCL から PDF への変換を可能にするために、Aspose.PDF には次のクラスがあります [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) これは LoadOptions オブジェクトを初期化するために使用されます。その後、このオブジェクトは Document オブジェクトの初期化時に引数として渡され、PDF レンダリングエンジンがソースドキュメントの入力形式を決定するのに役立ちます。

次のコードスニペットは、PCL ファイルを PDF 形式に変換するプロセスを示しています。

Python で PCL を PDF に変換する手順:

1. PCLLoadOptions () を使用して PCL のオプションをロードします。
1. ドキュメントをロードします。
1. PDF として保存します。

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_PCL_to_PDF(infile, outfile):
    load_options = ap.PclLoadOptions()
    load_options.supress_errors = True

    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## 整形済みテキストを PDF に変換

**.NET 経由の Python 用 Aspose.pdf ** は、プレーンテキストとフォーマット済みのテキストファイルを PDF 形式に変換する機能をサポートしています。

テキストをPDFに変換するということは、PDFページにテキストフラグメントを追加することを意味します。テキストファイルに関しては、プレフォーマット (例えば、25 行、1 行に 80 文字) とフォーマットされていないテキスト (プレーンテキスト) の 2 種類のテキストを扱っています。必要に応じて、この追加を自分で制御することも、ライブラリのアルゴリズムに任せることもできます。

{{% alert color="success" %}}
**オンラインでTEXTをPDFに変換してみてください**

.NET 経由の Python 用 Aspose.PDF を使用するとオンラインアプリケーションが表示されます [「テキストから PDF へ」](https://products.aspose.app/pdf/conversion/txt-to-pdf)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリを使ってテキストを PDF に変換](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

Python でテキストを PDF に変換する手順:

1. 入力テキストファイルを 1 行ずつ読み取ります。
1. 等幅フォント (Courier New) を設定すると、テキストの配置が一貫します。
1. 新しい PDF ドキュメントを作成し、カスタムの余白とフォント設定を使用して最初のページを追加します。
1. テキストファイルの行を繰り返し処理するタイプライターをシミュレートするには、「monospace_font」フォントを使用し、サイズは 12 にします。
1. ページ作成を 4 ページに制限します。
1. 最終的な PDF を指定されたパスに保存します。

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_TXT_to_PDF(infile, outfile):
    with open(infile, "r") as file:
        lines = file.readlines()

    monospace_font = ap.text.FontRepository.find_font("Courier New")

    document = ap.Document()
    page = document.pages.add()

    page.page_info.margin.left = 20
    page.page_info.margin.right = 10
    page.page_info.default_text_state.font = monospace_font
    page.page_info.default_text_state.font_size = 12
    count = 1
    for line in lines:
        if line != "" and line[0] == "\x0c":
            page = document.pages.add()
            page.page_info.margin.left = 20
            page.page_info.margin.right = 10
            page.page_info.default_text_state.font = monospace_font
            page.page_info.default_text_state.font_size = 12
            count = count + 1
        else:
            text = ap.text.TextFragment(line)
            page.paragraphs.add(text)

        if count == 4:
            break

    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## ポストスクリプトを PDF に変換

この例は、.NET 経由で Aspose.PDF for Python を使用して PostScript ファイルを PDF ドキュメントに変換する方法を示しています。

1. PS ファイルを正しく解釈するには、「PSLoadOptions」のインスタンスを作成してください。
1. ロードオプションを使用して、「PostScript」ファイルを Document オブジェクトにロードします。
1. 文書を PDF 形式で目的の出力パスに保存します。

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_PS_to_PDF(infile, outfile):
    load_options = ap.PsLoadOptions()

    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## XPS ファイルを PDF ファイルに変換します

**.NET 経由の Python 用 Aspose.pdf ** 機能変換をサポート <abbr title="XML Paper Specification">XPS</abbr> ファイルを PDF 形式に変換します。この記事を確認してタスクを解決してください。

XPSファイルタイプは、主にマイクロソフト社のXMLペーパー仕様に関連付けられています。XML Paper Specification (XPS) は、以前はMetro というコードネームで、次世代印刷パス (NGPP) のマーケティングコンセプトを取り入れていました。これは、ドキュメントの作成と表示を Windows オペレーティングシステムに統合するというマイクロソフトの取り組みです。

次のコードスニペットは、Python を使用して XPS ファイルを PDF 形式に変換するプロセスを示しています。

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XPS_to_PDF(infile, outfile):
    load_options = ap.XpsLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**オンラインでXPS形式をPDFに変換してみてください**

.NET 経由の Python 用 Aspose.PDF を使用するとオンラインアプリケーションが表示されます [「XPS から PDF へ」](https://products.aspose.app/pdf/conversion/xps-to-pdf/)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリで XPS を PDF に変換](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## XSL-FO ファイルを PDF ファイルに変換します

次のコードスニペットを使用すると、.NET 経由で Aspose.PDF for Python を使用して XSLFO を PDF 形式に変換できます。

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XSLFO_to_PDF(xsltfile, xmlfile, outfile):
    load_options = ap.XslFoLoadOptions(xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.THROW_EXCEPTION_IMMEDIATELY
    )
    document = ap.Document(xmlfile, load_options)
    document.save(outfile)

    print(xmlfile + " converted into " + outfile)
```

## XSLT 形式の XML ファイルを PDF 形式に変換

この例は、まず XSLT テンプレートを使用して XML ファイルを HTML に変換し、その HTML を Aspose.PDF に読み込むことで、XML ファイルを PDF に変換する方法を示しています。

1. 「HTMLロードオプション」のインスタンスを作成して、HTMLからPDFへの変換を設定します。
1. 変換された HTML ファイルを Aspose.PDF ドキュメントオブジェクトに読み込みます。
1. 指定した出力パスに文書を PDF として保存します。
1. 変換が成功したら、一時的な HTML ファイルを削除します。

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XSLFO_to_PDF(xsltfile, xmlfile, outfile):
    load_options = ap.XslFoLoadOptions(xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.THROW_EXCEPTION_IMMEDIATELY
    )
    document = ap.Document(xmlfile, load_options)
    document.save(outfile)

    print(xmlfile + " converted into " + outfile)
```

## 関連コンバージョン

- [HTML ファイルを PDF に変換](/pdf/ja/python-net/convert-html-to-pdf/) HTML および MHTML の変換シナリオに適しています。
- [画像形式を PDF に変換](/pdf/ja/python-net/convert-images-format-to-pdf/) 入力が PNG、JPEG、TIFF、SVG、またはその他のイメージの場合。
- [PDF を他の形式に変換](/pdf/ja/python-net/convert-pdf-to-other-files/) PDFからEPUB、マークダウン、またはテキストへの逆変換も必要な場合。
