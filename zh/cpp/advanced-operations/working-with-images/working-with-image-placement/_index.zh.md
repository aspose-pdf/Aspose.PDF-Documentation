---
title: 使用 C++ 进行图像放置
linktitle: 使用图像放置
type: docs
weight: 50
url: /cpp/working-with-image-placement/
description: 本节介绍使用 C++ 库处理图像放置 PDF 文件的功能。
lastmod: "2021-12-18"
---

**Aspose.PDF for C++** 支持 [ImagePlacement](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement), [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_absorber) 和 [ImagePlacementCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_collection)，它们提供与上述类类似的功能，以获取图像在 PDF 文档中的分辨率和位置。

- ImagePlacementAbsorber 执行图像使用搜索作为 ImagePlacement 对象集合。
- ImagePlacement 提供返回实际图像放置值的成员 Resolution 和 Rectangle。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithImagePlacement() {

    String _dataDir("C:\\Samples\\");

    // 加载源 PDF 文档
    auto document = MakeObject<Aspose::Pdf::Document>(_dataDir + u"ImagePlacement.pdf");

    auto abs = MakeObject<ImagePlacementAbsorber>();

    // 加载第一页的内容
    document->get_Pages()->idx_get(1)->Accept(abs);
    for(auto imagePlacement : abs->get_ImagePlacements())
    {
        // 获取图像属性
        Console::WriteLine(u"图像宽度: {0}", imagePlacement->get_Rectangle()->get_Width());
        Console::WriteLine(u"图像高度:{0}", imagePlacement->get_Rectangle()->get_Height());
        Console::WriteLine(u"图像 LLX:{0}", imagePlacement->get_Rectangle()->get_LLX());
        Console::WriteLine(u"图像 LLY:{0}", imagePlacement->get_Rectangle()->get_LLY());
        Console::WriteLine(u"图像水平分辨率:{0}", imagePlacement->get_Resolution()->get_X());
        Console::WriteLine(u"图像垂直分辨率:{0}", imagePlacement->get_Resolution()->get_Y());

        // 获取可见尺寸的图像
        auto imageStream = MakeObject<System::IO::MemoryStream>();

        // 从资源中检索图像
        imagePlacement->get_Image()->Save(imageStream, System::Drawing::Imaging::ImageFormat::get_Png());
        auto resourceImage = System::DynamicCast< System::Drawing::Bitmap>(System::Drawing::Bitmap::FromStream(imageStream));

        // 创建实际尺寸的位图
        auto scaledImage = MakeObject<System::Drawing::Bitmap>(resourceImage, (int)imagePlacement->get_Rectangle()->get_Width(), (int)imagePlacement->get_Rectangle()->get_Height());
        // ...

    }

}
```