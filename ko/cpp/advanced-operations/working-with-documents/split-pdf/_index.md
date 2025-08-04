---
title: PDF를 프로그래밍 방식으로 분할
linktitle: PDF 파일 분할
type: docs
weight: 60
url: /ko/cpp/split-pdf-document/
description: 이 주제는 C++로 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다.
lastmod: "2022-09-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 라이브 예제

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter)는 프레젠테이션 분할 기능이 어떻게 작동하는지 조사할 수 있는 무료 온라인 웹 애플리케이션입니다.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

이 주제는 C++ 애플리케이션에서 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다. C++를 사용하여 PDF 페이지를 단일 페이지 PDF 파일로 분할하려면 다음 단계를 따를 수 있습니다:

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체의 [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) 컬렉션을 통해 PDF 문서의 페이지를 반복합니다.
1. 각 반복마다 새로운 Document 객체를 생성하고 개별 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 객체를 빈 문서에 복사합니다.
1. Save 메소드를 사용하여 새 PDF를 저장합니다.

다음 C++ 코드 스니펫은 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다.

```cpp
void SplittingDocuments() {
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름을 위한 문자열
    String documentFileName("sample.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + documentFileName);

    int pageCount = 1;

    // 모든 페이지를 순회합니다.
    for(auto page : document->get_Pages())
    {
        auto newDocument = MakeObject<Document>(_dataDir + documentFileName);
        newDocument->get_Pages()->CopyPage(page);
        newDocument->Save(_dataDir + u"page_" + pageCount + u"_out.pdf");
        pageCount++;
    }
}
```