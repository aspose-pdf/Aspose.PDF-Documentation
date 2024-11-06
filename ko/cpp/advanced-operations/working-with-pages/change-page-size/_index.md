---
title: Change PDF Page Size Programmatically 
linktitle: Change PDF Page Size
type: docs
weight: 40
url: ko/cpp/change-page-size/
description: C++ 라이브러리를 사용하여 PDF 파일의 페이지 크기를 변경합니다.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF는 정적 레이아웃의 인쇄 가능 형식이기 때문에 비즈니스 생활에서 널리 사용되고 있습니다.

그러나 페이지 크기가 용지 크기보다 큰 경우 PDF 문서의 크기를 조정해야 하는 작업이 있을 수 있습니다. 하지만 어떻게 할까요?

걱정하지 마세요. 이 페이지에서는 작업을 해결하는 방법을 찾을 수 있습니다.

하지만 먼저 페이지 크기 시리즈가 있다는 것을 기억합시다.

세계적으로 널리 채택된 두 가지 페이지 크기 시리즈가 있습니다.
물론 많은 형식이 있지만 가장 일반적으로 사용되는 것들이 있습니다.
첫 번째는 ISO 종이 크기입니다. Series A4는 표준 인쇄 및 문구류에 사용됩니다. Letter 크기의 종이는 포스터, 벽 차트 등에 사용됩니다. 미국, 캐나다, 그리고 부분적으로 멕시코는 두 번째 페이지 크기 시리즈를 채택했으며, 오늘날 ISO 표준 종이 크기가 아직 널리 사용되지 않는 유일한 산업 국가들입니다.

이제 Aspose.PDF가 C++ 라이브러리를 사용하여 페이지 크기를 조정하도록 유도하는 방법을 살펴보겠습니다.

## PDF 페이지 크기 변경

Aspose.PDF for C++를 사용하면 C++ 응용 프로그램에서 간단한 코드 라인으로 PDF 페이지 크기를 변경할 수 있습니다. 이 주제는 기존 PDF 파일의 페이지 치수(크기)를 업데이트/변경하는 방법을 설명합니다.

[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 클래스에는 페이지 크기를 설정할 수 있는 SetPageSize(...) 메서드가 포함되어 있습니다. 아래 코드 스니펫은 몇 가지 간단한 단계로 페이지 치수를 업데이트합니다:

1. 소스 PDF 파일을 로드합니다.
1. [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) 객체에 페이지를 가져옵니다.
1. 주어진 페이지를 가져옵니다.
1. SetPageSize(..) 메서드를 호출하여 크기를 업데이트합니다.  
1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스의 Save(..) 메서드를 호출하여 업데이트된 페이지 크기로 PDF 파일을 생성합니다.

다음 코드 스니펫은 PDF 페이지 크기를 A4 크기로 변경하는 방법을 보여줍니다.

```cpp
void ChangePageSize() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("UpdateDimensions.pdf");
    String outputFileName("UpdateDimensions_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 특정 페이지 가져오기
    auto pdfPage = document->get_Pages()->idx_get(1);

    // 페이지 크기를 A4 (11.7 x 8.3 인치)로 설정
    // Aspose.Pdf에서는 1인치 = 72포인트이므로 A4 크기는 (842.4, 597.6) 포인트입니다.
    pdfPage->SetPageSize(597.6, 842.4);
    // 업데이트된 문서 저장
    document->Save(_dataDir + outputFileName);
}
```

## PDF 페이지 크기 가져오기

기존 PDF 파일의 PDF 페이지 크기를 Aspose.PDF for C++를 사용하여 읽을 수 있습니다. 다음 코드 샘플은 C++을 사용하여 PDF 페이지의 크기를 읽는 방법을 보여줍니다.

```cpp
void GetPDFPageSize() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("UpdateDimensions.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 특정 페이지 가져오기
    auto page = document->get_Pages()->idx_get(1);

    // 페이지 높이와 너비 정보 가져오기
    Console::WriteLine(u"{0} {1}", page->GetPageRect(true)->get_Width(), page->GetPageRect(true)->get_Height());
    // 페이지를 90도 각도로 회전
    page->set_Rotate(Rotation::on90);
    // 페이지 높이와 너비 정보 가져오기
    Console::WriteLine(u"{0} {1}", page->GetPageRect(true)->get_Width(), page->GetPageRect(true)->get_Height());

}
```