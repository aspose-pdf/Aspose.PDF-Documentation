---
title: PDF 하이라이트 주석을 C++로 사용하기
linktitle: 하이라이트 주석
type: docs
weight: 20
url: /cpp/highlights-annotation/
description: 마크업 주석은 문서의 텍스트에서 하이라이트, 밑줄, 취소선 또는 물결 밑줄로 표시됩니다.
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

텍스트 마크업 주석은 문서의 텍스트에서 하이라이트, 밑줄, 취소선 또는 물결 밑줄로 표시되어야 합니다. 열렸을 때 해당 노트의 텍스트를 포함한 팝업 창을 표시해야 합니다.

PDF 뷰어 컨트롤에서 제공하는 속성 창을 사용하여 PDF의 텍스트 마크업 주석의 속성을 편집할 수 있습니다. 텍스트 마크업 주석의 색상, 투명도, 작성자 및 테마를 변경할 수 있습니다.

highlightSettings 속성을 사용하여 하이라이트 주석 설정을 가져오거나 설정할 수 있습니다. The highlightSettings 속성은 하이라이트 주석의 색상, 불투명도, 작성자, 테마, 수정 날짜 및 잠금 여부 속성을 설정하는 데 사용됩니다.

strikethroughSettings 속성을 사용하여 취소선 주석 설정을 가져오거나 설정할 수도 있습니다. strikethroughSettings 속성은 취소선 주석의 색상, 불투명도, 작성자, 테마, 수정 날짜 및 잠금 여부 속성을 설정하는 데 사용됩니다.

다음 기능은 underlineSettings 속성을 사용하여 밑줄 주석의 설정을 가져오거나 설정할 수 있는 기능입니다. underlineSettings 속성은 밑줄 주석의 색상, 불투명도, 작성자, 테마, 수정 날짜 및 잠금 여부 속성을 설정하는 데 사용됩니다.

## 텍스트 마크업 주석 추가

PDF 문서에 텍스트 마크업 주석을 추가하려면 다음 작업을 수행해야 합니다:

1. PDF 파일 로드 - 새로운 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체.
1. 주석 생성:

    - [HighlightAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.highlight_annotation) 및 매개변수 설정 (제목, 색상).- [StrikeOutAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.strike_out_annotation) 및 매개변수 설정 (제목, 색상).
- [SquigglyAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.squiggly_annotation) 및 매개변수 설정 (제목, 색상).
- [UnderlineAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.underline_annotation) 및 매개변수 설정 (제목, 색상).
1. 그런 다음 모든 주석을 페이지에 추가해야 합니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void TextMarkupAnnotations::AddTextMarkupAnnotation()
{
    String _dataDir("C:\\Samples\\");

    try
    {
        // PDF 파일 로드
        auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
        auto tfa = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>(u"PDF");
        tfa->Visit(document->get_Pages()->idx_get(1));

        // 주석 생성
        auto highlightAnnotation = MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>(
        document->get_Pages()->idx_get(1),
        tfa->get_TextFragments()->idx_get(1)->get_Rectangle());
        highlightAnnotation->set_Title(u"Aspose User");
        highlightAnnotation->set_Color(Color::get_LightGreen());

        auto strikeOutAnnotation = MakeObject<Aspose::Pdf::Annotations::StrikeOutAnnotation>(
        document->get_Pages()->idx_get(1),
        tfa->get_TextFragments()->idx_get(2)->get_Rectangle());
        strikeOutAnnotation->set_Title(u"Aspose User");
        strikeOutAnnotation->set_Color(Color::get_Blue());

        auto squigglyAnnotation = MakeObject<Aspose::Pdf::Annotations::SquigglyAnnotation>(
        document->get_Pages()->idx_get(1),
        tfa->get_TextFragments()->idx_get(3)->get_Rectangle());
        squigglyAnnotation->set_Title(u"Aspose User");
        squigglyAnnotation->set_Color(Color::get_Blue());

        auto underlineAnnotation = MakeObject<Aspose::Pdf::Annotations::UnderlineAnnotation>(
        document->get_Pages()->idx_get(1),
        tfa->get_TextFragments()->idx_get(4)->get_Rectangle());
        underlineAnnotation->set_Title(u"Aspose User");
        underlineAnnotation->set_Color(Color::get_Blue());

        // 페이지에 주석 추가
        document->get_Pages()->idx_get(1)->get_Annotations()->Add(highlightAnnotation);
        document->get_Pages()->idx_get(1)->get_Annotations()->Add(squigglyAnnotation);
        document->get_Pages()->idx_get(1)->get_Annotations()->Add(strikeOutAnnotation);
        document->get_Pages()->idx_get(1)->get_Annotations()->Add(underlineAnnotation);
        document->Save(_dataDir + u"sample_mod.pdf");
    }
    catch (Exception ex)
    {
        Console::WriteLine(ex->get_Message());
    }
}
```

만약 여러 줄로 된 조각을 강조하고 싶다면 고급 예제를 사용해야 합니다:

```cpp
/// <summary>
/// 여러 줄로 된 조각을 강조하고 싶다면 고급 예제를 사용해야 합니다
/// </summary>

System::SmartPtr<Aspose::Pdf::Annotations::HighlightAnnotation> HighLightTextFragment(
    System::SmartPtr<Aspose::Pdf::Page> page,
    System::SmartPtr<TextFragment> textFragment,
    System::SharedPtr<Color> color);

