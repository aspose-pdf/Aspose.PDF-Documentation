---
title: C++를 사용하여 기본 글꼴 이름 설정
linktitle: 기본 글꼴 이름 설정
type: docs
weight: 90
url: ko/cpp/set-default-font-name/
description: 이 섹션에서는 C++ 라이브러리를 사용하여 기본 글꼴 이름을 설정하는 방법을 설명합니다.
lastmod: "2021-12-18"
---

**Aspose.PDF for C++** API는 문서에 글꼴이 없을 때 기본 글꼴 이름을 설정할 수 있게 해줍니다. RenderingOptions 클래스의 DefaultFontName 속성을 사용하여 기본 글꼴 이름을 설정할 수 있습니다. DefaultFontName이 `nullptr`로 설정된 경우 **Times New Roman** 글꼴이 사용됩니다. 다음 코드 스니핏은 PDF를 이미지로 저장할 때 기본 글꼴 이름을 설정하는 방법을 보여줍니다:

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