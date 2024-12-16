---
title: 将PDF转换为PDF/A格式在Python中
linktitle: 将PDF转换为PDF/A格式
type: docs
weight: 100
url: /zh/python-net/convert-pdf-to-pdfa/
lastmod: "2022-12-23"
description: 本主题向您展示如何通过Python使用Aspose.PDF将PDF文件转换为符合PDF/A标准的PDF文件。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Python** 允许您将PDF文件转换为符合<abbr title="Portable Document Format / A">PDF/A</abbr>标准的PDF文件。在执行此操作之前，必须验证文件。本文将解释如何操作。

{{% alert color="primary" %}}

请注意，我们遵循Adobe Preflight来验证PDF/A符合性。市场上的所有工具都有自己对PDF/A符合性的“表示”。请查看这篇关于PDF/A验证工具的文章以作参考。我们选择Adobe产品来验证Aspose.PDF如何生成PDF文件，因为Adobe是与PDF相关的一切的中心。

{{% /alert %}}

使用Document类的Convert方法转换文件。
 在将 PDF 转换为符合 PDF/A 的文件之前，请使用 Validate 方法验证 PDF。验证结果存储在一个 XML 文件中，然后此结果也传递给 Convert 方法。您还可以使用 ConvertErrorAction 枚举指定无法转换的元素的操作。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PDF/A**

Aspose.PDF for Python 为您提供免费的在线应用程序 ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将 PDF 转换为 PDF/A](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

## 将 PDF 文件转换为 PDF/A-1b

以下代码片段展示了如何将 PDF 文件转换为符合 PDF/A-1b 的 PDF。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_pdfa.pdf"
    output_log = DIR_OUTPUT + "convert_pdf_to_pdfa.log"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)
    # 转换为符合 PDF/A 的文档
    document.convert(output_log, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    # 保存输出文档
    document.save(output_pdf)
```