---
title: 在 Python 中将其他文件格式转换为 PDF
linktitle: 将其他文件格式转换为 PDF
type: docs
weight: 80
url: /zh/python-net/convert-other-files-to-pdf/
lastmod: "2025-09-01"
description: This topic show you how to Aspose.PDF allows to convert other file formats such as EPUB, MD, PCL, XPS, PS, XML and LaTeX to PDF document.
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 如何在 Python 中将其他文件格式转换为 PDF
Abstract: 本文提供了使用 Python 将各种文件格式转换为 PDF 的全面指南，利用 Aspose.PDF for Python via .NET 的功能。本文档概述了多种格式的转换过程，包括 EPUB、Markdown、PCL、文本、XPS、PostScript、XML、XSL-FO 和 LaTeX/TeX。每个章节提供了具体的代码片段和实现这些转换的说明。文章强调了 Aspose.PDF 功能的实用性，如针对每种文件类型定制的加载选项，以确保转换的准确性和高效性。此外，还突出显示了免费在线转换应用程序的可用性，供用户亲自体验其功能。该指南是开发者在其 Python 应用中集成 PDF 转换能力的实用资源。
---

本文解释了如何 **使用 Python 将各种其他文件格式转换为 PDF**。它涵盖了以下主题。

## 将 OFD 转换为 PDF

OFD 代表开放固定布局文档（也称为开放固定文档格式）。它是中国的国家标准（GB/T 33190-2016）用于电子文档，作为 PDF 的替代方案推出。

在 Python 中将 OFD 转换为 PDF 的步骤：

1. 使用 OfdLoadOptions() 设置 OFD 加载选项。
1. 加载 OFD 文档。
1. 保存为 PDF。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.OfdLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## 将 LaTeX/TeX 转换为 PDF

LaTeX 文件格式是一种基于 TeX 系列语言的 LaTeX 派生标记的文本文件格式，LaTeX 是 TeX 系统的衍生格式。LaTeX（ˈleɪtɛk/lay-tek 或 lah-tek）是一种文档排版系统和文档标记语言。它被广泛用于许多领域的科学文献交流和出版，包括数学、物理和计算机科学。它在包含复杂多语言材料（如韩语、日语、汉字和阿拉伯语）的书籍和文章的准备和出版中也起着关键作用，包括特刊。

LaTeX 使用 TeX 排版程序来格式化其输出，并且本身是用 TeX 宏语言编写的。

{{% alert color="success" %}}
**尝试在线将 LaTeX/TeX 转换为 PDF**

Aspose.PDF for Python via .NET 为您提供在线免费应用程序 ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf)，您可以尝试了解其功能和工作质量。

