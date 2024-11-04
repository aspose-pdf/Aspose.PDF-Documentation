---
title: C++를 사용한 이미지 배치 작업
linktitle: 이미지 배치 작업
type: docs
weight: 50
url: /cpp/working-with-image-placement/
description: 이 섹션에서는 C++ 라이브러리를 사용하여 이미지 배치 PDF 파일 작업의 기능에 대해 설명합니다.
lastmod: "2021-12-18"
---

**Aspose.PDF for C++**는 PDF 문서에서 이미지의 해상도와 위치를 얻기 위해 위에서 설명한 클래스와 유사한 기능을 제공하는 [ImagePlacement](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement), [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_absorber) 및 [ImagePlacementCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_collection)을 지원합니다.

- ImagePlacementAbsorber는 ImagePlacement 객체 컬렉션으로 이미지 사용 검색을 수행합니다.
- ImagePlacement는 실제 이미지 배치 값을 반환하는 Resolution 및 Rectangle 멤버를 제공합니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithImagePlacement() {

    String _dataDir("C:\\Samples\\");

    // 소스 PDF 문서 로드
    auto document = MakeObject<Aspose::Pdf::Document>(_dataDir + u"ImagePlacement.pdf");

    auto abs = MakeObject<ImagePlacementAbsorber>();

    // 첫 페이지의 내용 로드
    document->get_Pages()->idx_get(1)->Accept(abs);
    for(auto imagePlacement : abs->get_ImagePlacements())
    {
        // 이미지 속성 가져오기
        Console::WriteLine(u"image width: {0}", imagePlacement->get_Rectangle()->get_Width());
        Console::WriteLine(u"image height:{0}", imagePlacement->get_Rectangle()->get_Height());
        Console::WriteLine(u"image LLX:{0}", imagePlacement->get_Rectangle()->get_LLX());
        Console::WriteLine(u"image LLY:{0}", imagePlacement->get_Rectangle()->get_LLY());
        Console::WriteLine(u"image horizontal resolution:{0}", imagePlacement->get_Resolution()->get_X());
        Console::WriteLine(u"image vertical resolution:{0}", imagePlacement->get_Resolution()->get_Y());

        // 보이는 치수로 이미지 가져오기
        auto imageStream = MakeObject<System::IO::MemoryStream>();

        // 리소스에서 이미지 가져오기
        imagePlacement->get_Image()->Save(imageStream, System::Drawing::Imaging::ImageFormat::get_Png());
        auto resourceImage = System::DynamicCast< System::Drawing::Bitmap>(System::Drawing::Bitmap::FromStream(imageStream));

        // 실제 치수로 비트맵 생성
        auto scaledImage = MakeObject<System::Drawing::Bitmap>(resourceImage, (int)imagePlacement->get_Rectangle()->get_Width(), (int)imagePlacement->get_Rectangle()->get_Height());
        // ...

    }

}
```