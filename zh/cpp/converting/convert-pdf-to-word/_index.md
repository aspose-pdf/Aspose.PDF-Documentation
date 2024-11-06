---
title: 将PDF转换为Microsoft Word文档在C++
linktitle: 将PDF转换为Word
type: docs
weight: 10
url: zh/cpp/convert-pdf-to-word/
lastmod: "2021-11-19"
description: Aspose.PDF for C++库允许您使用C++轻松且完全控制地将PDF转换为Word格式。这些格式包括DOC和DOCX。了解更多关于如何调整PDF到Microsoft Word文档的转换。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 概述

本文解释了如何使用C++将PDF转换为Microsoft Word文档。它涵盖了以下主题。

_格式_： **DOC**
- [C++ PDF到DOC](#cpp-pdf-to-doc)
- [C++ 转换PDF到DOC](#cpp-pdf-to-doc)
- [C++ 如何将PDF文件转换为DOC](#cpp-pdf-to-doc)

_格式_： **DOCX**
- [C++ PDF到DOCX](#cpp-pdf-to-docx)
- [C++ 转换PDF到DOCX](#cpp-pdf-to-docx)
- [C++ 如何将PDF文件转换为DOCX](#cpp-pdf-to-docx)

_格式_： **Microsoft Word DOC格式**
- [C++ PDF到Word](#cpp-pdf-to-word-doc)
- [C++ 转换PDF到Word](#cpp-pdf-to-word-doc)

- [C++ 如何将PDF文件转换为Word](#cpp-pdf-to-word-doc)

_Format_: **Microsoft Word DOCX 格式**
- [C++ PDF 转换为 Word](#cpp-pdf-to-word-docx)
- [C++ 将 PDF 转换为 Word](#cpp-pdf-to-word-docx)
- [C++ 如何将 PDF 文件转换为 Word](#cpp-pdf-to-word-docx)

本文涵盖的其他主题
- [另请参阅](#see-also)

## C++ PDF 到 Word 转换

最受欢迎的功能之一是 PDF 到 Microsoft Word DOC 的转换，这使得内容易于操作。Aspose.PDF for C++ 允许您将 PDF 文件转换为 DOC。

## 将 PDF 转换为 DOC (Word 97-2003) 文件

轻松且完全控制地将 PDF 文件转换为 DOC 格式。Aspose.PDF for C++ 灵活且支持多种转换。例如，将 PDF 文档的页面转换为图像是一个非常受欢迎的功能。

我们许多客户要求的转换是 PDF 到 DOC：将 PDF 文件转换为 Microsoft Word 文档。 客户需要这样做，因为PDF文件不容易编辑，而Word文档可以编辑。一些公司希望他们的用户能够在最初为PDF的文件中操作文本、表格和图像。

为了保持简单易懂的传统，Aspose.PDF for C++让您可以通过两行代码将源PDF文件转换为DOC文件。为了实现这个功能，我们引入了一个名为SaveFormat的枚举，其值.Doc允许您将源文件保存为Microsoft Word格式。

以下C++代码片段显示了将PDF文件转换为DOC格式的过程。

<a name="cpp-pdf-to-doc" id="cpp-pdf-to-doc"><strong>步骤：在C++中将PDF转换为DOC</strong></a> | <a name="cpp-pdf-to-word-doc" id="cpp-pdf-to-word-doc"><strong>步骤：在C++中将PDF转换为Microsoft Word DOC格式</strong></a>

1. 使用源PDF文档创建一个[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)对象的实例。
2. 将其保存为 **SaveFormat::Doc** 格式，通过调用 **Document->Save()** 方法。

```cpp
void ConvertPDFtoWord()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 文件名的字符串
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.doc");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
        // 将文件保存为 MS 文档格式
        document->Save(_dataDir + outfilename, SaveFormat::Doc);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```

以下代码片段展示了将 PDF 文件转换为高级版本 DOC 的过程：

```cpp
void ConvertPDFtoWordDocAdvanced()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 文件名的字符串
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.doc");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto saveOptions = MakeObject<DocSaveOptions>();
    saveOptions->set_Format(DocSaveOptions::DocFormat::Doc);
    // 设置识别模式为 Flow
    saveOptions->set_Mode(DocSaveOptions::RecognitionMode::Flow);
    // 设置水平邻近度为 2.5
    saveOptions->set_RelativeHorizontalProximity(2.5f);
    // 启用转换过程中识别项目符号的值
    saveOptions->set_RecognizeBullets(true);

    try {
        // 将文件保存为 MS 文档格式
        document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="success" %}}
**尝试在线将PDF转换为DOC**

Aspose.PDF for C++为您提供在线免费应用程序["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)，您可以在其中尝试调查其功能和工作质量。

[![将PDF转换为DOC](pdf_to_doc.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## 将PDF转换为DOCX

Aspose.PDF for C++ API允许您使用C++语言读取和转换PDF文档为DOCX。DOCX是Microsoft Word文档的知名格式，其结构从纯二进制更改为XML和二进制文件的组合。Docx文件可以用Word 2007及更高版本打开，但不能用支持DOC文件扩展名的早期版本的MS Word打开。

以下C++代码片段显示了将PDF文件转换为DOCX格式的过程。

<a name="cpp-pdf-to-docx" id="cpp-pdf-to-docx"><strong>步骤：在C++中将PDF转换为DOCX</strong></a> | <a name="cpp-pdf-to-word-docx" id="cpp-pdf-to-word-docx"><strong>步骤：在C++中将PDF转换为Microsoft Word DOCX格式</strong></a>

1. 创建一个 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 对象的实例，并使用源 PDF 文档。
2. 调用 **Document->Save()** 方法将其保存为 **SaveFormat::DocX** 格式。

```cpp
void ConvertPDFtoWord_DOCX_Format()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 文件名的字符串
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.docx");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
        // 将文件保存为 MS 文档格式
        document->Save(_dataDir + outfilename, SaveFormat::DocX);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```

[`DocSaveOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options) 类有一个名为 Format 的属性，该属性提供指定结果文档格式（即 DOC 或 DOCX）的功能。 为了将 PDF 文件转换为 DOCX 格式，请从 DocSaveOptions.DocFormat 枚举中传递 Docx 值。

请查看以下代码片段，该代码片段提供了使用 C++ 将 PDF 文件转换为 DOCX 格式的功能。

```cpp
void ConvertPDFtoWord_Advanced_DOCX_Format()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 文件名称的字符串
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.docx");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto saveOptions = MakeObject<DocSaveOptions>();
    saveOptions->set_Format(DocSaveOptions::DocFormat::DocX);

    // 设置其他 DocSaveOptions 参数
    // ...

    // 将文件保存为 MS 文档格式

    try {
        // 将文件保存为 MS 文档格式
        document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="warning" %}}
**尝试在线将 PDF 转换为 DOCX**

Aspose.PDF for C++ 为您提供在线免费应用程序 ["PDF to DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx)，您可以在其中尝试调查其功能和工作质量。

[![Aspose.PDF 转换 PDF 为 Word 免费应用](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 另见

本文还涵盖以下主题。代码与上述相同。

_格式_: **Microsoft Word DOC 格式**
- [C++ PDF 转 Word 代码](#cpp-pdf-to-word-doc)
- [C++ PDF 转 Word API](#cpp-pdf-to-word-doc)
- [C++ PDF 转 Word 编程实现](#cpp-pdf-to-word-doc)
- [C++ PDF 转 Word 库](#cpp-pdf-to-word-doc)
- [C++ 将 PDF 保存为 Word](#cpp-pdf-to-word-doc)
- [C++ 从 PDF 生成 Word](#cpp-pdf-to-word-doc)
- [C++ 从 PDF 创建 Word](#cpp-pdf-to-word-doc)
- [C++ PDF 转 Word 转换器](#cpp-pdf-to-word-doc)

_格式_: **Microsoft Word DOCX 格式**

- [C++ PDF 转 Word 代码](#cpp-pdf-to-word-docx)
- [C++ PDF 转 Word API](#cpp-pdf-to-word-docx)
- [C++ 编程方式将 PDF 转 Word](#cpp-pdf-to-word-docx)
- [C++ PDF 转 Word 库](#cpp-pdf-to-word-docx)
- [C++ 保存 PDF 为 Word](#cpp-pdf-to-word-docx)
- [C++ 从 PDF 生成 Word](#cpp-pdf-to-word-docx)
- [C++ 从 PDF 创建 Word](#cpp-pdf-to-word-docx)
- [C++ PDF 转 Word 转换器](#cpp-pdf-to-word-docx)

_格式_: **DOC**
- [C++ PDF 转 DOC 代码](#cpp-pdf-to-doc)
- [C++ PDF 转 DOC API](#cpp-pdf-to-doc)
- [C++ 编程方式将 PDF 转 DOC](#cpp-pdf-to-doc)
- [C++ PDF 转 DOC 库](#cpp-pdf-to-doc)
- [C++ 保存 PDF 为 DOC](#cpp-pdf-to-doc)
- [C++ 从 PDF 生成 DOC](#cpp-pdf-to-doc)
- [C++ 从 PDF 创建 DOC](#cpp-pdf-to-doc)
- [C++ PDF 转 DOC 转换器](#cpp-pdf-to-doc)

_格式_: **DOC**
- [C++ PDF 转 DOCX 代码](#cpp-pdf-to-docx)
- [C++ PDF 转 DOCX API](#cpp-pdf-to-docx)
- [C++ 编程方式将 PDF 转 DOCX](#cpp-pdf-to-docx)
- [C++ PDF 转 DOCX 库](#cpp-pdf-to-docx)
- [C++ 保存 PDF 为 DOCX](#cpp-pdf-to-docx)

- [C++ 从 PDF 生成 DOCX](#cpp-pdf-to-docx)

- [C++ 从 PDF 创建 DOCX](#cpp-pdf-to-docx)
- [C++ PDF 转 DOCX 转换器](#cpp-pdf-to-docx)
```