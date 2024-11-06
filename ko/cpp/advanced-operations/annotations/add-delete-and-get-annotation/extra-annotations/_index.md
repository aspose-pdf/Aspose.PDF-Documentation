---
title: 추가 주석 사용 C++
linktitle: 추가 주석
type: docs
weight: 60
url: ko/cpp/extra-annotations/
description: 이 섹션은 PDF 문서에서 추가 종류의 주석을 추가, 가져오기 및 삭제하는 방법을 설명합니다.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 기존 PDF 파일에 Caret 주석 추가하는 방법

Caret 주석은 텍스트 편집을 나타내는 기호입니다. Caret 주석은 또한 마크업 주석이므로, Caret 클래스는 Markup 클래스에서 파생되며 Caret 주석의 속성을 가져오거나 설정하고 Caret 주석 모양의 흐름을 재설정하는 기능을 제공합니다.

Caret 주석을 생성하는 단계:

1. PDF 파일을 로드합니다 - 새로운 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. 새로운 [Caret Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.caret_annotation/)을 생성하고 Caret 매개변수(새 Rectangle, 제목, 주제, 플래그, 색상, 너비, StartingStyle 및 EndingStyle)를 설정합니다. 이 주석은 텍스트 삽입을 나타내는 데 사용됩니다.
1. 새로운 [Caret Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.caret_annotation/)을 생성하고 Caret 매개변수(새 Rectangle, 제목, 주제, 플래그, 색상, 너비, StartingStyle 및 EndingStyle)를 설정합니다. 이 주석은 텍스트 교체를 나타내는 데 사용됩니다.
1. 새로운 [StrikeOutAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.strike_out_annotation/)을 생성하고 매개변수(새 Rectangle, 제목, 색상, 새 QuadPoints 및 새 포인트, 주제, InReplyTo, ReplyType)를 설정합니다.
1. 그런 다음 페이지에 주석을 추가할 수 있습니다.

다음 코드 스니펫은 PDF 파일에 Caret Annotation을 추가하는 방법을 보여줍니다:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void MarkupAnnotations::AddCaretAnnotation() {
    String _dataDir("C:\\Samples\\");

    // PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    // 이 주석은 텍스트 삽입을 나타내는 데 사용됩니다
    auto caretAnnotation1 = MakeObject<CaretAnnotation>(
        document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(299.988, 713.664, 308.708, 720.769));
    caretAnnotation1->set_Title(u"Aspose User");
    caretAnnotation1->set_Subject(u"Inserted text 1");
    caretAnnotation1->set_Flags(AnnotationFlags::Print);
    caretAnnotation1->set_Color(Color::get_Blue());

    // 이 주석은 텍스트 교체를 나타내는 데 사용됩니다
    auto caretAnnotation2 = MakeObject<CaretAnnotation>(
        document->get_Pages()->idx_get(1),
        new Rectangle(361.246, 727.908, 370.081, 735.107));

    caretAnnotation2->set_Title(u"Aspose User");
    caretAnnotation2->set_Flags(AnnotationFlags::Print);
    caretAnnotation2->set_Subject(u"Inserted text 2");
    caretAnnotation2->set_Color(Color::get_Blue());

    auto strikeOutAnnotation = MakeObject<StrikeOutAnnotation>(
        document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(318.407, 727.826, 368.916, 740.098));

    strikeOutAnnotation->set_Color(Color::get_Blue());

    strikeOutAnnotation->set_QuadPoints(
        MakeArray<System::SharedPtr<Point>>({
            MakeObject<Point>(321.66, 739.416),
            MakeObject<Point>(365.664, 739.416),
            MakeObject<Point>(321.66, 728.508),
            MakeObject<Point>(365.664, 728.508) }));

    strikeOutAnnotation->set_Subject(u"Cross-out");
    strikeOutAnnotation->set_InReplyTo(caretAnnotation2);
    strikeOutAnnotation->set_ReplyType(ReplyType::Group);

    document->get_Pages()->idx_get(1)->get_Annotations()->Add(caretAnnotation1);
    document->get_Pages()->idx_get(1)->get_Annotations()->Add(caretAnnotation2);
    document->get_Pages()->idx_get(1)->get_Annotations()->Add(strikeOutAnnotation);

    document->Save(_dataDir + u"sample_caret.pdf");
}
```
### 캐럿 주석 가져오기

PDF 문서에서 캐럿 주석을 가져오기 위해 다음 코드 스니펫을 사용해 보세요.

```cpp
void MarkupAnnotations::GetCaretAnnotation() {

    String _dataDir("C:\\Samples\\");
    // PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"sample_caret.pdf");

    // AnnotationSelector를 사용하여 주석 필터링
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<CaretAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto caretAnnotations = annotationSelector->get_Selected();

    // 결과 출력
    for (auto ca : caretAnnotations) {
        Console::WriteLine(ca->get_Rect());
    }
}
```

### 캐럿 주석 삭제

다음 코드 스니펫은 PDF 파일에서 캐럿 주석을 삭제하는 방법을 보여줍니다.

```cpp

