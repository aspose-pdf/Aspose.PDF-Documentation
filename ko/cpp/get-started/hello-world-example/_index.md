---
title: Aspose.PDF С++ 예제
linktitle: Hello World 예제
type: docs
weight: 40
url: ko/cpp/hello-world-example/
description: 이 페이지는 간단한 프로그래밍으로 텍스트 - Hello World를 포함하는 PDF 문서를 만드는 방법을 보여줍니다.
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.6
---

"Hello World" 예제는 전통적으로 프로그래밍 언어나 소프트웨어의 기능을 간단한 사용 사례로 소개하는 데 사용됩니다.

Aspose.PDF for C++는 개발자가 C++ 애플리케이션에 PDF 문서 생성, 조작 및 변환 기능을 포함할 수 있도록 하는 기능이 풍부한 PDF API입니다. PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX 및 이미지 파일 형식을 포함한 많은 인기 있는 파일 형식을 지원합니다. 이 기사에서는 "Hello World!"라는 텍스트를 포함하는 PDF 문서를 생성합니다. 환경에 Aspose.PDF for C++를 설치한 후 아래 코드 샘플을 실행하여 Aspose.PDF API가 어떻게 작동하는지 확인할 수 있습니다.

아래 코드 조각은 다음 단계에 따릅니다:

1. 문자열 클래스](https://reference.aspose.com/pdf/cpp/class/system.string)를 경로 이름 및 파일 이름에 대해 생성하세요.
1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체를 인스턴스화합니다. 이 단계에서는 메타데이터는 있지만 페이지가 없는 빈 PDF 문서를 생성합니다.
1. 문서 객체에 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)를 추가합니다. 이제 문서에 한 페이지가 있습니다.
1. 결과 PDF 문서를 [저장](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa)합니다.

다음 코드 스니펫은 Aspose.PDF for C++ API의 작동을 보여주는 Hello World 프로그램입니다.

```cpp
void ExampleSimple()
{
    // 결합된 경로를 저장할 버퍼.
    String outputFileName;

    // 경로 이름을 위한 문자열.
    String _dataDir("C:\\Samples\\");

    // 파일 이름을 위한 문자열.
    String filename("HelloWorld_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // 새 페이지에 텍스트 추가
    auto text = MakeObject<TextFragment>(u"Hello world!");

    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // 업데이트된 PDF 저장
    outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```