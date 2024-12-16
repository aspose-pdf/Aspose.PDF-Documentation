---
title: C++로 PDF 파일에 링크 생성
linktitle: 링크 생성
type: docs
weight: 10
url: /ko/cpp/create-links/
description: 이 섹션은 C++로 PDF 문서에 링크를 생성하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 링크 생성

문서에 애플리케이션 링크를 추가함으로써 문서에서 애플리케이션으로 링크를 설정할 수 있습니다. 이는 독자가 튜토리얼의 특정 지점에서 특정 작업을 수행하거나 기능이 풍부한 문서를 생성하고자 할 때 유용합니다. 애플리케이션 링크를 생성하려면:

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체를 생성합니다.
1. 링크를 추가하려는 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)를 가져옵니다.
1. Page 및 [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle) 객체를 사용하여 [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) 객체를 생성합니다.
1. 링크 속성을 [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) 객체를 사용하여 설정합니다.
1. 또한, [LaunchAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.launch_action/) 객체의 Action 속성을 설정합니다.
1. [LaunchAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.launch_action/) 객체를 생성할 때 실행하려는 애플리케이션을 지정합니다.
1. 페이지 객체의 [Annotations](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.annotations) 속성에 링크를 추가합니다.
1. 마지막으로, Document 객체의 Save 메서드를 사용하여 업데이트된 PDF를 저장합니다.

다음 코드 스니펫은 PDF 파일에 애플리케이션에 대한 링크를 생성하는 방법을 보여줍니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;

void CreateLink() 
{
    String _dataDir("C:\\Samples\\");
    // Document 인스턴스 생성
    auto document = MakeObject<Document>(_dataDir + u"CreateApplicationLink.pdf");

    // PDF 파일의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->idx_get(1);

    auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 200, 300, 300));
    link->set_Color(Aspose::Pdf::Color::get_Green());
    link->set_Action(MakeObject<Aspose::Pdf::Annotations::LaunchAction>(document, _dataDir + u"sample.pdf"));
    page->get_Annotations()->Add(link);

    // 업데이트된 문서 저장
    document->Save(_dataDir + u"CreateApplicationLink.pdf");
}
```
### PDF 파일에 PDF 문서 링크 만들기

Aspose.PDF for C++를 사용하면 외부 PDF 파일에 링크를 추가하여 여러 문서를 함께 연결할 수 있습니다. PDF 문서 링크를 만들려면:

1. 먼저, [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체를 생성합니다.
1. 그런 다음, 링크를 추가하려는 특정 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)를 가져옵니다.
1. Page와 [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle) 객체를 사용하여 [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) 객체를 생성합니다.
1. [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) 객체를 사용하여 링크 속성을 설정합니다.
1. [GoToRemoteAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_remote_action/) 객체로 Action 속성을 설정합니다.
1. 문서의 내용을 한국어로 번역한 결과는 다음과 같습니다:

GoToRemoteAction 객체를 생성할 때 실행할 PDF 파일과 열어야 할 페이지 번호를 지정하세요.
1. 링크를 Page 객체의 Annotations 컬렉션에 추가합니다.
1. Document 객체의 Save 메서드를 사용하여 업데이트된 PDF를 저장합니다.

다음 코드 스니펫은 PDF 파일에서 PDF 문서 링크를 생성하는 방법을 보여줍니다.

 ```cpp
void CreatePDFDocumentLink() 
{

    String _dataDir("C:\\Samples\\");
    // Document 인스턴스 생성
    auto document = MakeObject<Document>(_dataDir + u"CreateDocumentLink.pdf");

    // PDF 파일의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->idx_get(1);


    auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 200, 300, 300));
    link->set_Color(Aspose::Pdf::Color::get_Green());

    link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToRemoteAction>(_dataDir + u"sample.pdf", 1));
    page->get_Annotations()->Add(link);

    // 업데이트된 문서 저장
    document->Save(_dataDir + u"CreateDocumentLink_out.pdf");
}
```