[![Aspose.PDF 将 LaTeX/TeX 转换为 PDF 免费应用](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

在 Python 中将 TEX 转换为 PDF 的步骤：

1. 使用 LatexLoadOptions() 设置 LaTeX 加载选项。
1. 加载 LaTeX 文档。
1. 保存为 PDF。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.LatexLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```
## 将 OFD 转换为 PDF

OFD 代表开放固定布局文档（有时称为开放固定文档格式）。它是中国的国家标准（GB/T 33190-2016）用于电子文档，作为 PDF 的替代方案。

在 Python 中将 OFD 转换为 PDF 的步骤：

1. 使用 OfdLoadOptions() 设置 OFD 加载选项。
1. 加载 OFD 文档。
1. 保存为 PDF。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.OfdLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## 将 LaTeX/TeX 转换为 PDF

LaTeX 文件格式是一种基于 TeX 系列语言的 LaTeX 派生标记的文本文件格式，LaTeX 是 TeX 系统的衍生格式。LaTeX（ˈleɪtɛk/lay-tek 或 lah-tek）是一种文档排版系统和文档标记语言。它被广泛用于许多领域的科学文献交流和出版，包括数学、物理和计算机科学。它在包含复杂多语言材料（如梵语和阿拉伯语）的书籍和文章的准备和出版中也具有重要作用，包括批判版。LaTeX 使用 TeX 排版程序来格式化其输出，并且本身是用 TeX 宏语言编写的。

{{% alert color="success" %}}
**尝试在线将 LaTeX/TeX 转换为 PDF**

Aspose.PDF for Python via .NET 为您提供在线免费应用程序 ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf)，您可以尝试了解其功能和工作质量。

[![Aspose.PDF 将 LaTeX/TeX 转换为 PDF 免费应用](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

在 Python 中将 TEX 转换为 PDF 的步骤：

1. 使用 LatexLoadOptions() 设置 LaTeX 加载选项。
1. 加载 LaTeX 文档。
1. 保存为 PDF。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.LatexLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## 将 EPUB 转换为 PDF

**Aspose.PDF for Python via .NET** 让您轻松将 EPUB 文件转换为 PDF 格式。

EPUB（全称 electronic publication）是一种由国际数字出版论坛（IDPF）推出的免费开源电子书标准。文件扩展名为 .epub。EPUB 旨在提供可重排的内容，这意味着 EPUB 阅读器可以针对特定显示设备优化文本。

<abbr title="电子出版物">EPUB</abbr> 也支持固定布局内容。该格式旨在作为单一格式，供出版商和转换机构内部使用以及用于分发和销售。它取代了 Open eBook 标准。EPUB 3 版本也得到了图书行业研究小组（BISG）的认可，BISG 是一个领先的图书贸易协会，提供标准化最佳实践、研究、信息和活动，旨在对内容进行包装。

{{% alert color="success" %}}
**尝试在线将 EPUB 转换为 PDF**

Aspose.PDF for Python via .NET 为您提供在线免费应用程序 ["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf)，您可以尝试了解其功能和质量。

[![Aspose.PDF 将 EPUB 转换为 PDF 的免费应用](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

在 Python 中将 EPUB 转换为 PDF 的步骤：

1. 使用 EpubLoadOptions() 加载 EPUB 文档。
1. 将 EPUB 转换为 PDF。
1. 打印确认信息。

下面的代码片段演示如何使用 Python 将 EPUB 文件转换为 PDF 格式。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.EpubLoadOptions()
    document = ap.Document(path_infile, load_options)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## 将 Markdown 转换为 PDF

**此功能支持 19.6 版或更高版本。**

{{% alert color="success" %}}
**尝试在线将 Markdown 转换为 PDF**

Aspose.PDF for Python via .NET 为您提供在线免费应用程序 ["Markdown to PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf)，您可以尝试了解其功能和质量。

[![Aspose.PDF 将 Markdown 转换为 PDF 的免费应用](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

这段由 Aspose.PDF for Python via .NET 提供的代码片段帮助将 Markdown 文件转换为 PDF，实现更好的文档共享、格式保持以及打印兼容性。

以下代码片段展示了如何使用 Aspose.PDF 库实现该功能：

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.MdLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## 将 PCL 转换为 PDF

<abbr title="打印机指令语言">PCL</abbr>（打印机指令语言）是一种由惠普开发的打印机语言，用于访问标准打印机功能。PCL 1 到 5e/5c 级别是基于命令的语言，使用控制序列按接收顺序进行处理和解释。在消费者层面，PCL 数据流由打印驱动生成。自定义应用程序也可以轻松生成 PCL 输出。

{{% alert color="success" %}}
**尝试在线将 PCL 转换为 PDF**

Aspose.PDF for for .NET 为您提供在线免费应用程序 ["PCL to PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf)，您可以尝试了解其功能和质量。

[![Aspose.PDF 将 PCL 转换为 PDF 的免费应用](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

为了实现 PCL 到 PDF 的转换，Aspose.PDF 提供了类 [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions)，用于初始化 LoadOptions 对象。随后在 Document 对象初始化时将该对象作为参数传入，帮助 PDF 渲染引擎确定源文档的输入格式。

以下代码片段展示了将 PCL 文件转换为 PDF 格式的过程。

在 Python 中将 PCL 转换为 PDF 的步骤：

1. 使用 PclLoadOptions() 加载 PCL 的选项。
1. 加载文档。
1. 保存为 PDF。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.PclLoadOptions()
    load_options.supress_errors = True

    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## 将预格式化文本转换为 PDF

**Aspose.PDF for Python via .NET** 支持将纯文本和预格式化文本文件转换为 PDF 格式的功能。

将文本转换为 PDF 意味着将文本片段添加到 PDF 页面中。对于文本文件，我们处理两种类型的文本：预格式化（例如，每行 80 个字符的 25 行）和非格式化文本（纯文本）。根据需求，我们可以自行控制添加方式，也可以交由库的算法处理。

{{% alert color="success" %}}
**尝试在线将 TEXT 转换为 PDF**

Aspose.PDF for Python via .NET 为您提供在线免费应用程序 ["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf)，您可以尝试了解其功能和质量。

[![Aspose.PDF 将 TEXT 转换为 PDF 的免费应用](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

在 Python 中将 TEXT 转换为 PDF 的步骤：

1. 按行读取输入的文本文件。
1. 设置等宽字体（Courier New），以保持文本对齐一致。
1. 创建新 PDF 文档并添加第一页，设置自定义边距和字体。
1. 遍历文本文件的每一行。为了模拟打字机效果，我们使用 'monospace_font' 字体，大小为 12。
1. 将页数限制为 4 页。
1. 将最终的 PDF 保存到指定路径。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    with open(path_infile, "r") as file:
        lines = file.readlines()

    monospace_font = ap.text.FontRepository.find_font("Courier New")

    document = ap.Document()
    page = document.pages.add()

    page.page_info.margin.left = 20
    page.page_info.margin.right = 10
    page.page_info.default_text_state.font = monospace_font
    page.page_info.default_text_state.font_size = 12
    count = 1
    for line in lines:
        if line != "" and line[0] == "\x0c":
            page = document.pages.add()
            page.page_info.margin.left = 20
            page.page_info.margin.right = 10
            page.page_info.default_text_state.font = monospace_font
            page.page_info.default_text_state.font_size = 12
            count = count + 1
        else:
            text = ap.text.TextFragment(line)
            page.paragraphs.add(text)

        if count == 4:
            break

    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## 将 PostScript 转换为 PDF

本示例演示如何使用 Aspose.PDF for Python via .NET 将 PostScript 文件转换为 PDF 文档。

1. 创建 'PsLoadOptions' 实例，以正确解释 PS 文件。
1. 使用加载选项将 'PostScript' 文件加载到 Document 对象中。
1. 将文档以 PDF 格式保存到所需的输出路径。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.PsLoadOptions()

    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## 将 XPS 转换为 PDF

**Aspose.PDF for Python via .NET** 支持将 <abbr title="XML Paper Specification">XPS</abbr> 文件转换为 PDF 格式。检查本文以解决您的任务。

XPS 文件类型主要与微软公司推出的 XML Paper Specification（XPS）相关。XML Paper Specification（XPS），前代号为 Metro 并包含下一代打印路径（NGPP）营销概念，是微软将文档创建和查看集成到其 Windows 操作系统中的倡议。

以下代码片段展示了使用 Python 将 XPS 文件转换为 PDF 格式的过程。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.XpsLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**尝试在线将 XPS 格式转换为 PDF**

Aspose.PDF for Python via .NET 为您提供在线免费应用程序 ["XPS 转 PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/)，您可以尝试了解其功能和质量。

[![Aspose.PDF 转换 XPS 到 PDF 的免费应用](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## 将 XSL-FO 转换为 PDF

以下代码片段可用于使用 Aspose.PDF for Python via .NET 将 XSL-FO 转换为 PDF 格式：

```python

    from os import path
    import aspose.pdf as ap

    path_xsltfile = path.join(self.data_dir, xsltfile)
    path_xmlfile = path.join(self.data_dir, xmlfile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.XslFoLoadOptions(path_xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately
    )
    document = ap.Document(path_xmlfile, load_options)
    document.save(path_outfile)

    print(xmlfile + " converted into " + outfile)
```

## 将 XML 与 XSLT 转换为 PDF

本示例演示如何通过先使用 XSLT 模板将 XML 文件转换为 HTML，然后将 HTML 加载到 Aspose.PDF 中，从而将 XML 文件转换为 PDF。

1. 创建 'HtmlLoadOptions' 实例，以配置 HTML 转 PDF 的转换。
1. 将转换后的 HTML 文件加载到 Aspose.PDF Document 对象中。
1. 将文档保存为 PDF，放置于指定的输出路径。
1. 成功转换后，删除临时的 HTML 文件。

```python

    from os import path
    import aspose.pdf as ap

    def transform_xml_to_html(xml_file, xslt_file, html_file):
        from lxml import etree
        """
        Transform XML to HTML using XSLT and return as a stream
        """
        # Parse XML document
        xml_doc = etree.parse(xml_file)

        # Parse XSLT stylesheet
        xslt_doc = etree.parse(xslt_file)
        transform = etree.XSLT(xslt_doc)

        # Apply transformation
        result = transform(xml_doc)

        # Save result to HTML file
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(str(result))


    def convert_XML_to_PDF(template, infile, outfile):
        path_infile = path.join(data_dir, infile)
        path_outfile = path.join(data_dir, "python", outfile)
        path_template = path.join(data_dir, template)
        path_temp_file = path.join(data_dir, "temp.html")

        load_options = ap.HtmlLoadOptions()
        transform_xml_to_html(path_infile, path_template, path_temp_file)

        document = ap.Document(path_temp_file, load_options)
        document.save(path_outfile)

        if path.exists(path_temp_file):
            os.remove(path_temp_file)

        print(infile + " converted into " + outfile)
```

