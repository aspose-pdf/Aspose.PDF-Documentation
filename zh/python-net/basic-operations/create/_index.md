---
title: 程序化创建PDF文档
linktitle: 创建PDF
type: docs
weight: 10
url: zh/python-net/create-document/
description: 本页描述如何使用Aspose.PDF for Python via .NET库从头开始创建PDF文档。
---

对于开发人员来说，在许多情况下需要程序化地生成PDF文件。您可能需要在软件中程序化地生成PDF报告和其他PDF文件。从头编写自己的代码和函数既漫长又低效。要使用Python创建PDF文件，有一个更好的解决方案 - **Aspose.PDF for Python via .NET**。

## 如何使用Python创建PDF文件

要使用Python创建PDF文件，可以使用以下步骤。

1. 创建一个[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)类的对象

1. 将 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 对象添加到 Document 对象的 [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 集合中
1. 将 [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) 添加到页面的 [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 集合中
1. 保存生成的 PDF 文档

```python

    import aspose.pdf as ap

    # 初始化文档对象
    document = ap.Document()
    # 添加页面
    page = document.pages.add()
    # 初始化 textfragment 对象
    text_fragment = ap.text.TextFragment("Hello,world!")
    # 将文本片段添加到新页面
    page.paragraphs.add(text_fragment)
    # 保存更新后的 PDF
    document.save("output.pdf")
```