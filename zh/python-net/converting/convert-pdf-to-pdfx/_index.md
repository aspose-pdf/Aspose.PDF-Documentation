---
title: 在Python中将PDF转换为PDF/x格式
linktitle: 将PDF转换为PDF/x格式
type: docs
weight: 120
url: /zh/python-net/convert-pdf-to-pdf_x/
lastmod: "2025-09-27"
description: 本主题展示如何使用 Aspose.PDF for Python via .NET 将 PDF 转换为 PDF/x 格式。
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 如何将 PDF 转换为 PDF/x 格式
Abstract: 本文提供了使用 Aspose.PDF for Python 将 PDF 转换为 PDF/A、PDF/E 和 PDF/X 格式的完整指南。
---

**PDF 转换为 PDF/x 格式指的是将 PDF 转换为额外的格式，即 PDF/A、PDF/E 和 PDF/X 的能力。**

## 将 PDF 转换为 PDF/A

**Aspose.PDF for Python** 允许您将 PDF 文件转换为符合 <abbr title="Portable Document Format / A">PDF/A</abbr> 标准的 PDF 文件。在此之前，必须对文件进行验证。本主题解释了如何操作。

{{% alert color="primary" %}}

请注意，我们遵循 Adobe Preflight 来验证 PDF/A 合规性。市场上的所有工具都有各自的 “PDF/A 合规性表示”。请参阅此文章了解 PDF/A 验证工具以供参考。我们选择 Adobe 产品来验证 Aspose.PDF 生成的 PDF 文件，因为 Adobe 是所有与 PDF 相关事物的核心。

{{% /alert %}}

使用 Document 类的 Convert 方法转换文件。在将 PDF 转换为符合 PDF/A 标准的文件之前，使用 Validate 方法对 PDF 进行验证。验证结果存储在 XML 文件中，然后该结果也会传递给 Convert 方法。您还可以使用 ConvertErrorAction 枚举指定对无法转换的元素的处理方式。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PDF/A**

