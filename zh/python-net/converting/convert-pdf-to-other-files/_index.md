---
title: 将 PDF 转换为 EPUB、LaTeX、文本、XPS 在 Python 中
linktitle: 将 PDF 转换为其他格式
type: docs
weight: 90
url: zh/python-net/convert-pdf-to-other-files/
lastmod: "2022-12-23"
keywords: 转换, PDF, EPUB, LaText, 文本, XPS, Python
description: 本主题向您展示如何使用 Python 将 PDF 文件转换为其他文件格式，如 EPUB、LaTeX、文本、XPS 等。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 将 PDF 转换为 EPUB

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 EPUB**

Aspose.PDF for Python 为您提供了一个在线免费应用程序 ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 为 EPUB 通过免费应用程序](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="电子出版物">EPUB</abbr>** 是国际数字出版论坛 (IDPF) 的一个免费和开放的电子书标准。
 文件扩展名为.epub。  
EPUB设计用于可重排内容，这意味着EPUB阅读器可以为特定显示设备优化文本。EPUB还支持固定布局内容。该格式旨在作为一种单一格式，供出版商和转换公司在内部使用，以及用于分发和销售。它取代了Open eBook标准。

Aspose.PDF for Python还支持将PDF文档转换为EPUB格式的功能。Aspose.PDF for Python有一个名为'EpubSaveOptions'的类，可以用作[save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)方法的第二个参数，以生成EPUB文件。  
请尝试使用以下代码片段来使用Python实现此要求。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_epub.epub"
    # 打开PDF文档
    document = ap.Document(input_pdf)

    # 实例化Epub保存选项
    save_options = ap.EpubSaveOptions()

    # 指定内容的布局
    save_options.content_recognition_mode = ap.EpubSaveOptions.RecognitionMode.FLOW

    # 保存ePUB文档
    document.save(output_pdf, save_options)
```

## 将 PDF 转换为 LaTeX/TeX

**Aspose.PDF for Python via .NET** 支持将 PDF 转换为 LaTeX/TeX。LaTeX 文件格式是一种带有特殊标记的文本文件格式，用于基于 TeX 的文档准备系统，以实现高质量的排版。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 LaTeX/TeX**

Aspose.PDF for Python 为您提供免费的在线应用程序 ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 到 LaTeX/TeX 的免费应用程序](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

要将 PDF 文件转换为 TeX，Aspose.PDF 提供了 [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) 类，该类提供 OutDirectoryPath 属性用于在转换过程中保存临时图像。

以下代码片段展示了使用 Python 将 PDF 文件转换为 TEX 格式的过程。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_tex.tex"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)
    # 实例化 LaTeXSaveOptions 对象
    saveOptions = ap.LaTeXSaveOptions()
    document.save(output_pdf, saveOptions)
```

## 将 PDF 转换为文本

**Aspose.PDF for Python** 支持将整个 PDF 文档和单个页面转换为文本文件。

### 将 PDF 文档转换为文本文件

您可以使用 'TextDevice' 类将 PDF 文档转换为 TXT 文件。

以下代码片段说明了如何从所有页面中提取文本。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_txt.txt"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)

    # 创建文本设备
    textDevice = ap.devices.TextDevice()

    # 转换特定页面并保存
    textDevice.process(document.pages[1], output_pdf)
```
**尝试在线转换 PDF 为文本**

{{% alert color="success" %}}

[![Aspose.PDF 转换 PDF 为文本的免费应用程序](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## 将 PDF 转换为 XPS

**Aspose.PDF for Python** 提供了将 PDF 文件转换为 <abbr title="XML Paper Specification">XPS</abbr> 格式的可能性。让我们尝试使用所提供的代码片段将 PDF 文件转换为 Python 中的 XPS 格式。

{{% alert color="success" %}}
**尝试在线转换 PDF 为 XPS**

Aspose.PDF for Python 为您提供了在线免费应用程序["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)，您可以在其中尝试调查其功能和工作质量。

[![Aspose.PDF 转换 PDF 为 XPS 的免费应用程序](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPS 文件类型主要与 Microsoft Corporation 的 XML 纸张规范相关联。XML 纸张规范（XPS），以前代号为 Metro，并且包含下一代打印路径（NGPP）营销概念，是微软将文档创建和查看集成到 Windows 操作系统中的一项计划。

为了将 PDF 文件转换为 XPS，Aspose.PDF 提供了类 [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/)，用于作为 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法的第二个参数来生成 XPS 文件。

以下代码片段展示了将 PDF 文件转换为 XPS 格式的过程。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xps.xps"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)

    # 实例化 XPS 保存选项
    save_options = ap.XpsSaveOptions()

    # 保存 XPS 文档
    document.save(output_pdf, save_options)
```

## 转换 PDF 为 XML

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 XML**

Aspose.PDF for Python 为您提供了一个在线免费应用程序 ["PDF to XML"](https://products.aspose.app/pdf/conversion/pdf-to-xml)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将 PDF 转换为 XML](pdf_to_xml.png)](https://products.aspose.app/pdf/conversion/pdf-to-xml)
{{% /alert %}}

<abbr title="可扩展标记语言">XML</abbr> 是一种用于存储、传输和重构任意数据的标记语言和文件格式。

Aspose.PDF for Python 还支持将 PDF 文档转换为 XML 格式的功能。Aspose.PDF for Python 有一个名为 'XmlSaveOptions' 的类，可以用作 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法的第二个参数，以生成 XML 文件。请尝试使用以下代码片段来完成此需求。

```python

    import aspose.pdf as ap

    def convert_pdf_to_xml(self, infile, outfile):
        path_infile = self.dataDir + infile
        path_outfile = self.dataDir + outfile

        # 打开 PDF 文档

        document = ap.Document(path_infile)

        # 实例化 XML 保存选项
        save_options = ap.XmlSaveOptions()

        # 保存 XML 文档
        document.save(path_outfile, save_options)
        print(infile + " 已转换为 " + outfile)
```