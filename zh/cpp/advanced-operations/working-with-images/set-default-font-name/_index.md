---
title: 使用C++设置默认字体名称
linktitle: 设置默认字体名称
type: docs
weight: 90
url: /zh/cpp/set-default-font-name/
description: 本节介绍如何使用C++库设置默认字体名称。
lastmod: "2021-12-18"
---

**Aspose.PDF for C++** API允许您在文档中没有可用字体时设置默认字体名称。您可以使用RenderingOptions类的DefaultFontName属性来设置默认字体名称。如果将DefaultFontName设置为`nullptr`，将使用**Times New Roman**字体。以下代码片段显示了如何在将PDF保存为图像时设置默认字体名称：

```cpp
void WorkingWithImages::ExampleSetDefaultFontName()
{
    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    auto imageStream = System::IO::File::OpenWrite(_dataDir + u"SetDefaultFontName.png");

    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);
    auto pngDevice = MakeObject<Aspose::Pdf::Devices::PngDevice>(resolution);
    auto ro = MakeObject<RenderingOptions>();
    ro->set_DefaultFontName(u"Arial");
    pngDevice->set_RenderingOptions(ro);
    pngDevice->Process(document->get_Pages()->idx_get(1), imageStream);
}
```