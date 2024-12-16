---
title: 向 PDF 添加页眉和页脚
linktitle: 向 PDF 添加页眉和页脚
type: docs
weight: 70
url: /zh/cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for C++ 允许您使用 TextStamp 类向 PDF 文件添加页眉和页脚。
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++** 允许您在现有的 PDF 文件中添加页眉和页脚。您可以向 PDF 文档中添加图像或文本。此外，还可以尝试在一个 PDF 文件中通过 C++ 添加不同的页眉。

## 在 PDF 文件的页眉中添加文本

您可以使用 [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) 类在 PDF 文件的页眉中添加文本。 TextStamp 类提供创建基于文本的印章所需的属性，如字体大小、字体样式和字体颜色等。为了在页眉添加文本，您需要使用所需的属性创建一个 Document 对象和一个 TextStamp 对象。之后，您可以调用 Page 的 AddStamp 方法在 PDF 的页眉添加文本。

您需要设置 TopMargin 属性，以便将文本调整到 PDF 的页眉区域。您还需要将 HorizontalAlignment 设置为 Center 并将 VerticalAlignment 设置为 Top。

以下代码片段向您展示如何使用 C++ 在 PDF 文件的页眉中添加文本。

```cpp
void AddingTextInHeaderOfPdfFile() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("TextinHeader.pdf");
    String outputFileName("TextinHeader_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 创建页眉
    auto textStamp = MakeObject<TextStamp>(u"Header Text");

    // 设置印章的属性
    textStamp->set_TopMargin(10);
    textStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    textStamp->set_VerticalAlignment(VerticalAlignment::Top);

    // 在所有页面添加页眉
    for(auto page : document->get_Pages())
    {
        page->AddStamp(textStamp);
    }

    // 保存更新后的文档
    document->Save(_dataDir + outputFileName);
}
```
## 在 PDF 文件的页脚添加文本

您可以使用 TextStamp 类在 PDF 文件的页脚添加文本。TextStamp 类提供了创建基于文本的印章所需的属性，例如字体大小、字体样式和字体颜色等。为了在页脚添加文本，您需要使用所需的属性创建一个 Document 对象和一个 TextStamp 对象。之后，您可以调用 Page 的 AddStamp 方法在 PDF 的页脚添加文本。

{{% alert color="primary" %}}

您需要以调整 PDF 页脚区域中的文本的方式设置底边距属性。同时需要将 HorizontalAlignment 设置为 Center，并将 VerticalAlignment 设置为 Bottom。

{{% /alert %}}

以下代码片段展示了如何使用 C++ 在 PDF 文件的页脚添加文本。

```cpp
void AddingTextInFooterOfPdfFile() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("TextinFooter.pdf");
    String outputFileName("TextinFooter_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 创建页脚
    auto textStamp = MakeObject<TextStamp>(u"Footer Text");

    // 设置印章的属性
    textStamp->set_BottomMargin(10);
    textStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    textStamp->set_VerticalAlignment(VirtualAlignment::Bottom);

    // 在所有页面添加页脚
    for (auto page : document->get_Pages())
    {
        page->AddStamp(textStamp);
    }

    // 保存更新后的文档
    document->Save(_dataDir + outputFileName);
}
```

## 在 PDF 文件的页眉中添加图像

您可以使用 [ImageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_stamp) 类在 PDF 文件的页眉中添加图像。Image Stamp 类提供了创建基于图像的印章所需的属性，如字体大小、字体样式和字体颜色等。为了在页眉中添加图像，您需要使用所需的属性创建一个 Document 对象和一个 Image Stamp 对象。之后，您可以调用 Page 的 AddStamp 方法在 PDF 的页眉中添加图像。

下面的代码片段展示了如何使用 C++ 在 PDF 文件的页眉中添加图像。

```cpp
void AddingImageInHeaderOfPdfFile() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ImageinHeader.pdf");
    String outputFileName("ImageinHeader_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 创建页眉
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    // 设置印章的属性
    imageStamp->set_TopMargin(10);
    imageStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    imageStamp->set_VerticalAlignment (VerticalAlignment::Top);

    // 在所有页面上添加页眉
    for(auto page : document->get_Pages())
    {
        page->AddStamp(imageStamp);
    }

    // 保存更新后的文档
    document->Save(_dataDir + outputFileName);
}
```

## 在 PDF 文件的页脚添加图像

