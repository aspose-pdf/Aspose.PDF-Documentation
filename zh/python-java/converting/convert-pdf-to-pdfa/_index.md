---
title: 将PDF转换为PDF/A格式的Python代码
linktitle: 将PDF转换为PDF/A格式
type: docs
weight: 100
url: /zh/python-java/convert-pdf-to-pdfa/
lastmod: "2023-04-06"
description: 本主题向您展示如何通过Aspose.PDF for Python将PDF文件转换为符合PDF/A标准的PDF文件。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Python** 允许您将PDF文件转换为符合<abbr title="Portable Document Format / A">PDF/A</abbr>标准的PDF文件。在此之前，文件必须经过验证。本主题将解释如何进行。

{{% alert color="primary" %}}

请注意，我们遵循Adobe Preflight来验证PDF/A符合性。市场上的所有工具都有它们自己的PDF/A符合性“表示”。请查看关于PDF/A验证工具的这篇文章以供参考。我们选择Adobe产品来验证Aspose.PDF如何生成PDF文件，因为Adobe是与PDF相关的中心。

{{% /alert %}}

使用Document类的Convert方法转换文件。
 在将 PDF 转换为符合 PDF/A 的文件之前，使用 Validate 方法验证 PDF。验证结果存储在一个 XML 文件中，然后此结果也传递给 Convert 方法。您还可以使用 ConvertErrorAction 枚举指定无法转换的元素的操作。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PDF/A**

Aspose.PDF for Python 为您提供免费的在线应用程序 ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)，您可以在其中尝试调查其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将 PDF 转换为 PDF/A](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

## 将 PDF 文件转换为 PDF/A-1b

以下代码片段展示了如何将 PDF 文件转换为符合 PDF/A-1b 的 PDF。

```python
from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"
input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pdfa.pdf"
output_log = DIR_OUTPUT + "convert_pdf_to_pdfa.log"
# 打开 PDF 文档
document = Api.Document(input_pdf)
# 转换为符合 PDF/A 的文档
document.convert(output_log, Api.PdfFormat.PDF_A_1B, Api.ConvertErrorAction.Delete)
# 保存输出文档
document.save(output_pdf)
```