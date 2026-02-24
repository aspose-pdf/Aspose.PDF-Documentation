---
title: 在 Python 中以编程方式拆分 PDF
linktitle: 拆分 PDF 文件
type: docs
weight: 60
url: /zh/python-net/split-pdf-document/
description: 本主题展示了如何在 Python 应用程序中将 PDF 页面拆分为单独的 PDF 文件。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 拆分 PDF 页面
Abstract: 本文讨论了使用 Python 将 PDF 页面拆分为单个文件的过程，强调此功能在管理大型 PDF 文档时的实用性。文中提到了 Aspose.PDF Splitter，这是一款用于演示 PDF 拆分功能的在线工具。文章提供了在 Python 应用程序中实现此功能的详细方法，包括通过 `Document` 对象的 `PageCollection` 来遍历 PDF 文档的页面。对于每一页，创建一个新的 `Document` 对象，将该页面添加进去，并使用 `save()` 方法保存新的 PDF 文件。随文附带的 Python 代码片段演示了此过程，展示了通过遍历页面并将每页保存为单独的 PDF 来拆分 PDF 文档所需的步骤。
---

拆分 PDF 页面对于希望将大型文件拆分为单独页面或页面组的用户来说是一项有用的功能。

## 实时示例

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) 是一个在线免费网页应用程序，允许您了解演示拆分功能的工作方式。

[![Aspose 拆分 PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

本主题展示了如何在 Python 应用程序中将 PDF 页面拆分为单独的 PDF 文件。要使用 Python 将 PDF 页面拆分为单页 PDF 文件，可按以下步骤进行：

1. 通过 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 集合循环遍历 PDF 文档的页面
1. 对于每次迭代，创建一个新的 Document 对象，并将单独的 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 对象添加到空文档中
1. 使用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法保存新的 PDF

## 在 Python 中将 PDF 拆分为多个文件或单独的 PDF

以下 Python 代码片段展示了如何将 PDF 页面拆分为单独的 PDF 文件。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    page_count = 1

    # Loop through all the pages
    for pdfPage in document.pages:
        new_document = ap.Document()
        new_document.pages.add(pdfPage)
        new_document.save(output_path + "_page_" + str(page_count) + ".pdf")
        page_count = page_count + 1
```


