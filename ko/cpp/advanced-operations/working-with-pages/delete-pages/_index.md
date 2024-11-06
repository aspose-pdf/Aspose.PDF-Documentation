---
title: PDF 페이지 프로그래밍 방식으로 삭제
linktitle: PDF 페이지 삭제
type: docs
weight: 30
url: ko/cpp/delete-pages/
description: C++ 라이브러리를 사용하여 PDF 파일에서 페이지를 삭제할 수 있습니다.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for C++를 사용하여 PDF 파일에서 페이지를 삭제할 수 있습니다. [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) 컬렉션에서 특정 페이지를 삭제합니다.

## PDF 파일에서 페이지 삭제

1. [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a02bb7a96e66ef6e10bcf4930b299b3b7) 메서드를 호출하고 페이지의 인덱스를 지정합니다.
1. Save 메서드를 호출하여 업데이트된 PDF 파일을 저장합니다.
다음 코드 스니펫은 C++를 사용하여 PDF 파일에서 특정 페이지를 삭제하는 방법을 보여줍니다.

```cpp
void DeletePDFPages() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("DeleteParticularPage.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 특정 페이지 삭제
    document->get_Pages()->Delete(2);

    // 업데이트된 PDF 저장
    document->Save(_dataDir + inputFileName);
}
```