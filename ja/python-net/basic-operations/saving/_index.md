---
title: PDF ドキュメントをプログラムで保存する
linktitle: PDF を保存
type: docs
weight: 30
url: /ja/python-net/save-pdf-document/
description: .NET ライブラリ経由で Python Aspose.PDF for Python に PDF ファイルを保存する方法を学びましょう。PDF ドキュメントをファイルシステム、ストリーミング、Web アプリケーションに保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の Aspose.PDF ライブラリを使用して PDF ドキュメントを保存する
Abstract: この記事では、Python の Aspose.PDF ライブラリを使用して PDF ドキュメントを保存するためのガイダンスを提供します。PDF をファイルシステムに保存する方法、ストリームに保存する方法、および PDF/A や PDF/X などの特定の形式で PDF を保存する方法の 3 つの主な方法を概説していますが、これらの操作の中心となるのは `Document` クラスの `save () `メソッドです。PDF をファイルシステムに保存するには、文書を作成または操作 (新しいページの追加など) して、パスに直接保存することができます。ストリームに保存する場合、`Save` メソッドのオーバーロードを使うと、ストリームオブジェクトにドキュメントを書き込むことができます。さらに、この記事では、長期アーカイブとグラフィック交換の標準である PDF/A 形式または PDF/X 形式で文書を保存する方法についても説明します。このプロセスでは、保存する前に `convert` メソッドで文書を準備する必要があります。提供されている Python コードスニペットは、それぞれの方法を示し、これらのメソッドの実際的な応用例を示しています。
---

## PDF ドキュメントをファイルシステムに保存

作成または操作した PDF ドキュメントは、を使用してファイルシステムに保存できます。 [保存 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) の方法 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス。

```python
import aspose.pdf as ap

def save_document_to_file(infile, outfile):
    document = ap.Document(infile)
    # make some manipulation, e.g. add new empty page
    document.pages.add()
    document.save(outfile)
```

## PDF ドキュメントをストリームに保存

のオーバーロードを使用して、作成または操作した PDF ドキュメントをストリームに保存することもできます。 `Save` 方法。

```python
import aspose.pdf as ap
import io

def save_document_to_stream(infile, outfile):
    document = ap.Document(infile)
    # make some manipulation, e.g. add new empty page
    document.pages.add()
    with io.FileIO(outfile, 'w') as stream:
        document.save(stream)
```

## PDF/A 形式または PDF/X 形式を保存

PDF/A や PDF/X など、特定のバージョンの PDF で文書を簡単に保存できます。この場合、文書を保存する前に convert メソッドを呼び出す必要があります。

PDF/Aは、電子文書のアーカイブと長期保存に使用するためのポータブルドキュメントフォーマット（PDF）のISO標準バージョンです。
PDF/Aは、（フォントの埋め込みではなく）フォントリンクや暗号化など、長期間のアーカイブに適さない機能を禁止している点でPDFとは異なります。PDF/A ビューアの ISO 要件には、カラーマネジメントガイドライン、埋め込みフォントのサポート、埋め込まれた注釈を読み込むためのユーザーインターフェイスなどがあります。

PDF/X は PDF ISO 規格のサブセットです。PDF/X の目的は、グラフィックの交換を容易にすることにあるため、標準の PDF ファイルには適用されない印刷関連の要件がいくつもあります。

どちらの場合も、 [保存 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) ドキュメントの保存にはメソッドを使用しますが、ドキュメントは次の方法で作成する必要があります [変換する](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。

```python
import aspose.pdf as ap
import io


def save_document_as_standard(infile, outfile, logfile):
    document = ap.Document(infile)
    document.pages.add()
    document.convert(logfile, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```
