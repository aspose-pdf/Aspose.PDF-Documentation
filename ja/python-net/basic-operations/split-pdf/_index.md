---
title: Python で PDF ファイルを分割する方法
linktitle: PDF ファイルの分割
type: docs
weight: 60
url: /ja/python-net/split-pdf/
description: Python で PDF ページを個別の PDF ファイルに分割する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ページを分割する
Abstract: この記事では、Python を使用して PDF ページを個々のファイルに分割するプロセスについて説明し、サイズの大きな PDF 文書を管理する場合のこのような機能の有用性を強調しています。PDF 分割機能を説明するために設計されたオンラインツール Aspose.PDF Splitter を参照しています。この記事では、Python アプリケーションでこれを実現する方法について詳しく説明します。これには、「Document」オブジェクトの「PageCollect」を介して PDF ドキュメントのページを繰り返し処理する方法が含まれます。ページごとに新しい「Document」オブジェクトが作成され、そのオブジェクトにページが追加され、新しい PDF ファイルが「save ()」メソッドを使用して保存されます。付属の Python コードスニペットではこのプロセスを説明し、ページを繰り返し処理して各ページを個別の PDF として保存することで PDF 文書を個別のファイルに分割する手順を示しています。
---

PDFページの分割は、大きなファイルを別々のページまたはページのグループに分割したい場合に便利な機能です。

このワークフローは、大きな PDF を 1 ページのファイルに分割したり、配布、レビュー、またはダウンストリーム処理のために小さな文書セットに分割したりする必要がある場合に使用します。

## ライブサンプル

[Aspose.PDF スプリッター](https://products.aspose.app/pdf/splitter) は、プレゼンテーション分割機能の仕組みを調べることができる無料のオンラインWebアプリケーションです。

[![アスポーススプリット PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

このトピックでは、Python アプリケーションで PDF ページを個別の PDF ファイルに分割する方法を説明します。Python を使用して PDF ページを 1 ページの PDF ファイルに分割するには、次の手順に従います。

1. PDFドキュメントのページをループ処理して [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトの [ページコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) コレクション
1. イテレーションごとに、新しい Document オブジェクトを作成し、個別のオブジェクトを追加します [ページ](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) オブジェクトを空の文書に入れる
1. 次の方法で新しい PDF を保存します。 [保存 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法

## Python で PDF を複数のファイルに分割したり、PDF を分割したりできます

次の Python コードスニペットは、PDF ページを個別の PDF ファイルに分割する方法を示しています。

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

## 関連ドキュメントトピック

- [Python で PDF ドキュメントを操作する](/pdf/ja/python-net/working-with-documents/)
- [Python で PDF ファイルをマージする](/pdf/ja/python-net/merge-pdf-documents/)
- [Python で PDF ファイルを最適化する方法](/pdf/ja/python-net/optimize-pdf/)
- [Python で PDF ドキュメントを操作する方法](/pdf/ja/python-net/manipulate-pdf-document/)

