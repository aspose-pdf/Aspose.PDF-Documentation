---
title: 如何使用 Python 创建 PDF
linktitle: 创建 PDF 文档
type: docs
weight: 10
url: /zh/python-net/create-pdf-document/
description: 使用 Aspose.PDF for Python via .NET 创建和格式化 PDF 文档。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 创建 PDF 文件
Abstract: Aspose.PDF for Python via .NET 是一款多功能 API，旨在帮助开发人员在面向 .NET 框架的 Python 应用程序中操作 PDF 文件。它使用户能够轻松创建、加载、修改和转换 PDF 文档。本文提供了使用 Aspose.PDF 创建简单 PDF 文件的分步指南。该过程包括初始化 `Document` 对象、向文档添加 `Page`、在页面的段落中插入 `TextFragment`，以及将文件保存为 PDF。附带的 Python 代码片段演示了这些步骤，创建了一个包含文本 "Hello World!" 的 PDF 文档。该 API 通过极少的代码简化了 PDF 处理，提高了在 .NET 环境中使用 PDF 的开发者的工作效率。
---

**Aspose.PDF for Python via .NET** 是一个 PDF 操作 API，允许开发人员仅用几行代码就能直接从 Python 为 .NET 应用程序创建、加载、修改和转换 PDF 文件。

## 如何创建简单的 PDF 文件

要使用 Aspose.PDF 通过 .NET 的 Python 创建 PDF，您可以按照以下步骤操作：

1. 创建一个 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类的对象
1. 向 Document 对象的 [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 集合中添加一个 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 对象
1. 将 [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) 添加到页面的 [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 集合中
1. 保存生成的 PDF 文档

```python

    import aspose.pdf as ap

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    # Save updated PDF
    document.save(output_pdf)
```


