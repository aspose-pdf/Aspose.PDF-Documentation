---
title: Python を使用したブックマークの追加と削除
linktitle: ブックマークの追加と削除
type: docs
weight: 10
url: /ja/python-net/add-and-delete-bookmark/
description: Python を使用して PDF ドキュメントにブックマークを追加できます。PDF ドキュメントからすべてのブックマークまたは特定のブックマークを削除することも可能です。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用してブックマークを追加および削除する方法
Abstract: 本記事では、Python 用 Aspose.PDF ライブラリを使用して PDF ドキュメントのブックマークを管理するための包括的な手順を提供します。PDF 内でブックマークを追加、変更、削除するプロセスについて概説しています。まず、`OutlineItemCollection` オブジェクトを作成し、ドキュメントの `OutlineCollection` に追加することでブックマークを追加する手順を紹介します。親ブックマークと子ブックマークの作成と追加を示すコード例が含まれ、階層関係を強調しています。さらに、すべてのブックマークまたはタイトルで特定のブックマークを削除する方法も取り上げています。各セクションには操作を示す Python のコードスニペットが含まれており、読者が PDF 操作タスクで記述された機能を容易に実装できるようになっています。
---

## PDF ドキュメントにブックマークを追加する

ブックマークは Document オブジェクトの [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) コレクションに格納され、さらに [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクションの中にあります。

PDF にブックマークを追加するには:

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトを使用して PDF ドキュメントを開きます。
1. ブックマークを作成し、プロパティを定義します。
1. [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) コレクションを Outlines コレクションに追加します。

以下のコードスニペットは、PDF ドキュメントにブックマークを追加する方法を示しています。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create a bookmark object
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Test Bookmark"
    outline.italic = True
    outline.bold = True
    # Set the destination page number
    outline.action = ap.annotations.GoToAction(document.pages[1])
    # Add bookmark in the document's outline collection.
    document.outlines.append(outline)

    # Save output
    document.save(output_pdf)
```

## PDF ドキュメントに子ブックマークを追加する

ブックマークは入れ子にでき、親ブックマークと子ブックマークの階層関係を示します。本記事では、子ブックマーク、すなわち第 2 レベルのブックマークを PDF に追加する方法を説明します。

PDF ファイルに子ブックマークを追加するには、まず親ブックマークを追加します。

1. ドキュメントを開きます。
1. [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) にブックマークを追加し、プロパティを定義します。
1. Document オブジェクトの [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクションに OutlineItemCollection を追加します。

子ブックマークは上記で説明した親ブックマークと同様に作成されますが、親ブックマークの Outlines コレクションに追加されます。

以下のコードスニペットは、PDF ドキュメントに子ブックマークを追加する方法を示しています。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create a parent bookmark object
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Parent Outline"
    outline.italic = True
    outline.bold = True

    # Create a child bookmark object
    childOutline = ap.OutlineItemCollection(document.outlines)
    childOutline.title = "Child Outline"
    childOutline.italic = True
    childOutline.bold = True

    # Add child bookmark in parent bookmark's collection
    outline.append(childOutline)
    # Add parent bookmark in the document's outline collection.
    document.outlines.append(outline)

    # Save output
    document.save(output_pdf)
```

## PDF ドキュメントからすべてのブックマークを削除する

PDF のすべてのブックマークは [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクションに格納されています。本記事では、PDF ファイルからすべてのブックマークを削除する方法を説明します。

PDF ファイルからすべてのブックマークを削除するには:

1. [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクションの Delete メソッドを呼び出します。
1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトの [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使用して変更されたファイルを保存します。

以下のコードスニペットは、PDF ドキュメントからすべてのブックマークを削除する方法を示しています。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete all bookmarks
    document.outlines.delete()

    # Save updated file
    document.save(output_pdf)

```

## PDF ドキュメントから特定のブックマークを削除する

PDF ファイルから特定のブックマークを削除するには:

1. ブックマークのタイトルをパラメータとして [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクションの Delete メソッドに渡します。
1. 次に、Document オブジェクトの Save メソッドで更新されたファイルを保存します。

[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスは [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクションを提供します。[delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) メソッドは、メソッドに渡されたタイトルを持つブックマークをすべて削除します。

以下のコードスニペットは、PDF ドキュメントから特定のブックマークを削除する方法を示しています。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete particular outline by Title
    document.outlines.delete("Child Outline")

    # Save updated file
    document.save(output_pdf)
```


