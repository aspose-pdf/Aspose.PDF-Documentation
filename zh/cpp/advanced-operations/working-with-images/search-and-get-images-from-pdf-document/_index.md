---
title: 使用C++从PDF文档中搜索和获取图像
linktitle: 搜索和获取图像
type: docs
weight: 60
url: zh/cpp/search-and-get-images-from-pdf-document/
description: 本节解释如何使用Aspose.PDF库从PDF文档中搜索和获取图像。
lastmod: "2021-12-18"
---

ImagePlacementAbsorber允许您在PDF文档的所有页面中搜索图像。

要在整个文档中搜索图像：

1. 调用[Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection)集合的[Accept](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#ae71a2782e747936e3c14b7ded5c6dc3f)方法。Accept方法将[ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_absorber/)对象作为参数。这将返回一个ImagePlacement对象的集合。
2. 循环遍历ImagePlacements对象并获取其属性（图像、尺寸、分辨率等）。

以下代码片段展示了如何搜索文档中的所有图像。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SearchAndGetImagesFromPDFDocument() {

    String _dataDir("C:\\Samples\\");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + u"SearchAndGetImages.pdf");

    // 创建 ImagePlacementAbsorber 对象来执行图像放置搜索
    auto abs = MakeObject<ImagePlacementAbsorber>();

    // 接受所有页面的吸收器
    document->get_Pages()->Accept(abs);

    // 遍历所有 ImagePlacements，获取图像和 ImagePlacement 属性
    for(auto imagePlacement : abs->get_ImagePlacements())
    {
        // 使用 ImagePlacement 对象获取图像
        auto image = imagePlacement->get_Image();

        // 显示所有放置的图像放置属性
        Console::WriteLine(u"图像宽度: {0}", imagePlacement->get_Rectangle()->get_Width());
        Console::WriteLine(u"图像高度:{0}", imagePlacement->get_Rectangle()->get_Height());
        Console::WriteLine(u"图像 LLX:{0}", imagePlacement->get_Rectangle()->get_LLX());
        Console::WriteLine(u"图像 LLY:{0}", imagePlacement->get_Rectangle()->get_LLY());
        Console::WriteLine(u"图像水平分辨率:{0}", imagePlacement->get_Resolution()->get_X());
        Console::WriteLine(u"图像垂直分辨率:{0}", imagePlacement->get_Resolution()->get_Y());
    }
}
```