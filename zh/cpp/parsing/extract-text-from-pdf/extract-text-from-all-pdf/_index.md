---
title: 使用C++从所有PDF页面提取文本
linktitle: 从PDF提取文本
type: docs
weight: 10
url: zh/cpp/extract-text-from-all-pdf/
description: 本文介绍了使用Aspose.PDF在C++中从PDF文档提取文本的各种方法。包括从整个页面、特定部分、基于列等。
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从PDF文档的所有页面提取文本

从PDF文档提取文本是一个常见的需求。 在这个例子中，你将看到 Aspose.PDF for C++ 如何从 PDF 文档的所有页面提取文本。你需要创建一个 [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) 类的对象。之后，使用 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 类打开 PDF，并调用 [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 集合的 'Accept' 方法。[TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) 类从文档中吸收文本并返回在 'Text' 属性中。以下代码片段向你展示了如何从 PDF 文档的所有页面提取文本。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ExtractTextFromAllThePages() {

    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Create TextAbsorber object to extract text
    auto textAbsorber = MakeObject<TextAbsorber>();
    // Accept the absorber for all the pages
    document->get_Pages()->Accept(textAbsorber);
    // Get the extracted text
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
调用 Document 对象特定页面的 **Accept** 方法。Index 是需要提取文本的特定页码。

```cpp
void ExtractTextFromParticularPage() {

    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Parsing\\");

    // 文件名称的字符串
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 创建 TextAbsorber 对象以提取文本
    auto textAbsorber = MakeObject<TextAbsorber>();
    // 接受所有页面的吸收器
    document->get_Pages()->idx_get(1)->Accept(textAbsorber);
    // 获取提取的文本
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 使用文本设备从页面提取文本

您可以使用 [TextDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.text_device/) 类从 PDF 文件中提取文本。TextDevice 在其实现中使用 TextAbsorber，因此，实际上，它们执行相同的操作，但 TextDevice 只是实现了统一的 "Device" 方法，以从页面中提取任何内容，如 ImageDevice、PageDevice 等。 TextAbsorber 可以从页面、整个 PDF 或 XForm 中提取文本，这个 TextAbsorber 更加通用。

### 从所有页面提取文本

以下步骤和代码示例向您展示如何使用文本设备从 PDF 中提取文本。

1. 使用指定的输入 PDF 文件创建 Document 类的对象
1. 创建 TextDevice 类的对象
1. 使用 TextExtractOptions 类的对象指定提取选项
1. 使用 TextDevice 类的 Process 方法将内容转换为文本
1. 将文本保存到输出文件

```cpp
void ExtractTextUsingTextDevice() {

    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Parsing\\");

    // 文件名称的字符串
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto builder = MakeObject<System::Text::StringBuilder>();
    // 字符串以保存提取的文本
    String extractedText;

    for (auto page : document->get_Pages()) {
        auto textStream = MakeObject<System::IO::MemoryStream>();
        // 创建文本设备
        auto textDevice = MakeObject<Aspose::Pdf::Devices::TextDevice>();

        // 设置文本提取选项 - 设置文本提取模式（原始或纯文本）
        auto textExtOptions = MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure);

        textDevice->set_ExtractionOptions(textExtOptions);

        // 转换特定页面并将文本保存到流中
        textDevice->Process(page, textStream);

        // 关闭内存流
        textStream->Close();

        // 从内存流中获取文本
        extractedText = System::Text::Encoding::get_Unicode()->GetString(textStream->ToArray());
        builder->Append(extractedText);

    }
    // 将提取的文本保存到文本文件中
    System::IO::File::WriteAllText(_dataDir + outfilename, builder->ToString());
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## 从特定页面区域提取文本

[TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) 类提供了从 PDF 文档的特定页面或所有页面提取文本的功能。该类在 'Text' 属性中返回提取的文本。然而，如果我们需要从特定页面区域提取文本，我们可以使用 [TextSearchOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_search_options/) 的 **Rectangle** 属性。Rectangle 属性采用一个 Rectangle 对象作为值，并使用该属性，我们可以指定需要从中提取文本的页面区域。

调用页面的 **Accept** 方法来提取文本。 创建 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) 和 [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) 类的对象。在 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) 对象的单个页面上调用 'Accept' 方法，作为 **Page** 索引。**索引** 是需要提取文本的特定页码。您可以从 [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) 类的 'Text' 属性中获取文本。以下代码片段向您展示如何从单个页面中提取文本。

```cpp
void ExtractTextFromParticularPageRegion() {

    std::clog << __func__ << ": Start" << std::endl;
    // 路径名的字符串
    String _dataDir("C:\\Samples\\Parsing\\");

    // 文件名的字符串
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 创建 TextAbsorber 对象以提取文本
    auto textAbsorber = MakeObject<TextAbsorber>();
    textAbsorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
    textAbsorber->get_TextSearchOptions()->set_Rectangle(MakeObject<Rectangle>(100, 200, 250, 350));

    // 对所有页面接受吸收器
    document->get_Pages()->idx_get(1)->Accept(textAbsorber);
    // 获取提取的文本
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;

}
```
## 基于列提取文本

PDF 是一种非常流行的格式，这是有充分理由的：使用 PDF，您几乎可以确定您的文档将在不同的计算机上以相同的方式显示和打印。

然而，PDF 文档有一个缺点，即它们通常缺乏关于段落、表格、图形、页眉/页脚信息等内容的信息。

