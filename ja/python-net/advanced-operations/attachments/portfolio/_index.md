---
title: Python で PDF ポートフォリオを作成する方法
linktitle: ポートフォリオ
type: docs
weight: 20
url: /ja/python-net/portfolio/
description: .NET 経由の Aspose.PDF for Python を使用して Python で PDF ポートフォリオを作成および管理する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で埋め込みファイルを使用した PDF ポートフォリオの構築と編集
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ポートフォリオを作成および管理する方法について説明します。Python を使用して複数のファイルタイプを 1 つの PDF ポートフォリオにまとめたり、文書コレクションにファイルを追加したり、ポートフォリオ項目をプログラムから削除したりする方法を学びます。
---

PDF ポートフォリオを作成すると、さまざまな種類のファイルを 1 つの一貫した文書に統合してアーカイブできます。このような文書には、テキストファイル、画像、スプレッドシート、プレゼンテーション、その他の資料を含めることができ、すべての関連資料を 1 か所に保存して整理できます。

PDFポートフォリオは、どこで使用してもプレゼンテーションを高品質に表示するのに役立ちます。一般的に、PDF ポートフォリオの作成は最新かつ最新の作業です。

PDF ポートフォリオは、各ファイルを元の形式のまま 1 つの PDF コンテナにまとめて配布する場合に使用します。

## PDF ポートフォリオの作成方法

.NET 経由の Python 用 Aspose.PDF では、を使用して PDF ポートフォリオドキュメントを作成できます [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス。を使用してファイルを取得した後、document.collection オブジェクトにファイルを追加します。 [ファイル仕様](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) クラス。ファイルが追加されたら、「Document クラス」を使用してください。 [保存 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) ポートフォリオドキュメントを保存する方法。

次の例では、Microsoft Excel ファイル、Word 文書、および画像ファイルを使用して PDF ポートフォリオを作成します。

以下のコードは次のポートフォリオになります。

### Python 用 Aspose.PDF で作成された PDF ポートフォリオ

![Python 用 Aspose.PDF で作成された PDF ポートフォリオ](working-with-pdf-portfolio_1.jpg)

```python
import aspose.pdf as ap

def create_pdf_portfolio(input_files, outfile):
    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_files[0])
    word = ap.FileSpecification(input_files[1])
    image = ap.FileSpecification(input_files[2])

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(outfile)
```

## PDF ポートフォリオからのファイルの削除

PDF ポートフォリオからファイルを削除/削除するには、次のコード行を使用してみてください。

```python
import aspose.pdf as ap

def remove_files_from_pdf_portfolio(infile, outfile):
    # Open document
    document = ap.Document(infile)
    document.collection.delete()

    # Save updated file
    document.save(outfile)
```

## 関連する添付トピック

- [Python で PDF の添付ファイルを操作する](/pdf/ja/python-net/attachments/)
- [Python で PDF に添付ファイルを追加する方法](/pdf/ja/python-net/add-attachment-to-pdf-document/)
- [Python で PDF から添付ファイルを削除する](/pdf/ja/python-net/removing-attachment-from-an-existing-pdf/)

