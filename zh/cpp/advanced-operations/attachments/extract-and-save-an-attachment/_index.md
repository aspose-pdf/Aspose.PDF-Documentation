---
title: 提取并保存附件
linktitle: 提取并保存附件
type: docs
weight: 20
url: /zh/cpp/extract-and-save-an-attachment/
description: Aspose.PDF for C++ 允许您从 PDF 文档中获取所有附件。此外，您还可以从文档中获取单个附件。
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 获取所有附件

使用 Aspose.PDF，可以从 PDF 文档中获取所有附件。这在您希望将文档与 PDF 分开保存时很有用，或者如果您需要从 PDF 中删除附件。

从 PDF 文件中获取所有附件：

1. 遍历 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 对象的 [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) 集合。[EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) 集合包含所有附件。该集合的每个元素代表一个 [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) 对象。通过 [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) 集合的 foreach 循环的每次迭代返回一个 [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) 对象。
1. 一旦对象可用，检索所有附加文件的属性或文件本身。

以下代码片段展示了如何从 PDF 文档中获取所有附件。

```cpp
void WorkingWithAttachments::GetAllAttachments()
{
 String _dataDir("C:\\Samples\\");

 // 打开文档
 auto pdfDocument = new Document(_dataDir + u"GetAlltheAttachments.pdf");

 // 获取嵌入文件集合
 auto embeddedFiles = pdfDocument->get_EmbeddedFiles();

 // 获取嵌入文件的数量
 Console::WriteLine(u"Total files : {0}", embeddedFiles->get_Count());

 int count = 1;

 // 遍历集合以获取所有附件
 for (auto fileSpecification : embeddedFiles)
 {
  Console::WriteLine(u"Name: {0}", fileSpecification->get_Name());
  Console::WriteLine(u"Description: {0}", fileSpecification->get_Description());
  Console::WriteLine(u"Mime Type: {0}", fileSpecification->get_MIMEType());

  // 检查参数对象是否包含参数
  if (fileSpecification->get_Params() != nullptr)
  {
   Console::WriteLine(u"CheckSum: {0}",
    fileSpecification->get_Params()->get_CheckSum());
   Console::WriteLine(u"Creation Date: {0}",
    fileSpecification->get_Params()->get_CreationDate());
   Console::WriteLine(u"Modification Date: {0}",
    fileSpecification->get_Params()->get_ModDate());
   Console::WriteLine(u"Size: {0}", fileSpecification->get_Params()->get_Size());
  }

  // 获取附件并写入文件或流
  auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
  fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());
  auto fileStream = System::IO::File::OpenWrite(_dataDir + u"test" + count + u"_out.txt");
  fileStream->Write(fileContent, 0, fileContent->get_Length());
  fileStream->Close();
  count += 1;
 }
}
```
## 获取单个附件

为了获取单个附件，我们可以在文档实例的 `EmbeddedFiles` 对象中指定附件的索引。请尝试使用以下代码片段。

```cpp
void WorkingWithAttachments::GetIndividualAttachment() {
    String _dataDir("C:\\Samples\\");

    // 打开文档
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetIndividualAttachment.pdf");

    // 获取特定的嵌入文件
    auto fileSpecification = pdfDocument->get_EmbeddedFiles()->idx_get(1);

    // 获取文件属性
    Console::WriteLine(u"Name: {0}", fileSpecification->get_Name());
    Console::WriteLine(u"Description: {0}", fileSpecification->get_Description());
    Console::WriteLine(u"Mime Type: {0}", fileSpecification->get_MIMEType());

    // 检查参数对象是否包含参数
    if (fileSpecification->get_Params() != nullptr)
    {
        Console::WriteLine(u"CheckSum: {0}",
        fileSpecification->get_Params()->get_CheckSum());
        Console::WriteLine(u"Creation Date: {0}",
        fileSpecification->get_Params()->get_CreationDate());
        Console::WriteLine(u"Modification Date: {0}",
        fileSpecification->get_Params()->get_ModDate());
        Console::WriteLine(u"Size: {0}",
        fileSpecification->get_Params()->get_Size());
    }

    // 获取附件并写入文件或流
    auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
    fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());

    auto fileStream = System::IO::File::OpenWrite(_dataDir + u"test_out.txt");
    fileStream->Write(fileContent, 0, fileContent->get_Length());
    fileStream->Close();

}
```