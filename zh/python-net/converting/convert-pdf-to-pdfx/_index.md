---
title: 在 Python 中将 PDF 转换为 PDF/A、PDF/E 和 PDF/X
linktitle: 将 PDF 转换为 PDF/A、PDF/E 和 PDF/X
type: docs
weight: 120
url: /zh/python-net/convert-pdf-to-pdf_x/
lastmod: "2026-06-08"
description: 了解如何使用 Aspose.PDF for Python via .NET 在 Python 中将 PDF 文件转换为 PDF/A、PDF/E 和 PDF/X，以用于归档、可访问性和打印工作流。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 如何将 PDF 转换为 PDF/x 格式
Abstract: 本文提供了使用 Aspose.PDF for Python 将 PDF 转换为 PDF/A、PDF/E 和 PDF/X 格式的全面指南。
---

**PDF 到 PDF/x 格式指的是将 PDF 转换为其他附加格式的能力，即 PDF/A、PDF/E 和 PDF/X。**

## 将 PDF 转换为 PDF/A

**Aspose.PDF for Python** 允许您将 PDF 文件转换为 <abbr title="Portable Document Format / A">PDF/A</abbr> 符合规范的 PDF 文件。在此之前，必须验证该文件。本主题说明如何操作。

{{% alert color="primary" %}}

请注意，我们使用 Adobe Preflight 来验证 PDF/A 合规性。市场上的所有工具都有各自对 PDF/A 合规性的“表示”。请参考此关于 PDF/A 验证工具的文章。我们选择 Adobe 产品来验证 Aspose.PDF 生成 PDF 文件的方式，因为 Adobe 是所有与 PDF 相关事物的核心。

{{% /alert %}}

使用 Document 类的 Convert 方法转换文件。在将 PDF 转换为符合 PDF/A 标准的文件之前，使用 Validate 方法对 PDF 进行验证。验证结果存储在 XML 文件中，然后该结果也传递给 Convert 方法。您还可以使用 ConvertErrorAction 枚举指定对无法转换的元素的操作。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PDF/A**

Aspose.PDF for Python 为您呈现在线应用 [PDF 转 PDF/A-1A](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)，在此您可以尝试调查其功能以及其工作质量。

