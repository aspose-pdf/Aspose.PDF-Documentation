---
title: PDF 내 텍스트 서식 설정 C++ 사용
linktitle: PDF 내 텍스트 서식 설정
type: docs
weight: 30
url: ko/cpp/text-formatting-inside-pdf/
description: 이 페이지는 PDF 파일 내에서 텍스트를 서식화하는 방법을 설명합니다. 줄 들여쓰기 추가, 텍스트 테두리 추가, 밑줄 텍스트 추가, 추가된 텍스트 주위에 테두리 추가, 플로팅 박스 내용의 텍스트 정렬 등을 설명합니다.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF에 줄 들여쓰기 추가하는 방법

PDF에 줄 들여쓰기를 추가하기 위해 Aspose.PDF for C++는 [TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options/) 클래스의 [SubsequentLinesIndent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a89b064ab1f39d56040625d7d98194ad3) 속성을 사용하며 [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) 및 [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs) 컬렉션도 지원합니다.

다음 코드 스니펫을 사용하여 속성을 사용하세요:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddLineIndent() {

    String _dataDir("C:\\Samples\\");

    // 출력 파일 이름에 대한 문자열
    String outputFileName("SubsequentIndent_out.pdf");


    // 새로운 문서 객체 생성
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto text = MakeObject<TextFragment>("A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog.");

    // 텍스트 조각을 위한 TextFormattingOptions 초기화 및 SubsequentLinesIndent 값 지정

    text->get_TextState()->set_FormattingOptions(MakeObject<Aspose::Pdf::Text::TextFormattingOptions>());
    text->get_TextState()->get_FormattingOptions()->set_SubsequentLinesIndent(20);

    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line2");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line3");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line4");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line5");
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);

}
```

## 텍스트 테두리 추가 방법

다음 코드 스니펫은 [TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state)의 DrawTextRectangleBorder 속성을 설정하고 TextBuilder를 사용하여 텍스트에 테두리를 추가하는 방법을 보여줍니다.

```cpp
void AddTextBorder() {

    String _dataDir("C:\\Samples\\");

    // 출력 파일 이름에 대한 문자열
    String outputFileName("PDFWithTextBorder_out.pdf");

    // 새 문서 객체 생성
    auto document = MakeObject<Document>();
    // 특정 페이지 가져오기
    auto page = document->get_Pages()->Add();

    // 텍스트 조각 생성
    auto textFragment = MakeObject<TextFragment>("main text");
    textFragment->set_Position(MakeObject<Position>(100, 600));

    // 텍스트 속성 설정
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
    // 텍스트 주위에 테두리(스트로킹)를 그리기 위한 StrokingColor 속성 설정
    // 사각형
    textFragment->get_TextState()->set_StrokingColor(Color::get_DarkRed());
    // DrawTextRectangleBorder 속성 값을 true로 설정
    textFragment->get_TextState()->set_DrawTextRectangleBorder(true);
    auto tb = MakeObject<TextBuilder>(page);
    tb->AppendText(textFragment);
    // 문서 저장
    document->Save(_dataDir + outputFileName);
}
```

## 밑줄 텍스트 추가 방법

다음 코드 스니펫은 새 PDF 파일을 만들 때 밑줄 텍스트를 추가하는 방법을 보여줍니다.

```cpp
void AddUnderlineText() {
    String _dataDir("C:\\Samples\\");

    // 출력 파일 이름을 위한 문자열
    String outputFileName("AddUnderlineText_out.pdf");

    // 새 문서 객체 생성
    auto document = MakeObject<Document>();
    // 특정 페이지 가져오기
    auto page = document->get_Pages()->Add();

    // 샘플 텍스트가 포함된 TextFragment
    auto fragment = MakeObject<TextFragment>("Text with underline decoration");
    // TextFragment의 폰트 설정
    fragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    fragment->get_TextState()->set_FontSize(10);

    // 텍스트 서식을 밑줄로 설정
    fragment->get_TextState()->set_Underline(true);

    // TextFragment가 배치되어야 할 위치 지정
    fragment->set_Position(MakeObject<Position>(10, 800));

    auto tb = MakeObject<TextBuilder>(page);
    // TextFragment를 PDF 파일에 추가
    tb->AppendText(fragment);

    // 결과 PDF 문서 저장.
    document->Save(_dataDir + outputFileName);
}
```

## 추가된 텍스트 주위에 테두리 추가하는 방법

추가한 텍스트의 모양과 느낌을 제어할 수 있습니다. 아래 예제는 추가한 텍스트 주위에 사각형을 그려서 테두리를 추가하는 방법을 보여줍니다. [PdfContentEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor/) 클래스에 대해 더 알아보세요.

```cpp
void AddBorderAroundAddedText() {

    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름을 위한 문자열
    String inputFileName("sample.pdf");

    // 출력 파일 이름을 위한 문자열
    String outputFileName("AddingBorderAroundAddedText_out.pdf");

    auto editor = MakeObject<Aspose::Pdf::Facades::PdfContentEditor>();

    editor->BindPdf(_dataDir + inputFileName);
    auto lineInfo = MakeObject<Aspose::Pdf::Facades::LineInfo>();

    lineInfo->set_LineWidth(2);
    lineInfo->set_VerticeCoordinate(MakeArray<float>({ 0, 0, 100, 100, 50, 100 }));
    lineInfo->set_Visibility(true);
    auto rect = MakeObject<System::Drawing::Rectangle>(0, 0, 0, 0);
    editor->CreatePolygon(lineInfo, 1, System::Drawing::Rectangle(0, 0, 0, 0), String::Empty);

    // 결과 PDF 문서를 저장합니다.
    editor->Save(_dataDir + outputFileName);
}
```

## NewLine 피드를 추가하는 방법

줄 바꿈이 포함된 텍스트를 추가하려면 [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment)와 [TextParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_paragraph)를 사용하세요.

다음 코드 조각은 PDF 파일에 NewLine 피드를 추가하는 방법을 보여줍니다:

```cpp
void AddNewLineFeed() {
    String _dataDir("C:\\Samples\\");

    // 출력 파일 이름에 대한 문자열
    String outputFileName("AddNewLineFeed_out.pdf");

    // 새 문서 객체 생성
    auto document = MakeObject<Document>();
    // 특정 페이지 가져오기
    auto page = document->get_Pages()->Add();

    // 필요한 줄 바꿈 마커가 포함된 텍스트로 새 TextFragment 초기화
    auto textFragment = MakeObject<TextFragment>("Applicant Name: \r\n Joe Smoe");

    // 필요한 경우 텍스트 조각 속성 설정
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());

    // TextParagraph 객체 생성
    auto par = MakeObject<TextParagraph>();

    // 새 TextFragment를 단락에 추가
    par->AppendLine(textFragment);

    // 단락 위치 설정
    par->set_Position(MakeObject<Position>(100, 600));

    // TextBuilder 객체 생성
    auto textBuilder = new TextBuilder(page);
    // TextBuilder를 사용하여 TextParagraph 추가
    textBuilder->AppendParagraph(par);

    // 결과 PDF 문서 저장.
    document->Save(_dataDir + outputFileName);
}
```

## 취소선 텍스트 추가하는 방법

[TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state) 클래스를 사용하여 굵게, 기울임꼴, 밑줄과 같은 텍스트 서식을 설정할 수 있으며, API는 텍스트 서식을 취소선으로 표시하는 기능도 제공합니다.

취소선 서식이 있는 TextFragment를 추가하려면 다음 코드 스니펫을 사용해 보세요.

```cpp
void AddStrikeOutText() {
    String _dataDir("C:\\Samples\\");

    // 출력 파일 이름용 문자열
    String outputFileName("AddStrikeOutText_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>();
    // 특정 페이지 가져오기
    auto page = document->get_Pages()->Add();

    // 텍스트 조각 생성
    auto textFragment = MakeObject<TextFragment>("main text");
    textFragment->set_Position(MakeObject<Position>(100, 600));

    // 텍스트 속성 설정
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
    // 취소선 속성 설정
    textFragment->get_TextState()->set_StrikeOut(true);
    // 텍스트를 굵게 표시
    textFragment->get_TextState()->set_FontStyle(FontStyles::Bold);

    // TextBuilder 객체 생성
    auto textBuilder = MakeObject<TextBuilder>(page);
    // PDF 페이지에 텍스트 조각 추가
    textBuilder->AppendText(textFragment);

    // 결과 PDF 문서 저장.
    document->Save(_dataDir + outputFileName);
}
```

## 텍스트에 그라데이션 음영 적용

[Aspose.Pdf.Color](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.color) 클래스는 텍스트에 음영 색상을 지정할 수 있는 [PatternColorSpace](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.color#a8be6d8ab626d2ba6935a13a9c5b0de54)라는 새로운 속성을 도입하여 더욱 강화되었습니다. 이 새로운 속성은 텍스트에 다양한 그라데이션 음영을 추가합니다. 예를 들어, 다음 코드 조각에 표시된 것처럼 축 음영, 반경(타입 3) 음영 등이 있습니다:

```cpp
void ApplyGradientShading() {

    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름에 대한 문자열
    String inputFileName("sample.pdf");

    // 출력 파일 이름에 대한 문자열
    String outputFileName("ApplyGradientShading_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto absorber = MakeObject<TextFragmentAbsorber>("항상 올바르게 인쇄");

    document->get_Pages()->Accept(absorber);

    auto textFragment = absorber->get_TextFragments()->idx_get(1);

    auto foregroundColor = MakeObject<Aspose::Pdf::Color>();
    foregroundColor->set_PatternColorSpace(MakeObject<Aspose::Pdf::Drawing::GradientAxialShading>(Color::get_Red(), Color::get_Blue()));

    // 패턴 색상 공간으로 새 색상 생성
    textFragment->get_TextState()->set_ForegroundColor(foregroundColor);

    textFragment->get_TextState()->set_Underline(true);

    document->Save(_dataDir + outputFileName);

}
```

> 방사형 그라디언트를 적용하려면 위의 코드 조각에서 'PatternColorSpace' 속성을 'Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)'로 설정할 수 있습니다.

## 플로트 콘텐츠에 텍스트 정렬하는 방법

Aspose.PDF는 부동 상자 요소 내부의 콘텐츠에 대한 텍스트 정렬 설정을 지원합니다. [Aspose.Pdf.FloatingBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.floating_box) 인스턴스의 정렬 속성을 사용하여 다음 코드 샘플에서 보여주는 것처럼 이를 달성할 수 있습니다.

```cpp
void ApplyGradientShadingRadial() {

    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("sample.pdf");

    // String for output file name
    String outputFileName("ApplyGradientShadingRadial_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto absorber = MakeObject<TextFragmentAbsorber>(u"always print correctly");
    document->get_Pages()->Accept(absorber);

    auto textFragment = absorber->get_TextFragments()->idx_get(1);

    auto foregroundColor = MakeObject<Aspose::Pdf::Color>();
    foregroundColor->set_PatternColorSpace(MakeObject<Aspose::Pdf::Drawing::GradientRadialShading>(Color::get_Red(), Color::get_Blue()));

    // Create new color with pattern colorspace
    textFragment->get_TextState()->set_ForegroundColor(foregroundColor);

    textFragment->get_TextState()->set_Underline(true);

    document->Save(_dataDir + outputFileName);
}
```