---
title: 在 Python 中将 PDF 转换为 EPUB、LaTeX、Text、XPS
linktitle: 将 PDF 转换为其他格式
type: docs
weight: 90
url: /zh/python-net/convert-pdf-to-other-files/
lastmod: "2025-09-27"
description: 本主题向您展示如何使用 Python 将 PDF 文件转换为 EPUB、LaTeX、Text、XPS 等其他文件格式。
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 如何在 Python 中将 PDF 转换为其他格式
Abstract: 本文提供了使用 Aspose.PDF for Python 将 PDF 文件转换为各种格式的全面指南。内容涵盖将 PDF 转换为 EPUB、LaTeX/TeX、Text、XPS 和 XML 格式。每个章节均以邀请读者尝试 Aspose 提供的在线免费应用程序来将 PDF 转换为相应格式开始，强调这些工具的易用性和高质量。
---

## 将 PDF 转换为 EPUB

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 EPUB**

Aspose.PDF for Python 为您提供在线免费应用程序 ["PDF 转 EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)，您可以在其中尝试了解其功能和质量。

[![Aspose.PDF 转换 PDF 为 EPUB 的免费应用](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="电子出版物">EPUB</abbr> 是由国际数字出版论坛（IDPF）制定的免费且开放的电子书标准。文件扩展名为 .epub。
EPUB 旨在支持可重排的内容，这意味着 EPUB 阅读器可以针对特定显示设备优化文本。EPUB 还支持固定布局的内容。该格式旨在成为出版商和转换机构可内部使用的统一格式，同时用于分发和销售。它取代了 Open eBook 标准。

Aspose.PDF for Python 也支持将 PDF 文档转换为 EPUB 格式的功能。Aspose.PDF for Python 提供名为 'EpubSaveOptions' 的类，可作为 [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法的第二个参数，用于生成 EPUB 文件。
请尝试使用以下代码片段在 Python 中实现此需求。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = (
        ap.EpubSaveOptions.RecognitionMode.FLOW
    )
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## 将 PDF 转换为 LaTeX/TeX

**Aspose.PDF for Python via .NET** 支持将 PDF 转换为 LaTeX/TeX。
LaTeX 文件格式是一种带有特殊标记的文本文件格式，用于基于 TeX 的文档排版系统，以实现高质量的排版。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 LaTeX/TeX**

Aspose.PDF for Python 为您提供在线免费应用程序 ["PDF 转 LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)，您可以在其中尝试了解其功能和质量。

[![Aspose.PDF 转换 PDF 为 LaTeX/TeX 的免费应用](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

要将 PDF 文件转换为 TeX，Aspose.PDF 提供了 [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) 类，该类提供 OutDirectoryPath 属性，用于在转换过程中保存临时图像。

以下代码片段展示了使用 Python 将 PDF 文件转换为 TEX 格式的过程。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.LaTeXSaveOptions()

    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

## 将 PDF 转换为 Text

**Aspose.PDF for Python** 支持将整个 PDF 文档或单页转换为 Text 文件。您可以使用 'TextDevice' 类将 PDF 文档转换为 TXT 文件。以下代码片段说明了如何从所有页面提取文本。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 Text**

Aspose.PDF for Python 为您提供在线免费应用程序 ["PDF 转 Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)，您可以在其中尝试了解其功能和质量。

[![Aspose.PDF 转换 PDF 为 Text 的免费应用](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## 将 PDF 转换为 XPS

**Aspose.PDF for Python** 提供了将 PDF 文件转换为 XPS 格式的可能性。让我们尝试使用下面的代码片段在 Python 中将 PDF 文件转换为 XPS 格式。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 XPS**

Aspose.PDF for Python 为您提供在线免费应用程序 ["PDF 转 XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)，您可以在其中尝试了解其功能和质量。

[![Aspose.PDF 转换 PDF 为 XPS 的免费应用](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPS 文件类型主要与微软公司的 XML Paper Specification（XML 纸张规范）相关联。XML Paper Specification（XPS），前代号为 Metro，并整合了下一代打印路径（NGPP）营销概念，是微软将文档创建和查看集成到 Windows 操作系统中的倡议。

要将 PDF 文件转换为 XPS，Aspose.PDF 提供了 [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) 类，该类作为第二个参数传递给 [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法，以生成 XPS 文件。

以下代码片段展示了将 PDF 文件转换为 XPS 格式的过程。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## 将 PDF 转换为 MD

Aspose.PDF 有类 'MarkdownSaveOptions()'，它可以在保留图像和资源的同时将 PDF 文档转换为 Markdown (MD) 格式。

1. 使用 'ap.Document' 加载源 PDF。
1. 创建 'MarkdownSaveOptions' 的实例。
1. 将 'resources_directory_name' 设置为 'images' ——提取的图像将存储在此文件夹中。
1. 使用配置的选项保存转换后的 Markdown 文档。
1. 转换完成后打印确认信息。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.MarkdownSaveOptions()
    # save_options.extract_vector_graphics = True
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

一个包含文本和已链接图像的 Markdown 文件，图像存储在指定的 images 文件夹中。

## 将 PDF 转换为 MobiXML

此方法将 PDF 文档转换为 MOBI (MobiXML) 格式，该格式常用于 Kindle 设备的电子书。

1. 使用 'ap.Document' 加载源 PDF 文档。
1. 使用格式 'ap.SaveFormat.MOBI_XML' 保存文档。
1. 转换完成后打印确认信息。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.save(path_outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)
```
