---
title: 使用 Python 添加和删除书签
linktitle: 添加和删除书签
type: docs
weight: 10
url: /zh/python-net/add-and-delete-bookmark/
description: 您可以使用 Python 向 PDF 文档添加书签。也可以删除 PDF 文档中的所有书签或特定书签。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 添加和删除书签
Abstract: 本文提供了使用 Aspose.PDF Python 库管理 PDF 文档中书签的完整指南。它概述了在 PDF 中添加、修改和删除书签的流程。文章首先介绍通过创建 `OutlineItemCollection` 对象并将其追加到文档的 `OutlineCollection` 来添加书签的步骤。它包含展示父书签和子书签的创建与添加的代码示例，突出层级关系。此外，本文还介绍了删除所有书签或按标题删除特定书签的方法。每个章节都包含 Python 代码片段来说明这些操作，确保读者能够轻松地在 PDF 操作任务中实现这些功能。
---

## 向 PDF 文档添加书签

书签存储在 Document 对象的 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 集合中，而该集合本身位于 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合中。

向 PDF 添加书签：

1. 使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象打开 PDF 文档。
1. 创建书签并定义其属性。
1. 将 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 集合添加到 Outlines 集合中。

下面的代码片段展示了如何在 PDF 文档中添加书签。

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

## 向 PDF 文档添加子书签

书签可以嵌套，表示父子书签之间的层级关系。本文解释了如何向 PDF 添加子书签，即二级书签。

要向 PDF 文件添加子书签，首先添加父书签：

1. 打开文档。
1. 向 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 添加书签，并定义其属性。
1. 将 OutlineItemCollection 添加到 Document 对象的 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合中。

子书签的创建方式与上文所述的父书签相同，只是将其添加到父书签的 Outlines 集合中。

下面的代码片段展示了如何向 PDF 文档添加子书签。

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

## 删除 PDF 文档中的所有书签

PDF 中的所有书签都存储在 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合中。本文说明了如何删除 PDF 文件中的所有书签。

要删除 PDF 文件中的所有书签：

1. 调用 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合的 Delete 方法。
1. 使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法保存修改后的文件。

下面的代码片段展示了如何从 PDF 文档中删除所有书签。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete all bookmarks
    document.outlines.delete()

    # Save updated file
    document.save(output_pdf)

```

## 删除 PDF 文档中的特定书签

要删除 PDF 文件中的特定书签：

1. 将书签的标题作为参数传递给 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合的 Delete 方法。
1. 然后使用 Document 对象的 Save 方法保存更新后的文件。

The [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类提供了 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合。[delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) 方法会删除任何具有传入标题的书签。

下面的代码片段展示了如何从 PDF 文档中删除特定书签。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete particular outline by Title
    document.outlines.delete("Child Outline")

    # Save updated file
    document.save(output_pdf)
```


