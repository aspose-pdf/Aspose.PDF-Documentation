---
title: Python を使用したブックマークの取得、更新、展開
linktitle: ブックマークの取得、更新、展開
type: docs
weight: 20
url: /ja/python-net/get-update-and-expand-bookmark/
description: この記事では、Aspose.PDF for Python ライブラリを使用して PDF ファイルのブックマークを使用する方法について説明します。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF のブックマークを使用する方法
Abstract: この記事では、Python の Aspose.PDF ライブラリを使用して PDF ドキュメント内のブックマークを管理するための包括的なガイドを提供します。まず、すべてのブックマークを含む `OutlineCollection` を介して PDF ファイルからブックマークを取得する方法を説明し、`OutlineItemCollection` を利用したブックマーク属性へのアクセス方法を詳しく解説します。その後、`PdfBookmarkEditor` を使用してブックマークに関連付けられたページ番号を取得する手順を紹介します。さらに、各 `OutlineItemCollection` 内の子ブックマークを取得することで階層的なブックマーク構造を処理する方法を説明します。また、ブックマークのプロパティを更新する方法についても取り上げ、ブックマーク属性を変更し PDF に変更を保存する方法を示します。最後に、文書を表示する際にブックマークを展開する必要性に対処し、各ブックマークの開閉ステータスを設定してデフォルトで展開されるようにする方法を示します。各セクションにはコードスニペットが付随しており、これらの機能を実装する実用的な例を提供しています。
---

## ブックマークの取得

The [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトの [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクションには、PDF ファイルのすべてのブックマークが含まれています。この記事では、PDF ファイルからブックマークを取得する方法と、特定のブックマークがどのページにあるかを取得する方法を説明します。

ブックマークを取得するには、[OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクションをループして OutlineItemCollection 内の各ブックマークを取得します。[OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) はブックマークのすべての属性へのアクセスを提供します。以下のコードスニペットは、PDF ファイルからブックマークを取得する方法を示しています。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Loop through all the bookmarks
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```

## ブックマークのページ番号の取得

ブックマークを追加したら、Bookmark オブジェクトに関連付けられた目的地の PageNumber を取得することで、そのブックマークがあるページを確認できます。

```python

    import aspose.pdf as ap

    # Create PdfBookmarkEditor
    bookmarkEditor = ap.facades.PdfBookmarkEditor()
    # Open PDF file
    bookmarkEditor.bind_pdf(input_pdf)
    # Extract bookmarks
    bookmarks = bookmarkEditor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_seprator = ""
        for i in range(bookmark.level):
            str_level_seprator += "----"

        print(str_level_seprator, "Title:", bookmark.title)
        print(str_level_seprator, "Page Number:", bookmark.page_number)
        print(str_level_seprator, "Page Action:", bookmark.action)
```

## PDF ドキュメントから子ブックマークを取得する

ブックマークは親子関係の階層構造で整理できます。すべてのブックマークを取得するには、Document オブジェクトの Outlines コレクションをループします。ただし、子ブックマークも取得するには、最初のループで取得した各 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) オブジェクト内のすべてのブックマークもループします。以下のコードスニペットは、PDF ドキュメントから子ブックマークを取得する方法を示しています。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Loop through all the bookmarks
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
        count = len(outline_item)
        if count > 0:
            print("Child Bookmarks")
            # There are child bookmarks then loop through that as well
            for j in range(len(outline_item)):
                child_outline_item = outline_item[i + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## PDF ドキュメントでブックマークを更新する

PDF ファイルでブックマークを更新するには、まず Document オブジェクトの OutlineCollection コレクションからブックマークのインデックスを指定して対象のブックマークを取得します。ブックマークを [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) オブジェクトに取得したら、そのプロパティを更新し、Save メソッドを使用して更新された PDF ファイルを保存できます。以下のコードスニペットは、PDF ドキュメントでブックマークを更新する方法を示しています。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Get a bookmark object
    outline = document.outlines[1]

    # Get child bookmark object
    child_outline = outline[1]
    child_outline.title = "Updated Outline"
    child_outline.italic = True
    child_outline.bold = True

    # Save output
    document.save(output_pdf)
```

## ドキュメント表示時のブックマーク展開

ブックマークは Document オブジェクトの [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) コレクションに格納されており、さらに [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクションに含まれています。ただし、PDF ファイルを表示する際にすべてのブックマークを展開する必要がある場合があります。

この要件を実現するために、各アウトライン/ブックマーク項目の開閉ステータスを Open に設定できます。以下のコードスニペットは、PDF ドキュメントで各ブックマークを展開された状態に設定する方法を示しています。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Set page view mode i.e. show thumbnails, full-screen, show attachment panel
    document.page_mode = ap.PageMode.USE_OUTLINES
    # Traverse through each Ouline item in outlines collection of PDF file
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        # Set open status for outline item
        item.open = True

    # Save output
    document.save(output_pdf)
```


