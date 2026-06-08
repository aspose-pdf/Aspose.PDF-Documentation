---
title: 在 Python 中移动 PDF 页面
linktitle: 移动 PDF 页面
type: docs
weight: 100
url: /zh/python-net/move-pages/
description: 了解如何在 Python 中在文档内部或在文档之间移动 PDF 页面。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中在文档之间移动 PDF 页面
Abstract: 本文介绍了如何使用 Aspose.PDF for Python via .NET 在 PDF 中移动页面。了解如何将单个页面或多个页面移动到另一个文档，以及如何使用 Document 和 PageCollection API 在同一 PDF 中重新定位页面。
---

## 将页面从一个 PDF 文档移动到另一个

Aspose.PDF for Python 允许您将页面（而不仅仅是复制）从一个 PDF 移动到另一个。它会从原始文档中删除所选页面，然后将其添加到新的 PDF 文件中。

可以把它想象成把一本书中的页面剪下来粘到另一本书上——移动后该页面在原文件中不再存在。

1. 使用 ... 打开源 PDF 文档 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类。
1. 选择要移动的特定页面（在本例中，第 2 页）— 这指的是 a [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. 创建新的 PDF 文档（实例化另一个 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. 使用目标文档的 将选定的页面添加到新 PDF 文档中 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) （例如， `another_document.pages.add(page)`).
1. 通过其从原始文档中删除页面 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) （例如， `document.pages.delete(index)`).
1. 保存两个文档。

以下代码片段向您展示如何移动一页。

```python
import aspose.pdf as ap

def move_page_from_one_document_to_another(
    input_file_name: str, output_file_name: str
) -> None:

    document = ap.Document(input_file_name)
    page = document.pages[2]
    another_document = ap.Document()
    another_document.pages.add(page)
    document.pages.delete(2)
    document.save(input_file_name.replace(".pdf", "_new.pdf"))
    another_document.save(output_file_name)
```

## 将多个页面从一个 PDF 文档移动到另一个 PDF 文档

与复制不同，此操作会转移所选页面——将它们从源文件中移除并保存到一个新的 PDF 中。

1. 创建一个新的、空的目标文档 ("`Document`).
1. 从源文档中选择多个页面（在本例中为第 1 页和第 3 页） [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 遍历所选页面并将每个页面添加到目标文档中 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 保存包含已移动页面的目标文档。
1. 使用其从源文档中删除已移动的页面。 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 使用新文件名保存已修改的源文档，以保留两个版本。

下面的代码片段展示了如何移动多个页面。

```python
import aspose.pdf as ap

def move_multiple_pages_from_one_document_to_another(
    input_file_name: str, output_file_name: str
) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    pages = [1, 2]
    for page_index in pages:
        page = src_document.pages[page_index]
        dst_document.pages.add(page)
    # Save output files
    dst_document.save(output_file_name)
    src_document.pages.delete(pages)
    src_document.save(input_file_name.replace(".pdf", "_new.pdf"))
```

## 在同一 PDF 文档中将页面移动到新位置

它展示了如何在同一文档中将特定页面移动到不同位置——在重新组织或编辑 PDF 布局时的常见需求。

1. 使用以下方法加载输入 PDF 文档 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类。
1. 选择要移动的页面（第 2 页）——这是一 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. 使用文档的…将其添加到文档末尾 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 通过以下方式从其先前位置删除原始页面 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 将修改后的文档另存为新文件。

```python
import aspose.pdf as ap

def move_page_in_new_location_in_same_document(
    input_file_name: str, output_file_name: str
) -> None:
    src_document = ap.Document(input_file_name)

    page = src_document.pages[2]
    src_document.pages.add(page)
    src_document.pages.delete(2)

    # Save output file
    src_document.save(output_file_name)
```

## 相关页面主题

- [在 Python 中处理 PDF 页面](/pdf/zh/python-net/working-with-pages/)
- [在 Python 中添加 PDF 页面](/pdf/zh/python-net/add-pages/)
- [在 Python 中删除 PDF 页面](/pdf/zh/python-net/delete-pages/)
- [在 Python 中提取 PDF 页面](/pdf/zh/python-net/extract-pages/)
