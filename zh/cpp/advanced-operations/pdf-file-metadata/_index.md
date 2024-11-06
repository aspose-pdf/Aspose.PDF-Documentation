---
title: PDF 文件元数据
type: docs
weight: 20
url: zh/cpp/pdf-file-metadata/
---

## 获取/设置 PDF 文件信息

为了获取 PDF 文件的特定信息，首先需要调用 Document 类的 **get_Info()** 方法。一旦获取到 DocumentInfo 对象，就可以获取各个属性的值。此外，还可以通过使用 DocumentInfo 类的相应方法来设置属性。以下代码片段演示了如何使用 Aspose.PDF for C++ 获取/设置 PDF 文件信息：

{{% alert color="primary" %}}

请注意，您无法设置 **Application** 和 **Producer** 字段的值，因为这些字段将显示 Aspose Ltd. 和 Aspose.PDF for C++ x.x.x。

{{% /alert %}}

```cpp
void WorkingWithPDFMetadata::GetPDFFileInformation()
{
    String _dataDir("C:\\Samples\\");
    // 打开文档
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetFileInfo.pdf");
    // 获取文档信息
    auto docInfo = pdfDocument->get_Info();
    // 显示文档信息
    Console::WriteLine(u"Author: {0}", docInfo->get_Author());
    Console::WriteLine(u"Creation Date: {0}", docInfo->get_CreationDate());
    Console::WriteLine(u"Keywords: {0}", docInfo->get_Keywords());
    Console::WriteLine(u"Modify Date: {0}", docInfo->get_ModDate());
    Console::WriteLine(u"Subject: {0}", docInfo->get_Subject());
    Console::WriteLine(u"Title: {0}", docInfo->get_Title());
}

void WorkingWithPDFMetadata::SetPDFFileInformation()
{
    String _dataDir("C:\\Samples\\");
    // 打开文档
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetFileInfo.pdf");

    // 指定文档信息
    auto docInfo = MakeObject<DocumentInfo>(pdfDocument);

    docInfo->set_Author(u"Aspose");
    docInfo->set_CreationDate(DateTime::get_Now());
    docInfo->set_Keywords (u"Aspose.Pdf, DOM, API");
    docInfo->set_ModDate (DateTime::get_Now());
    docInfo->set_Subject (u"PDF Information");
    docInfo->set_Title (u"Setting PDF Document Information");

    // 保存输出文档
    pdfDocument->Save(_dataDir + u"SetFileInfo_out.pdf");
}
```

## 获取/设置 PDF 文件的 XMP 元数据

Aspose.PDF for C++ 允许您访问和设置 PDF 文件的 XMP 元数据。要获取/设置 PDF 文件的元数据：

1. 创建一个 Document 对象并打开输入的 PDF 文件。
1. 使用相应的方法获取/设置文件的元数据。

下面的代码片段展示了如何从 PDF 文件获取/设置元数据。

```cpp
void WorkingWithPDFMetadata::GetXMPMetadata()
{
    String _dataDir("C:\\Samples\\");
    // 打开文档
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetXMPMetadata.pdf");

    // 获取属性
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:CreateDate"));
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:Nickname"));
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:CustomProperty"));
}

void WorkingWithPDFMetadata::SetXMPMetadata()
{
    String _dataDir("C:\\Samples\\");
    // 打开文档
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetXMPMetadata.pdf");

    // 设置属性
    pdfDocument->get_Metadata()->idx_set(u"xmp:CreateDate", MakeObject<XmpValue>(DateTime::get_Now()));
    pdfDocument->get_Metadata()->idx_set(u"xmp:Nickname", MakeObject<XmpValue>(u"Nickname"));
    pdfDocument->get_Metadata()->idx_set(u"xmp:CustomProperty", MakeObject<XmpValue>(u"Custom Value"));

    // 保存文档
    pdfDocument->Save(_dataDir + u"SetXMPMetadata_out.pdf");
}

void WorkingWithPDFMetadata::InsertMetadataWithPrefix()
{
    String _dataDir("C:\\Samples\\");
    // 打开文档
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetXMPMetadata.pdf");
    pdfDocument->get_Metadata()->RegisterNamespaceUri(u"xmp", u"http:// Ns.adobe.com/xap/1.0/"); // xmlns 前缀已被移除
    pdfDocument->get_Metadata()->idx_set(u"xmp:ModifyDate", MakeObject<XmpValue>(DateTime::get_Now()));

    // 保存文档
    pdfDocument->Save(_dataDir + u"SetPrefixMetadata_out.pdf");
}
```