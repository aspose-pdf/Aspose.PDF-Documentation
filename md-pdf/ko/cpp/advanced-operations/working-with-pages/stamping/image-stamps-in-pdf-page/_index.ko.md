---
title: PDF에 이미지 스탬프 프로그래밍 방식으로 추가하기
linktitle: PDF 파일의 이미지 스탬프
type: docs
weight: 10
url: /cpp/image-stamps-in-pdf-page/
description: Aspose.PDF for C++ 라이브러리의 ImageStamp 클래스를 사용하여 PDF 문서에 이미지 스탬프를 추가합니다.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 파일에 이미지 스탬프 추가하기

ImageStamp 클래스를 사용하여 PDF 파일에 이미지 스탬프를 추가할 수 있습니다. ImageStamp 클래스는 높이, 너비, 불투명도 등 이미지 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다.

이미지 스탬프를 추가하려면:

1. 필요한 속성을 사용하여 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체와 ImageStamp 객체를 만듭니다.
1. [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 클래스의 [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) 메서드를 호출하여 PDF에 스탬프를 추가합니다.

다음 코드 스니펫은 PDF 파일에 이미지 스탬프를 추가하는 방법을 보여줍니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddImageStampToPDFFile()
{    
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("AddImageStamp.pdf");

    String outputFileName("AddImageStamp_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Create image stamp
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");
    imageStamp->set_Background(true);
    imageStamp->set_XIndent(100);
    imageStamp->set_YIndent(100);
    imageStamp->set_Height(48);
    imageStamp->set_Width(225);
    imageStamp->set_Rotate(Rotation::on270);
    imageStamp->set_Opacity(0.5);
   
    // Add stamp to particular page    
    document->get_Pages()->idx_get(1)->AddStamp(imageStamp);

    // Save output document
    document->Save(_dataDir + outputFileName);
}
```

## 스탬프 추가 시 이미지 품질 제어

이미지를 스탬프 객체로 추가할 때 이미지의 품질을 제어할 수 있습니다. [ImageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_stamp) 클래스의 Quality 속성은 이 목적을 위해 사용됩니다. 이는 퍼센트로 이미지의 품질을 나타냅니다 (유효한 값은 0..100입니다).

```cpp
void ControlImageQualityWhenAddingStamp() {
    
    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름에 대한 문자열
    String inputFileName("AddImageStamp.pdf");
    String outputFileName("ControlImageQuality_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 이미지 스탬프 생성
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    imageStamp->set_Quality(10);
    document->get_Pages()->idx_get(1)->AddStamp(imageStamp);    
    document->Save(_dataDir + u"ControlImageQuality_out.pdf");
}
```

## 플로팅 박스 내 배경으로 이미지 스탬프

Aspose.PDF API는 플로팅 박스 내 배경으로 이미지 스탬프를 추가할 수 있게 합니다. FloatingBox 클래스의 BackgroundImage 속성은 다음 코드 샘플과 같이 플로팅 박스의 배경 이미지 스탬프를 설정하는 데 사용될 수 있습니다.

```cpp
void ImageStampAsBackgroundInFloatingBox() {

    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름에 대한 문자열
    String inputFileName("AddImageStamp.pdf");
    String outputFileName("AddImageStampAsBackgroundInFloatingBox_out.pdf");

    // Document 객체 인스턴스화
    auto document = MakeObject<Document>();

    // PDF 문서에 페이지 추가
    auto page = document->get_Pages()->Add();

    // FloatingBox 객체 생성
    auto aBox = MakeObject<FloatingBox>(200, 100);

    // FloatingBox의 왼쪽 위치 설정
    aBox->set_Left(40);
    // FloatingBox의 상단 위치 설정
    aBox->set_Top(80);
    // FloatingBox의 수평 정렬 설정
    aBox->set_HorizontalAlignment(HorizontalAlignment::Center);
    
    // FloatingBox의 단락 컬렉션에 텍스트 조각 추가    
    aBox->get_Paragraphs()->Add(MakeObject<TextFragment>(u"main text"));

    // FloatingBox의 테두리 설정
    aBox->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));

    // 배경 이미지 추가
    auto image = MakeObject<Image>();
    image->set_File(_dataDir + u"aspose-logo.png");
    aBox->set_BackgroundImage(image);

    // FloatingBox의 배경색 설정
    aBox->set_BackgroundColor(Color::get_Yellow());

    // 페이지 객체의 단락 컬렉션에 FloatingBox 추가
    page->get_Paragraphs()->Add(aBox);
    // PDF 문서 저장
    document->Save(_dataDir + outputFileName);
}
```