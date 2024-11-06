---
title: C++를 사용하여 이미지 크기 설정
linktitle: 이미지 크기 설정
type: docs
weight: 80
url: ko/cpp/set-image-size/
description: 이 섹션에서는 C++ 라이브러리를 사용하여 PDF 파일의 이미지 크기를 설정하는 방법을 설명합니다.
lastmod: "2021-12-18"
---

PDF 파일에 추가되는 이미지의 크기를 설정할 수 있습니다. 크기를 설정하려면 [Aspose.Pdf.Image 클래스](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image)의 [FixWidth](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image#a08f2f92b184632385eab19fb96c6d40e) 및 [FixHeight](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image#aed67b52e058b97df6931c214d7092dfa) 속성을 사용할 수 있습니다.

다음 코드 스니펫은 이미지의 크기를 설정하는 방법을 보여줍니다:

```cpp
void WorkingWithImages::ExampleSetImageSize()
{
    String _dataDir("C:\\Samples\\");
    // Document 객체를 인스턴스화합니다
    auto document = MakeObject<Document>();
    // PDF 파일의 페이지 컬렉션에 페이지를 추가합니다
    auto page = document->get_Pages()->Add();
    // 이미지 인스턴스를 생성합니다
    auto img = MakeObject<Image>();
    // 이미지 너비와 높이를 포인트 단위로 설정합니다
    img->set_FixWidth(100);
    img->set_FixHeight(100);
    // 이미지 유형을 SVG로 설정합니다
    img->set_FileType(Aspose::Pdf::ImageFileType::Unknown);
    // 소스 파일의 경로
    img->set_File(_dataDir + u"aspose-logo.jpg");
    page->get_Paragraphs()->Add(img);
    // 페이지 속성을 설정합니다
    page->get_PageInfo()->set_Width(800);
    page->get_PageInfo()->set_Height(800);
    // 결과 PDF 파일을 저장합니다
    document->Save(_dataDir + u"SetImageSize_out.pdf");
}
```