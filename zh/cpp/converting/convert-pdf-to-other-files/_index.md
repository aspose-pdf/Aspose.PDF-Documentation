---
title: 将PDF文件转换为其他格式
linktitle: 将PDF转换为其他格式
type: docs
weight: 90
url: zh/cpp/convert-pdf-to-other-files/
lastmod: "2021-11-19"
description: 本主题向您展示如何使用Aspose.PDF将PDF文件转换为其他文件格式。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 将PDF转换为EPUB

{{% alert color="success" %}}
**尝试在线将PDF转换为EPUB**

Aspose.PDF for C++为您提供在线免费应用程序["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)，您可以在此尝试研究其功能和工作质量。

[![Aspose.PDF使用免费应用程序将PDF转换为EPUB](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="电子出版物">EPUB</abbr>（电子出版物的缩写）是国际数字出版论坛（IDPF）制定的免费开放电子书标准。文件扩展名为.epub。
EPUB旨在用于可重排内容，这意味着EPUB阅读器可以针对特定的显示设备优化文本。 EPUB 也支持固定布局内容。该格式旨在作为一种单一格式，供出版商和转换公司在内部使用，以及用于分发和销售。它取代了 Open eBook 标准。

Aspose.PDF for C++ 也支持将 PDF 文档转换为 EPUB 格式的功能。Aspose.PDF for C++ 有一个名为 EpubSaveOptions 的类，可以作为 [`Document.Save(..)`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) 方法的第二个参数来生成 EPUB 文件。
请尝试使用以下代码片段通过 C++ 完成此要求。

```cpp
void ConvertPDFtoEPUB()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 用于路径名的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 输入文件名的字符串
    String infilename("sample.pdf");
    // 输出文件名的字符串
    String outfilename("PDFToEPUB_out.epub");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 将 PDF 文件保存为 EPUB 格式
    document->Save(_dataDir + outfilename, SaveFormat::Epub);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## 将 PDF 转换为 LaTeX/TeX

**Aspose.PDF for C++** 支持将 PDF 转换为 LaTeX/TeX。LaTeX 文件格式是一种具有特殊标记的文本文件格式，用于基于 TeX 的文档准备系统中的高质量排版。

为了将 PDF 文件转换为 TeX，Aspose.PDF 提供了类 [LaTeXSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.la_te_x_save_options)，它提供了属性 OutDirectoryPath 用于在转换过程中保存临时图像。

以下代码片段展示了使用 C++ 将 PDF 文件转换为 TEX 格式的过程。

```cpp
void ConvertPDFtoLaTeX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 输入文件名的字符串
    String infilename("sample.pdf");
    // 输出文件名的字符串
    String outfilename("PDFToTeX_out.tex");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 实例化 LaTex 保存选项
    auto saveOptions = MakeObject<LaTeXSaveOptions>();

    // 设置保存选项对象的输出目录路径
    saveOptions->set_OutDirectoryPath(_dataDir);

    // 将 PDF 文件保存为 LaTex 格式
    document->Save(_dataDir + outfilename, saveOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 LaTeX/TeX**

Aspose.PDF for C++ 向您提供免费的在线应用程序 ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)，您可以在其中尝试调查其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将 PDF 转换为 LaTeX/TeX](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## 将 PDF 转换为文本

**Aspose.PDF for C++** 支持将整个 PDF 文档和单页转换为文本文件。

### 将整个 PDF 文档转换为文本文件

您可以使用 [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_absorber/) 类将 PDF 文档转换为 TXT 文件。

以下代码片段说明了如何从所有页面提取文本。

```cpp
void ConvertPDFDocToTXT()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 输入文件名的字符串
    String infilename("sample.pdf");
    // 输出文件名的字符串
    String outfilename("input_Text_Extracted_out.txt");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto ta = MakeObject<TextAbsorber>();
    ta->Visit(document);
    // 将提取的文本保存在文本文件中
    System::IO::File::WriteAllText(_dataDir + outfilename, ta->get_Text());
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### 将PDF页面转换为文本文件

您可以使用Aspose.PDF for C++将PDF文档转换为TXT文件。您应该使用[TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_absorber/)类来解决此任务。

以下代码片段解释了如何从特定页面提取文本。

```cpp
void ConvertPDFPagestoTXT()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 输入文件名的字符串
    String infilename("sample-4pages.pdf");
    // 输出文件名的字符串
    String outfilename("sample-4pages_out.txt");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto ta = MakeObject<TextAbsorber>();

    auto pages = { 1, 3, 4 };
    try {
    for (auto page : pages)
    {
    ta->Visit(document->get_Pages()->idx_get(page));
    }
    // 将提取的文本保存在文本文件中
    auto text = ta->get_Text();
    System::IO::File::WriteAllText(_dataDir + outfilename, text);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为文本**

Aspose.PDF for C++ 为您提供在线免费应用程序 ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将 PDF 转换为文本](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## 将 PDF 转换为 XPS

**Aspose.PDF for C++** 提供将 PDF 文件转换为 <abbr title="XML Paper Specification">XPS</abbr> 格式的可能性。让我们尝试使用提供的代码片段将 PDF 文件转换为 C++ 中的 XPS 格式。

XPS 文件类型主要与 Microsoft Corporation 的 XML Paper Specification 相关联。XML Paper Specification (XPS)，以前代号为 Metro，并包含下一代打印路径 (NGPP) 营销概念，是微软将文档创建和查看集成到 Windows 操作系统中的举措。

要将 PDF 文件转换为 XPS，Aspose.PDF 提供了类 [XpsSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.xps_save_options)，它用作 [Document.Save(..)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) 方法的第二个参数，以生成 XPS 文件。

将 PDF 文件转换为 XPS 格式的过程如下代码片段所示。

```cpp
void ConvertPDFtoXPS()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 输入文件名称的字符串
    String infilename("sample.pdf");
    // 输出文件名称的字符串
    String outfilename("PDFToXPS_out.xps");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 实例化 LaTex 保存选项
    auto saveOptions = MakeObject<XpsSaveOptions>();

    // 将 PDF 文件保存为 XPS 格式
    document->Save(_dataDir + outfilename, saveOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 SVG**

Aspose.PDF for C++ 为您提供在线免费应用程序 ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)，您可以在其中尝试研究其功能和工作质量。


[![Aspose.PDF 将 PDF 转换为 SVG 的免费应用](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}
