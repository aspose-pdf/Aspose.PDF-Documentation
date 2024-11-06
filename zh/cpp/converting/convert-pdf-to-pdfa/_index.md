---
title: 将PDF转换为PDF/A格式
linktitle: 将PDF转换为PDF/A格式
type: docs
weight: 100
url: zh/cpp/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: 本主题展示了如何使用Aspose.PDF将PDF文件转换为符合PDF/A标准的PDF文件。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for C++** 允许您将PDF文件转换为符合<abbr title="Portable Document Format / A">PDF/A</abbr>标准的PDF文件。在此之前，必须对文件进行验证。本文解释了如何进行。

{{% alert color="primary" %}}

请注意，我们遵循Adobe Preflight来验证PDF/A的一致性。市场上的所有工具都有自己对PDF/A一致性的“表示”。请参考这篇关于PDF/A验证工具的文章。我们选择Adobe产品来验证Aspose.PDF如何生成PDF文件，因为Adobe在与PDF相关的所有方面都处于核心位置。

{{% /alert %}}

使用Document类的Convert方法转换文件。 在将PDF转换为符合PDF/A的文件之前，使用Validate方法验证PDF。验证结果存储在XML文件中，然后此结果也传递给Convert方法。您还可以使用ConvertErrorAction枚举指定无法转换的元素的操作。
## 将PDF文件转换为PDF/A-1b

以下代码片段展示了如何将PDF文件转换为符合PDF/A-1b的PDF。

```cpp
void ConverttoPDFA_1b()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 输入文件名的字符串
    String infilename("sample.pdf");
    // 日志文件名的字符串
    String logfilename("log.xml");
    // 输出文件名的字符串
    String outfilename("PDFToPDFA_out.pdf");

    // 打开文档
    auto document = new Document(_dataDir + infilename);

    // 转换为符合PDF/A的文档
    // 在转换过程中，也会进行验证
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);

    // 保存输出文档
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
要仅执行验证，请使用以下代码行：

```cpp
void ConverttoPDFA_1b_Validation()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 输入文件名称的字符串
    String infilename("sample.pdf");
    // 日志文件名称的字符串
    String logfilename("log.xml");

    // 打开文档
    auto document = new Document(_dataDir + infilename);

    // 转换为符合 PDF/A 的文档
    // 在转换过程中，也会执行验证
    document->Validate(_dataDir + logfilename, PdfFormat::PDF_A_1B);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 将 PDF 文件转换为 PDF/A-3b

Aspose.PDF for C++ 也支持将 PDF 文件转换为 PDF/A-3b 格式的功能。

```cpp
void ConverttoPDFA_3b()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 输入文件名称的字符串
    String infilename("sample.pdf");
    // 日志文件名称的字符串
    String logfilename("log.xml");
    // 输入文件名称的字符串
    String outfilename("PDFToPDFA3b_out.pdf");

    // 打开文档
    auto document = new Document(_dataDir + infilename);

    // 转换为符合 PDF/A 的文档
    // 在转换过程中，也会执行验证
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_3B, ConvertErrorAction::Delete);

    // 保存输出文档
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 将PDF文件转换为PDF/A-2u

Aspose.PDF for C++ 还支持将PDF文件转换为PDF/A-2u格式的功能。

```cpp
void ConverttoPDFA_2u()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 输入文件名的字符串
    String infilename("sample.pdf");
    // 日志文件名的字符串
    String logfilename("log.xml");
    // 输出文件名的字符串
    String outfilename("PDFToPDFA3b_out.pdf");

    // 打开文档
    auto document = new Document(_dataDir + infilename);

    // 转换为符合PDF/A的文档
    // 在转换过程中，还会进行验证
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_2U, ConvertErrorAction::Delete);

    // 保存输出文档
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 将PDF文件转换为PDF/A-3u

Aspose.PDF for C++ 还支持将PDF文件转换为PDF/A-3u格式的功能。

```cpp
void ConverttoPDFA_3u()
{
    std::clog << __func__ << ": 开始" << std::endl;
    // 路径名的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 输入文件名的字符串
    String infilename("sample.pdf");
    // 日志文件名的字符串
    String logfilename("log.xml");
    // 输出文件名的字符串
    String outfilename("PDFToPDFA3b_out.pdf");

    // 打开文档
    auto document = new Document(_dataDir + infilename);

    // 转换为符合 PDF/A 的文档
    // 在转换过程中，还会进行验证
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_2U, ConvertErrorAction::Delete);

    // 保存输出文档
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": 完成" << std::endl;
}
```

## 将附件添加到 PDF/A 文件

如果您需要将文件附加到符合 PDF/A 的格式，我们建议使用 Aspose.PDF.PdfFormat 枚举中的 PDF_A_3A 值。

PDF/A_3a 是一种格式，提供将任何文件格式作为附件附加到符合 PDF/A 的文件的功能。

```cpp
void ConverttoPDFA_AddAttachment()
{
    std::clog << __func__ << ": 开始" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 输入文件名的字符串
    String infilename("sample.pdf");
    // 日志文件名的字符串
    String logfilename("log.xml");
    // 输出文件名的字符串
    String outfilename("PDFToPDFA3b_out.pdf");

    // 打开文档
    auto document = new Document(_dataDir + infilename);

    // 设置要添加为附件的新文件
    auto fileSpecification = MakeObject<FileSpecification>(_dataDir + String("aspose-logo.jpg"), String("大型图像文件"));
    // 将附件添加到文档的附件集合
    document->get_EmbeddedFiles()->Add(fileSpecification);

    // 转换为符合PDF/A的文档
    // 在转换过程中，还会进行验证
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_3A, ConvertErrorAction::Delete);

    // 保存输出文档
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": 完成" << std::endl;
}
```

## 使用替代字体替换缺失字体

根据PDFA标准，字体应嵌入在PDFA文档中。但是，如果字体未嵌入源文档中或不存在于机器上，则PDFA验证会失败。在这种情况下，我们需要用机器上的一些替代字体替换缺失的字体。我们可以在PDF到PDFA转换过程中使用SimpleFontSubsituation方法替换缺失的字体，如下所示。

```cpp
void ConverttoPDFA_ReplaceFont()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 输入文件名的字符串
    String infilename("sample.pdf");
    // 日志文件名的字符串
    String logfilename("log.xml");
    // 输出文件名的字符串
    String outfilename("PDFToPDFA3b_out.pdf");

    // 打开文档
    auto document = new Document(_dataDir + infilename);

    System::SharedPtr<Aspose::Pdf::Text::Font> originalFont;
    try
    {
        originalFont = FontRepository::FindFont(String("AgencyFB"));
    }
    catch (Exception)
    {
        // 目标机器上缺少字体
        auto substitutions = FontRepository::get_Substitutions();
        auto substitution = MakeObject<SimpleFontSubstitution>(String("AgencyFB"), String("Helvetica"));
        substitutions->Add(substitution);
    }

    // 转换为PDF/A兼容文档
    try {
        // 在转换过程中，也会进行验证
        document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);

        // 保存输出文档
        document->Save(_dataDir + outfilename);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="primary" %}}
**尝试在线将 PDF 转换为 PDF/A**

Aspose.PDF for C++ 为您提供在线免费应用程序 ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)，您可以在此尝试调查其功能和工作质量。

[![Aspose.PDF 转换 PDF 为 PDF/A 免费应用](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}