[![Aspose.PDF 将 PDF 转换为 PDF/A 的应用](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

'document.validate()' 方法验证 PDF 文件是否符合 PDF/A-1B 标准（ISO 标准化的 PDF 版本，旨在长期存档）。验证结果保存到日志文件中。

### 将 PDF 转换为 PDF/A-1B

以下代码片段展示了如何将 PDF 文件转换为 PDF/A-1B 格式：

1. 使用 'ap.Document' 加载 PDF 文档。
1. 使用以下参数调用 convert 方法：
    - 日志文件路径 - 存储转换过程和合规检查的详细信息。
    - 目标格式 - 'ap.PdfFormat.PDF_A_1B'（存档标准）。
    - Error action - ‘ap.ConvertErrorAction.DELETE’ — 自动删除阻止合规性的元素。
1. 将转换后的符合 PDF/A 标准的文件保存到输出路径。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA(infile, outfile):
    """Convert PDF to PDF/A-1B format."""

    document = ap.Document(infile)
    document.convert(
        outfile.replace(".pdf", "-log.xml"),
        ap.PdfFormat.PDF_A_1B,
        ap.ConvertErrorAction.DELETE,
    )
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

### 将 PDF 转换为 PDF 2.0 和 PDF/A-4

此示例演示如何将 PDF 文档转换为更新的标准化格式：PDF 2.0 和 PDF/A-4。
两种转换都有助于确保符合现代规范和归档要求。

1. 使用 ap.Document 加载输入文档。
1. 通过调用 document.convert 执行首次转换为 PDF 2.0：
    - 转换详情的日志文件路径。
    - 目标格式 - 'ap.PdfFormat.V_2_0'。
    - 错误操作 - 'ap.ConvertErrorAction.DELETE' 用于移除不合规的元素。
1. 使用相同的方法进行第二次转换为 PDF/A-4，确保文件也符合归档标准。
1. 将生成的文档保存到指定的输出路径。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA4(infile, outfile):
    logfile = outfile.replace(".pdf", "_log.xml")

    document = ap.Document(infile)
    document.convert(logfile, ap.PdfFormat.V_2_0, ap.ConvertErrorAction.DELETE)
    document.convert(logfile, ap.PdfFormat.PDF_A_4, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

### 将 PDF 转换为带嵌入文件的 PDF/A-3A

下面的代码片段演示了如何将外部文件嵌入 PDF 中，然后将 PDF 转换为 PDF/A-3A 格式，该格式支持附件，适用于带有嵌入内容的长期归档。

1. 使用 'ap.Document' 加载输入 PDF。
1. 创建一个指向要嵌入的文件（例如 "aspose-logo.jpg"）的 'FileSpecification' 对象，并提供描述。
1. 将文件规范添加到 PDF 的 'embedded_files' 集合中。
1. 使用 'document.convert' 将文档转换为 PDF/A-3A，指定：
    - 日志文件路径。
    - 目标格式 - 'ap.PdfFormat.PDF_A_3A'.
    - 错误操作 - 'ap.ConvertErrorAction.DELETE' 用于移除不合规的元素。
1. 将转换后的 PDF 保存到输出路径。
1. 打印确认消息。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_with_attachment(infile, attachement_file, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")
    document = ap.Document(infile)

    fileSpecification = ap.FileSpecification(attachement_file, "Large Image file")
    document.embedded_files.add(fileSpecification)
    document.convert(
        logfile, ap.PdfFormat.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE
    )
    document.save(outfile)
```

### 将 PDF 转换为 PDF/A-1B 并进行字体替换

此函数将 PDF 转换为 PDF/A-1B 格式，同时通过用可用的字体替换缺失的字体来处理。这样可确保转换后的 PDF 在视觉上保持一致，并符合归档标准。

1. 使用 'ap.Document' 加载 PDF。
1. 使用 'document.convert' 将 PDF 转换为 PDF/A-1B，指定：
    - 日志文件路径。
    - 目标格式 - 'ap.PdfFormat.PDF_A_1B'。
    - 错误操作 - 'ap.ConvertErrorAction.DELETE' 用于移除不合规的元素。
1. 将转换后的 PDF 保存到输出路径。
1. 打印确认消息。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_replace_missing_fonts(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")
    try:
        ap.text.FontRepository.find_font("AgencyFB")

    except ap.FontNotFoundException:
        font_substitution = ap.text.SimpleFontSubstitution("AgencyFB", "Arial")
        ap.text.FontRepository.Substitutions.append(font_substitution)

    document = ap.Document(infile)
    document.convert(logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

### 将 PDF 转换为 PDF/A-1B 并自动标记

此函数将 PDF 文档转换为 PDF/A-1B 格式，同时自动为内容添加标签，以实现可访问性和结构一致性。自动标记可提升文档在屏幕阅读器中的可用性，并确保正确的语义结构。

1. 使用 'ap.Document' 加载 PDF。
1. 创建 'PdfFormatConversionOptions' 并指定：
    - 日志文件路径。
    - 目标格式 - 'ap.PdfFormat.PDF_A_1B'。
    - 错误操作 - 'ap.ConvertErrorAction.DELETE' 用于移除不合规的元素。
1. 配置 'AutoTaggingSettings'：
    - 启用 'enable_auto_tagging = True'。
    - 设置 'heading_recognition_strategy = AUTO' 以自动检测标题。
1. 将自动标记设置分配给转换选项。
1. 使用 'document.convert(options)' 将 PDF 转换。
1. 将转换后的 PDF 保存到输出路径。
1. 打印确认消息。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_with_automatic_tagging(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE
    )

    auto_tagging_settings = ap.AutoTaggingSettings()
    auto_tagging_settings.enable_auto_tagging = True

    auto_tagging_settings.heading_recognition_strategy = (
        ap.HeadingRecognitionStrategy.AUTO
    )

    options.auto_tagging_settings = auto_tagging_settings
    document.convert(options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## 将 PDF 转换为 PDF/E

此代码片段演示了如何将 PDF 文档转换为 PDF/E-1 格式，该格式是专为工程和技术文档制定的 ISO 标准。该格式保留了工程工作流所需的精确布局、图形和元数据。

1. 使用 'ap.Document' 加载源 PDF。
1. 创建 'PdfFormatConversionOptions' 并指定：
    - 用于跟踪转换问题的日志文件路径。
    - 目标格式 - 'ap.PdfFormat.PDF_E_1'.
    - 错误操作 - 'ap.ConvertErrorAction.DELETE' 用于移除不合规的元素。
1. 使用 'document.convert(options)' 将 PDF 转换。
1. 将转换后的 PDF 保存到指定的输出路径。
1. 打印确认消息。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDF_E(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE
    )

    document.convert(options)

    # Save PDF document
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## 将 PDF 转换为 PDF/X

下面的代码片段将 PDF 文档转换为 PDF/X-4 格式，这是印刷和出版行业常用的 ISO 标准。PDF/X-4 确保颜色准确性，保持透明度，并嵌入 ICC 配置文件，以在不同设备之间实现一致的输出。

1. 使用 'ap.Document' 加载源 PDF。
1. 创建 'PdfFormatConversionOptions' 并指定：
    - 日志文件路径。
    - 目标格式 - 'ap.PdfFormat.PDF_X_4'.
    - 错误操作 - 'ap.ConvertErrorAction.DELETE' 用于移除不合规的元素。
1. 通过 'icc_profile_file_name' 提供用于颜色管理的 **ICC 配置文件**。
1. 为打印要求指定带有条件标识符（例如 "FOGRA39"）的 **OutputIntent**。
1. 使用 'document.convert()' 将 PDF 转换。
1. 将转换后的 PDF 保存到指定的输出路径。
1. 打印确认消息。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDF_X(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_X_4, ap.ConvertErrorAction.DELETE
    )

    # Provide the name of the external ICC profile file (optional)
    options.icc_profile_file_name = path.join(
        path.dirname(infile), "ISOcoated_v2_eci.icc"
    )
    # Provide an output condition identifier and other necessary OutputIntent properties (optional)
    options.output_intent = ap.OutputIntent("FOGRA39")

    document.convert(options)

    # Save PDF document
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## 相关转换

- [转换 PDF 为 Word](/pdf/zh/python-net/convert-pdf-to-word/) 用于标准验证后的可编辑内容工作流。
- [将 PDF 转换为 HTML](/pdf/zh/python-net/convert-pdf-to-html/) 当您的目标输出是面向网页而不是基于标准的 PDF 时。
