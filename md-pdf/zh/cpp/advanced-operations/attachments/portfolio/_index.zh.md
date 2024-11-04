---
title: 使用 PDF 创建作品集
linktitle: 作品集
type: docs
weight: 40
url: /cpp/portfolio/
description: 使用 Aspose.PDF for C++ 创建 PDF 作品集。您应该使用 Microsoft Excel 文件、Word 文档和图像文件来创建 PDF 作品集。
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 如何创建 PDF 作品集

Aspose.PDF 允许使用 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 类创建 PDF 作品集文档。在通过 [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) 类获取文件后，将文件添加到 Document.Collection 对象中。当文件添加完成后，使用 Document 类的 Save 方法保存作品集文档。

以下示例使用 Microsoft Excel 文件、Word 文档和图像文件创建 PDF 作品集。

下面的代码生成了以下作品集。

### 使用 Aspose.PDF 创建的 PDF 作品集

![使用 Aspose.PDF for C++ 创建的 PDF 作品集](working-with-pdf-portfolio_1.jpg)

```cpp
void WorkingWithAttachments::CreatePortfolio()
{
    String _dataDir("C:\\Samples\\");

    // 实例化 Document 对象
    auto pdfDocument = MakeObject<Document>();

    // 实例化文档 Collection 对象
    pdfDocument->set_Collection(MakeObject<Collection>());

    // 获取要添加到 Portfolio 的文件
    auto excel = MakeObject<FileSpecification>(_dataDir + u"HelloWorld.xlsx");
    auto word = MakeObject<FileSpecification>(_dataDir + u"HelloWorld.docx");
    auto image = MakeObject<FileSpecification>(_dataDir + u"sample.jpg");

    // 提供文件的描述
    excel->set_Description(u"Excel 文件");
    word->set_Description(u"Word 文件");
    image->set_Description(u"图像文件");

    // 将文件添加到文档集合中
    pdfDocument->get_Collection()->Add(excel);
    pdfDocument->get_Collection()->Add(word);
    pdfDocument->get_Collection()->Add(image);

    // 保存 Portfolio 文档
    pdfDocument->Save(_dataDir + u"PDFPortfolio.pdf");
}
```

## 从 PDF Portfolio 中提取文件

PDF Portfolio 允许您将来自多种来源的内容（例如，PDF、Word、Excel、JPEG 文件）整合到一个统一的容器中。原始文件保留其各自的身份，但被组装成一个 PDF Portfolio 文件。用户可以独立于其他组件文件地打开、阅读、编辑和格式化每个组件文件。

Aspose.PDF 允许使用 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 类创建 PDF Portfolio 文档。它还提供了从 PDF Portfolio 中提取文件的功能。

以下代码片段向您展示了从 PDF Portfolio 中提取文件的步骤。

```cpp
void WorkingWithAttachments::ExtractPortfolio()
{
    String _dataDir("C:\\Samples\\");
    // 打开文档
    auto pdfDocument = MakeObject <Document>(_dataDir + u"PDFPortfolio.pdf");
    // 获取嵌入文件的集合
    auto embeddedFiles = pdfDocument->get_EmbeddedFiles();

    // 遍历 Portfolio 中的每个文件
    for (auto fileSpecification : embeddedFiles) {
    auto initialStream = fileSpecification->get_Contents();
    auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
    fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());
    auto filename = System::IO::Path::GetFileName(fileSpecification->get_Name());
    // 将提取的文件保存到某个位置
    auto fileStream = System::IO::File::OpenWrite(_dataDir + u"_out_" + filename);
    fileStream->Write(fileContent, 0, fileContent->get_Length());
    // 关闭流对象
    fileStream->Close();
    }
}
```

![从PDF组合包中提取文件](working-with-pdf-portfolio_2.jpg)

## 从PDF组合包中删除文件

为了从PDF组合包中删除/移除文件，请尝试使用以下代码行。

```cpp
void WorkingWithAttachments::RemoveFilesFromPDFPortfolio()
{
    String _dataDir("C:\\Samples\\");
    // 加载源PDF组合包
    auto pdfDocument = MakeObject<Document>(_dataDir + u"PDFPortfolio.pdf");
    pdfDocument->get_Collection()->Delete();
    pdfDocument->Save(_dataDir + u"No_PortFolio_out.pdf");
}
```