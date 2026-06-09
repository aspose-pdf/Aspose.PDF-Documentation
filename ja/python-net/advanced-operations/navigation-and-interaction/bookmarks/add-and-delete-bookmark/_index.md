---
title: Python での PDF ブックマークの追加と削除
linktitle: ブックマークを追加する/削除する
type: docs
weight: 10
url: /ja/python-net/add-and-delete-bookmark/
description: Python を使用して PDF 文書にブックマークを追加および削除する方法を学びます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用してブックマークを追加および削除する方法
Abstract: この記事では、Python 用 Aspose.PDF ライブラリを使用して PDF ドキュメント内のブックマークを管理する方法を包括的に説明します。PDF 内のブックマークを追加、変更、削除するプロセスの概要を説明します。この記事の冒頭では、「OutlineItemCollection」オブジェクトを作成し、それをドキュメントの「OutlineCollection」に追加することでブックマークを追加する方法について説明します。親ブックマークと子ブックマークの両方の作成と追加を示すコード例が含まれており、階層関係が強調されています。さらに、この記事ではすべてのブックマークまたは特定のブックマークをタイトルごとに削除する方法についても説明しています。各セクションには操作を説明する Python コードスニペットが含まれており、読者が説明した機能を PDF 操作タスクに簡単に実装できるようになっています。
---

## PDF ドキュメントへのブックマークの追加

ブックマークは Document オブジェクトに保持されます [アウトラインアイテムコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) コレクション自体は [アウトラインコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクション。

PDF にブックマークを追加するには:

1. を使用して PDF ドキュメントを開く [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 対象。
1. ブックマークを作成し、そのプロパティを定義します。
1. を追加 [アウトラインアイテムコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) コレクションをアウトラインコレクションに追加します。

次のコードスニペットは、PDF ドキュメントにブックマークを追加する方法を示しています。

```python
import aspose.pdf as ap
import sys
from os import path

def add_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Create a bookmark object
    pdf_outline = ap.OutlineItemCollection(document.outlines)
    pdf_outline.title = "Test Outline"
    pdf_outline.italic = True
    pdf_outline.bold = True

    # Set the destination page number
    pdf_outline.action = ap.annotations.GoToAction(document.pages[1])

    # Add bookmark to the document's outline collection
    outlines = document.outlines
    outlines.append(pdf_outline)

    # Save PDF document
    document.save(outfile)
```

## PDF ドキュメントに子ブックマークを追加

ブックマークはネストでき、親ブックマークと子ブックマークとの階層関係を示します。この記事では、子ブックマーク、つまりセカンドレベルのブックマークを PDF に追加する方法について説明します。

PDF ファイルに子ブックマークを追加するには、まず親ブックマークを追加します。

1. 文書を開きます。
1. にブックマークを追加 [アウトラインアイテムコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/)、そのプロパティを定義します。
1. OutlineItemコレクションをドキュメントオブジェクトに追加します [アウトラインコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクション。

子ブックマークは、上で説明した親ブックマークと同じように作成されますが、親ブックマークの Outlines コレクションに追加されます。

次のコードスニペットは、PDF ドキュメントに子ブックマークを追加する方法を示しています。

```python
import aspose.pdf as ap
import sys
from os import path

def add_child_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Create a parent bookmark object
    pdf_outline = ap.OutlineItemCollection(document.outlines)
    pdf_outline.title = "Parent Outline"
    pdf_outline.italic = True
    pdf_outline.bold = True

    # Create a child bookmark object
    pdf_child_outline = ap.OutlineItemCollection(document.outlines)
    pdf_child_outline.title = "Child Outline"
    pdf_child_outline.italic = True
    pdf_child_outline.bold = True

    # Add child bookmark to parent bookmark's collection
    pdf_outline.append(pdf_child_outline)

    # Add parent bookmark to the document's outline collection
    document.outlines.append(pdf_outline)

    # Save PDF document
    document.save(outfile)
```

## PDF ドキュメントからすべてのブックマークを削除する

PDF 内のすべてのブックマークは、次の場所に保持されます。 [アウトラインコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクション。この記事では、PDF ファイルからすべてのブックマークを削除する方法について説明します。

PDF ファイルからすべてのブックマークを削除するには:

1. に電話してください [アウトラインコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクションの Delete メソッド。
1. を使用して変更したファイルを保存します [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトの [保存 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。

次のコードスニペットは、PDF ドキュメントからすべてのブックマークを削除する方法を示しています。

```python
import aspose.pdf as ap
import sys
from os import path

def delete_bookmarks(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Delete all bookmarks in the PDF document
    document.outlines.delete()

    # Save PDF document
    document.save(outfile)
```

## PDF ドキュメントから特定のブックマークを削除する

PDF ファイルから特定のブックマークを削除するには：

1. ブックマークのタイトルをパラメータとしてに渡します [アウトラインコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクションの Delete メソッド。
1. 次に、更新したファイルを Document オブジェクトの Save メソッドで保存します。

ザの [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 「クラス」が提供するのは [アウトラインコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクション。ザル [削除 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) メソッドは、メソッドに渡されたタイトルのブックマークをすべて削除します。

次のコードスニペットは、PDF ドキュメントから特定のブックマークを削除する方法を示しています。

```python
import aspose.pdf as ap
import sys
from os import path

def delete_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Delete a specific bookmark by title.
    # Note: If multiple bookmarks have the same title, only the first matching bookmark will be deleted.
    document.outlines.delete("Child Outline")

    # Save PDF document
    document.save(outfile)
```

## 関連ブックマークトピック

- [Python で PDF ブックマークを操作する](/pdf/ja/python-net/bookmarks/)
- [Python で PDF ブックマークを取得、更新、拡張する方法](/pdf/ja/python-net/get-update-and-expand-bookmark/)
- [Python を使用した PDF でのナビゲーションとインタラクション](/pdf/ja/python-net/navigation-and-interaction/)

