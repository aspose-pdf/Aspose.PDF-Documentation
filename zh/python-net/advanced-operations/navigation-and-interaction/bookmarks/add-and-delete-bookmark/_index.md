---
title: 在 Python 中添加和删除 PDF 书签
linktitle: 添加和删除书签
type: docs
weight: 10
url: /zh/python-net/add-and-delete-bookmark/
description: 了解如何使用 Python 在 PDF 文档中添加和删除书签。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 添加和删除书签
Abstract: 本文提供了使用 Aspose.PDF library for Python 在 PDF 文档中管理书签的完整指南。它概述了在 PDF 中添加、修改和删除书签的流程。文章首先通过创建 `OutlineItemCollection` 对象并将其追加到文档的 `OutlineCollection` 来介绍如何添加书签。文中包含代码示例，演示了父书签和子书签的创建与添加，突出层级关系。此外，本文还介绍了删除所有书签或按标题删除特定书签的方法。每个章节都包含 Python 代码片段，以便读者能够轻松在其 PDF 操作任务中实现所描述的功能。
---

## 在 PDF 文档中添加书签

书签存放在 Document 对象的 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 集合本身在 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合。

要向 PDF 添加书签：

1. 使用打开 PDF 文档 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象。
1. 创建书签并定义其属性。
1. 添加 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 集合到 Outlines 集合。

下面的代码片段展示了如何在 PDF 文档中添加书签。

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

## 向 PDF 文档添加子书签

书签可以嵌套，表示父书签和子书签之间的层级关系。本文说明了如何向 PDF 添加子书签，即二级书签。

要向 PDF 文件添加子书签，首先添加父书签：

1. 打开文档。
1. 将书签添加到 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/)，定义其属性。
1. 将 OutlineItemCollection 添加到 Document 对象的 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合。

子书签的创建方式与上文解释的父书签相同，但它被添加到父书签的 Outlines 集合中

以下代码片段展示了如何向 PDF 文档添加子书签。

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

## 删除 PDF 文档中的所有书签

PDF 中的所有书签都存储在 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合中。本篇文章解释如何从 PDF 文件中删除所有书签。

要从 PDF 文件中删除所有书签：

1. 调用 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection 的 Delete 方法。
1. 使用以下方式保存已修改的文件 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。

以下代码片段展示了如何从 PDF 文档中删除所有书签。

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

## 删除 PDF 文档中的特定书签

要从 PDF 文件中删除特定书签，请：

1. 将书签的标题作为参数传递给 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection 的 Delete 方法。
1. 然后使用 Document 对象的 Save 方法保存更新后的文件。

这 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class’ 提供了 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合。The [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) method 删除传递给该方法的标题的任何书签。

以下代码片段展示了如何从 PDF 文档中删除特定的书签。

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

## 相关书签主题

- [在 Python 中使用 PDF 书签](/pdf/zh/python-net/bookmarks/)
- [在 Python 中获取、更新和展开 PDF 书签](/pdf/zh/python-net/get-update-and-expand-bookmark/)
- [使用 Python 在 PDF 中进行导航和交互](/pdf/zh/python-net/navigation-and-interaction/)

