---
title: Python 中 Hello World 的示例
linktitle: Hello World 示例
type: docs
weight: 20
url: zh/python-net/hello-world-example/
description: 此示例演示如何使用 Aspose.PDF for Python via .NET 创建一个包含文本 Hello World 的简单 PDF 文档。
lastmod: "2022-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

"Hello World" 示例展示了任何编程语言中最简单的语法和最简单的程序。开发人员通过学习如何在设备屏幕上打印 "Hello World"，来了解基本的编程语言语法。因此，我们将传统地从它开始与我们的库的相识。

在本文中，我们正在创建一个包含文本 "Hello World!" 的 PDF 文档。在您的环境中安装 **Aspose.PDF for Python via .NET** 后，您可以执行下面的代码示例以查看 Aspose.PDF API 的工作方式。

下面的代码片段遵循这些步骤：

1. 实例化一个 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象
1. 向文档对象添加一个 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)
1. 创建一个 [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) 对象
1. 将 TextFragment 添加到页面的 [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 集合中
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 生成的 PDF 文档

以下代码片段是一个 "Hello World" 程序，用于展示 Aspose.PDF for Python via .NET API 的工作原理。

```python

    import aspose.pdf as ap

    # 初始化文档对象
    document = ap.Document()
    # 添加页面
    page = document.pages.add()
    # 初始化文本片段对象
    text_fragment = ap.text.TextFragment("Hello,world!")
    # 将文本片段添加到新页面
    page.paragraphs.add(text_fragment)
    # 保存更新后的 PDF
    document.save("output.pdf")
```