---
title: 以编程方式创建 PDF 文档
linktitle: 创建 PDF
type: docs
weight: 10
url: /zh/python-net/create-document/
description: 本页描述了如何使用 Aspose.PDF for Python via .NET 库从头创建 PDF 文档。
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Python 生成 PDF 文件
Abstract: 在软件开发中，以编程方式生成 PDF 文件是常见需求，尤其用于创建报告和其他文档。为此任务编写自定义代码可能低效且耗时。相反，开发者可以使用 **Aspose.PDF for Python via .NET**，这是一种使用 Python 创建 PDF 文件的强大解决方案。该过程包括创建 `Document` 对象，向文档的 `Pages` 集合添加 `Page` 对象，将 `TextFragment` 插入页面的 `paragraphs` 集合，然后保存文档。示例 Python 代码片段演示了这些步骤，展示了使用 Aspose.PDF 生成 PDF 文件的简便性。
---

对于开发者而言，有许多场景需要以编程方式生成 PDF 文件。您可能需要在软件中以编程方式生成 PDF 报告和其他 PDF 文件。自行从头编写代码和函数既冗长又低效。使用 Python 创建 PDF 文件，有一种更好的解决方案——**Aspose.PDF for Python via .NET**。

## 使用 Python 创建 PDF 文件的方法

要使用 Python 创建 PDF 文件，可按以下步骤进行。

1. 创建一个 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类的对象
1. 向 Document 对象的 [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 集合中添加一个 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 对象
1. 将 [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) 添加到页面的 [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 集合中
1. 保存生成的 PDF 文档

```python

    import aspose.pdf as ap

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Initialize textfragment object
    text_fragment = ap.text.TextFragment("Hello,world!")
    # Add text fragment to new page
    page.paragraphs.add(text_fragment)
    # Save updated PDF
    document.save("output.pdf")
```



