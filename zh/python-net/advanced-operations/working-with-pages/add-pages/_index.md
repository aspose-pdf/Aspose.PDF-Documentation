---
title: 使用 Python 在 PDF 中添加页面
linktitle: 添加页面
type: docs
weight: 10
url: /zh/python-net/add-pages/
description: 了解如何使用 Aspose.PDF 在 Python 中向 PDF 文档添加页面，以实现灵活的文档创建和编辑。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 在 PDF 中添加页面
Abstract: 本文提供了使用 Aspose.PDF for Python via .NET API 操作 PDF 文档页面的指南。它强调了 API 所提供的灵活性，特别是通过 `PageCollection` 类来管理 PDF 中的所有页面。文档详细说明了在 PDF 文件的特定位置添加或插入页面的步骤。它概述了两种主要操作——在文档的指定位置插入空白页以及在文档末尾添加空白页。对于这两种操作，流程包括创建 `Document` 对象，使用 `PageCollection` 的 `insert` 或 `add` 方法，然后保存修改后的文档。文章还包含了演示这些任务的代码片段，展示了使用 Python 通过此 API 操作 PDF 文档的简便性。
---

Aspose.PDF for Python via .NET API 为使用 Python 操作 PDF 文档页面提供了完全的灵活性。它将 PDF 文档的所有页面保存在 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 中，可用于处理 PDF 页面。
Aspose.PDF for Python via .NET 允许您在文件的任意位置向 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 插入页面，也可以在 PDF 文件末尾添加页面。本节展示了如何使用 Python 向 PDF 添加页面。

## 在 PDF 文件中添加或插入页面

Aspose.PDF for Python via .NET 允许您在文件的任意位置向 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 插入页面，也可以在 PDF 文件的末尾添加页面。

### 在 PDF 文件中插入空白页

在 PDF 文件中插入空白页的方法如下：

1. 使用适当的方法打开已有的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 使用 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 的 `insert()` 方法在特定索引处插入新空白页。
1. 将修改后的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 保存到所需的输出路径。

在指定位置向现有 PDF 文件插入空白页：

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def insert_empty_page(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### 在 PDF 文件末尾添加空白页

有时，您希望文档以空白页结束。本主题说明如何在 PDF 文档末尾插入空白页。

在 PDF 文件末尾插入空白页的步骤如下：

1. 使用适当的方法打开已有的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 使用 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 的 `add()` 方法在文档末尾添加新空白页。
1. 保存更新后的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。

以下代码片段展示了如何在 PDF 文件末尾插入空白页。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_empty_page_to_end(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Insert an empty page at the end of a PDF file
    document.pages.add()

    # Save output file
    document.save(output_file_name)
```

### 从另一个 PDF 文档中添加页面

使用 Aspose.PDF for Python 库，您可以创建一个新的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)，添加一个初始页面，然后从另一个 PDF 导入页面到该文档中。

1. 创建一个新的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 添加一个新的空白 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)，并使用 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) 在其上写入一些文字。
1. 打开另一个已有的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 从该文档复制一个 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)。
1. 使用 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 将复制的页面粘贴到您的主文档中。
1. 保存合并后的文件。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_from_another_document(input_file_name, output_file_name):
    # Open document
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    # Save output file
    document.save(output_file_name)
```
