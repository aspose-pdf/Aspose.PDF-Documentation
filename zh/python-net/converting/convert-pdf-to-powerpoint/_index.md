---
title: 将PDF转换为PowerPoint在Python中
linktitle: 将PDF转换为PowerPoint
type: docs
weight: 30
url: zh/python-net/convert-pdf-to-powerpoint/
description: Aspose.PDF允许您使用Python将PDF转换为PPT（PowerPoint）格式。可以通过将幻灯片作为图像的方式将PDF转换为PPTX。
lastmod: "2022-12-23"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 概述

是否可以将PDF文件转换为PowerPoint？是的，你可以！而且很简单！
本文解释了如何**使用Python将PDF转换为PowerPoint**。它涵盖了以下主题。

_格式_：**PPTX**
- [Python PDF到PPTX](#python-pdf-to-pptx)
- [Python 转换PDF到PPTX](#python-pdf-to-pptx)
- [Python 如何将PDF文件转换为PPTX](#python-pdf-to-pptx)

_格式_：**PowerPoint**
- [Python PDF到PowerPoint](#python-pdf-to-powerpoint)
- [Python 转换PDF到PowerPoint](#python-pdf-to-powerpoint)
- [Python 如何将PDF文件转换为PowerPoint](#python-pdf-to-powerpoint)


## Python PDF到PowerPoint和PPTX转换

**Aspose.PDF for Python via .NET** 允许您跟踪 PDF 到 PPTX 转换的进度。

我们有一个名为 Aspose.Slides 的 API，它提供了创建和操作 PPT/PPTX 演示文稿的功能。此 API 还提供了将 PPT/PPTX 文件转换为 PDF 格式的功能。在此转换过程中，PDF 文件的各个页面将转换为 PPTX 文件中的单独幻灯片。

在 PDF 到 <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr> 转换过程中，文本会呈现为可选择/更新的文本。请注意，为了将 PDF 文件转换为 PPTX 格式，Aspose.PDF 提供了一个名为 [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) 的类。PptxSaveOptions 类的对象作为第二个参数传递给 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)。以下代码片段展示了将 PDF 文件转换为 PPTX 格式的过程。

## 使用 Python 和 Aspose.PDF for Python 简单转换 PDF 到 PowerPoint

为了将 PDF 转换为 PPTX，Aspose.PDF for Python 建议使用以下代码步骤。

<a name="csharp-pdf-to-powerpoint"><strong>步骤：在 Python 中将 PDF 转换为 PowerPoint</strong></a> | <a name="csharp-pdf-to-pptx"><strong>步骤：在 Python 中将 PDF 转换为 PPTX</strong></a>

1. 创建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类的实例
2. 创建 [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) 类的实例
3. 使用 **Document** 对象的 **Save** 方法将 PDF 保存为 PPTX

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx.pptx"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)
    # 实例化 PptxSaveOptions 实例
    save_option = ap.PptxSaveOptions()
    # 将文件保存为 MS PowerPoint 格式
    document.save(output_pdf, save_option)
```

## 将 PDF 转换为带幻灯片图像的 PPTX


{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PowerPoint**

Aspose.PDF for Python 为您提供在线免费应用程序 ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)，您可以在其中尝试研究其功能和工作质量。

[![通过免费应用程序将 Aspose.PDF 转换为 PDF 到 PPTX](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

如果您需要将可搜索的 PDF 转换为以图像而非可选择文本形式的 PPTX，Aspose.PDF 提供了这样的功能，通过 [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) 类来实现。为此，设置 [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) 类的属性 [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) 为 'true'，如以下代码示例所示。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_pptx_with_slides_as_images.pptx"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)
    # 实例化 PptxSaveOptions 实例
    save_option = ap.PptxSaveOptions()
    save_option.slides_as_images = True
    # 将文件保存为 MS PowerPoint 格式
    document.save(output_pdf, save_option)
```


## 另请参阅

本文还涵盖这些主题。代码与上述相同。

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