void TextMarkupAnnotations::AddHighlightAnnotationAdvanced()
{
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>(
        u"Adobe\\W+Acrobat\\W+Reader",
        MakeObject<Aspose::Pdf::Text::TextSearchOptions>(true));

    tfa->Visit(page);

    for (auto textFragment : tfa->get_TextFragments())
    {
        auto highlightAnnotation = HighLightTextFragment(page, textFragment, Color::get_Yellow());
        page->get_Annotations()->Add(highlightAnnotation);
    }
    document->Save(_dataDir + u"sample_mod.pdf");
}


System::SmartPtr<Aspose::Pdf::Annotations::HighlightAnnotation> HighLightTextFragment(
    System::SmartPtr<Aspose::Pdf::Page> page,
    System::SmartPtr<TextFragment> textFragment,
    System::SharedPtr<Color> color)
{
    if (textFragment->get_Segments()->get_Count() == 1)
    {
        auto ha = MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>
        (page, textFragment->get_Segments()->idx_get(1)->get_Rectangle());
        ha->set_Title(u"Aspose User");
        ha->set_Color(color);

        ha->set_Modified(DateTime::get_Now());

        auto quadPoints = MakeArray<System::SharedPtr<Point>>(4);

        quadPoints[0] = MakeObject<Point>(textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_LLX(),
        textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_URY());
        quadPoints[1] = MakeObject<Point>(textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_URX(),
        textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_URY());
        quadPoints[2] = MakeObject<Point>(textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_LLX(),
        textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_LLY());
        quadPoints[3] = MakeObject<Point>(textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_URX(),
        textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_LLY());
        ha->set_QuadPoints(quadPoints);
        return ha;
    }

    auto offset = 0;
    auto quadPoints = MakeArray<System::SharedPtr<Point>>(textFragment->get_Segments()->get_Count() * 4);

    for (auto segment : textFragment->get_Segments())
    {
        quadPoints[offset + 0] = MakeObject<Point>(segment->get_Rectangle()->get_LLX(), segment->get_Rectangle()->get_URY());
        quadPoints[offset + 1] = MakeObject<Point>(segment->get_Rectangle()->get_URX(), segment->get_Rectangle()->get_URY());
        quadPoints[offset + 2] = MakeObject<Point>(segment->get_Rectangle()->get_LLX(), segment->get_Rectangle()->get_LLY());
        quadPoints[offset + 3] = MakeObject<Point>(segment->get_Rectangle()->get_URX(), segment->get_Rectangle()->get_LLY());
        offset += 4;
    }

    double llx = quadPoints[0]->get_X();
    double lly = quadPoints[0]->get_Y();
    double urx = quadPoints[0]->get_X();
    double ury = quadPoints[0]->get_Y();
    for (auto &pt : quadPoints) {
        if (llx > pt->get_X())
        llx = pt->get_X();
        if (lly > pt->get_Y())
        lly = pt->get_Y();
        if (urx < pt->get_X())
        urx = pt->get_X();
        if (ury < pt->get_Y())
        ury = pt->get_Y();
    }

    auto ha = MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>
        (page, textFragment->get_Segments()->idx_get(1)->get_Rectangle());
    ha->set_Title(u"Aspose User");
    ha->set_Color(color);

    ha->set_Modified(DateTime::get_Now());

    ha->set_QuadPoints(quadPoints);
    return ha;
}


/// <summary>
/// 강조된 텍스트를 얻는 방법
/// </summary>
void TextMarkupAnnotations::GetHighlightedText()
{
    String _dataDir("C:\\Samples\\");

    // PDF 파일을 로드합니다
    auto document = MakeObject<Document>(_dataDir + u"sample_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>(page, Rectangle::get_Trivial()));

    for (auto ta : annotationSelector->get_Selected())
    {
        auto ha = System::DynamicCast<Aspose::Pdf::Annotations::HighlightAnnotation>(ta);
        Console::WriteLine(ha->GetMarkedText());
    }
}
```

## 텍스트 마크업 주석 가져오기

다음 코드 스니펫을 사용하여 PDF 문서에서 텍스트 마크업 주석을 가져오십시오.

```cpp
void TextMarkupAnnotations::GetTextMarkupAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // PDF 파일 불러오기
    auto document = MakeObject<Document>(_dataDir + u"sample_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>(page, Rectangle::get_Trivial()));

    for (auto ta : annotationSelector->get_Selected())
    {
        Console::WriteLine(u"{0} {1}", ta->get_AnnotationType(), ta->get_Rect());
    }
}
```

## 텍스트 마크업 주석 삭제

다음 코드 스니펫은 PDF 파일에서 텍스트 마크업 주석을 삭제하는 방법을 보여줍니다.

```cpp
void TextMarkupAnnotations::DeleteTextMarkupAnnotation() {

    String _dataDir("C:\\Samples\\");

    // PDF 파일 불러오기
    auto document = MakeObject<Document>(_dataDir + u"sample_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector1 = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector1);
    auto annotationSelector2 = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::SquigglyAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector2);

    for (auto ta : annotationSelector1->get_Selected()) {
        page->get_Annotations()->Delete(ta);
    }
    for (auto ta : annotationSelector2->get_Selected()) {
        page->get_Annotations()->Delete(ta);
    }
    document->Save(_dataDir + u"sample_del.pdf");
}
```