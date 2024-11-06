---
title: 创建 PDF 文档
linktitle: 创建 PDF
type: docs
weight: 10
url: zh/cpp/create-pdf-document/
description: 本文描述了如何使用 Aspose.PDF for C++ 创建和格式化 PDF 文档。
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

我们一直在寻找一种方法来生成 PDF 文档，并在 C++ 项目中更精确、准确和有效地处理它们。使用库中的易用功能使我们能够跟踪更多工作，而不是花费大量时间在尝试生成 PDF 的细节上，无论是在 C++ 中。

## 使用 C++ 生成 PDF

Aspose.PDF for C++ API 允许您使用 C++ 创建和读取 PDF 文件。该 API 可以用于多种 C++ 应用程序，包括 WinForms 和其他几种。在本文中，我们将展示如何使用 Aspose.PDF for C++ API 在 C++ 应用程序中轻松生成和读取 PDF 文件。

### 如何创建简单的 PDF 文件

要使用 C++ 创建 PDF 文件，可以使用以下步骤。

1. 创建一个 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 类的对象
1. 向 Document 对象的 'Pages' 集合中添加一个 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 对象
1. 向页面的 [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs) 集合中添加 [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/)
1. 保存生成的 PDF 文档

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CreateDocument() {
    // 路径名称的字符串。
    String _dataDir("C:\\Samples\\");

    // 文件名称的字符串。
    String outputFileName("HelloWorld_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // 向新页面添加文本
    auto text = MakeObject<TextFragment>(u"Hello world!");

    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // 保存更新后的 PDF
    document->Save(_dataDir + outputFileName);
}
```
## 创建可搜索的 PDF 文档

Aspose.PDF for C++ 允许您从头开始创建 PDF 并操作现有的 PDF。 当您向 PDF 添加文本元素时，生成的 PDF 是可搜索的。 但是，如果我们将包含文本的图像转换为 PDF 文件，则 PDF 内的内容是不可搜索的。 然而，作为一种解决方法，我们可以对生成的文件使用 OCR 以使其可搜索。 因此，首先您需要在您的系统上安装 Tesseract-OCR，并且您将拥有一个 tesseract 控制台应用程序。

以下是完成此需求的完整代码：

```cpp
void CreateSearchableDocument() {
    // 用于路径名称的字符串。
    String _dataDir("C:\\Samples\\");
    // 用于文件名的字符串。
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);
    bool convertResult = false;
    try
    {
        convertResult = document->Convert(CallBackGetHocr);
    }
    catch (Exception ex)
    {
        std::cerr << ex->get_Message() << std::endl;
    }
    document->Dispose();
}

static String CallBackGetHocr(System::SharedPtr<System::Drawing::Image> img)
{
    String tmpFile = System::IO::Path::GetTempFileNameSafe();

    auto bmp = MakeObject<System::Drawing::Bitmap>(img);

    bmp->Save(tmpFile, System::Drawing::Imaging::ImageFormat::get_Bmp());
    String inputFile = String::Format(u"\"{0}\"", tmpFile);
    String outputFile = String::Format(u"\"{0}\"", tmpFile);
    String arguments = inputFile + u" " + outputFile + u" -l eng hocr";
    String tesseractProcessName = u"C:\\Program Files\\Tesseract-OCR\\Tesseract.exe";

    auto psi = MakeObject<System::Diagnostics::ProcessStartInfo>(tesseractProcessName, arguments);
    psi->set_UseShellExecute(true);
    psi->set_CreateNoWindow(true);
    psi->set_WindowStyle(System::Diagnostics::ProcessWindowStyle::Hidden);
    psi->set_WorkingDirectory(System::IO::Path::GetDirectoryName(tesseractProcessName));

    auto p = MakeObject<System::Diagnostics::Process>(psi);
    p->Start();
    p->WaitForExit();

    auto streamReader = MakeObject<System::IO::StreamReader>(tmpFile + u".hocr");
    String text = streamReader->ReadToEnd();
    streamReader->Close();

    if (System::IO::File::Exists(tmpFile))
        System::IO::File::Delete(tmpFile);
    if (System::IO::File::Exists(tmpFile + u".hocr"))
        System::IO::File::Delete(tmpFile + u".hocr");

    return text;
}
```