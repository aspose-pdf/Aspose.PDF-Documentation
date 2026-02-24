---
title: 在 Python 中将 PDF 转换为 Microsoft Word 文档
linktitle: 将 PDF 转换为 Word
type: docs
weight: 10
url: /zh/python-net/convert-pdf-to-word/
lastmod: "2025-09-27"
description: 了解如何使用 Aspose.PDF 在 Python 中将 PDF 文档转换为 Word 格式，以便轻松编辑文档。
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何在 Python 中将 PDF 转换为 Word
Abstract: 本文提供了使用 Python 将 PDF 文件转换为 Microsoft Word 格式（DOC 和 DOCX）的全面指南，特别是利用 Aspose.PDF 库。它概述了将 PDF 转换为可编辑的 Word 文档的优势，使得文本、表格和图像等内容的操作更加简便。文章详细说明了将 PDF 转换为 DOC（Word 97-2003 格式）和 DOCX 的过程，并通过代码片段演示了在 Python 中进行这些转换。该过程包括从 PDF 创建 `Document` 对象，并使用 `save()` 方法和 `SaveFormat` 枚举将其保存为所需格式。此外，还介绍了 `DocSaveOptions` 类，可进一步自定义转换过程，例如指定识别模式。文章还强调了 Aspose.PDF 提供的在线应用程序，以测试转换质量和功能。内容包括结构化概览以及指向每种格式对应章节的链接。
---

## 将 PDF 转换为 DOC

最受欢迎的功能之一是 PDF 转换为 Microsoft Word DOC，使内容管理更容易。**Aspose.PDF for Python via .NET** 允许您不仅将 PDF 文件转换为 DOC，还可以转换为 DOCX 格式，轻松高效。

[DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) 类提供了众多属性，以改进将 PDF 文件转换为 DOC 格式的过程。在这些属性中，Mode 使您能够指定 PDF 内容的识别模式。您可以为此属性指定 RecognitionMode 枚举中的任意值。这些值各有具体的优势和限制：

步骤：在 Python 中将 PDF 转换为 DOC

1. 将 PDF 加载到 `ap.Document` 对象中。
1. 创建 `DocSaveOptions` 实例。
1. 将 format 属性设置为 `DocFormat.DOC`，以确保输出为 .doc 格式（旧版 Word 格式）。
1. 使用指定的保存选项将 PDF 保存为 Word 文档。
1. 打印确认信息。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.DocSaveOptions()
    save_options.format = apdf.DocSaveOptions.DocFormat.DOC
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 DOC**

Aspose.PDF for Python 为您提供在线免费应用程序 ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)，您可以尝试了解其功能和质量。

[![Convert PDF to DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## 将 PDF 转换为 DOCX

Aspose.PDF for Python API 让您使用 Python via .NET 读取并将 PDF 文档转换为 DOCX。DOCX 是一种广为人知的 Microsoft Word 文档格式，其结构已从纯二进制更改为 XML 与二进制文件的组合。Docx 文件可以在 Word 2007 及更高版本中打开，但无法在仅支持 DOC 文件扩展名的早期 MS Word 版本中打开。

以下 Python 代码片段展示了将 PDF 文件转换为 DOCX 格式的过程。

步骤：在 Python 中将 PDF 转换为 DOCX

1. 使用 `ap.Document` 加载源 PDF。
1. 创建 `DocSaveOptions` 实例。
1. 将 format 属性设置为 `DocFormat.DOC_X`，以生成 .docx 文件（现代 Word 格式）。
1. 使用配置好的保存选项将 PDF 保存为 DOCX 文件。
1. 转换后打印确认信息。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.DocSaveOptions()
    save_options.format = apdf.DocSaveOptions.DocFormat.DOC_X
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

[DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) 类具有名为 Format 的属性，可用于指定生成文档的格式，即 DOC 或 DOCX。要将 PDF 文件转换为 DOCX 格式，请使用 DocSaveOptions.DocFormat 枚举中的 Docx 值。

{{% alert color="warning" %}}
**尝试在线将 PDF 转换为 DOCX**

Aspose.PDF for Python 为您提供在线免费应用程序 ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)，您可以尝试了解其功能和质量。

[![Aspose.PDF Convertion PDF to Word Free App](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

