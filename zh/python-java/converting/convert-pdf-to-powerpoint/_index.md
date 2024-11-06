---
title: 将 PDF 转换为 PowerPoint 在 Python 中
linktitle: 将 PDF 转换为 PowerPoint
type: docs
weight: 30
url: zh/python-java/convert-pdf-to-powerpoint/
description: Aspose.PDF 允许您使用 Python 将 PDF 转换为 PPT (PowerPoint) 格式。可以将 PDF 转换为带有幻灯片图像的 PPTX。
lastmod: "2023-04-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 概述

是否可以将 PDF 文件转换为 PowerPoint？是的，你可以！而且很简单！
本文解释了如何**使用 Python 将 PDF 转换为 PowerPoint**。它涵盖了这些主题。

_格式_: **PPTX**
- [Python PDF 转 PPTX](#python-pdf-to-pptx)
- [Python 转换 PDF 到 PPTX](#python-pdf-to-pptx)
- [Python 如何将 PDF 文件转换为 PPTX](#python-pdf-to-pptx)

_格式_: **PowerPoint**
- [Python PDF 转 PowerPoint](#python-pdf-to-powerpoint)
- [Python 转换 PDF 到 PowerPoint](#python-pdf-to-powerpoint)
- [Python 如何将 PDF 文件转换为 PowerPoint](#python-pdf-to-powerpoint)


## Python PDF 转 PowerPoint 和 PPTX 转换



**Aspose.PDF for Python via Java** 允许您跟踪 PDF 到 PPTX 转换的进度。

我们有一个名为 Aspose.Slides 的 API，它提供创建和操作 PPT/PPTX 演示文稿的功能。此 API 还提供将 PPT/PPTX 文件转换为 PDF 格式的功能。在此转换过程中，PDF 文件的各个页面被转换为 PPTX 文件中的单独幻灯片。

在 PDF 到<abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>转换期间，文本被呈现为可选择/更新的文本。请注意，为了将 PDF 文件转换为 PPTX 格式，Aspose.PDF 提供了一个名为[`PptxSaveOptions`](https://reference.aspose.com/pdf/java/aspose.pdf/pptxsaveoptions)的类。PptxSaveOptions 类的对象作为第二个参数传递给[`Document.Save(..) method`](https://reference.aspose.com/pdf/java/aspose.pdf/document/methods/save)。以下代码片段显示了将 PDF 文件转换为 PPTX 格式的过程。

## 使用 Python 和 Aspose.PDF for Python 简单地将 PDF 转换为 PowerPoint

为了将 PDF 转换为 PPTX，Aspose.PDF for Python 建议使用以下代码步骤。

<a name="csharp-pdf-to-powerpoint"><strong>步骤：在 Python 中将 PDF 转换为 PowerPoint</strong></a> | <a name="csharp-pdf-to-pptx"><strong>步骤：在 Python 中将 PDF 转换为 PPTX</strong></a>

1. 创建一个 [Document](https://reference.aspose.com/pdf/java/aspose.pdf/document) 类的实例
2. 创建一个 [PptxSaveOptions](https://reference.aspose.com/pdf/java/aspose.pdf/pptxsaveoptions) 类的实例
3. 使用 **Document** 对象的 **Save** 方法将 PDF 保存为 PPTX

```python

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx_with_options.pptx"
# 打开 PDF 文档
document = Api.Document(input_pdf)

save_options = Api.PptxSaveOptions()
save_options._ImageResolution = 300
save_options._SeparateImages = True
save_options._OptimizeTextBoxes = True

# 将文件保存为 MS Word 文档格式
document.save(output_pdf, save_options)
```


## 将 PDF 转换为包含图像幻灯片的 PPTX

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PowerPoint**

Aspose.PDF for Python 为您提供免费的在线应用程序 ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

如果您需要将可搜索的 PDF 转换为图像形式的 PPTX，而不是可选择的文本，Aspose.PDF 提供了通过 [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/) 类实现此功能的特性。为此，请将 [PptxSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/) 类的 [SlidesAsImages](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/#properties) 属性设置为 'true'，如下代码示例所示。

```python

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx_with_options.pptx"
# 打开 PDF 文档
document = Api.Document(input_pdf)

save_options = Api.PptxSaveOptions()
save_options._ImageResolution = 300
save_options._SlidesAsImages = True

# 将文件保存为 MS Word 文档格式
document.save(output_pdf, save_options)
```


## 另请参阅

本文还涵盖了这些主题。代码与上述相同。

_格式_: **PowerPoint**
- [Python PDF 转 PowerPoint 代码](#python-pdf-to-powerpoint)
- [Python PDF 转 PowerPoint API](#python-pdf-to-powerpoint)
- [Python PDF 转 PowerPoint 编程实现](#python-pdf-to-powerpoint)
- [Python PDF 转 PowerPoint 库](#python-pdf-to-powerpoint)
- [Python 将 PDF 保存为 PowerPoint](#python-pdf-to-powerpoint)
- [Python 从 PDF 生成 PowerPoint](#python-pdf-to-powerpoint)
- [Python 从 PDF 创建 PowerPoint](#python-pdf-to-powerpoint)
- [Python PDF 转 PowerPoint 转换器](#python-pdf-to-powerpoint)

_格式_: **PPTX**
- [Python PDF 转 PPTX 代码](#python-pdf-to-pptx)
- [Python PDF 转 PPTX API](#python-pdf-to-pptx)
- [Python PDF 转 PPTX 编程实现](#python-pdf-to-pptx)
- [Python PDF 转 PPTX 库](#python-pdf-to-pptx)
- [Python 将 PDF 保存为 PPTX](#python-pdf-to-pptx)
- [Python 从 PDF 生成 PPTX](#python-pdf-to-pptx)
- [Python 从 PDF 创建 PPTX](#python-pdf-to-pptx)

- [Python PDF 转 PPTX 转换器](#python-pdf-to-pptx)