---
title: 在 Python 中获取、更新和展开 PDF 书签
linktitle: 获取、更新并展开书签
type: docs
weight: 20
url: /zh/python-net/get-update-and-expand-bookmark/
description: 了解如何使用 Python 检索、更新和展开 PDF 文档中的书签。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 在 PDF 中使用书签
Abstract: 本文提供了使用 Aspose.PDF 库在 Python 中管理 PDF 文档书签的完整指南。文章首先说明如何通过 `OutlineCollection` 检索 PDF 文件中的书签，该集合包含所有书签，并详细介绍通过 `OutlineItemCollection` 访问书签属性。接下来，文章描述了使用 `PdfBookmarkEditor` 确定书签对应页码的过程。随后，文章进一步解释了如何通过在每个 `OutlineItemCollection` 中检索子书签来处理层次结构书签。文章还涵盖了更新书签属性，演示如何修改书签属性并将更改保存到 PDF。最后，文章讨论了在查看文档时展开书签的需求，展示了如何设置每个书签的打开状态，以确保默认展开。每个部分都附有代码片段，提供实现这些功能的实际示例。
---

## 获取书签

这 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection 包含 PDF 文件的所有书签。本篇文章解释了如何从 PDF 文件获取书签，以及如何获取特定书签所在的页面。

要获取书签，遍历 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合，并在 OutlineItemCollection 中获取每个书签。 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 提供访问所有书签属性的功能。以下代码片段展示了如何从 PDF 文件中获取书签。

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

## 获取书签的页面编号

添加书签后，您可以通过获取与 Bookmark 对象关联的目标 PageNumber 来确定它所在的页码。

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

## 从 PDF 文档获取子书签

书签可以以层次结构组织，拥有父级和子级。要获取所有书签，遍历 Document 对象的 Outlines 集合。然而，要同时获取子书签，还需遍历每个在第一次循环中获得的对象的所有书签。 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 在第一次循环中获取的对象。以下代码片段展示了如何从 PDF 文档中获取子书签。

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

## 在 PDF 文档中更新书签

要更新 PDF 文件中的书签，首先通过指定书签的索引，从 Document 对象的 OutlineColletion 集合中获取特定书签。检索到书签后，将其 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 对象后，您可以更新其属性，然后使用 Save 方法保存更新后的 PDF 文件。以下代码片段展示了如何在 PDF 文档中更新书签。

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

## 在查看文档时展开书签

书签存放在 Document 对象的 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 集合本身在 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合。不过，我们可能需要在查看 PDF 文件时将所有书签展开。

为了实现此需求，我们可以将每个大纲/书签项的打开状态设置为 Open。下面的代码片段展示了如何在 PDF 文档中将每个书签的打开状态设置为展开。

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

## 相关书签主题

- [在 Python 中使用 PDF 书签](/pdf/zh/python-net/bookmarks/)
- [在 Python 中添加和删除 PDF 书签](/pdf/zh/python-net/add-and-delete-bookmark/)
- [使用 Python 在 PDF 中进行导航和交互](/pdf/zh/python-net/navigation-and-interaction/)

