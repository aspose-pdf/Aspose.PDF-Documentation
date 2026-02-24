---
title: Python を使用して PDF を作成する方法
linktitle: PDF ドキュメントを作成
type: docs
weight: 10
url: /ja/python-net/create-pdf-document/
description: Aspose.PDF for Python via .NET を使用して PDF ドキュメントを作成およびフォーマットします。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF ファイルを作成
Abstract: Aspose.PDF for Python via .NET は、.NET フレームワークを対象とした Python アプリケーション内で PDF ファイルを操作するために開発者向けに設計された多目的 API です。ユーザーは PDF ドキュメントを簡単に作成、読み込み、修正、変換できます。本記事では Aspose.PDF を使用してシンプルな PDF ファイルを作成する手順をステップバイステップで示します。手順は `Document` オブジェクトの初期化、`Page` のドキュメントへの追加、ページの段落への `TextFragment` の挿入、そして PDF としてファイルを保存することです。添付の Python コードスニペットは、テキスト "Hello World!" を含む PDF ドキュメントを作成するこれらの手順を示しています。この API は最小限のコードで PDF の取り扱いを簡素化し、.NET 環境で PDF を扱う開発者の生産性を向上させます。
---

**Aspose.PDF for Python via .NET** は、数行のコードだけで .NET アプリケーション向け Python から直接 PDF ファイルを作成、読み込み、修正、変換できる PDF 操作 API です。

## シンプルな PDF ファイルの作成方法

Aspose.PDF を使用して Python via .NET で PDF を作成するには、以下の手順に従います：

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスのオブジェクトを作成する
1. [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) オブジェクトを Document オブジェクトの [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) コレクションに追加する
1. [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) をページの [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) コレクションに追加する
1. 生成された PDF ドキュメントを保存する

```python

    import aspose.pdf as ap

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    # Save updated PDF
    document.save(output_pdf)
```


