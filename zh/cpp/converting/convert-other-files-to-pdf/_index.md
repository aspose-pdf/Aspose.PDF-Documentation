---
linktitle: 将其他文件格式转换为PDF
type: docs
weight: 80
url: zh/cpp/convert-other-files-to-pdf/
lastmod: "2021-11-19"
description: 本主题向您展示如何使用Aspose.PDF将其他文件格式转换为PDF文档。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 将EPUB转换为PDF

**Aspose.PDF for C++** 允许您简单地将EPUB文件转换为PDF格式。

<abbr title="electronic publication">EPUB</abbr>（电子出版物的缩写）是国际数字出版论坛（IDPF）制定的免费和开放的电子书标准。文件的扩展名为.epub。EPUB旨在用于可重排内容，这意味着EPUB阅读器可以为特定的显示设备优化文本。

EPUB还支持固定布局内容。 格式旨在作为出版商和转换公司可在内部使用的单一格式，也用于分发和销售。它取代了 Open eBook 标准。EPUB 3 版本还得到了图书行业研究小组（BISG）的认可，该小组是一个领先的图书贸易协会，致力于标准化最佳实践、研究、信息和活动，用于内容包装。

转换步骤：

1. 为路径名和文件名创建一个[String Class](https://reference.aspose.com/pdf/cpp/class/system.string)。
1. 创建一个[EpubLoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options)类的实例。
1. 创建一个带有指定源文件名和选项的[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)类的实例。
1. 加载并[保存](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)输入文件。

下面的代码片段展示了如何使用 C++ 将 EPUB 文件转换为 PDF 格式。

```cpp
void ConvertEPUBtoPDF()
{
    std::clog << "EPUB to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("aliceDynamic.epub");
    String outfilename("epub_test.pdf");
    auto options = MakeObject<EpubLoadOptions>();
    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << "EPUB to PDF convert: End" << std::endl;
}
```
{{% alert color="success" %}}
**尝试在线将EPUB转换为PDF**

Aspose.PDF for C++ 为您提供在线免费应用程序["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf)，您可以在此尝试研究其功能和工作质量。

[![Aspose.PDF Convertion EPUB to PDF with Free App](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## 将文本转换为PDF

**Aspose.PDF for C++** 支持将纯文本和预格式化文本文件转换为PDF格式的功能。

将文本转换为PDF意味着将文本片段添加到PDF页面。对于文本文件，我们处理两种类型的文本：预格式化文本（例如，每行80个字符的25行）和非格式化文本（纯文本）。根据我们的需要，我们可以自行控制这种添加，或者将其委托给库的算法。

### 将纯文本文件转换为PDF

对于纯文本文件，我们可以使用以下技术：

1. 创建一个用于路径名和文件名的[String Class](https://reference.aspose.com/pdf/cpp/class/system.string)。
1. 使用[TextReader](https://reference.aspose.com/pdf/cpp/class/system.i_o.text_reader/.）读取源文本文件。
1. 实例化[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)对象。
1. 向文档的页面集合中添加一个[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)。
1. 创建一个新的TextFragment对象，并将TextReader对象传递给其构造函数。
1. 在段落集合中添加一个新的文本段落，并传递TextFragment对象。
1. 加载并[保存](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)输入文件。

```cpp
void ConvertTextToPDF()
{
    std::clog << "Text to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.txt");
    String outfilename("TextToPDF.pdf");

    // 读取源文本文件
    String content = System::IO::File::ReadAllText(_dataDir + infilename);

    // 通过调用其空构造函数实例化一个Document对象
    auto document = MakeObject<Document>();

    // 在Document的Pages集合中添加一个新页面
    auto page = document->get_Pages()->Add();

    // 创建一个TextFragment实例，并将reader对象中的文本作为参数传递给其构造函数
    auto text = MakeObject<TextFragment>(content);

    // 在段落集合中添加一个新的文本段落，并传递TextFragment对象
    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // 保存生成的PDF文件
    document->Save(_dataDir + outfilename);
    std::clog << "Text to PDF convert: End" << std::endl;
}
```
### 将预格式化文本文件转换为PDF

转换预格式化文本类似于纯文本，但您需要进行一些额外的操作，例如设置边距、字体类型和大小。显然，该字体应为等宽字体（例如Courier New）。

按照以下步骤使用C++将预格式化文本转换为PDF：

1. 通过调用其空构造函数实例化一个Document对象。
1. 设置左右边距以获得更好的展示效果。
1. 实例化[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)对象并在Pages集合中添加新页面。
1. 加载和[保存](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)输入图像文件。

```CPP
void ConvertPreFormattedTextToPdf()
{
    std::clog << "Performatted Text to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("rfc822.txt");
    String outfilename("TextToPDF.pdf");
    // 将文本文件读取为字符串数组
    auto lines = System::IO::File::ReadAllLines(_dataDir + infilename);

    // 通过调用其空构造函数实例化Document对象
    auto document = MakeObject<Document>();

    // 在Document的Pages集合中添加新页面
    auto page = document->get_Pages()->Add();

    // 设置左右边距以获得更好的展示效果
    page->get_PageInfo()->get_Margin()->set_Left(20);
    page->get_PageInfo()->get_Margin()->set_Right(10);
    page->get_PageInfo()->get_DefaultTextState()->set_Font(FontRepository::FindFont(u"Courier New"));
    page->get_PageInfo()->get_DefaultTextState()->set_FontSize(12);

    for (int index = 0; index < lines->get_Length(); index++)
    {
        // 检查行是否包含“换页”字符
        // 参见 https://en.wikipedia.org/wiki/Page_break
        auto line = lines->idx_get(index);
        if (line.StartsWith(u"\x0c"))
        {
        if (document->get_Pages()->get_Count() > 3) break;
        page = document->get_Pages()->Add();
        // 设置左右边距以获得更好的展示效果
        page->get_PageInfo()->get_Margin()->set_Left(20);
        page->get_PageInfo()->get_Margin()->set_Right(10);
        page->get_PageInfo()->get_DefaultTextState()->set_Font(FontRepository::FindFont(u"Courier New"));
        page->get_PageInfo()->get_DefaultTextState()->set_FontSize(12);
        }
        else
        {
        // 创建TextFragment实例
        // 并将该行作为参数传递给其构造函数
        auto text = MakeObject<TextFragment>(line);

        // 在段落集合中添加新文本段落并传递TextFragment对象
        page->get_Paragraphs()->Add(text);
        }
    }

    // 保存生成的PDF文件
    document->Save(_dataDir + outfilename);
    std::clog << "Performatted Text to PDF convert: End" << std::endl;
}
```

{{% alert color="success" %}}
**尝试在线将文本转换为PDF**

Aspose.PDF for C++ 为您提供在线免费应用程序["文本到PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf)，您可以在其中尝试调查其功能和工作质量。

[![Aspose.PDF 将文本转换为PDF的免费应用程序](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

## 将XPS转换为PDF

**Aspose.PDF for C++** 支持将<abbr title="XML Paper Specification">XPS</abbr>文件转换为PDF格式的功能。查看本文以解决您的任务。

XPS文件类型主要与Microsoft Corporation的XML Paper Specification相关联。XML Paper Specification (XPS)，以前代号为Metro，并包含下一代打印路径(NGPP)营销概念，是Microsoft将文档创建和查看集成到其Windows操作系统中的举措。

{{% alert color="primary" %}}

该文件格式基本上是一个压缩的XML文件，主要用于分发和存储。 很难编辑，并且主要由Microsoft实现。

{{% /alert %}}

为了使用Aspose.PDF for C++将XPS转换为PDF，我们引入了一个名为[XpsLoadOption](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options)的类，用于初始化[LoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options)对象。随后，此对象在Document对象初始化期间作为参数传递，它帮助PDF渲染引擎确定源文档的输入格式。

以下代码段显示了使用C++将XPS文件转换为PDF格式的过程。

```cpp
void ConvertXPStoPDF()
{
    std::clog << "XPS to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.oxps");
    String outfilename("XPStoPDF.pdf");
    auto options = MakeObject<XpsLoadOptions>();
    try {
        auto document = MakeObject<Document>(_dataDir + infilename, options);
        document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
        std::cerr << ex->get_Message() << std::endl;
    };
    std::clog << "XPS to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**尝试将XPS格式在线转换为PDF**

Aspose.PDF for C++为您提供在线免费应用程序["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF转换XPS到PDF免费应用](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## 将XML转换为PDF

XML格式用于存储结构化数据。在Aspose.PDF中有几种方法可以将<abbr title="可扩展标记语言">XML</abbr>转换为PDF。

## 将XSL-FO转换为PDF

1. 创建路径名和文件名的[String类](https://reference.aspose.com/pdf/cpp/class/system.string)。
1. 实例化[XslFoLoadOption对象](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options)。
1. 设置错误处理策略。
1. 实例化[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)对象。
1. [保存](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) 输入图像文件。

```cpp
void Convert_XSLFO_to_PDF()
{
    std::clog << "XSL-FO 转换为 PDF：开始" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilenameXSL("c:\\samples\\employees.xslt");
    String infilenameXML("c:\\samples\\employees.xml");

    String outfilename("XMLFOtoPDF.pdf");
    // 实例化 XslFoLoadOption 对象
    auto options = new XslFoLoadOptions(infilenameXSL);
    // 设置错误处理策略
    options->ParsingErrorsHandlingType = XslFoLoadOptions::ParsingErrorsHandlingTypes::ThrowExceptionImmediately;
    // 创建 Document 对象
    auto document = MakeObject<Document>(infilenameXML, options);
    document->Save(_dataDir + outfilename);
}
```

{{% alert color="success" %}}
**尝试在线将 XML 转换为 PDF**

Aspose.PDF for C++ 为您提供在线免费应用程序 ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf)，您可以尝试研究其功能和工作质量。
[![Aspose.PDF 转换 XML 到 PDF 免费应用](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}