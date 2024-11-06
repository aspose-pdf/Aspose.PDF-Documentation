---
title: 使用C++设置图像大小
linktitle: 设置图像大小
type: docs
weight: 80
url: zh/cpp/set-image-size/
description: 本节介绍如何使用C++库设置PDF文件的图像大小。
lastmod: "2021-12-18"
---

可以设置要添加到PDF文件的图像的大小。为了设置大小，可以使用[Aspose.Pdf.Image类](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image)的[FixWidth](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image#a08f2f92b184632385eab19fb96c6d40e)和[FixHeight](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image#aed67b52e058b97df6931c214d7092dfa)属性。

以下代码片段演示了如何设置图像的大小：

```cpp
void WorkingWithImages::ExampleSetImageSize()
{
    String _dataDir("C:\\Samples\\");
    // 实例化Document对象
    auto document = MakeObject<Document>();
    // 向PDF文件的页面集合添加页面
    auto page = document->get_Pages()->Add();
    // 创建图像实例
    auto img = MakeObject<Image>();
    // 设置图像的宽度和高度（以点为单位）
    img->set_FixWidth(100);
    img->set_FixHeight(100);
    // 将图像类型设置为SVG
    img->set_FileType(Aspose::Pdf::ImageFileType::Unknown);
    // 源文件路径
    img->set_File(_dataDir + u"aspose-logo.jpg");
    page->get_Paragraphs()->Add(img);
    // 设置页面属性
    page->get_PageInfo()->set_Width(800);
    page->get_PageInfo()->set_Height(800);
    // 保存生成的PDF文件
    document->Save(_dataDir + u"SetImageSize_out.pdf");
}
```