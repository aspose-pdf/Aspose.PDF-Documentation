---
title: Pythonでプログラム的にPDFを分割する
linktitle: PDFファイルを分割
type: docs
weight: 60
url: /ja/python-net/split-pdf-document/
description: このトピックでは、Python アプリケーションで PDF ページを個別の PDF ファイルに分割する方法を示します。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用した PDF ページの分割
Abstract: この記事では、Python を使用して PDF ページを個別のファイルに分割するプロセスについて説明し、大規模な PDF ドキュメントの管理におけるこの機能の有用性を強調しています。PDF 分割機能を実証するために設計されたオンラインツールである Aspose.PDF Splitter が参照されています。記事では、Python アプリケーションでこれを実現するための詳細な手順を提供しており、`Document` オブジェクトの `PageCollection` を介して PDF ドキュメントのページを反復処理します。各ページについて、新しい `Document` オブジェクトを作成し、ページをそのオブジェクトに追加し、`save()` メソッドを使用して新しい PDF ファイルを保存します。添付の Python コードスニペットは、このプロセスを示しており、ページを反復処理してそれぞれを個別の PDF として保存することで、PDF ドキュメントを別々のファイルに分割する手順を示しています。
---

PDF ページの分割は、大きなファイルを個別のページやページグループに分割したいユーザーにとって有用な機能となります。

## ライブ例

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) は、プレゼンテーションの分割機能がどのように動作するかを調査できるオンラインの無料ウェブアプリケーションです。

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

このトピックでは、Python アプリケーションで PDF ページを個別の PDF ファイルに分割する方法を示します。Python を使用して PDF ページを単一ページの PDF ファイルに分割するには、以下の手順に従います。

1. PDF ドキュメントのページを、[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトの [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) コレクションを通じてループ処理します
1. 各イテレーションで新しい Document オブジェクトを作成し、個々の [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) オブジェクトを空のドキュメントに追加します
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使用して新しい PDF を保存します

## Python で PDF を複数のファイルまたは別々の PDF に分割する

以下の Python コードスニペットは、PDF ページを個別の PDF ファイルに分割する方法を示しています。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    page_count = 1

    # Loop through all the pages
    for pdfPage in document.pages:
        new_document = ap.Document()
        new_document.pages.add(pdfPage)
        new_document.save(output_path + "_page_" + str(page_count) + ".pdf")
        page_count = page_count + 1
```


