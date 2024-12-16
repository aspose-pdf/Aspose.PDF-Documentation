---
title: 使用 C++ 保存 PDF 文档
linktitle: 保存
type: docs
weight: 30
url: /zh/cpp/save-pdf-document/
description: 学习如何使用 Aspose.PDF for C++ 库保存 PDF 文件。
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 保存 PDF 文档到文件系统

您可以使用 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 类的 Save 方法将创建或操作的 PDF 文档保存到文件系统。

```cpp
void SaveDocument()
{
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\");

    String originalFileName("SimpleResume.pdf");
    String modifiedFileName("SimpleResumeModified.pdf");

    auto document = MakeObject<Document>(_dataDir + originalFileName);
    // 进行一些操作，例如添加新的空白页
    document->get_Pages()->Add();
    document->Save(_dataDir + modifiedFileName);
}
```

## 保存 PDF 文档到流

您也可以通过使用 Save 方法的重载将创建或操作的 PDF 文档保存到流。

```cpp
void SaveDocumentStream()
{
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\");

    String originalFileName("SimpleResume.pdf");
    String modifiedFileName("SimpleResumeModified.pdf");

    auto document = MakeObject<Document>(_dataDir + originalFileName);

    // 进行一些操作，例如添加新的空白页
    document->get_Pages()->Add();

    auto fileStream = System::IO::File::OpenWrite(_dataDir + modifiedFileName);
    document->Save(fileStream);
}
```

## 保存为 PDF/A 或 PDF/X 格式

PDF/A 是便携文档格式 (PDF) 的 ISO 标准化版本，用于电子文档的归档和长期保存。PDF/A 与 PDF 的不同之处在于它禁止了不适合长期归档的功能，例如字体链接（相对于字体嵌入）和加密。ISO 对 PDF/A 查看器的要求包括颜色管理指南、嵌入字体支持以及用于阅读嵌入注释的用户界面。

PDF/X 是 PDF ISO 标准的一个子集。PDF/X 的目的是促进图形交换，因此它具有一系列不适用于标准 PDF 文件的打印相关要求。

在这两种情况下，使用 Save 方法来存储文档，而文档必须使用 [PdfFormatConversionOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pdf_format_conversion_options) 进行准备。

```cpp
void SaveDocumentAsPDFx()
{
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\");

    // 文件名称的字符串
    String infilename("SimpleResume.pdf");
    String outfilename("SimpleResume_A3U.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);
    auto options = new PdfFormatConversionOptions(Aspose::Pdf::PdfFormat::PDF_A_3U);
    try
    {
        document->Convert(options);
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what();
    }

    document->Save(_dataDir + outfilename);
}
```