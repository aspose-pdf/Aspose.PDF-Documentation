---
title: Python を使用した PDF の Portfolio の操作
linktitle: ポートフォリオ
type: docs
weight: 20
url: /ja/python-net/portfolio/
description: Python で PDF ポートフォリオを作成する方法。Microsoft Excel ファイル、Word ドキュメント、画像ファイルを使用して PDF ポートフォリオを作成します。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用した PDF の Portfolio の操作方法
Abstract: この記事では、Aspose.PDF for Python via .NET を使用した PDF ポートフォリオの作成と管理について説明します。PDF ポートフォリオは、テキストファイル、画像、スプレッドシート、プレゼンテーションなど、さまざまなファイルタイプを単一の整理されたドキュメントに統合し、関連するすべての資料を一元的に保存できるようにします。この記事では、`Document` クラスと `FileSpecification` クラスを使用してファイルをドキュメント コレクションに追加することで、PDF ポートフォリオを作成する手順を概説します。例として、Microsoft Excel ファイル、Word ドキュメント、画像ファイルを PDF ポートフォリオに組み込む方法を示します。また、ポートフォリオの作成およびファイルの削除のコードスニペットを掲載し、Aspose.PDF for Python を使用した PDF ポートフォリオの管理がいかにシンプルで効率的であるかを示しています。
---

PDF ポートフォリオを作成すると、さまざまなタイプのファイルを単一の一貫したドキュメントに統合し、アーカイブできます。こうしたドキュメントには、テキストファイル、画像、スプレッドシート、プレゼンテーション、その他の資料が含まれ、関連するすべての資料が一か所に保存・整理されます。

PDF ポートフォリオは、使用する場所を問わずプレゼンテーションを高品質で提示できるようにします。一般に、PDF ポートフォリオの作成は非常に時代に合ったモダンな作業です。

## PDF ポートフォリオの作成方法

Aspose.PDF for Python via .NET は、[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスを使用して PDF ポートフォリオ ドキュメントを作成できます。[FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) クラスで取得した後、document.collection オブジェクトにファイルを追加します。ファイルを追加したら、Document クラスの [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使用してポートフォリオ ドキュメントを保存します。

以下の例では、Microsoft Excel ファイル、Word ドキュメント、画像ファイルを使用して PDF ポートフォリオを作成します。

以下のコードは、次のポートフォリオを生成します。

### Aspose.PDF for Python で作成された PDF ポートフォリオ

![Aspose.PDF for Python で作成された PDF ポートフォリオ](working-with-pdf-portfolio_1.jpg)

```python

    import aspose.pdf as ap

    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_excel)
    word = ap.FileSpecification(input_doc)
    image = ap.FileSpecification(input_jpg)

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(output_pdf)
```

## PDF ポートフォリオからファイルを削除

PDF ポートフォリオからファイルを削除/除去するには、以下のコード行を試してください。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    document.collection.delete()

    # Save updated file
    document.save(output_pdf)
```