Aspose.PDF for Python 为您提供在线免费应用 ["PDF 转 PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)，您可以在此尝试调查其功能和质量。

[![Aspose.PDF 转换 PDF 为 PDF/A 的免费应用](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

`document.validate()` 方法验证 PDF 文件是否符合 PDF/A-1B 标准（ISO 标准化的长期存档 PDF 版本）。验证结果保存到日志文件中。

1. 使用 'ap.Document' 加载 PDF 文档。
1. 使用目标合规级别 (ap.PdfFormat.PDF_A_1B) 调用 validate 方法。
1. 验证结果写入指定的日志文件。

```python

    path_infile = path.join(self.data_dir, infile)
    path_logfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.validate(path_logfile, ap.PdfFormat.PDF_A_1B)
```

### 将 PDF 转换为 PDF/A-1B

以下代码片段展示了如何将 PDF 文件转换为 PDF/A-1B 格式：

1. 使用 'ap.Document' 加载 PDF 文档。
1. 使用以下参数调用 convert 方法：
- 日志文件路径 - 存储转换过程和合规性检查的详细信息。
- 目标格式 - 'ap.PdfFormat.PDF_A_1B'（归档标准）。
- 错误处理 - 'ap.ConvertErrorAction.DELETE' — 自动移除阻碍合规的元素。
1. 将转换后的符合 PDF/A 标准的文件保存到输出路径。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.convert(
        self.data_dir + "pdf_pdfa.log",
        ap.PdfFormat.PDF_A_1B,
        ap.ConvertErrorAction.DELETE,
    )
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

### 将 PDF 转换为 PDF 2.0 和 PDF/A-4

本示例演示如何将 PDF 文档转换为更新的标准化格式：PDF 2.0 和 PDF/A-4。
这两种转换都有助于确保符合现代规范和归档要求。

1. 使用 ap.Document 加载输入文档。
1. 调用 document.convert 执行第一次转换为 PDF 2.0，使用以下参数：
- 用于转换细节的日志文件路径。
- 目标格式 - 'ap.PdfFormat.V_2_0'。
- 错误处理 - 'ap.ConvertErrorAction.DELETE'，用于删除不合规的元素。
1. 使用相同方法执行第二次转换为 PDF/A-4，确保文件同样符合归档标准。
1. 将生成的文档保存到指定的输出路径。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    document.convert(path_logfile, ap.PdfFormat.V_2_0, ap.ConvertErrorAction.DELETE)

    document.convert(path_logfile, ap.PdfFormat.PDF_A_4, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

### 将 PDF 转换为带嵌入文件的 PDF/A-3A

以下代码片段演示如何将外部文件嵌入 PDF，然后将 PDF 转换为支持附件且适合长期归档的 PDF/A-3A 格式。

1. 使用 'ap.Document' 加载输入 PDF。
1. 创建一个指向要嵌入文件的 'FileSpecification' 对象（例如 "aspose-logo.jpg"），并提供描述。
1. 将文件规范添加到 PDF 的 'embedded_files' 集合中。
1. 使用 'document.convert' 将文档转换为 PDF/A-3A，并指定：
- 日志文件路径。
- 目标格式 - 'ap.PdfFormat.PDF_A_3A'。
- 错误操作 - 'ap.ConvertErrorAction.DELETE'，用于删除不符合要求的元素。
1. 将转换后的 PDF 保存到输出路径。
1. 打印确认信息。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)

    fileSpecification = ap.FileSpecification(self.data_dir + "aspose-logo.jpg", "Large Image file")
    document.embedded_files.add(fileSpecification)
    document.convert(path_logfile, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

### 将 PDF 转换为 PDF/A-1B（使用字体替换）

此函数将 PDF 转换为 PDF/A-1B 格式，并通过用可用字体替换缺失的字体来处理字体缺失问题。这样可确保转换后的 PDF 在视觉上保持一致，并符合归档标准。

1. 使用 'ap.Document' 加载 PDF。
1. 使用 'document.convert' 将 PDF 转换为 PDF/A-1B，并指定：
- 日志文件路径。
- 目标格式 - 'ap.PdfFormat.PDF_A_1B'。
- 错误操作 - 'ap.ConvertErrorAction.DELETE'，用于删除不符合要求的元素。
1. 将转换后的 PDF 保存到输出路径。
1. 打印确认信息。

```python

    from os import path
    import aspose.pdf as ap 

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    try:
        ap.text.FontRepository.find_font("AgencyFB")

    except ap.FontNotFoundException:
        font_substitution = ap.text.SimpleFontSubstitution("AgencyFB", "Arial")
        ap.text.FontRepository.Substitutions.append(font_substitution)

    document = ap.Document(path_infile)
    document.convert(path_logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

### 将 PDF 转换为 PDF/A-1B（自动标记）

此函数将 PDF 文档转换为 PDF/A-1B 格式，并自动为内容添加标签，以提升可访问性和结构一致性。自动标记可改善屏幕阅读器的文档可用性，并确保语义结构正确。

1. 使用 'ap.Document' 加载 PDF。
1. 创建 'PdfFormatConversionOptions' 并指定：
- 日志文件路径。
- 目标格式 - 'ap.PdfFormat.PDF_A_1B'。
- 错误操作 - 'ap.ConvertErrorAction.DELETE'，用于删除不符合要求的元素。
1. 配置 'AutoTaggingSettings'：
- 启用 'enable_auto_tagging = True'。
- 将 'heading_recognition_strategy = AUTO' 设置为自动检测标题。
1. 将自动标记设置分配给转换选项。
1. 使用 'document.convert(options)' 转换 PDF。
1. 将转换后的 PDF 保存到输出路径。
1. 打印确认信息。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)

    auto_tagging_settings = ap.AutoTaggingSettings()
    auto_tagging_settings.enable_auto_tagging = True

    auto_tagging_settings.heading_recognition_strategy = ap.HeadingRecognitionStrategy.AUTO

    options.auto_tagging_settings = auto_tagging_settings
    document.convert(options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## 将 PDF 转换为 PDF/E

此代码片段验证 PDF 文档是否符合 PDF/E-1 标准，该标准是面向工程和技术文档的 ISO 标准。验证结果将保存到日志文件中。

1. 使用 'ap.Document' 加载 PDF 文档。
1. 调用 validate 方法，并指定：
- 用于存储验证结果的日志文件路径。
- 目标格式 - 'ap.PdfFormat.PDF_E_1'。
1. 验证结果已保存至日志文件以供查看。

```python

    path_infile = path.join(self.data_dir, infile)
    path_logfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.validate(path_logfile, ap.PdfFormat.PDF_E_1)
```

下面的示例演示如何将 PDF 转换为 PDF/E-1 格式，该格式是针对工程和技术文档的 ISO 标准。此格式保留了工程工作流所需的精确布局、图形和元数据。

1. 使用 'ap.Document' 加载源 PDF。
1. 创建 'PdfFormatConversionOptions' 并指定：
- 用于跟踪转换问题的日志文件路径。
- 目标格式 - 'ap.PdfFormat.PDF_E_1'。
- 错误操作 - 'ap.ConvertErrorAction.DELETE'，用于删除不符合要求的元素。
1. 使用 'document.convert(options)' 转换 PDF。
1. 将转换后的 PDF 保存到指定的输出路径。
1. 打印确认信息。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE)

    document.convert(options)

    # Save PDF document
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## 将 PDF 转换为 PDF/X

下面的代码片段将 PDF 文档转换为 PDF/X-4 格式，该格式是印刷和出版行业常用的 ISO 标准。PDF/X-4 确保颜色精度，保持透明度，并嵌入 ICC 配置文件，以实现跨设备的一致输出。

1. 使用 'ap.Document' 加载源 PDF。
1. 创建 'PdfFormatConversionOptions' 并指定：
- 日志文件路径。
- 目标格式 - 'ap.PdfFormat.PDF_X_4'。
- 错误操作 - 'ap.ConvertErrorAction.DELETE' 用于删除不合规的元素。
1. 通过 'icc_profile_file_name' 提供用于颜色管理的 **ICC 配置文件**。
1. 为打印需求指定带有条件标识符（例如 "FOGRA39"）的 **OutputIntent**。
1. 使用 'document.convert()' 转换 PDF。
1. 将转换后的 PDF 保存到指定的输出路径。
1. 打印确认信息。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_X_4, ap.ConvertErrorAction.DELETE)

    # Provide the name of the external ICC profile file (optional)
    options.icc_profile_file_name = path.join(self.data_dir,"ISOcoated_v2_eci.icc")
    # Provide an output condition identifier and other necessary OutputIntent properties (optional)
    options.output_intent = ap.OutputIntent("FOGRA39")

    document.convert(options)

    # Save PDF document
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```
