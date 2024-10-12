---
title: PDF에서 이미지 추출
linktitle: PDF에서 이미지 추출
type: docs
weight: 20
url: /cpp/extract-images-from-the-pdf-file/
description: Aspose.PDF for C++를 사용하여 PDF에서 이미지의 일부를 추출하는 방법.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 문서 작업 시 많이 요구되는 작업 중 하나는 PDF 파일에서 이미지를 추출하는 것입니다. 예를 들어, 당신이 많은 훌륭한 이미지가 포함된 PDF 이메일을 받았고, 이를 개별 파일로 추출하고 싶을 수 있습니다.

Aspose.PDF 라이브러리는 다음 코드 조각을 사용하여 PDF에서 이미지를 추출할 수 있게 해줍니다:

```cpp
void ExtractImage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Parsing\\");

    // 파일 이름을 위한 문자열
    String infilename("sample-image.pdf");
    String outfilename("extracted_image.jpeg");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 특정 이미지 추출
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(_dataDir + outfilename);

    // 출력 이미지 저장
    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();

    std::clog << __func__ << ": Finish" << std::endl;
}
```