void MarkupAnnotations::DeleteCaretAnnotation() {

    String _dataDir("C:\\Samples\\");
    // PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"sample_caret.pdf");

    // AnnotationSelector를 사용하여 주석 필터링
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<CaretAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto caretAnnotations = annotationSelector->get_Selected();

    // 주석 삭제
    for (auto ca : caretAnnotations) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(ca);
    }
    document->Save(_dataDir + u"sample_caret_del.pdf");
}
```

## 링크 주석 추가 방법

[링크 주석](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation)은 문서의 다른 위치로 이동하거나 수행할 작업으로 이어지는 하이퍼텍스트 링크입니다.

링크는 페이지 어디에나 배치할 수 있는 사각형 영역입니다. 각 링크에는 해당 링크 영역을 클릭할 때 수행되는 관련 PDF 작업이 있습니다.

다음 코드 스니펫은 전화번호 예제를 사용하여 PDF 파일에 링크 주석을 추가하는 방법을 보여줍니다:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddLinkAnnotation() {
    String _dataDir("C:\\Samples\\");

    // PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    auto page = document->get_Pages()->idx_get(1);

    // 전화번호를 찾기 위해 TextFragmentAbsorber 객체 생성
    auto textFragmentAbsorber = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>("678-555-0103");

    // 첫 번째 페이지에 대해 흡수기 수락
    page->Accept(textFragmentAbsorber);

    auto phoneNumberFragment = textFragmentAbsorber->get_TextFragments()->idx_get(1);

    // 링크 주석 생성 및 전화번호 호출 작업 설정
    auto linkAnnotation = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, phoneNumberFragment->get_Rectangle());
    linkAnnotation->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("callto:678-555-0103"));

    // 페이지에 주석 추가
    page->get_Annotations()->Add(linkAnnotation);
    document->Save(_dataDir + u"SimpleResume_mod.pdf");
}
```

### 링크 주석 가져오기

PDF 문서에서 LinkAnnotation을 가져오기 위해 다음 코드 스니펫을 사용해 보세요.

```cpp
void GetLinkAnnotations() {

    String _dataDir("C:\\Samples\\");
    // PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"SimpleResume_mod.pdf");

    // AnnotationSelector를 사용하여 주석 필터링
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto linkAnnotations = annotationSelector->get_Selected();

    // 결과 출력
    for (auto la : linkAnnotations) {

        auto l = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(la);

        // 각 링크 주석의 URL 출력
        Console::WriteLine(u"URI: " + System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(l->get_Action())->get_URI());

        auto absorber = MakeObject<TextAbsorber>();
        absorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
        absorber->get_TextSearchOptions()->set_Rectangle(l->get_Rect());
        page->Accept(absorber);

        String extractedText = absorber->get_Text();

        // 하이퍼링크와 연결된 텍스트 출력
        Console::WriteLine(extractedText);
    }
}
```

### 링크 주석 삭제

다음 코드 스니펫은 PDF 파일에서 링크 주석을 삭제하는 방법을 보여줍니다. 이를 위해 1페이지에 있는 모든 링크 주석을 찾아 제거해야 합니다. 그런 다음 주석이 제거된 문서를 저장합니다.

```cpp
void DeleteLinkAnnotations()
{
    String _dataDir("C:\\Samples\\");
    // PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"SimpleResume_mod.pdf");

    // AnnotationSelector를 사용하여 주석 필터링
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto lineAnnotations = annotationSelector->get_Selected();

    // 결과 출력
    for (auto la : lineAnnotations) {
        page->get_Annotations()->Delete(la);
    }

    // 주석이 제거된 문서 저장
    document->Save(_dataDir + u"SimpleResume_del.pdf");
}
```

## Redact certain page region with Redaction Annotation using Aspose.PDF for C++

Aspose.PDF for C++는 기존 PDF 파일에서 주석을 추가하고 조작하는 기능을 지원합니다. 최근 일부 고객이 PDF 문서의 특정 페이지 영역에서 텍스트, 이미지 등의 요소를 삭제(편집)해야 한다고 요청했습니다. 이러한 요구를 충족하기 위해 RedactionAnnotation이라는 클래스가 제공되며, 이를 사용하여 특정 페이지 영역을 편집하거나 기존의 RedactionAnnotations를 조작하고 편집(즉, 주석을 평탄화하고 그 아래의 텍스트를 제거)할 수 있습니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;


void RedactAnnotation::AddRedactionAnnotation() {

    String _dataDir("C:\\Samples\\");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // 특정 페이지 영역에 대한 RedactionAnnotation 인스턴스 생성
    auto annot = MakeObject<RedactionAnnotation>(page, MakeObject<Rectangle>(200, 500, 300, 600));
    annot->set_FillColor(Color::get_Green());
    annot->set_BorderColor(Color::get_Yellow());
    annot->set_Color(Color::get_Blue());

    // 편집 주석에 인쇄할 텍스트
    annot->set_OverlayText(u"REDACTED");
    annot->set_TextAlignment(HorizontalAlignment::Center);

    // 편집 주석에 오버레이 텍스트 반복
    annot->set_Repeat(true);

    // 첫 페이지의 주석 컬렉션에 주석 추가
    page->get_Annotations()->Add(annot);

    // 주석을 평탄화하고 페이지 내용을 편집(즉, 텍스트 및 이미지 제거
    // 편집된 주석 아래의 내용)
    annot->Redact();
    document->Save(_dataDir + u"RedactPage_out.pdf");
}
```

## 파사드 접근 방식

Aspose.PDF.Facades는 PDF 파일 내부의 기존 주석을 조작하는 기능을 제공하는 [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/) 클래스를 지원합니다.

이 클래스는 특정 페이지 영역을 제거할 수 있는 기능을 제공하는 [RedactArea(..)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a35ebd333b63b6df2c0c299c7331e3c63)라는 메서드를 포함하고 있습니다.

```cpp
void RedactAnnotation::AddRedactionAnnotationViaFacades() {

    String _dataDir("C:\\Samples\\");

    auto editor = MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();

    editor->BindPdf(_dataDir + u"sample.pdf");

    // 특정 페이지 영역을 수정
    editor->RedactArea(1, MakeObject<Rectangle>(100, 100, 20, 70), System::Drawing::Color::get_White());
    editor->BindPdf(_dataDir + u"sample.pdf");
    editor->Save(_dataDir + u"FacadesApproach_out.pdf");
}
```