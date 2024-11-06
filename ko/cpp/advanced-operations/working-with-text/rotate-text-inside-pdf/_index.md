---
title: PDF 내부 텍스트 회전 C++ 사용
linktitle: PDF 내부 텍스트 회전
type: docs
weight: 50
url: ko/cpp/rotate-text-inside-pdf/
description: 텍스트를 PDF로 회전하는 다양한 방법을 배웁니다. Aspose.PDF는 텍스트를 임의의 각도로 회전하거나 텍스트 단편 또는 전체 단락을 회전할 수 있습니다.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 회전 속성을 사용하여 PDF 내부 텍스트 회전

[TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) 클래스의 Rotation 속성을 사용하여 텍스트를 다양한 각도로 회전할 수 있습니다. 텍스트 회전은 문서 생성의 다양한 시나리오에서 사용될 수 있습니다. 필요에 따라 텍스트를 회전시키기 위해 회전 각도를 도 단위로 지정할 수 있습니다. 다음의 다양한 시나리오를 확인하여 텍스트 회전을 구현할 수 있습니다.

## TextFragment 및 TextBuilder를 사용한 회전 구현

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ImplementRotationUsingTextFragmentAndTextBuilder() {

    String _dataDir("C:\\Samples\\");

    // 문서 객체 초기화
    auto document = MakeObject<Document>();
    // 특정 페이지 가져오기
    auto page = document->get_Pages()->Add();
    // 텍스트 단편 생성
    auto textFragment1 = MakeObject<TextFragment>("main text");
    textFragment1->set_Position(MakeObject<Position>(100, 600));

    // 텍스트 속성 설정
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // 회전된 텍스트 단편 생성
    auto textFragment2 = MakeObject<TextFragment>("rotated text");
    textFragment2->set_Position(MakeObject<Position>(200, 600));
    // 텍스트 속성 설정
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment2->get_TextState()->set_Rotation(45);

    // 회전된 텍스트 단편 생성
    auto textFragment3 = MakeObject<TextFragment>("rotated text");
    textFragment3->set_Position(MakeObject<Position>(300, 600));

    // 텍스트 속성 설정
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment3->get_TextState()->set_Rotation(90);

    // TextBuilder 객체 생성
    auto textBuilder = MakeObject<TextBuilder>(page);
    // 텍스트 단편을 PDF 페이지에 추가
    textBuilder->AppendText(textFragment1);
    textBuilder->AppendText(textFragment2);
    textBuilder->AppendText(textFragment3);

    // 문서 저장
    document->Save(_dataDir + u"TextFragmentTests_Rotated1_out.pdf");
}
```

## TextParagraph 및 TextBuilder를 사용하여 회전 구현 (회전된 프래그먼트)

```cpp
void ImplementRotationUsingTextParagraphAndTextBuilder_RotatedFragments() {

    String _dataDir("C:\\Samples\\");

    // 문서 객체 초기화
    auto document = MakeObject<Document>();
    // 특정 페이지 가져오기
    auto page = document->get_Pages()->Add();
    auto paragraph = MakeObject<TextParagraph>();
    paragraph->set_Position(MakeObject<Position>(200, 600));

    // 텍스트 프래그먼트 생성
    auto textFragment1 = MakeObject<TextFragment>("rotated text");
    // 텍스트 속성 설정
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    // 회전 설정
    textFragment1->get_TextState()->set_Rotation(45);

    // 텍스트 프래그먼트 생성
    auto textFragment2 = MakeObject<TextFragment>("main text");
    // 텍스트 속성 설정
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // 텍스트 프래그먼트 생성
    auto textFragment3 = MakeObject<TextFragment>("another rotated text");
    // 텍스트 속성 설정
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    // 회전 설정
    textFragment3->get_TextState()->set_Rotation(-45);

    // 텍스트 프래그먼트를 단락에 추가
    paragraph->AppendLine(textFragment1);
    paragraph->AppendLine(textFragment2);
    paragraph->AppendLine(textFragment3);
    // TextBuilder 객체 생성
    auto textBuilder = MakeObject<TextBuilder>(page);
    // PDF 페이지에 텍스트 단락 추가
    textBuilder->AppendParagraph(paragraph);
    // 문서 저장
    document->Save(_dataDir + u"TextFragmentTests_Rotated2_out.pdf");

}
```

## TextFragment 및 Page.Paragraphs를 사용하여 회전 구현

```cpp
void ImplementRotationUsingTextFragmentAndPageParagraphs() {

    String _dataDir("C:\\Samples\\");

    // 문서 객체 초기화
    auto document = MakeObject<Document>();
    // 특정 페이지 가져오기
    auto page = document->get_Pages()->Add();
    // 텍스트 프래그먼트 생성
    auto textFragment1 = MakeObject<TextFragment>("main text");
    // 텍스트 속성 설정
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // 텍스트 프래그먼트 생성
    auto textFragment2 = MakeObject<TextFragment>("rotated text");

    // 텍스트 속성 설정
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // 회전 설정
    textFragment2->get_TextState()->set_Rotation(315);

    // 텍스트 프래그먼트 생성
    auto textFragment3 = MakeObject<TextFragment>("rotated text");
    // 텍스트 속성 설정
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // 회전 설정
    textFragment3->get_TextState()->set_Rotation(270);
    page->get_Paragraphs()->Add(textFragment1);
    page->get_Paragraphs()->Add(textFragment2);
    page->get_Paragraphs()->Add(textFragment3);

    // 문서 저장
    document->Save(_dataDir + u"TextFragmentTests_Rotated3_out.pdf");
}
```

## 텍스트 단락 및 텍스트 빌더를 사용한 회전 구현 (전체 단락 회전)

```cpp
void ImplementRotationUsingTextParagraphAndTextBuilder() {

    String _dataDir("C:\\Samples\\");

    // 문서 객체 초기화
    auto document = MakeObject<Document>();
    // 특정 페이지 가져오기
    auto page = document->get_Pages()->Add();
    for (int i = 0; i < 4; i++) {
        auto paragraph = MakeObject<TextParagraph>();
        paragraph->set_Position(MakeObject<Position>(200, 600));
        // 회전 지정
        paragraph->set_Rotation(i * 90 + 45);
        // 텍스트 조각 생성
        auto textFragment1 = MakeObject<TextFragment>("단락 텍스트");
        // 텍스트 조각 생성
        textFragment1->get_TextState()->set_FontSize(12);
        textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment1->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment1->get_TextState()->set_ForegroundColor(Color::get_Blue());

        // 텍스트 조각 생성
        auto textFragment2 = MakeObject<TextFragment>("텍스트의 두 번째 줄");
        // 텍스트 속성 설정
        textFragment2->get_TextState()->set_FontSize(12);
        textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment2->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment2->get_TextState()->set_ForegroundColor(Color::get_Blue());

        // 텍스트 조각 생성
        auto textFragment3 = MakeObject<TextFragment>("그리고 일부 추가 텍스트...");
        // 텍스트 속성 설정
        textFragment3->get_TextState()->set_FontSize(12);
        textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment3->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment3->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment3->get_TextState()->set_Underline(true);

        paragraph->AppendLine(textFragment1);
        paragraph->AppendLine(textFragment2);
        paragraph->AppendLine(textFragment3);
        // 텍스트 빌더 객체 생성
        auto textBuilder = MakeObject<TextBuilder>(page);
        // PDF 페이지에 텍스트 조각 추가
        textBuilder->AppendParagraph(paragraph);
    }
    // 문서 저장
    document->Save(_dataDir + u"TextFragmentTests_Rotated4_out.pdf");
}
```