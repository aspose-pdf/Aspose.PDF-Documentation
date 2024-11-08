---
title: C++를 사용하여 PDF 파일에서 이미지 추출
linktitle: 이미지 추출
type: docs
weight: 30
url: /ko/cpp/extract-images-from-pdf-file/
description: 이 섹션은 C++ 라이브러리를 사용하여 PDF 파일에서 이미지를 추출하는 방법을 보여줍니다.
lastmod: "2021-12-18"
---

Aspose.PDF for C++를 사용하여 PDF 문서에서 모든 이미지를 추출하여 다른 프로그램에서 재사용할 수 있는 별도의 파일로 저장할 수 있습니다.

이미지는 각 페이지의 Resources 컬렉션의 Images 컬렉션에 저장됩니다. 특정 페이지를 추출한 다음, 이미지의 특정 인덱스를 사용하여 Images 컬렉션에서 이미지를 가져옵니다.

이미지의 인덱스는 [XImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image) 객체를 반환합니다. 이 객체는 추출된 이미지를 저장할 수 있는 Save 메서드를 제공합니다.

다음 코드 스니펫은 PDF 파일에서 이미지를 추출하는 방법을 보여줍니다.

```cpp
void WorkingWithImages::ExtractImages()
{
    String _dataDir("C:\\Samples\\");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + u"ExtractImages.pdf");

    // 특정 이미지 추출
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(_dataDir + u"output.jpg");

    // 출력 이미지 저장
    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();

    // 업데이트된 PDF 파일 저장
    document->Save(_dataDir + u"ExtractImages_out.pdf");
}
```