---
title: PDF의 링크 업데이트
linktitle: 링크 업데이트
type: docs
weight: 20
url: /ko/cpp/update-links/
description: Aspose.PDF for C++로 PDF의 링크를 프로그래밍 방식으로 업데이트합니다. 이 가이드는 PDF 파일에서 링크를 업데이트하는 방법에 관한 것입니다.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 파일에서 링크 업데이트

PDF 파일에 하이퍼링크 추가에서 논의된 것처럼, [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) 클래스는 PDF 파일에 링크를 추가할 수 있게 해줍니다. PDF 파일 내부에서 기존 링크를 얻기 위해 사용되는 유사한 클래스도 있습니다. 기존 링크를 업데이트해야 할 경우 이것을 사용하십시오. 기존 링크를 업데이트하려면:

1. PDF 파일을 로드합니다.
1. PDF 파일의 특정 페이지로 이동합니다.
1. [GoToAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_action) 객체의 Destination 속성을 사용하여 링크 목적지를 지정합니다.
1. 대상 페이지는 [XYZExplicitDestination](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.x_y_z_explicit_destination) 생성자를 사용하여 지정됩니다.

### 동일 문서의 페이지로 링크 대상 설정

다음 코드 스니펫은 PDF 파일의 링크를 업데이트하고 해당 대상을 문서의 두 번째 페이지로 설정하는 방법을 보여줍니다.

```cpp
void SetLinkTargetToAPageInTheSameDocument()
{
    String _dataDir("C:\\Samples\\");
    // 문서 인스턴스 생성
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // 페이지를 PDF 파일의 페이지 컬렉션에 추가
    auto page = document->get_Pages()->idx_get(1);
    auto link = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // 링크 수정: 링크 대상 변경
    auto goToAction = System::DynamicCast<Aspose::Pdf::Annotations::GoToAction>(link->get_Action());

    // 링크 객체에 대한 대상을 지정
    // 창의 왼쪽 위 모서리에 위치한 좌표 (left, top)으로 페이지를 표시하고 페이지의 내용을 확대된 배율로 표시하는 명시적 대상을 나타냅니다.
    // 첫 번째 매개변수는 대상 페이지 번호입니다.
    // 두 번째는 왼쪽 좌표입니다.
    // 세 번째는 위쪽 좌표입니다.
    // 네 번째 인수는 해당 페이지를 표시할 때의 확대 배율입니다. 2를 사용하면 페이지가 200% 확대되어 표시됩니다.
    goToAction->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(1, 1, 2, 2));

    // 업데이트된 링크로 문서를 저장
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```
### 웹 주소로 링크 대상 설정

하이퍼링크가 웹 주소를 가리키도록 업데이트하려면 [GoToURIAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_u_r_i_action) 객체를 인스턴스화하고 이를 LinkAnnotation의 Action 속성에 전달하십시오. 다음 코드 스니펫은 PDF 파일의 링크를 업데이트하고 해당 대상을 웹 주소로 설정하는 방법을 보여줍니다.

```cpp
void SetLinkDestinationToWebAddress() 
{
    // PDF 파일 로드
    String _dataDir("C:\\Samples\\");
    // Document 인스턴스 생성
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // PDF 파일의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->idx_get(1);
    auto link = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // 링크 수정: 링크 작업 변경 및 대상을 웹 주소로 설정
    link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("www.aspose.com"));

    // 업데이트된 링크로 문서 저장
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### 다른 PDF 파일로 링크 대상 설정

다음 코드 스니펫은 PDF 파일의 링크를 업데이트하고 대상 파일을 다른 PDF 파일로 설정하는 방법을 보여줍니다.

```cpp
void SetLinkTargetToAnotherPDFFile()
{
    // PDF 파일 불러오기
    String _dataDir("C:\\Samples\\");
    // Document 인스턴스 생성
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // PDF 파일의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->idx_get(1);
    auto linkAnnot = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // 링크 수정: 링크 액션 변경 및 웹 주소로 대상 설정
    auto goToR = System::DynamicCast<Aspose::Pdf::Annotations::GoToRemoteAction>(linkAnnot->get_Action());
    // 다음 줄은 목적지를 업데이트하며, 파일을 업데이트하지 않음
    goToR->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(2, 0, 0, 1.5));
    // 다음 줄은 파일을 업데이트
    goToR->set_File(MakeObject<FileSpecification>(_dataDir + u"input.pdf"));

    // 업데이트된 링크로 문서를 저장
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### 링크 주석 텍스트 색상 업데이트

링크 주석에는 텍스트가 포함되어 있지 않습니다. 대신, 텍스트는 주석 아래의 페이지 내용에 배치됩니다. 따라서, 텍스트의 색상을 변경하려면 주석의 색상을 변경하려고 시도하는 대신 페이지 텍스트의 색상을 교체해야 합니다. 다음 코드 스니펫은 PDF 파일에서 링크 주석의 색상을 업데이트하는 방법을 보여줍니다.

```cpp
void UpdateLinkAnnotationTextColor() 
{
    // PDF 파일 로드
    String _dataDir("C:\\Samples\\");

    // Document 인스턴스 생성
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // PDF 파일의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->idx_get(1);

    for (auto annotation : page->get_Annotations())
    {
        if (annotation->get_AnnotationType() == Aspose::Pdf::Annotations::AnnotationType::Link)
        {
            // 주석 아래의 텍스트 검색
            auto ta = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>();
            auto rect = annotation->get_Rect();
            rect->set_LLX(rect->get_LLX() - 10);
            rect->set_LLY(rect->get_LLY() - 10);
            rect->set_URX(rect->get_URX() + 10);
            rect->set_URY(rect->get_URY() + 10);

            ta->set_TextSearchOptions(MakeObject<Aspose::Pdf::Text::TextSearchOptions>(rect));
            ta->Visit(page);
            // 텍스트의 색상 변경
            for (auto tf : ta->get_TextFragments())
            {
                tf->get_TextState()->set_ForegroundColor(Color::get_Red());
            }
        }

    }
    // 업데이트된 링크와 함께 문서 저장
    document->Save(_dataDir + u"UpdateLinkTextColor_out.pdf");
}
```