---
title: PDF 문서에서 이미지 검색 및 가져오기 C++ 사용
linktitle: 검색 및 이미지 가져오기
type: docs
weight: 60
url: /cpp/search-and-get-images-from-pdf-document/
description: 이 섹션은 Aspose.PDF 라이브러리를 사용하여 PDF 문서에서 이미지를 검색하고 가져오는 방법을 설명합니다.
lastmod: "2021-12-18"
---

ImagePlacementAbsorber를 사용하면 PDF 문서의 모든 페이지에서 이미지를 검색할 수 있습니다.

문서 전체에서 이미지를 검색하려면:

1. [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) 컬렉션의 [Accept](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#ae71a2782e747936e3c14b7ded5c6dc3f) 메서드를 호출합니다. Accept 메서드는 [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_absorber/) 객체를 매개변수로 사용합니다. 이 메서드는 ImagePlacement 객체의 컬렉션을 반환합니다.
1. ImagePlacements 객체를 반복하여 그 속성(이미지, 치수, 해상도 등)을 가져옵니다.

다음 코드 스니펫은 문서의 모든 이미지를 검색하는 방법을 보여줍니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SearchAndGetImagesFromPDFDocument() {

    String _dataDir("C:\\Samples\\");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + u"SearchAndGetImages.pdf");

    // 이미지 배치 검색을 수행하기 위해 ImagePlacementAbsorber 객체 생성
    auto abs = MakeObject<ImagePlacementAbsorber>();

    // 모든 페이지에 대해 흡수기 수락
    document->get_Pages()->Accept(abs);

    // 모든 ImagePlacements를 순회하여 이미지 및 ImagePlacement 속성 가져오기
    for(auto imagePlacement : abs->get_ImagePlacements())
    {
        // ImagePlacement 객체를 사용하여 이미지 가져오기
        auto image = imagePlacement->get_Image();

        // 모든 배치에 대해 이미지 배치 속성 표시
        Console::WriteLine(u"이미지 너비: {0}", imagePlacement->get_Rectangle()->get_Width());
        Console::WriteLine(u"이미지 높이:{0}", imagePlacement->get_Rectangle()->get_Height());
        Console::WriteLine(u"이미지 LLX:{0}", imagePlacement->get_Rectangle()->get_LLX());
        Console::WriteLine(u"이미지 LLY:{0}", imagePlacement->get_Rectangle()->get_LLY());
        Console::WriteLine(u"이미지 수평 해상도:{0}", imagePlacement->get_Resolution()->get_X());
        Console::WriteLine(u"이미지 수직 해상도:{0}", imagePlacement->get_Resolution()->get_Y());
    }
}
```