Aspose.PDf for C++ - 它是一个易于使用的工具，允许您基于列提取文本。

```cpp
void ExtractTextBasedOnColumns() {

    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Create TextAbsorber object to extract text
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>();


    // Accept the absorber for all the pages
    document->get_Pages()->Accept(textFragmentAbsorber);

    auto tfc = textFragmentAbsorber->get_TextFragments();
    for (auto tf : tfc)
    {
        // Need to reduce font size at least for 70%
        auto size = tf->get_TextState()->get_FontSize() * 0.7f;
        tf->get_TextState()->set_FontSize(size);
    }
    auto stream = MakeObject<System::IO::MemoryStream>();
    document->Save(stream);
    document = MakeObject<Document>(stream);
    auto textAbsorber = MakeObject<TextAbsorber>();
    document->get_Pages()->Accept(textAbsorber);
    String extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### 第二种方法 - 使用 ScaleFactor

在这个新版本中，我们还在 TextAbsorber 和内部文本格式化机制中引入了若干改进。所以现在在使用“纯”模式进行文本提取时，您可以指定 [ScaleFactor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_extraction_options#a4f9a173765d483b493c31e416f8b035a) 选项，它可以是从多栏 PDF 文档中提取文本的另一种方法，除了上述方法之外。可以设置此缩放因子以调整在文本提取期间用于内部文本格式化机制的网格。指定 1 到 0.1（包括 0.1）之间的 ScaleFactor 值具有与字体缩小相同的效果。

指定 0.1 到 -0.1 之间的 ScaleFactor 值被视为零值，但它使算法能够在提取文本期间自动计算所需的缩放因子。 计算基于页面上最流行字体的平均字形宽度，但我们不能保证在提取的文本中没有列的字符串到达下一个列的开始。请注意，如果未指定ScaleFactor值，将使用默认值1.0。 这意味着不会进行缩放。如果指定的ScaleFactor值大于10或小于-0.1，将使用默认值1.0。

我们建议在处理大量PDF文件以提取文本内容时使用自动缩放（ScaleFactor = 0）。或者手动设置多余的网格宽度减小（约ScaleFactor = 0.5）。但是，您不必确定具体文档是否需要缩放。如果您为文档设置了多余的网格宽度减小（其实不需要），提取的文本内容将保持完全适当。请查看以下代码片段。

```cpp
void ExtractTextUsingScaleFactor() {

    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Parsing\\");

    // 文件名的字符串
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto textAbsorber = MakeObject<TextAbsorber>();
    textAbsorber->set_ExtractionOptions(MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure));
    // 设置缩放因子为0.5足以拆分大多数文档的列
    // 设置为零允许算法自动选择缩放因子
    textAbsorber->get_ExtractionOptions()->set_ScaleFactor(0.5); /* 0; */
    document->get_Pages()->Accept(textAbsorber);
    String extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## 从 PDF 文档中提取高亮文本

在从 PDF 文档中提取文本的各种场景中，您可能需要仅从 PDF 文档中提取高亮文本。为了实现该功能，我们在 API 中添加了 TextMarkupAnnotation.GetMarkedText() 和 TextMarkupAnnotation.GetMarkedTextFragments() 方法。您可以通过过滤 TextMarkupAnnotation 并使用上述方法从 PDF 文档中提取高亮文本。以下代码片段展示了如何从 PDF 文档中提取高亮文本。

```cpp
void ExtractHighlightedText() {

    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Parsing\\");

    // 文件名称的字符串
    String infilename("sample-highlight.pdf");
    String outfilename("extracted-text.txt");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 遍历所有注释
    for (auto annotation : document->get_Pages()->idx_get(1)->get_Annotations())
    {
        // 过滤 TextMarkupAnnotation
        if (annotation->get_AnnotationType() == Aspose::Pdf::Annotations::AnnotationType::Highlight)
        {
        auto highlightedAnnotation = System::DynamicCast<Aspose::Pdf::Annotations::HighlightAnnotation>(annotation);

        // 检索高亮文本片段
        auto collection = highlightedAnnotation->GetMarkedTextFragments();
        for (auto tf : collection)
        {
            // 显示高亮文本
            String s = tf->get_Text();
            std::cout << s << std::endl;
        }
        }
    }
}
```

## 从 XML 访问文本片段和段元素

有时候在处理从 XML 生成的 PDF 文档时，我们需要访问 TextFragment 或 TextSegment 项。Aspose.PDF for C++ 提供了按名称访问这些项目的功能。下面的代码片段展示了如何使用此功能。

```cpp
void AccessTextFragmentandSegmentElementsXML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称字符串
    String _dataDir("C:\\Samples\\Parsing\\");

    // 文件名称字符串
    String infilename("sample-doc.xml");
    String outfilename("sample-doc.pdf");

    auto document = MakeObject<Document>();
    document->BindXml(_dataDir + infilename);

    System::SharedPtr<Page> page = System::DynamicCast<Aspose::Pdf::Page>(document->GetObjectById(u"mainSection"));
    // 对页面进行一些操作
    // ...

    System::SharedPtr<TextSegment> segment = System::DynamicCast<Aspose::Pdf::Text::TextSegment>(document->GetObjectById(u"product_description"));
    // 对段进行一些操作
    // ...
    document->Save(_dataDir + outfilename);

    std::clog << __func__ << ": Finish" << std::endl;
}
```