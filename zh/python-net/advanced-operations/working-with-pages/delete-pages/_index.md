---
title: 在 Python 中删除 PDF 页面
linktitle: 删除 PDF 页面
type: docs
weight: 80
url: /zh/python-net/delete-pages/
description: 了解如何在 Python 中删除 PDF 文件的页面。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中删除一个或多个 PDF 页面
Abstract: 本文解释了如何使用 Aspose.PDF for Python via .NET 从 PDF 文件中删除页面。了解如何通过使用 PageCollection API 删除文档中的单个页面或多个页面，然后保存更新后的 PDF。
---

您可以使用 Aspose.PDF for Python via .NET 删除 PDF 文件中的页面。要删除特定页面，请使用 the [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 的一个 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

在需要在共享、归档或合并文档之前删除 PDF 中不需要的页面时，请使用此工作流。

## 从 PDF 文件删除页面

Aspose.PDF for Python via .NET 从输入 PDF 中删除第 2 页，并将更新后的文档保存为新文件。此功能有助于在不更改文档其余部分的情况下删除不需要或敏感的页面。

1. 将输入 PDF 加载为一个 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 使用该方法删除页面 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 调用 [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 用于保存已更新的 PDF 文件的方法。

以下代码片段展示了如何使用 Python 删除 PDF 文件中的特定页面。

```python
import aspose.pdf as ap

def delete_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.delete(2)
    document.save(output_file_name)
```

## 从 PDF 文档中删除多个页面

删除多个页面可让您一次性移除一组指定的页面，这比逐页删除更高效。生成的 PDF 将保存为新文件，保留原始文档。

1. 将输入 PDF 加载为一个 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 使用 pages 数组中列出的页面进行删除 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 保存已更新的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 保存到新文件。

```python
import aspose.pdf as ap

def delete_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    # Example: delete pages 2, 3, and 4.
    pages = [2, 3, 4]
    document.pages.delete(pages)
    document.save(output_file_name)
```

## 相关页面主题

- [在 Python 中处理 PDF 页面](/pdf/zh/python-net/working-with-pages/)
- [在 Python 中添加 PDF 页面](/pdf/zh/python-net/add-pages/)
- [在 Python 中移动 PDF 页面](/pdf/zh/python-net/move-pages/)
- [在 Python 中提取 PDF 页面](/pdf/zh/python-net/extract-pages/)
