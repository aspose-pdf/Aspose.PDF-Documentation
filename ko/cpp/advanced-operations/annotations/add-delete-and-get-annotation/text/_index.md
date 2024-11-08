---
title: PDF 텍스트 주석
Texttitle: 텍스트 주석
type: docs
weight: 10
url: /ko/cpp/text-annotation/
description: Aspose.PDF for C++는 PDF 문서에 텍스트 주석을 추가, 가져오기 및 삭제할 수 있습니다.
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 기존 PDF 파일에 텍스트 주석 추가하는 방법

텍스트 주석은 PDF 문서의 특정 위치에 첨부된 주석입니다. 닫힌 경우 주석은 아이콘으로 표시되며, 열리면 독자가 선택한 글꼴 및 크기로 메모 텍스트를 포함하는 팝업 창을 표시해야 합니다.

주석은 특정 페이지의 [Annotations](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation) 컬렉션에 포함되어 있습니다. 이 컬렉션은 해당 개별 페이지에 대한 주석만 포함하며; 각 페이지는 자체적인 Annotations 컬렉션을 가지고 있습니다.

특정 페이지에 주석을 추가하려면 [Add](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_collection#a1f7bf6c38fe2f97904a3575f5241d6c9) 메서드를 사용하여 해당 페이지의 Annotations 컬렉션에 추가하십시오.

1. 먼저, PDF에 추가하려는 주석을 만드십시오.
1. 그런 다음 입력 PDF를 엽니다.
1. [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 객체의 Annotations 컬렉션에 주석을 추가하십시오.

다음 코드 스니펫은 PDF 페이지에 주석을 추가하는 방법을 보여줍니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddTextAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // PDF 파일을 로드합니다
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    auto page = document->get_Pages()->idx_get(1);
    auto rect = MakeObject<Rectangle>(200, 750, 400, 790);
    auto textAnnotation = MakeObject<Aspose::Pdf::Annotations::TextAnnotation>(page, rect);

    textAnnotation->set_Title(u"Aspose User");
    textAnnotation->set_Subject(u"Sample Subject");
    textAnnotation->set_State(Aspose::Pdf::Annotations::AnnotationState::Accepted);
    textAnnotation->set_Contents(u"Sample contents for the annotation");
    textAnnotation->set_Open(true);
    textAnnotation->set_Icon(Aspose::Pdf::Annotations::TextIcon::Circle);

    auto border = MakeObject<Aspose::Pdf::Annotations::Border>(textAnnotation);
    border->set_Width(5);
    border->set_Dash(MakeObject<Aspose::Pdf::Annotations::Dash>(1, 1));
    textAnnotation->set_Border(border);
    textAnnotation->set_Rect(rect);

    page->get_Annotations()->Add(textAnnotation);
    document->Save(_dataDir + u"sample_textannot.pdf");
}
```

## Get Text Annotation

PDF 문서에서 텍스트 주석을 가져오기 위해 다음 코드 스니펫을 사용해 보세요:

```cpp
void GetTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"sample_textannot.pdf");

    // AnnotationSelector를 사용하여 주석 필터링
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LineAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);
    auto textAnnotations = annotationSelector->get_Selected();

    // 결과 출력
    for (auto fa : textAnnotations) {
        Console::WriteLine(fa->get_Rect());
    }
}
```

## PDF 파일에서 텍스트 주석 삭제

다음 코드 스니펫은 PDF 파일에서 텍스트 주석을 삭제하는 방법을 보여줍니다.

```cpp
void DeleteTextAnnotation() {

    String _dataDir("C:\\Samples\\");
    // PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"sample_textannot.pdf");

    // AnnotationSelector를 사용하여 주석 필터링
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LineAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);
    auto textAnnotations = annotationSelector->get_Selected();

    // 주석 삭제
    for (auto fa : textAnnotations) {
        page->get_Annotations()->Delete(fa);
    }
    document->Save(_dataDir + u"sample_textannot_del.pdf");
}
```

## 새로운 자유 텍스트 주석 추가(또는 생성)하는 방법

자유 텍스트 주석은 페이지에 텍스트를 직접 표시합니다. 다음 스니펫에서는 문자열의 첫 번째 발생 위에 자유 텍스트 주석을 추가합니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void FreeTextAnnotations::AddFreeTextAnnotationDemo()
{
    String _dataDir("C:\\Samples\\");

    // PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto defaultAppearance = MakeObject<DefaultAppearance>();
    defaultAppearance->set_FontName(u"Helvetica");
    defaultAppearance->set_FontSize(12);
    defaultAppearance->set_TextColor(System::Drawing::Color::get_Blue());

    auto freeTextAnnotation = MakeObject<FreeTextAnnotation>(page, new Rectangle(300.0, 770.0, 400.0, 790.0), defaultAppearance);

    freeTextAnnotation->set_RichText(u"Free Text Demo");
    page->get_Annotations()->Add(freeTextAnnotation);
    document->Save(_dataDir + u"sample_freetext.pdf");
}
```

## Get FreeText Annotation

PDF 문서에서 텍스트 주석을 가져오기 위해 다음 코드 스니펫을 사용해 보세요:

```cpp
void FreeTextAnnotations::GetFreeTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"sample_freetext.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // AnnotationSelector를 사용하여 주석 필터링
    auto annotationSelector = MakeObject<AnnotationSelector>(
        new FreeTextAnnotation(page, Rectangle::get_Trivial(), new DefaultAppearance()));
    page->Accept(annotationSelector);
    auto freeTextAnnotations = annotationSelector->get_Selected();

    // 결과 출력
    for (auto fa : freeTextAnnotations) {
        Console::WriteLine(fa->get_Rect());
    }
}
```

### Make Free Text Annotation Invisible

때때로 문서에서 볼 때는 보이지 않지만 문서를 인쇄할 때는 보여야 하는 워터마크를 만들어야 할 필요가 있습니다. 주석 플래그를 이 목적으로 사용하십시오. 다음 코드 스니펫은 방법을 보여줍니다.

```cpp
void FreeTextAnnotations::MakeFreeTextAnnotationInvisble() {

    String _dataDir("C:\\Samples\\");

    // 문서 열기
    auto doc = MakeObject<Document>(_dataDir + u"input.pdf");

    auto annotation = new FreeTextAnnotation(doc->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(50, 600, 250, 650),
        MakeObject<DefaultAppearance>(u"Helvetica", 16,
            System::Drawing::Color::get_Red()));
    annotation->set_Contents(u"ABCDEFG");
    annotation->get_Characteristics()->set_Border(System::Drawing::Color::get_Red());
    annotation->set_Flags (AnnotationFlags::Print | AnnotationFlags::NoView);
    doc->get_Pages()->idx_get(1)->get_Annotations()->Add(annotation);

    // 출력 파일 저장
    doc->Save(_dataDir + u"InvisibleAnnotation_out.pdf");
}
```

## FreeText 주석 삭제

다음 코드 스니펫은 PDF 파일에서 FreeText 주석을 삭제하는 방법을 보여줍니다.

```cpp
void FreeTextAnnotations::DeleteFreeTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"sample_freetext.pdf");

    // AnnotationSelector를 사용하여 주석 필터링
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        new FreeTextAnnotation(page, Rectangle::get_Trivial(), new DefaultAppearance()));
    page->Accept(annotationSelector);
    auto freeTextAnnotations = annotationSelector->get_Selected();

    // 주석 삭제
    for (auto fa : freeTextAnnotations) {
        page->get_Annotations()->Delete(fa);
    }
    document->Save(_dataDir + u"sample_freetext_del.pdf");
}
```