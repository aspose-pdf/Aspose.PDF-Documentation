---
title: 使用 Python 获取、更新和展开书签
linktitle: 获取、更新和展开书签
type: docs
weight: 20
url: /zh/python-net/get-update-and-expand-bookmark/
description: 本文介绍了如何使用我们的 Aspose.PDF for Python 库在 PDF 文件中使用书签。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何在 PDF 中使用 Python 书签
Abstract: 本文提供了使用 Aspose.PDF 库在 Python 中管理 PDF 文档书签的全面指南。文章首先说明如何通过 `OutlineCollection` 检索 PDF 文件中的书签，该集合包含所有书签，并详细介绍通过 `OutlineItemCollection` 访问书签属性。随后描述了使用 `PdfBookmarkEditor` 确定书签对应页码的过程。进一步解释了如何通过在每个 `OutlineItemCollection` 中检索子书签来处理层级书签结构。文章还涵盖了更新书签属性，演示如何修改书签属性并将更改保存到 PDF。最后，文章讨论了在查看文档时展开书签的需求，展示如何设置每个书签的打开状态以默认展开。每个章节均附有代码片段，提供实现这些功能的实用示例。
---

## 获取书签

[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合包含 PDF 文件的所有书签。本文解释了如何从 PDF 文件获取书签，以及如何获取特定书签所在的页码。

要获取书签，遍历 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合并在 OutlineItemCollection 中获取每个书签。[OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 提供了对书签所有属性的访问。以下代码片段展示了如何从 PDF 文件获取书签。

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

## 获取书签的页码

添加书签后，您可以通过获取与 Bookmark 对象关联的目标 PageNumber 来确定其所在页码。

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

## 从 PDF 文档获取子书签

书签可以组织成层级结构，包含父子关系。要获取所有书签，遍历 Document 对象的 Outlines 集合。然而，要同时获取子书签，还需要遍历第一次循环中获取的每个 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 对象中的所有书签。以下代码片段展示了如何从 PDF 文档获取子书签。

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

## 更新 PDF 文档中的书签

要更新 PDF 文件中的书签，首先通过指定书签索引从 Document 对象的 OutlineCollection 集合中获取相应书签。检索到书签后，将其放入 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 对象中，您可以更新其属性，然后使用 Save 方法保存更新后的 PDF 文件。以下代码片段展示了如何在 PDF 文档中更新书签。

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

## 查看文档时展开书签

书签存放在 Document 对象的 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 集合中，该集合本身位于 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合中。然而，可能需要在查看 PDF 文件时将所有书签展开。

为实现此需求，我们可以将每个大纲/书签项的打开状态设置为 Open。以下代码片段展示了如何在 PDF 文档中将每个书签的打开状态设为展开。

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


