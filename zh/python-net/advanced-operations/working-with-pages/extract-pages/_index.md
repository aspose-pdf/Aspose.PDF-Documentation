---
title: 在 Python 中提取 PDF 页面
linktitle: 提取 PDF 页面
type: docs
weight: 80
url: /zh/python-net/extract-pages/
description: 了解如何在 Python 中将单个或多个 PDF 页面提取到新文件中。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 提取 PDF 页面
Abstract: 本文解释了如何使用 Aspose.PDF for Python via .NET 从 PDF 文件中提取页面。了解如何通过使用基于 1 的页面索引和 PageCollection API 将单个页面或多个页面复制到新文档中。
---

## 从 PDF 中提取单个页面

从 PDF 文档中提取特定页面并将其保存为新文件。使用 Aspose.PDF 库，脚本将所需页面复制到一个新的 PDF 中，保持原始文档不变。这对于拆分 PDF 或提取重要页面进行分发非常有用。

1. 使用以下方式加载源 PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. 创建一个新 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 用于保存提取的页面。
1. 添加所需的 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 从源文档到新 PDF，使用目标文档的 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (`dst_document.pages.add(...)`).
    - 在此示例中，提取第 2 页（基于 1 的索引）。
1. 保存新的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 将提取的页面保存到指定的输出文件中。

```python
import aspose.pdf as ap

def extract_page(input_file_name: str, output_file_name: str) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    dst_document.pages.add(src_document.pages[2])
    dst_document.save(output_file_name)
```

## 提取 PDF 的多个页面

从 PDF 文档中提取多个特定页面并将其保存到新文件中。使用 Aspose.PDF 库，所选页面会被复制到新的 PDF 中，同时保持原始文档不变。这对于创建仅包含较大文档中相关部分的更小 PDF 非常有用。

1. 使用以下方式加载源 PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. 创建一个新 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 用于保存提取的页面。
1. 选择要提取的页面（在本例中，使用基于1的索引选择第2页和第3页）。
1. 添加每个已选择的 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 从源文档到新PDF，使用其 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 保存新的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 将提取的页面写入指定的输出文件。

```python
import aspose.pdf as ap

def extract_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    pages = [2, 3]
    another_document = ap.Document()
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    another_document.save(output_file_name)
```

## 相关页面主题

- [在 Python 中处理 PDF 页面](/pdf/zh/python-net/working-with-pages/)
- [在 Python 中删除 PDF 页面](/pdf/zh/python-net/delete-pages/)
- [在 Python 中移动 PDF 页面](/pdf/zh/python-net/move-pages/)
- [在 Python 中拆分 PDF 文件](/pdf/zh/python-net/split-document/)
