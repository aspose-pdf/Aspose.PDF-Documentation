---
title: 在PDF中以编程方式添加图片印章
linktitle: PDF文件中的图片印章
type: docs
weight: 10
url: /zh/cpp/image-stamps-in-pdf-page/
description: 使用Aspose.PDF for C++库中的ImageStamp类在PDF文档中添加图片印章。
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 在PDF文件中添加图片印章

您可以使用ImageStamp类向PDF文件添加图片印章。ImageStamp类提供了创建基于图片印章所需的属性，例如高度、宽度、不透明度等。

要添加图片印章：

1. 使用所需属性创建一个[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)对象和一个ImageStamp对象。
1. 调用[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)类的[AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02)方法将印章添加到PDF中。

以下代码片段展示了如何在PDF文件中添加图片印章。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddImageStampToPDFFile()
{    
    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String inputFileName("AddImageStamp.pdf");

    String outputFileName("AddImageStamp_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 创建图像印章
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");
    imageStamp->set_Background(true);
    imageStamp->set_XIndent(100);
    imageStamp->set_YIndent(100);
    imageStamp->set_Height(48);
    imageStamp->set_Width(225);
    imageStamp->set_Rotate(Rotation::on270);
    imageStamp->set_Opacity(0.5);
   
    // 将印章添加到特定页面    
    document->get_Pages()->idx_get(1)->AddStamp(imageStamp);

    // 保存输出文档
    document->Save(_dataDir + outputFileName);
}
```

## 添加印章时控制图像质量

当将图像作为印章对象添加时，您可以控制图像的质量。 质量属性的 [ImageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_stamp) 类用于此目的。它表示图像的质量，以百分比表示（有效值为 0..100）。

```cpp
void ControlImageQualityWhenAddingStamp() {
    
    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String inputFileName("AddImageStamp.pdf");
    String outputFileName("ControlImageQuality_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 创建图像印章
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    imageStamp->set_Quality(10);
    document->get_Pages()->idx_get(1)->AddStamp(imageStamp);    
    document->Save(_dataDir + u"ControlImageQuality_out.pdf");
}
```

## 浮动框中的图像印章作为背景

Aspose.PDF API 允许您在浮动框中添加图像印章作为背景。 FloatingBox 类的 BackgroundImage 属性可用于设置浮动框的背景图像戳记，如以下代码示例所示。

```cpp
void ImageStampAsBackgroundInFloatingBox() {
    
    String _dataDir("C:\\Samples\\");

    // 输入文件名称的字符串
    String inputFileName("AddImageStamp.pdf");
    String outputFileName("AddImageStampAsBackgroundInFloatingBox_out.pdf");

    // 实例化 Document 对象
    auto document = MakeObject<Document>();

    // 向 PDF 文档添加页面
    auto page = document->get_Pages()->Add();

    // 创建 FloatingBox 对象
    auto aBox = MakeObject<FloatingBox>(200, 100);

    // 设置 FloatingBox 的左侧位置
    aBox->set_Left(40);
    // 设置 FloatingBox 的顶部位置
    aBox->set_Top(80);
    // 设置 FloatingBox 的水平对齐
    aBox->set_HorizontalAlignment(HorizontalAlignment::Center);
    
    // 向 FloatingBox 的段落集合中添加文本片段    
    aBox->get_Paragraphs()->Add(MakeObject<TextFragment>(u"main text"));

    // 设置 FloatingBox 的边框
    aBox->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));

    // 添加背景图像
    auto image = MakeObject<Image>();
    image->set_File(_dataDir + u"aspose-logo.png");
    aBox->set_BackgroundImage(image);

    // 设置 FloatingBox 的背景颜色
    aBox->set_BackgroundColor(Color::get_Yellow());

    // 将 FloatingBox 添加到页面对象的段落集合中
    page->get_Paragraphs()->Add(aBox);
    // 保存 PDF 文档
    document->Save(_dataDir + outputFileName);
}
```