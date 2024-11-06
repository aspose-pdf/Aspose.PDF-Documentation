---
title: C++를 사용하여 PDF 병합
linktitle: PDF 파일 병합
type: docs
weight: 50
url: ko/cpp/merge-pdf-documents/
description: 이 페이지는 C++로 PDF 문서를 단일 PDF 파일로 병합하는 방법을 설명합니다.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

PDF 파일 병합은 쉽지 않지만 매우 인기 있는 작업입니다. Aspose.PDF for C++ 라이브러리를 사용하여 PDF 파일을 하나의 문서로 빠르고 쉽게 결합할 수 있습니다.

## C++를 사용하여 PDF 파일 병합

두 개의 PDF 파일을 연결하려면:

1. 입력 PDF 파일 각각을 포함하는 두 개의 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체를 생성합니다.
2. 그런 다음 다른 PDF 파일을 추가할 Document 객체에 대해 [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) 컬렉션의 Add 메서드를 호출합니다.
3. 두 번째 문서의 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)를 첫 번째 파일에 추가합니다.
4. 마지막으로 Save 메서드를 사용하여 출력 PDF 파일을 저장합니다.

다음 코드 스니펫은 PDF 파일을 연결하는 방법을 보여줍니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
void MergingDocuments() {
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름을 위한 문자열
    String pdfDocumentFileName1("Concat1.pdf");
    String pdfDocumentFileName2("Concat2.pdf");
    String outputFileName("ConcatenatePdfFiles.pdf");

    // 문서 열기
    auto pdfDocument1 = MakeObject<Document>(_dataDir + pdfDocumentFileName1);
    auto pdfDocument2 = MakeObject<Document>(_dataDir + pdfDocumentFileName2);

    // 두 번째 문서의 페이지를 첫 번째 문서에 추가
    pdfDocument1->get_Pages()->Add(pdfDocument2->get_Pages());

    // 병합된 출력 파일 저장
    pdfDocument1->Save(_dataDir+outputFileName);
}
```

## 라이브 예제

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger)는 프레젠테이션 병합 기능이 어떻게 작동하는지 조사할 수 있는 온라인 무료 웹 애플리케이션입니다.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)