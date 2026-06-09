---
title: 以编程方式创建 PDF 文档
linktitle: 创建 PDF
type: docs
weight: 10
url: /zh/python-net/create-document/
description: 本页描述了如何使用 Aspose.PDF for Python via .NET 库从头开始创建 PDF 文档。
lastmod: "2026-06-08"
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Python 生成 PDF 文件
Abstract: 在软件开发中，以编程方式生成 PDF 文件是一个常见需求，尤其是用于创建报告和其他文档。为此任务编写自定义代码可能效率低下且耗时。相反，开发者可以使用 **Aspose.PDF for Python via .NET**，这是一种使用 Python 创建 PDF 文件的强大解决方案。该过程包括创建一个 `Document` 对象，将 `Page` 对象添加到文档的 `Pages` 集合中，将 `TextFragment` 插入到页面的 `paragraphs` 集合中，然后保存文档。示例 Python 代码片段演示了这些步骤，展示了使用 Aspose.PDF 生成 PDF 文件的简便性。
---

对于开发者来说，有许多情景需要以编程方式生成 PDF 文件。您可能需要在软件中以编程方式生成 PDF 报告和其他 PDF 文件。自行从头编写代码和函数既冗长又低效。要使用 Python 创建 PDF 文件，有一个更好的解决方案——**Aspose.PDF for Python via .NET**。

## 如何使用 Python 创建 PDF 文件

使用 Python 创建 PDF 文件，可按照以下步骤进行。

1. 创建一个对象 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类
1. 添加一个 [页面](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 对象到 [页面](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) Document 对象的集合
1. 添加 [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) 到 [段落](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 页面集合
1. 保存生成的 PDF 文档

```python
import aspose.pdf as ap

# Initialize document object
document = ap.Document()
# Add page
page = document.pages.add()
# Add text to new page
page.paragraphs.add(ap.text.TextFragment("Hello World!"))
# Define output file path
output_pdf = "output.pdf"
# Save updated PDF
output_pdf = "output.pdf"
document.save(output_pdf)
```
