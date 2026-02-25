---
title: 通过 Python 编程移动 PDF 页面
linktitle: 移动 PDF 页面
type: docs
weight: 100
url: /zh/python-net/move-pages/
description: 尝试使用 Aspose.PDF for Python via .NET 将页面移动到 PDF 文件的指定位置或文件末尾。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 在 PDF 文档之间移动页面
Abstract: 本文提供了使用 Python（特别是利用 Aspose.PDF 库）在 PDF 文档之间或在单个 PDF 文档内部移动页面的全面指南。它概述了三种情景的逐步流程——将单页从一个 PDF 移动到另一个 PDF、转移多页以及在同一文档中重新定位页面。每种情景都涉及为源和目标 PDF 创建 `Document` 类对象，通过 `PageCollection` 类操作页面，并使用 `add`、`delete` 和 `save` 方法实现所需的页面重组。文中提供了代码片段以供实际实现，演示如何使用 Python 脚本高效地移动页面。
---

## 将页面从一个 PDF 文档移动到另一个

Aspose.PDF for Python 允许您将页面（不仅仅是复制）从一个 PDF 移动到另一个 PDF。它会从原始文档中移除所选页面，然后将其添加到新的 PDF 文件中。

可以把它想象成从一本书中剪下页面并粘贴到另一本书——移动后该页面在原文件中不再存在。

1. 使用 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类打开源 PDF 文档。
1. 选择要移动的特定页面（此例中为第 2 页）——这指的是一个 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)。
1. 创建一个新的 PDF 文档（实例化另一个 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)）。
1. 使用目标文档的 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 将选定页面添加到新 PDF 文档中（例如，`another_document.pages.add(page)`）。
1. 通过原文档的 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 删除该页面（例如，`document.pages.delete(index)`）。
1. 保存两个文档。

下面的代码片段演示了如何移动单页。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_page_from_one_document_to_another(input_file_name, output_file_name):
    """
    Move a single page from one PDF document to another.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file after moving the page.
    """
    document = ap.Document(input_file_name)
    page = document.pages[2]
    another_document = ap.Document()
    another_document.pages.add(page)
    document.pages.delete(2)
    document.save(input_file_name.replace(".pdf","_new.pdf"))
    another_document.save(output_file_name)
```

## 将一批页面从一个 PDF 文档移动到另一个

与复制不同，此操作会转移所选页面——从源文件中删除并保存到新的 PDF 中。

1. 创建一个新的空目标文档（`Document`）。
1. 从源文档的 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 中选择多个页面（此例中为第 1 页和第 3 页）。
1. 循环遍历选定的页面，并将每个页面添加到目标文档的 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 中。
1. 保存包含已移动页面的目标文档。
1. 使用其 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 从源文档中删除已移动的页面。
1. 以新文件名保存修改后的源文档，以保留两个版本。

下面的代码片段展示了如何在 PDF 文件末尾插入一个空白页面。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_bunch_pages_from_one_document_to_another(input_file_name, output_file_name):
    """
    Move a set of pages from one PDF document to another.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file where selected pages will be saved.
    """
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = src_document.pages[page_index]
        dst_document.pages.add(page)
    # Save output files
    dst_document.save(output_file_name)
    src_document.pages.delete(pages)
    src_document.save(input_file_name.replace(".pdf","_new.pdf"))
```

## 在当前 PDF 文档中将页面移动到新位置

它展示了如何将特定页面移动到同一文档中的不同位置——在重新组织或编辑 PDF 布局时的常见需求。

1. 使用 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类加载输入 PDF 文档。
1. 选择要移动的页面（第 2 页）——这是一​​个 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)。
1. 使用文档的 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 将其添加到文档末尾。
1. 通过 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 从其原位置删除原始页面。
1. 将修改后的文档另存为新文件。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_page_in_new_location_in_same_document(input_file_name, output_file_name):
    """
    Move a page to a new location within the same PDF document.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file after moving the page.
    """
    srcDocument = ap.Document(input_file_name)

    page = srcDocument.pages[2]
    srcDocument.pages.add(page)
    srcDocument.pages.delete(2)

    # Save output file
    srcDocument.save(output_file_name)
```


