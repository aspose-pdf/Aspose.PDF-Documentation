---
title: Add Pages in PDF with C++
linktitle: Add Pages
type: docs
weight: 10
url: ko/cpp/add-pages/
description: 이 문서는 원하는 위치의 PDF 파일에 페이지를 삽입(추가)하는 방법을 가르칩니다. C++를 사용하여 PDF 파일에서 페이지를 이동, 제거(삭제)하는 방법을 알아보세요.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

이 섹션은 **Aspose.PDF for C++** 라이브러리를 사용하여 PDF에 페이지를 추가하는 방법을 보여줍니다.

Aspose.PDF for C++ API는 C++를 사용하여 PDF 문서의 페이지를 작업하는 데 완전한 유연성을 제공합니다.

PDF 문서의 모든 페이지를 [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection)에서 유지하며, 이를 사용하여 PDF 페이지를 작업할 수 있습니다.
Aspose.PDF for C++는 파일의 원하는 위치에 PDF 문서에 페이지를 삽입할 수 있을 뿐만 아니라 PDF 파일의 끝에 페이지를 추가할 수 있습니다.

## PDF 파일에 페이지 추가 또는 삽입

Aspose.PDF for C++는 파일의 원하는 위치에 PDF 문서에 페이지를 삽입할 수 있을 뿐만 아니라 PDF 파일의 끝에 페이지를 추가할 수 있습니다.

### 원하는 위치에 PDF 파일에 빈 페이지 삽입하기

다음 코드 샘플은 PDF 문서에 페이지를 추가하는 방법을 설명합니다.

1. 입력 PDF 파일로 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스 객체를 생성합니다.
1. 지정된 인덱스로 [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) 컬렉션의 [Insert](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#a1fb1fe44df4d325df5ad41b691501bb2) 메서드를 호출합니다.
1. 출력 PDF를 저장합니다.

다음 코드 스니펫은 PDF 파일에 페이지를 삽입하는 방법을 보여줍니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void InsertEmptyPageAtDesiredLocation() {
    // 문서 열기
    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름을 위한 문자열
    String inputFileName("InsertEmptyPage.pdf");

    String outputFileName("InsertEmptyPage_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // PDF에 빈 페이지 삽입
    document->get_Pages()->Insert(2);

    // 출력 파일 저장
    document->Save(_dataDir + outputFileName);
}
```

다음 코드 예제에서는 지정된 페이지의 매개변수를 복사하여 원하는 위치에 빈 페이지를 삽입할 수 있습니다.

```cpp
void InsertEmptyPageAtDesiredLocation2() {
    // 문서 열기
    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름에 대한 문자열
    String inputFileName("InsertEmptyPage.pdf");

    String outputFileName("InsertEmptyPage_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    auto page = document->get_Pages()->idx_get(1);
    // PDF에 빈 페이지 삽입
    auto pageNew = document->get_Pages()->Insert(2);

    // 페이지 1에서 페이지 매개변수 복사
    pageNew->set_ArtBox(page->get_ArtBox());
    pageNew->set_BleedBox(page->get_BleedBox());
    pageNew->set_CropBox(page->get_CropBox());
    pageNew->set_MediaBox(page->get_MediaBox());
    pageNew->set_TrimBox(page->get_TrimBox());

    // 출력 파일 저장
    document->Save(_dataDir + outputFileName);
}
```

### PDF 파일의 끝에 빈 페이지 추가

때로는 문서가 빈 페이지로 끝나도록 보장하고 싶습니다. 이 주제는 PDF 문서의 끝에 빈 페이지를 삽입하는 방법을 설명합니다.

PDF 파일의 끝에 빈 페이지를 삽입하려면:

1. 입력 PDF 파일로 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스 객체를 생성합니다.
1. [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) 컬렉션의 [Add](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) 메서드를 매개변수 없이 호출합니다.
1. Save 메서드를 사용하여 출력 PDF를 저장합니다.

다음 코드 스니펫은 PDF 파일의 끝에 빈 페이지를 삽입하는 방법을 보여줍니다.

```cpp
void AddEmptyPageEnd() {
    // 문서 열기
    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름을 위한 문자열
    String inputFileName("InsertEmptyPageAtEnd.pdf");
    String outputFileName("InsertEmptyPageAtEnd_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // PDF 파일의 끝에 빈 페이지를 삽입합니다
    document->get_Pages()->Add();

    // 출력 파일 저장
    document->Save(_dataDir + outputFileName);
}
```