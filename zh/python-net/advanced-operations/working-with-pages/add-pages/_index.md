---
title: 在 Python 中添加 PDF 页面
linktitle: 添加页面
type: docs
weight: 10
url: /zh/python-net/add-pages/
description: 了解如何在 Python 中向 PDF 文档添加或插入页面。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 添加或插入 PDF 页面
Abstract: 本文解释了如何使用 Aspose.PDF for Python via .NET 向 PDF 文件添加页面。了解如何在特定位置插入空白页、在文档末尾追加页面，以及使用 Document 和 PageCollection API 从另一个 PDF 导入页面。
---

Aspose.PDF for Python via .NET 为 PDF 文档提供灵活的页面级操作。您可以通过 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 并向 a 添加页面 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 在特定位置或文件末尾。

在生成工作流中需要向现有 PDF 插入新的空白页或在文档末尾追加页面时，请使用此页面。

## 在 PDF 文件中添加或插入页面

Aspose.PDF for Python via .NET 支持在特定索引处插入页面以及在 PDF 末尾追加页面。

### 在 PDF 文件中插入空白页

在 PDF 文件中插入空白页：

1. 打开现有的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 使用适当的方法。
1. 使用该在特定索引处插入新的空白页 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `insert()` 方法。
1. 保存已修改的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 到所需的输出路径。

在指定位置向现有 PDF 文件插入一个空白页：

```python
import aspose.pdf as ap

def insert_empty_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### 在 PDF 文件末尾添加空白页

有时，您希望确保文档以空白页结束。本主题说明如何在 PDF 文档的末尾插入空白页。

要在 PDF 文件的末尾插入一个空白页：

1. 打开现有的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 使用适当的方法。
1. 使用以下方式在文档末尾添加一个新空白页 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `add()` 方法。
1. 保存已更新的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

以下代码片段向您展示如何在 PDF 文件的末尾插入一个空白页。

```python
import aspose.pdf as ap

def add_empty_page_to_end(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.add()
    document.save(output_file_name)
```

### 从另一个 PDF 文档添加页面

使用 Aspose.PDF for Python via .NET，您可以创建一个新的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)，添加一个初始页面，然后将另一个 PDF 的页面导入其中。

1. 创建一个新 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 添加一个新的空白 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 并使用它在其上写入一些文本 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/).
1. 打开另一个现有的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 复制一个 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 从该文档。
1. 使用 将复制的页面粘贴到您的主文档中 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 保存合并后的文件。

```python
import aspose.pdf as ap

def add_page_from_another_document(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    document.save(output_file_name)
```

## 相关页面主题

- [在 Python 中处理 PDF 页面](/pdf/zh/python-net/working-with-pages/)
- [在 Python 中移动 PDF 页面](/pdf/zh/python-net/move-pages/)
- [在 Python 中删除 PDF 页面](/pdf/zh/python-net/delete-pages/)
- [在 Python 中提取 PDF 页面](/pdf/zh/python-net/extract-pages/)
