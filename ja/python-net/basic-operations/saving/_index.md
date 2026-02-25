---
title: PDF文書をプログラムで保存する
linktitle: PDFを保存
type: docs
weight: 30
url: /ja/python-net/save-pdf-document/
description: Python 用 Aspose.PDF for .NET ライブラリを使用して、PDF ファイルを保存する方法を学びます。PDF 文書をファイルシステム、ストリーム、Web アプリケーションに保存する方法を紹介します。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で Aspose.PDF ライブラリを使用して PDF 文書を保存する
Abstract: この記事では、Python で Aspose.PDF ライブラリを使用して PDF 文書を保存する方法について解説します。PDF の保存方法は主に 3 つあり、ファイルシステムへの保存、ストリームへの保存、PDF/A や PDF/X といった特定のフォーマットでの保存です。`Document` クラスの `save()` メソッドがこれらの操作の中心となります。ファイルシステムに PDF を保存する場合、文書を作成または操作（例 新しいページの追加）した後、パスを指定して直接保存できます。ストリームに保存する場合は、`Save` メソッドのオーバーロードを使用して文書をストリームオブジェクトに書き出すことができます。さらに、記事では長期保存用の標準である PDF/A や、グラフィック交換用の標準である PDF/X 形式での保存方法も説明しています。このプロセスでは、保存前に `convert` メソッドで文書を準備する必要があります。提供された Python のコードスニペットはそれぞれのアプローチを実演しており、これらのメソッドの実践的な使い方を示しています。
---

## PDF 文書をファイルシステムに保存する

作成または操作した PDF 文書は、[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスの [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使用してファイルシステムに保存できます。

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # make some manipation, i.g add new empty page
    document.pages.add()
    document.save(output_pdf)
```

## PDF 文書をストリームに保存する

作成または操作した PDF 文書は、`Save` メソッドのオーバーロードを使用してストリームに保存することもできます。

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # make some manipation, i.g add new empty page
    document.pages.add()
    document.save(io.FileIO(output_pdf, 'w'))
```

## PDF/A または PDF/X 形式で保存する

PDF/A は、電子文書のアーカイブおよび長期保存のために使用される、ポータブルドキュメント形式 (PDF) の ISO 標準化バージョンです。
PDF/A は、フォントリンク（フォント埋め込みとは異なる）や暗号化など、長期保存に適さない機能を禁止している点で PDF と異なります。PDF/A ビューアに対する ISO の要件には、色管理ガイドライン、埋め込みフォントのサポート、埋め込みアノテーションを読み取るためのユーザーインターフェイスが含まれます。

PDF/X は PDF ISO 標準のサブセットです。PDF/X の目的はグラフィックの交換を容易にすることであり、そのため標準的な PDF ファイルには適用されない印刷に関する一連の要件を持ちます。

いずれの場合も、[save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使用して文書を保存し、文書は [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドで事前に準備する必要があります。

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    document.pages.add()
    document.convert(output_log, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(output_pdf)
```

