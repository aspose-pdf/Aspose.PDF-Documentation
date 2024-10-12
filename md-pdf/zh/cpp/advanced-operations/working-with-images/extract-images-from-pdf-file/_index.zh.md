---
title: 提取PDF文件中的图像使用C++
linktitle: 提取图像
type: docs
weight: 30
url: /cpp/extract-images-from-pdf-file/
description: 本节展示如何使用C++库从PDF文件中提取图像。
lastmod: "2021-12-18"
---

您可以使用Aspose.PDF for C++将PDF文档中的所有图像提取到可以在其他程序中重复使用的单独文件中。

图像存储在每个页面的资源集合的图像集合中。要提取特定页面，然后使用图像的特定索引从图像集合中获取图像。

图像的索引返回一个[XImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image)对象。该对象提供了一个Save方法，可以用来保存提取的图像。

以下代码片段展示了如何从PDF文件中提取图像。

```cpp
void WorkingWithImages::ExtractImages()
{
    String _dataDir("C:\\Samples\\");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + u"ExtractImages.pdf");

    // 提取特定图像
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(_dataDir + u"output.jpg");

    // 保存输出图像
    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();

    // 保存更新后的PDF文件
    document->Save(_dataDir + u"ExtractImages_out.pdf");
}
```