---
title: C++를 사용하여 PDF 문서 생성
linktitle: 생성
type: docs
weight: 10
url: ko/cpp/create-document/
description: PDF 파일 작업의 가장 인기 있고 기본적인 작업은 처음부터 문서를 만드는 것입니다. Aspose.PDF for C++ 라이브러리를 사용하세요.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++** API는 C++ 애플리케이션 개발자가 애플리케이션에 PDF 문서 처리 기능을 포함할 수 있게 해줍니다. 기본 머신에 다른 소프트웨어가 설치되어 있지 않아도 PDF 파일을 생성하고 읽을 수 있습니다. Aspose.PDF for C++는 QT, MFC 및 콘솔 앱과 같은 다양한 C++ 애플리케이션 유형에서 사용할 수 있습니다.

## C++를 사용하여 PDF 파일을 생성하는 방법

C++를 사용하여 PDF 파일을 생성하려면 다음 단계를 사용할 수 있습니다.

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체를 인스턴스화합니다.
1. 문서 객체에 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/)를 추가합니다.
1. [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) 객체를 생성합니다.
1. [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/)을 페이지의 [Paragraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs/) 컬렉션에 추가합니다.
1. 결과 PDF 문서를 저장합니다.

```cpp
void CreatePDF() {
    // 경로 이름을 위한 문자열.
    String _dataDir("C:\\Samples\\");

    // 파일 이름을 위한 문자열.
    String filename("sample-new.pdf");

    // 문서 객체를 초기화합니다.
    auto document = MakeObject<Document>();
    // 페이지 추가
    auto page = document->get_Pages()->Add();

    // 새 페이지에 텍스트 추가
    auto textFragment = MakeObject<TextFragment>(u"Hello World!");
    page->get_Paragraphs()->Add(textFragment);

    // 업데이트된 PDF 저장
    String outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```