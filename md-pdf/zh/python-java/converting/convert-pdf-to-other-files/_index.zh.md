---
title: 将PDF转换为EPUB、LaTeX、文本、XPS格式在Python中
linktitle: 将PDF转换为其他格式
type: docs
weight: 90
url: /python-java/convert-pdf-to-other-files/
lastmod: "2023-04-06"
keywords: convert, PDF, EPUB, LaText, Text, XPS, Python
description: 本主题向您展示如何使用Python将PDF文件转换为其他文件格式，如EPUB、LaTeX、文本、XPS等。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 将PDF转换为EPUB

{{% alert color="success" %}}
**尝试在线将PDF转换为EPUB**

Aspose.PDF for Python为您提供在线免费应用程序["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF 转换PDF到EPUB的免费应用程序](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="电子出版物">EPUB</abbr>** 是国际数字出版论坛（IDPF）的一种免费和开放的电子书标准。
 文件具有扩展名 .epub。  
EPUB 旨在用于可重排内容，这意味着 EPUB 阅读器可以为特定显示设备优化文本。EPUB 也支持固定布局内容。该格式旨在作为出版商和转换公司可以在内部使用以及用于分发和销售的单一格式。它取代了 Open eBook 标准。

Aspose.PDF for Python 还支持将 PDF 文档转换为 EPUB 格式的功能。Aspose.PDF for Python 有一个名为 'EpubSaveOptions' 的类，可以用作 [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) 方法的第二个参数，以生成 EPUB 文件。  
请尝试使用以下代码片段来使用 Python 实现此需求。

```python

from asposepdf import Api

# 初始化许可证
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# 转换为 Epub
documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.epub"
doc.save(documentOutName, Api.SaveFormat.Epub)
```

## 将 PDF 转换为 LaTeX/TeX

**Aspose.PDF for Python via Java** 支持将 PDF 转换为 LaTeX/TeX。 LaTeX 文件格式是一种具有特殊标记的文本文件格式，用于基于 TeX 的文档准备系统，以实现高质量的排版。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 LaTeX/TeX**

Aspose.PDF for Python 为您提供在线免费应用程序 ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF Convertion PDF to LaTeX/TeX with Free App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

要将 PDF 文件转换为 TeX，Aspose.PDF 提供了类 [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/latexsaveoptions/)，它提供了属性 OutDirectoryPath，用于在转换过程中保存临时图像。

以下代码片段展示了使用 Python 将 PDF 文件转换为 TEX 格式的过程。

```python
from asposepdf import Api

documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.tex"
doc.save(documentOutName, Api.SaveFormat.TeX)
```

## 将 PDF 转换为文本

**Aspose.PDF for Python** 支持将整个 PDF 文档和单个页面转换为文本文件。

### 将 PDF 文档转换为文本文件

您可以使用 'TextDevice' 类将 PDF 文档转换为 TXT 文件。

以下代码片段说明了如何从所有页面提取文本。

```python

from asposepdf import Api, Device

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_text"
# 打开 PDF 文档
document = Api.Document(input_pdf)

device = Device.TextDevice()

for i in range(0, document.getPages.size):
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.txt"
    # 转换特定页面并保存为文本文件
    device.process(document.getPages.getPage(i + 1), imageFileName)
`
**尝试在线将 PDF 转换为文本**

Aspose.PDF for Python 为您提供了一个在线免费应用程序 ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 为文本的免费应用](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## 将 PDF 转换为 XPS

**Aspose.PDF for Python** 提供了将 PDF 文件转换为 <abbr title="XML Paper Specification">XPS</abbr> 格式的可能性。让我们尝试使用所提供的代码片段将 PDF 文件转换为 Python 的 XPS 格式。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 XPS**

Aspose.PDF for Python 为您提供了一个在线免费应用程序 ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 为 XPS 的免费应用](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPS 文件类型主要与 Microsoft Corporation 的 XML Paper Specification 相关联。XML Paper Specification (XPS) 以前代号为 Metro，并包含下一代打印路径 (NGPP) 营销概念，是微软将文档创建和查看集成到 Windows 操作系统中的举措。

要将 PDF 文件转换为 XPS，Aspose.PDF 提供了 [XpsSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/xpssaveoptions/) 类，用作 [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) 方法的第二个参数来生成 XPS 文件。

以下代码片段展示了将 PDF 文件转换为 XPS 格式的过程。

```python

from asposepdf import Api

documentName = "../../testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "../../testout/out.xps"
doc.save(documentOutName, Api.SaveFormat.Xps)

```