您可以使用图像印章类在 PDF 文件的页脚添加图像。图像印章类提供了创建基于图像的印章所需的属性，如字体大小、字体样式和字体颜色等。为了在页脚添加图像，您需要使用所需的属性创建一个文档对象和一个图像印章对象。之后，您可以调用页面的 AddStamp 方法在 PDF 的页脚中添加图像。

您需要设置 [BottomMargin](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.stamp#aeab91949cf3eb473018b31a74fed7173) 属性，以便调整图像在 PDF 的页脚区域中。您还需要将 [HorizontalAlignment](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#aefec9c0bf30ee5e6fb2640e69aed6cd9) 设置为 `Center` 和 [VerticalAlignment](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ad4956d03096fc515eaa34319a6bf636a) 设置为 `Bottom`。

以下代码片段向您展示了如何使用 C++ 在 PDF 文件的页脚添加图像。

```cpp
void AddingImageInFooterOfPdfFile() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ImageinFooter.pdf");
    String outputFileName("ImageinFooter_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 创建页眉
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    // 设置图章的属性
    imageStamp->set_TopMargin(10);
    imageStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    imageStamp->set_VerticalAlignment(VerticalAlignment::Top);

    // 在所有页面添加页眉
    for (auto page : document->get_Pages())
    {
        page->AddStamp(imageStamp);
    }

    // 保存更新的文档
    document->Save(_dataDir + outputFileName);
}
```

## 在一个PDF文件中添加不同的页眉

我们知道可以通过使用TopMargin或Bottom Margin属性在文档的页眉/页脚部分添加TextStamp，但有时我们可能需要在单个PDF文档中添加多个页眉/页脚。 **Aspose.PDF for C++** 解释了如何做到这一点。

为了完成这个要求，我们将创建单独的 TextStamp 对象（对象的数量取决于所需的页眉/页脚数量），并将它们添加到 PDF 文档中。我们还可以为单个图章对象指定不同的格式信息。在以下示例中，我们创建了 Document 对象和三个 TextStamp 对象，然后使用页面的 [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) 方法将文本添加到 PDF 的页眉部分。以下代码片段向您展示了如何使用 Aspose.PDF for C++ 将图像添加到 PDF 文件的页脚中。

```cpp
void AddingDifferentHeadersInOnePDFFile()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("multiheader.pdf");
    String outputFileName("multiheader_out.pdf");

    // 打开源文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 创建三个图章
    auto stamp1 = MakeObject<TextStamp>("Header 1");
    auto stamp2 = MakeObject<TextStamp>("Header 2");
    auto stamp3 = MakeObject<TextStamp>("Header 3");

    // 设置图章对齐（将图章放在页面顶部，水平居中）
    stamp1->set_VerticalAlignment(VerticalAlignment::Top);
    stamp1->set_HorizontalAlignment(HorizontalAlignment::Center);
    // 指定字体样式为粗体
    stamp1->get_TextState()->set_FontStyle(FontStyles::Bold);
    // 设置文本前景色信息为红色
    stamp1->get_TextState()->set_ForegroundColor(Color::get_Red());
    // 指定字体大小为14
    stamp1->get_TextState()->set_FontSize(14);

    // 现在我们需要将第二个图章对象的垂直对齐设置为顶部
    stamp2->set_VerticalAlignment(VerticalAlignment::Top);
    // 设置图章的水平对齐信息为居中对齐
    stamp2->set_HorizontalAlignment (HorizontalAlignment::Center);
    // 设置图章对象的缩放因子
    stamp2->set_Zoom(10);

    // 设置第三个图章对象的格式
    // 指定图章对象的垂直对齐信息为顶部
    stamp3->set_VerticalAlignment(VerticalAlignment::Top);
    // 设置图章对象的水平对齐信息为居中对齐
    stamp3->set_HorizontalAlignment(HorizontalAlignment::Center);
    // 设置图章对象的旋转角度
    stamp3->set_RotateAngle(35);
    // 将粉色设置为图章的背景色
    stamp3->get_TextState()->set_BackgroundColor(Color::get_Pink());
    // 更改图章的字体信息为 Verdana
    stamp3->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));

    // 第一个图章添加在第一页;
    document->get_Pages()->idx_get(1)->AddStamp(stamp1);
    // 第二个图章添加在第二页;
    document->get_Pages()->idx_get(2)->AddStamp(stamp2);
    // 第三个图章添加在第三页。
    document->get_Pages()->idx_get(3)->AddStamp(stamp3);

    // 保存更新后的文档
    document->Save(_dataDir + outputFileName);
}
```