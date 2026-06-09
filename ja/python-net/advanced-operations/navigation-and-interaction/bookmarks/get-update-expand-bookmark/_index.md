---
title: Python で PDF ブックマークを取得、更新、および展開する方法
linktitle: ブックマークを取得、更新、拡張する
type: docs
weight: 20
url: /ja/python-net/get-update-and-expand-bookmark/
description: Python を使用して PDF 文書内のブックマークを取得、更新、および展開する方法について説明します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF のブックマークを使用する方法
Abstract: この記事では、Python の Aspose.PDF ライブラリを使用して PDF ドキュメント内のブックマークを管理するための包括的なガイドを提供します。最初に、すべてのブックマークを含む「OutlineCollection」を使用して PDF ファイルからブックマークを取得する方法と、「OutlineItemCollection」を介してブックマーク属性にアクセスする方法について詳しく説明します。次に、「PDFBookmarkEditor」を使用してブックマークに関連するページ番号を決定するプロセスについて説明します。さらに、各「OutlineItemCollection」内の子ブックマークを取得して階層的なブックマーク構造を処理する方法についても説明します。また、ブックマークのプロパティの更新についても説明し、ブックマークの属性を変更して PDF に変更を保存する方法についても説明します。最後に、文書を表示するときにブックマークを拡張する必要があることについて説明し、各ブックマークのオープンステータスを設定してデフォルトで展開されるようにする方法を示します。各セクションにはコードスニペットが付属しており、これらの機能を実装する実際的な例が示されています。
---

## ブックマークを取得

ザの [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトの [アウトラインコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクションには、PDF ファイルのすべてのブックマークが含まれます。この記事では、PDF ファイルからブックマークを取得する方法と、特定のブックマークがどのページにあるかを取得する方法について説明します。

ブックマークを取得するには、ループ処理を行います [アウトラインコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクションを作成し、OutlineItemコレクションの各ブックマークを取得します。は [アウトラインアイテムコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) ブックマークのすべての属性にアクセスできます。次のコードスニペットは、PDF ファイルからブックマークを取得する方法を示しています。

```python
from os import path
import sys
import aspose.pdf as ap

def get_bookmarks(input_pdf):
    document = ap.Document(input_pdf)
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```

## ブックマークのページ番号の取得

ブックマークを追加したら、Bookmark オブジェクトに関連付けられている保存先の PageNumber を取得することで、そのブックマークがどのページにあるかを確認できます。

```python
from os import path
import sys
import aspose.pdf as ap

def get_bookmark_page_number(input_pdf):
    # Create PdfBookmarkEditor
    bookmark_editor = ap.facades.PdfBookmarkEditor()
    # Open PDF file
    bookmark_editor.bind_pdf(input_pdf)
    # Extract bookmarks
    bookmarks = bookmark_editor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_separator = ""
        for i in range(bookmark.level):
            str_level_separator += "----"

        print(str_level_separator, "Title:", bookmark.title)
        print(str_level_separator, "Page Number:", bookmark.page_number)
        print(str_level_separator, "Page Action:", bookmark.action)
```

## PDF ドキュメントから子ブックマークを取得

ブックマークは、親子で階層構造に整理できます。すべてのブックマークを取得するには、Document オブジェクトの Outlines コレクションをループ処理します。ただし、子ブックマークも取得するには、それぞれのすべてのブックマークをループ処理してください。 [アウトラインアイテムコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 最初のループで取得したオブジェクト。以下のコードスニペットは、PDF ドキュメントから子ブックマークを取得する方法を示しています。

```python
from os import path
import sys
import aspose.pdf as ap

def get_child_bookmarks(input_pdf):
    document = ap.Document(input_pdf)
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
                child_outline_item = outline_item[j + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## PDF ドキュメント内のブックマークの更新

PDF ファイル内のブックマークを更新するには、まず、ブックマークのインデックスを指定して、Document オブジェクトの OutlineColletion コレクションから特定のブックマークを取得します。ブックマークをに取得したら [アウトラインアイテムコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) オブジェクトの場合、そのプロパティを更新し、更新された PDF ファイルを Save メソッドを使用して保存できます。次のコードスニペットは、PDF ドキュメント内のブックマークを更新する方法を示しています。

```python
from os import path
import sys
import aspose.pdf as ap

def update_bookmarks(input_pdf, output_pdf):
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

## ドキュメント表示時の拡張ブックマーク

ブックマークは Document オブジェクトに保持されます [アウトラインアイテムコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) コレクション自体は [アウトラインコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクション。ただし、PDF ファイルを表示する場合、すべてのブックマークを展開する必要がある場合があります。

この要件を満たすために、各アウトライン/ブックマークアイテムのオープンステータスを「オープン」に設定できます。次のコードスニペットは、PDF 文書内で展開された各ブックマークのオープンステータスを設定する方法を示しています。

```python
from os import path
import sys
import aspose.pdf as ap

def expanded_bookmarks(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.page_mode = ap.PageMode.USE_OUTLINES
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        item.open = True
    document.save(output_pdf)
```

## 関連ブックマークトピック

- [Python で PDF ブックマークを操作する](/pdf/ja/python-net/bookmarks/)
- [Python で PDF ブックマークを追加および削除する方法](/pdf/ja/python-net/add-and-delete-bookmark/)
- [Python を使用した PDF でのナビゲーションとインタラクション](/pdf/ja/python-net/navigation-and-interaction/)

