---
title: 使用 Python 编程方式删除 PDF 页面
linktitle: 删除 PDF 页面
type: docs
weight: 80
url: /zh/python-net/delete-pages/
description: 您可以使用 Aspose.PDF for Python via .NET 库删除 PDF 文件中的页面。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 删除 PDF 页面
Abstract: 本文提供了一个简明指南，介绍如何使用 Aspose.PDF for Python via .NET 库从 PDF 文件中删除页面。它侧重于使用 `PageCollection` 类来移除特定页面。该过程包括调用 `delete()` 方法并传入要删除的页面索引，然后使用 `save()` 方法保存更新后的文档。此外，还提供了一段代码示例，演示如何从 PDF 文件中删除页面，展示了在实际场景中使用 Aspose.PDF 库的方式。
---

您可以使用 Aspose.PDF for Python via .NET 删除 PDF 文件中的页面。要删除特定页面，请使用[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)的[`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)。

## 删除 PDF 文件中的页面

Aspose.PDF for Python via .NET 从输入 PDF 中删除第 2 页，并将更新后的文档保存为新文件。此功能有助于在不更改文档其余部分的情况下，移除不需要或敏感的页面。

1. 将输入 PDF 加载为[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 使用[`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)删除页面。
1. 调用[`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)方法以保存更新后的 PDF 文件。

以下代码片段展示了如何使用 Python 删除 PDF 文件中的特定页面。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def delete_page(input_file_name, output_file_name):
    """
    Delete a single page from a PDF document.

    Demonstrates how to remove a specific page from a PDF document using
    the Aspose.PDF library. This function deletes page 2 from the input
    document and saves the result to a new file.

    Args:
        input_file_name (str): Path to the input PDF file from which to delete a page.
        output_file_name (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Deletes page 2 (1-based indexing) from the document
        - Page numbering is 1-based (page 2 is the second page)
        - The original document is not modified; a new file is created
        - If the document has fewer than 2 pages, this may raise an error

    Example:
        >>> delete_page("input.pdf", "output.pdf")
        # Removes page 2 from input.pdf and saves result as output.pdf
    """
    # Open the PDF as a Document
    document = ap.Document(input_file_name)
    # Delete page using PageCollection API
    document.pages.delete(2)
    # Save updated Document
    document.save(output_file_name)
```

## 删除 PDF 文档中的多个页面

一次性删除多个页面可让您在单次操作中移除一组指定页面，这比逐页删除更高效。生成的 PDF 将保存为新文件，以保留原始文档。

1. 将输入 PDF 加载为[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 使用[`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)删除 pages 数组中列出的页面。
1. 将更新后的[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)保存为新文件。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def delete_bunch_pages(input_file_name, output_file_name):
    """
    Delete multiple pages from a PDF document in a single operation.

    Demonstrates bulk page deletion by removing multiple specified pages
    from a PDF document. This is more efficient than deleting pages
    one by one when removing multiple pages.

    Args:
        input_file_name (str): Path to the input PDF file from which to delete pages.
        output_file_name (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Deletes pages 2, 3, 4, 6, 7, and 9 in this example
        - Page numbers are 1-based (page 2 is the second page)
        - Pages are deleted in the order specified in the list
        - The original document is not modified; a new file is created
        - Ensure the document has enough pages to avoid errors
        - Page numbers should be adjusted if the source document has fewer pages

    Example:
        >>> delete_bunch_pages("input.pdf", "output.pdf")
        # Removes pages 2, 3, 4, 6, 7, and 9 from input.pdf
    """
    # Open the PDF as a Document
    document = ap.Document(input_file_name)
    # Example: Deleting pages 2, 3, 4, 6, 7, and 9; modify this list as needed for your use case.
    pages = [2,3,4,6,7,9]
    # Delete pages via PageCollection API
    document.pages.delete(pages)
    # Save updated Document
    document.save(output_file_name)
```

