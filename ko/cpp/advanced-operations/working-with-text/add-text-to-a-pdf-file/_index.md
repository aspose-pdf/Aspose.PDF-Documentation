---
title: C++를 사용하여 PDF에 텍스트 추가
linktitle: PDF에 텍스트 추가
type: docs
weight: 10
url: /ko/cpp/add-text-to-pdf-file/
description: 이 문서는 Aspose.PDF에서 텍스트 작업의 다양한 측면을 설명합니다. PDF에 텍스트를 추가하고, HTML 조각을 추가하거나, 사용자 정의 OTF 글꼴을 사용하는 방법을 배웁니다.
lastmod: "2021-12-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 텍스트 추가

기존 PDF 파일에 텍스트를 추가하려면:

1. Document 객체를 사용하여 입력 PDF를 엽니다.
2. 텍스트를 추가하려는 특정 페이지를 가져옵니다.
3. 입력 텍스트와 기타 텍스트 속성을 포함하여 TextFragment 객체를 생성합니다. 특정 페이지에서 생성된 TextBuilder 객체를 사용하면 AppendText 메서드를 사용하여 페이지에 TextFragment 객체를 추가할 수 있습니다.
4. Document 객체의 Save 메서드를 호출하고 출력 PDF 파일을 저장합니다.

다음 코드 스니펫은 기존 PDF 파일에 텍스트를 추가하는 방법을 보여줍니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddingText() {
    
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("sample.pdf");
    // String for output file name
    String outputFileName("AddingText_out.pdf");

    // Load the PDF file
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // get particular page
    auto pdfPage = document->get_Pages()->idx_get(1);

    // create text fragment
    auto textFragment = MakeObject<TextFragment>("Aspose.PDF");
    textFragment->set_Position(MakeObject<Position>(80, 700));

    // set text properties
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
    textFragment->get_TextState()->set_FontSize(14);
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());

    // create TextBuilder object
    auto textBuilder = MakeObject<TextBuilder>(pdfPage);
    // append the text fragment to the PDF page
    textBuilder->AppendText(textFragment);

    // Save resulting PDF document.
    document->Save(_dataDir + outputFileName);
}
```

## 스트림에서 폰트 로드하기

다음 코드 스니펫은 PDF 문서에 텍스트를 추가할 때 스트림 객체에서 폰트를 로드하는 방법을 보여줍니다.

```cpp
void LoadingFontFromStream() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("sample.pdf");
    String outputFileName("LoadingFontFromStream_out.pdf");

    String fontFile("C:\\Windows\\Fonts\\Arial.ttf");

    // 입력 PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 문서의 첫 번째 페이지에 대한 텍스트 빌더 객체 생성
    auto textBuilder = MakeObject<TextBuilder>(document->get_Pages()->idx_get(1));
    // 샘플 문자열로 텍스트 조각 생성
    auto textFragment = MakeObject<TextFragment>("Hello world");

    if (!fontFile.IsNullOrEmpty()) {
        // TrueType 폰트를 스트림 객체로 로드
        auto fontStream = System::IO::File::OpenRead(fontFile);
        // 텍스트 문자열에 폰트 이름 설정
        textFragment->get_TextState()->set_Font(FontRepository::OpenFont(fontStream, FontTypes::TTF));
        // 텍스트 조각의 위치 지정
        textFragment->set_Position(MakeObject<Position>(10, 10));
        // PDF 파일 위에 배치될 수 있도록 텍스트를 TextBuilder에 추가
        textBuilder->AppendText(textFragment);

        // 결과 PDF 문서 저장
        document->Save(_dataDir + outputFileName);
    }
}
```

## TextParagraph를 사용하여 텍스트 추가하기

다음 코드 스니펫은 [TextParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_paragraph) 클래스를 사용하여 PDF 문서에 텍스트를 추가하는 방법을 보여줍니다.

```cpp
void AddTextUsingTextParagraph() {

    String _dataDir("C:\\Samples\\");

    // 문서 열기
    auto document = MakeObject<Document>();

    String outputFileName("AddTextUsingTextParagraph_out.pdf");

    // 문서 객체의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();
    auto builder = MakeObject<TextBuilder>(page);

    // 텍스트 단락 생성
    auto paragraph = MakeObject<TextParagraph>();

    // 후속 줄 들여쓰기 설정
    paragraph->set_SubsequentLinesIndent(20);

    // TextParagraph를 추가할 위치 지정
    paragraph->set_Rectangle(MakeObject<Rectangle>(100, 300, 200, 700));

    // 단어 줄바꿈 모드 지정
    paragraph->get_FormattingOptions()->set_WrapMode(TextFormattingOptions::WordWrapMode::ByWords);

    // 텍스트 조각 생성
    auto fragment1 = MakeObject<TextFragment>("the quick brown fox jumps over the lazy dog");
    fragment1->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    fragment1->get_TextState()->set_FontSize(12);
    // 단락에 조각 추가
    paragraph->AppendLine(fragment1);
    // 단락 추가
    builder->AppendParagraph(paragraph);

    // 결과 PDF 문서를 저장합니다.
    document->Save(_dataDir + outputFileName);
}

```

## TextSegment에 하이퍼링크 추가

PDF 페이지는 하나 이상의 TextFragment 객체로 구성될 수 있으며, 각 TextFragment 객체는 하나 이상의 TextSegment 인스턴스를 가질 수 있습니다. TextSegment에 하이퍼링크를 설정하기 위해, [TextSegment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_segment) 클래스의 Hyperlink 속성을 Aspose.Pdf.WebHyperlink 인스턴스의 객체를 제공하여 사용할 수 있습니다. 이 요구 사항을 달성하기 위해 다음 코드 조각을 사용해 보십시오.

```cpp
void AddHyperlinkToTextSegment() {
    
    String _dataDir("C:\\Samples\\");
    String outputFileName("AddHyperlinkToTextSegment_out.pdf");

    // 문서 인스턴스 생성
    auto document = MakeObject<Document>();

    // PDF 파일의 페이지 컬렉션에 페이지 추가
    auto page1 = document->get_Pages()->Add();

    // TextFragment 인스턴스 생성
    auto tf = MakeObject<TextFragment>("Sample Text Fragment");
    // TextFragment의 수평 정렬 설정
    tf->set_HorizontalAlignment(HorizontalAlignment::Right);

    // 샘플 텍스트로 textsegment 생성
    auto segment = MakeObject<TextSegment>(" ... Text Segment 1...");
    // TextFragment의 세그먼트 컬렉션에 세그먼트 추가
    tf->get_Segments()->Add(segment);

    // 새로운 TextSegment 생성
    segment = MakeObject<TextSegment>("Link to Google");
    // TextFragment의 세그먼트 컬렉션에 세그먼트 추가

    tf->get_Segments()->Add(segment);

    // TextSegment에 하이퍼링크 설정
    segment->set_Hyperlink(MakeObject<Aspose::Pdf::WebHyperlink>("www.aspose.com"));

    // 텍스트 세그먼트의 전경색 설정
    segment->get_TextState()->set_ForegroundColor(Color::get_Blue());

    // 텍스트 서식을 이탤릭체로 설정
    segment->get_TextState()->set_FontStyle(FontStyles::Italic);

    // 또 다른 TextSegment 객체 생성
    segment = MakeObject<TextSegment>(u"TextSegment without hyperlink");

    // TextFragment의 세그먼트 컬렉션에 세그먼트 추가
    tf->get_Segments()->Add(segment);

    // 페이지 객체의 단락 컬렉션에 TextFragment 추가
    page1->get_Paragraphs()->Add(tf);

    // 결과 PDF 문서 저장.
    document->Save(_dataDir + outputFileName);

}
```

## OTF 폰트 사용

Aspose.PDF for C++는 PDF 파일 내용을 생성/조작할 때 기본 시스템 폰트 이외의 콘텐츠를 사용하여 파일 내용을 표시할 수 있도록 사용자 지정/TrueType 폰트를 사용할 수 있는 기능을 제공합니다.

```cpp
void UseOTFFont() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("OTFFont_out.pdf");

    // 새 문서 인스턴스 생성
    auto document = MakeObject<Document>();

    // PDF 파일의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();

    // 샘플 텍스트로 TextFragment 인스턴스 생성
    auto fragment = MakeObject<TextFragment>("OTF 폰트의 샘플 텍스트");

    // 또는 시스템 디렉토리에서 OTF 폰트의 경로를 지정할 수도 있습니다.
    fragment->get_TextState()->set_Font(FontRepository::OpenFont(u"C:\\Samples\\Fonts\\Montserrat-Black.otf"));
    // PDF 파일 안에 폰트를 포함시켜서 지정된 폰트가 대상 컴퓨터에 설치/존재하지 않더라도
    // 제대로 표시되도록 설정합니다.
    fragment->get_TextState()->get_Font()->set_IsEmbedded(true);
    // Page 인스턴스의 단락 컬렉션에 TextFragment 추가
    page->get_Paragraphs()->Add(fragment);
    // 결과 PDF 문서를 저장합니다.
    document->Save(_dataDir + outputFileName);
}
```

## DOM을 사용하여 HTML 문자열 추가하기

Aspose.Pdf.Generator.Text 클래스는 IsHtmlTagSupported라는 속성을 포함하고 있어 HTML 태그/콘텐츠를 PDF 파일에 추가할 수 있습니다. 추가된 콘텐츠는 단순한 텍스트 문자열로 나타나는 대신 기본 HTML 태그로 렌더링됩니다. Aspose.Pdf 네임스페이스의 새로운 문서 객체 모델(DOM)에서도 유사한 기능을 지원하기 위해 HtmlFragment 클래스가 도입되었습니다.

[HtmlFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_fragment) 인스턴스를 사용하여 PDF 파일 내에 배치될 HTML 콘텐츠를 지정할 수 있습니다. TextFragment와 유사하게, HtmlFragment는 단락 수준 객체이며 Page 객체의 단락 컬렉션에 추가할 수 있습니다. 다음 코드 스니펫은 DOM 접근 방식을 사용하여 PDF 파일 내에 HTML 콘텐츠를 배치하는 단계를 보여줍니다.

```cpp
void AddingHtmlString() {
    
    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름에 대한 문자열
    String inputFileName("sample.pdf");

    // 출력 파일 이름에 대한 문자열
    String outputFileName("sample_html_out.pdf");

    // Document 인스턴스 생성
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // PDF 파일의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();

    // HTML 콘텐츠로 HtmlFragment 인스턴스화
    auto title = MakeObject<HtmlFragment>("<h1 style=\"color:blue\"><strong>HTML String Demo</strong></h1>");

    // 여백 세부 정보를 위한 MarginInfo 설정
    auto margin = MakeObject<MarginInfo>();
    margin->set_Bottom(10);
    margin->set_Top(200);
    // 여백 정보 설정
    title->set_Margin(margin);

    // 페이지의 단락 컬렉션에 HTML Fragment 추가
    page->get_Paragraphs()->Add(title);
    // PDF 파일 저장
    document->Save(_dataDir + outputFileName);
}
```

다음 코드 스니펫은 문서에 HTML 순서 목록을 추가하는 방법을 보여줍니다:

```cpp
void AddHTMLOrderedListIntoDocuments() {
    
    String _dataDir("C:\\Samples\\");

    // 출력 파일 이름을 위한 문자열
    String outputFileName("AddHTMLOrderedListIntoDocuments_out.pdf");

    // Document 객체 인스턴스화    
    auto document = MakeObject<Document>();

    // 해당 HTML 조각을 가진 HtmlFragment 객체 인스턴스화
    auto htmlFragment = MakeObject<HtmlFragment>(
        "<div style=\"font-family: sans-serif\"><ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li><li>Fifth</li></ul><p>Text after the list.</p><p>Next line<br/>Last line</p></div>");
    // Pages 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();

    // 페이지 안에 HtmlFragment 추가
    page->get_Paragraphs()->Add(htmlFragment);

    // 결과 PDF 파일 저장
    document->Save(_dataDir + outputFileName);
}
```

다음과 같이 TextState 객체를 사용하여 HTML 문자열 형식을 설정할 수도 있습니다:

```cpp
void AddHTMLStringFormatting() {
    
    String _dataDir("C:\\Samples\\");

    // 출력 파일 이름을 위한 문자열
    String outputFileName("sample_html_out.pdf");

    // Document 객체 인스턴스화    
    auto document = MakeObject<Document>();

    // Pages 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();

    // HTML 내용을 가진 HtmlFragment 인스턴스화
    auto title = MakeObject<HtmlFragment>("<h1><strong>HTML String Demo</strong></h1>");

    auto textState = MakeObject<TextState>(12);

    textState->set_Font(FontRepository::FindFont(u"Calibri"));
    textState->set_ForegroundColor(Color::get_Green());
    textState->set_BackgroundColor(Color::get_Coral());
    title->set_TextState(textState);

    // 페이지의 단락 컬렉션에 HTML Fragment 추가
    page->get_Paragraphs()->Add(title);
    // PDF 파일 저장
    document->Save(_dataDir + outputFileName);
}

```

문자 속성 값을 HTML 마크업을 통해 설정한 후 동일한 값을 TextState 속성에 제공하면 TextState 인스턴스의 속성 형식에 의해 HTML 매개 변수가 덮어쓰여집니다. 다음 코드 조각은 설명된 동작을 보여줍니다.

```cpp
void AddHTMLUsingDOMAndOverwrite() {

    String _dataDir("C:\\Samples\\");
    // 출력 파일 이름에 대한 문자열
    String outputFileName("AddHTMLUsingDOMAndOverwrite_out.pdf");

    // Document 객체 인스턴스화
    auto document = MakeObject<Document>();

    // Pages 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();

    // HTML 내용을 가진 HtmlFragment 인스턴스화
    auto title = MakeObject<HtmlFragment>("<p style='font-family: Verdana'><b><i>Table contains text</i></b></p>");

    // 'Verdana'의 글꼴 패밀리가 'Arial'로 재설정됩니다
    title->set_TextState(new TextState(u"Arial Black"));
    title->set_TextState(new TextState(20));

    // 아래쪽 여백 정보 설정
    title->get_Margin()->set_Bottom(10);
    // 위쪽 여백 정보 설정
    title->get_Margin()->set_Top(400);
    // 페이지의 단락 컬렉션에 HTML 조각 추가
    page->get_Paragraphs()->Add(title);
    // PDF 파일 저장
    document->Save(_dataDir + outputFileName);
}
```

## 각주 및 미주 (DOM)

각주는 연속적인 위첨자 번호를 사용하여 논문 본문에 있는 주석을 나타냅니다. 실제 주석은 들여쓰기되며 페이지 하단에 각주로 나타날 수 있습니다.

### 각주 추가하기

각주 참조 시스템에서 참조를 나타내려면:

- 출처 자료 바로 뒤의 줄 위에 작은 숫자를 넣습니다. 이 숫자는 주석 식별자라고 하며, 텍스트 라인 위에 약간 위치합니다. 
- 같은 숫자를 페이지 하단에 출처 인용과 함께 넣습니다. 각주는 숫자 순서대로 이루어져야 하며, 첫 번째 참조는 1, 두 번째는 2, 이런 식으로 진행됩니다.

각주의 장점은 독자가 간단히 페이지 아래를 내려다보면 관심 있는 참조의 출처를 발견할 수 있다는 것입니다.

다음 단계를 따르세요:

- [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 인스턴스를 생성합니다
- [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 객체를 생성합니다

- [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment) 객체를 생성합니다
- Note 인스턴스를 생성하고 그 값을 TextFragment [FootNote](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment#abe1663009fbceed84a0a392527463219) 속성에 전달합니다.
- 페이지 인스턴스의 단락 컬렉션에 TextFragment를 추가합니다.

```cpp
void AddFootNote() {
    
    String _dataDir("C:\\Samples\\");

    // 출력 파일 이름을 위한 문자열
    String inputFileName("sample.pdf");
    String outputFileName("sample_footnote_out.pdf");

    // Document 객체 인스턴스화
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Pages Collection에 페이지 추가
    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>("Portable Document Format");
    tfa->Visit(page);

    auto t = tfa->get_TextFragments()->idx_get(1);
    auto note = MakeObject<Note>();
    note->set_Text(u"Demo");
    t->set_FootNote(note);

    // TextFragment 인스턴스 생성
    auto text = MakeObject<TextFragment>("Hello World");
    // TextFragment에 대한 FootNote 값 설정
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    // 문서의 첫 번째 페이지의 단락 컬렉션에 TextFragment 추가
    page->get_Paragraphs()->Add(text);
    // 두 번째 TextFragment 생성
    text = MakeObject<TextFragment>("Aspose.Pdf for Java");
    // 두 번째 텍스트 조각에 대한 FootNote 설정
    text->set_FootNote(MakeObject<Note>("foot note for test text 2"));
    // PDF 파일의 단락 컬렉션에 두 번째 텍스트 조각 추가
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

### FootNote의 사용자 지정 선 스타일

다음 예제는 Pdf 페이지 하단에 각주를 추가하고 사용자 지정 선 스타일을 정의하는 방법을 보여줍니다.

```cpp
void CustomFootNote_Line() {
    
    String _dataDir("C:\\Samples\\");

    // 출력 파일 이름을 위한 문자열    
    String outputFileName("customFootNote_Line.pdf");

    // Document 인스턴스 생성
    auto document = MakeObject<Document>();

    // PDF의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();
    
    // GraphInfo 객체 생성
    auto graph = MakeObject<GraphInfo>();
    // 선 너비를 2로 설정
    graph->set_LineWidth(2);
    // 그래프 객체의 색상 설정
    graph->set_Color(Color::get_Red());
    // 대시 배열 값을 3으로 설정
    graph->set_DashArray(MakeArray<int>(3));
    // 대시 페이즈 값을 1로 설정
    graph->set_DashPhase(1);
    // 페이지의 각주 선 스타일을 그래프로 설정
    page->set_NoteLineStyle(graph);

    // TextFragment 인스턴스 생성
    auto text = MakeObject<TextFragment>("Hello World");
    // TextFragment에 각주 값 설정
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    // 문서의 첫 번째 페이지의 단락 컬렉션에 TextFragment 추가
    page->get_Paragraphs()->Add(text);
    // 두 번째 TextFragment 생성
    text = MakeObject<TextFragment>("Aspose.Pdf for Java");
    // 두 번째 텍스트 프래그먼트에 각주 설정
    text->set_FootNote(MakeObject<Note>("foot note for test text 2"));
    // PDF 파일의 단락 컬렉션에 두 번째 텍스트 프래그먼트 추가
    page->get_Paragraphs()->Add(text);
    // PDF 파일 저장
    document->Save(_dataDir + outputFileName);
}
```

문자 상태 개체를 사용하여 각주 레이블(참고 식별자) 서식을 다음과 같이 설정할 수 있습니다:

```csharp
void AddCustomFootNoteLabel() {
    
    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름에 대한 문자열    
    String inputFileName("sample.pdf");

    // 출력 파일 이름에 대한 문자열    
    String outputFileName("sample_footnote.pdf");

    // 문서 인스턴스 생성
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>("Portable Document Format");
    tfa->Visit(page);

    auto t = tfa->get_TextFragments()->idx_get(1);
    auto note = MakeObject<Note>("Demo");
    t->set_FootNote(note);

    // TextFragment 인스턴스 생성
    auto text = MakeObject<TextFragment>("Hello World");
    // TextFragment에 대한 각주 값 설정
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    text->get_FootNote()->set_Text(u"21");

    auto ts = MakeObject<TextState>();
    ts->set_ForegroundColor(Color::get_Blue());
    ts->set_FontStyle(FontStyles::Italic);
    text->get_FootNote()->set_TextState(ts);

    // 문서의 첫 번째 페이지의 단락 컬렉션에 TextFragment 추가
    page->get_Paragraphs()->Add(text);
    // 두 번째 TextFragment 생성
    text = MakeObject<TextFragment>(u"Aspose.Pdf for C++");
    // 두 번째 텍스트 조각에 대한 각주 설정
    text->set_FootNote(MakeObject<Note>("foot note for test text 2"));
    // PDF 파일의 단락 컬렉션에 두 번째 텍스트 조각 추가
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

### 각주 레이블 사용자 정의

기본적으로 각주 번호는 1부터 시작하여 증가합니다. 그러나 사용자 정의 각주 레이블을 설정해야 하는 요구 사항이 있을 수 있습니다. 이 요구 사항을 충족하려면 다음 코드 스니펫을 사용해 보십시오.

```cpp
void CustomFootNote_Label() {

    String _dataDir("C:\\Samples\\");
    // 출력 파일 이름에 대한 문자열    
    String outputFileName("CustomizeFootNoteLabel_out.pdf");

    // Document 인스턴스 생성
    auto document = MakeObject<Document>();

    // PDF의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();

    // GraphInfo 객체 생성
    auto graph = MakeObject<GraphInfo>();

    // 선 너비를 2로 설정
    graph->set_LineWidth(2);

    // 그래프 객체의 색상을 설정
    graph->set_Color(Color::get_Red());

    // 대시 배열 값을 3으로 설정
    graph->set_DashArray(MakeArray<int>(3));

    // 대시 단계 값을 1로 설정
    graph->set_DashPhase(1);

    // 페이지의 각주 선 스타일을 그래프로 설정
    page->set_NoteLineStyle(graph);

    // TextFragment 인스턴스 생성
    auto text = MakeObject<TextFragment>("Hello World");
    // TextFragment에 각주 값 설정
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    // 각주에 사용자 정의 레이블 지정
    text->get_FootNote()->set_Text(u" Aspose(2021)");
    // 문서의 첫 번째 페이지의 단락 컬렉션에 TextFragment 추가
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## 이미지 및 표를 각주에 추가하기

다음 코드 스니펫은 [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment) 객체에 [각주](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment#a017ff999979d9f799b8e3cd32ab95722)를 추가한 다음 각주 섹션의 단락 컬렉션에 이미지 및 표 객체를 추가하는 단계를 보여줍니다.

```cpp

void AddingImageAndTableToFootnote() {
    
    String _dataDir("C:\\Samples\\");

    // 출력 파일 이름을 위한 문자열    
    String outputFileName("AddImageAndTableToFootNote_out.pdf");

    // Document 인스턴스 생성
    auto document = new Document();
    // PDF의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();

    // TextFragment 인스턴스 생성
    auto text = MakeObject<TextFragment>("Hello World");

    page->get_Paragraphs()->Add(text);

    text->set_FootNote(MakeObject<Note>());
    auto image = MakeObject<Image>();
    image->set_File(_dataDir + u"aspose-logo.jpg");
    image->set_FixHeight(20);

    text->get_FootNote()->get_Paragraphs()->Add(image);

    auto footNote = MakeObject<TextFragment>("footnote text");
    footNote->get_TextState()->set_FontSize(20);
    footNote->set_IsInLineParagraph(true);
    text->get_FootNote()->get_Paragraphs()->Add(footNote);
    
    auto table = MakeObject<Table>();
    table->get_Rows()->Add()->get_Cells()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Row 1 Cell 1"));
    text->get_FootNote()->get_Paragraphs()->Add(table);

    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## EndNotes를 작성하는 방법

EndNote는 독자가 논문의 끝부분에 있는 특정 위치를 참조하여 인용된 정보나 언급된 단어의 출처를 찾을 수 있도록 하는 출처 인용입니다. EndNote를 사용할 때 인용문, 요약문 또는 요약된 자료는 위첨자로 된 번호가 뒤따릅니다.

다음 예제는 Pdf 페이지에서 EndNote를 추가하는 방법을 보여줍니다.

```cpp
void HowToCreateEndNotes() {
    
    String _dataDir("C:\\Samples\\");

    // 출력 파일 이름에 대한 문자열    
    String outputFileName("endNote_out.pdf");

    // Document 인스턴스 생성
    auto document = new Document();
    // PDF의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();

    // TextFragment 인스턴스 생성
    auto text = MakeObject<TextFragment>("Hello World");

    // TextFragment에 대한 FootNote 값 설정
    text->set_EndNote(MakeObject<Note>("sample End note"));

    // FootNote에 대한 사용자 정의 레이블 지정
    text->get_EndNote()->set_Text(u" Aspose(2021)");
    // 문서의 첫 번째 페이지의 단락 컬렉션에 TextFragment 추가
    page->get_Paragraphs()->Add(text);
    // PDF 파일 저장
    document->Save(_dataDir + outputFileName);
}
```

## 텍스트와 이미지 인라인 문단으로 추가하기

PDF 파일의 기본 레이아웃은 흐름 레이아웃(왼쪽 위에서 오른쪽 아래)입니다. 따라서 새 요소가 PDF 파일에 추가될 때마다 오른쪽 아래 흐름에 추가됩니다. 그러나 이미지와 텍스트를 동일 수준(연속적으로)에 표시해야 하는 요구 사항이 있을 수 있습니다. 한 가지 방법은 테이블 인스턴스를 생성하고 두 요소를 개별 셀 객체에 추가하는 것입니다. 그러나 또 다른 방법은 인라인 문단일 수 있습니다. 이미지와 텍스트의 IsInLineParagraph 속성을 true로 설정하면 이러한 문단이 다른 페이지 요소와 인라인으로 나타납니다.

다음 코드 스니펫은 PDF 파일에서 텍스트와 이미지를 인라인 문단으로 추가하는 방법을 보여줍니다.

```cpp
void TextAndImageAsInLineParagraph() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("TextAndImageAsParagraph_out.pdf");

    // Document 인스턴스 생성
    auto document = MakeObject<Document>();

    // 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();

    // TextFragment 생성
    auto text = MakeObject<TextFragment>("Hello World.. ");
    // 페이지 객체의 문단 컬렉션에 텍스트 조각 추가
    page->get_Paragraphs()->Add(text);

    // 이미지 인스턴스 생성
    auto image = MakeObject<Image>();

    // 이미지를 인라인 문단으로 설정하여
    // 이전 문단 객체(TextFragment) 바로 뒤에 나타나도록 함
    image->set_IsInLineParagraph(true);

    // 이미지 파일 경로 지정
    image->set_File(_dataDir + u"aspose-logo.jpg");
    // 이미지 높이 설정 (선택사항)
    image->set_FixHeight(30);
    // 이미지 너비 설정 (선택사항)
    image->set_FixWidth(100);
    // 페이지 객체의 문단 컬렉션에 이미지 추가
    page->get_Paragraphs()->Add(image);
    // 다른 내용으로 TextFragment 객체 재초기화
    text = MakeObject<TextFragment>(" Hello Again..");
    // TextFragment를 인라인 문단으로 설정
    text->set_IsInLineParagraph(true);
    // 새로 생성된 TextFragment를 페이지의 문단 컬렉션에 추가
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## 텍스트 추가 시 문자 간격 지정

텍스트는 TextFragment 인스턴스나 TextParagraph 객체를 사용하여 PDF의 단락 컬렉션에 추가할 수 있으며, TextStamp 클래스를 사용하여 PDF 내에 텍스트를 스탬프할 수도 있습니다. 텍스트를 추가할 때 텍스트 객체의 문자 간격을 지정해야 할 수 있습니다. 이 요구 사항을 충족하기 위해 새로운 속성이 도입되었습니다: Property CharacterSpacing.

이 요구 사항을 충족시키기 위한 다음의 접근 방식을 고려하세요.

다음 접근 방식은 PDF 문서에 텍스트를 추가할 때 문자 간격을 지정하는 단계를 보여줍니다.

### TextBuilder와 TextFragment 사용

```cpp
// TextBuilder와 TextFragment를 사용하여 텍스트 추가 시 문자 간격 지정
void CharacterSpacing_TextFragment() {
    
    String _dataDir("C:\\Samples\\");

    // 출력 파일 이름을 위한 문자열    
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // Document 인스턴스 생성
    auto document = MakeObject<Document>();
    // Document의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();

    // TextBuilder 인스턴스 생성
    auto builder = MakeObject<TextBuilder>(page);

    // 샘플 내용으로 텍스트 조각 인스턴스 생성
    auto wideFragment = MakeObject<TextFragment>("Text with increased character spacing");
    wideFragment->get_TextState()->ApplyChangesFrom(MakeObject<TextState>("Arial", 12));

    // TextFragment에 대한 문자 간격 지정
    wideFragment->get_TextState()->set_CharacterSpacing(2.0f);

    // TextFragment의 위치 지정
    wideFragment->set_Position(MakeObject<Position>(100, 650));

    // TextBuilder 인스턴스에 TextFragment 추가
    builder->AppendText(wideFragment);

    // 결과 PDF 문서를 저장합니다.
    document->Save(_dataDir + outputFileName);
}
```

### Using TextParagraph

```cpp
void CharacterSpacing_TextParagraph() {
    
    String _dataDir("C:\\Samples\\");

    // String for output file name    
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // Create Document instance
    auto document = MakeObject<Document>();

    // Add page to pages collection of Document
    auto page = document->get_Pages()->Add();

    // Create TextBuilder instance
    auto builder = MakeObject<TextBuilder>(page);

    // Instantiate TextParagraph instance
    auto paragraph = MakeObject<TextParagraph>();

    // Create TextState instance to specify font name and size
    auto state = MakeObject<TextState>("Arial", 12);

    // Specify the character spacing
    state->set_CharacterSpacing(1.5f);

    // Append text to TextParagraph object
    paragraph->AppendLine(u"This is paragraph with character spacing", state);

    // Specify the position for TextParagraph
    paragraph->set_Position(MakeObject<Position>(100, 550));

    // Append TextParagraph to TextBuilder instance
    builder->AppendParagraph(paragraph);

    // Save resulting PDF document.
    document->Save(_dataDir + outputFileName);
}
```

### 텍스트 단락 사용

```cpp
void CharacterSpacing_TextParagraph() {
    
    String _dataDir("C:\\Samples\\");

    // 출력 파일 이름에 대한 문자열    
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // 문서 인스턴스 생성
    auto document = MakeObject<Document>();

    // 문서의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();

    // 텍스트 빌더 인스턴스 생성
    auto builder = MakeObject<TextBuilder>(page);

    // 텍스트 단락 인스턴스 생성
    auto paragraph = MakeObject<TextParagraph>();

    // 폰트 이름과 크기를 지정하기 위한 텍스트 상태 인스턴스 생성
    auto state = MakeObject<TextState>("Arial", 12);

    // 문자 간격 지정
    state->set_CharacterSpacing(1.5f);

    // 텍스트 단락 객체에 텍스트 추가
    paragraph->AppendLine(u"문자 간격이 있는 단락입니다", state);

    // 텍스트 단락의 위치 지정
    paragraph->set_Position(MakeObject<Position>(100, 550));

    // 텍스트 빌더 인스턴스에 텍스트 단락 추가
    builder->AppendParagraph(paragraph);

    // 결과 PDF 문서 저장
    document->Save(_dataDir + outputFileName);
}
```

### Using TextStamp

```cpp
void CharacterSpacing_TextStamp() {
    
    String _dataDir("C:\\Samples\\");
    String outputFileName("CharacterSpacingUsingTextStamp_out.pdf");
    // Document 인스턴스 생성
    auto document = MakeObject<Document>();

    // 페이지 컬렉션에 페이지 추가    
    auto page = document->get_Pages()->Add();

    // 샘플 텍스트로 TextStamp 인스턴스화
    auto stamp = MakeObject<TextStamp>("This is text stamp with character spacing");

    // Stamp 객체에 대한 글꼴 이름 지정
    stamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    // TextStamp에 대한 글꼴 크기 지정
    stamp->get_TextState()->set_FontSize(12);
    // 문자 간격을 1f로 지정
    stamp->get_TextState()->set_CharacterSpacing(1.0f);
    // Stamp에 대한 XIndent 설정
    stamp->set_XIndent(100);
    // Stamp에 대한 YIndent 설정
    stamp->set_YIndent(500);
    // 페이지 인스턴스에 텍스트 스탬프 추가
    stamp->Put(page);
    // 결과 PDF 문서 저장.
    document->Save(_dataDir + outputFileName);
}
```

## 다중 열 PDF 문서 만들기

이 주제에서는 Aspose.Pdf for C++를 사용하여 다중 열 PDF를 만드는 방법을 보여줍니다.

오늘날, 우리는 책보다는 주로 별도의 페이지에 여러 열로 표시된 뉴스를 더 자주 보게 됩니다. 책에서는 텍스트의 단락이 대부분 왼쪽에서 오른쪽으로 모든 페이지에 인쇄됩니다. Microsoft Word 및 Adobe Acrobat Writer와 같은 많은 문서 처리 응용 프로그램은 사용자가 단일 페이지에 여러 열을 만들고 그 안에 데이터를 추가할 수 있도록 합니다.

Aspose.Pdf for C++ 또한 PDF 문서 페이지에 여러 열을 생성할 수 있는 기능을 제공합니다. 여러 열이 있는 PDF를 생성하려면, [Aspose.Pdf.FloatingBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.floating_box) 클래스를 사용할 수 있습니다. 이 클래스는 FloatingBox 내부의 열 수를 지정하는 ColumnInfo.ColumnCount 속성을 제공하며, ColumnInfo.ColumnSpacing 및 ColumnInfo.ColumnWidths를 사용하여 열 간격 및 열 너비도 지정할 수 있습니다.

아래 예제는 Graphs 객체(선)를 사용하여 두 개의 열을 생성하는 방법을 보여줍니다. 이 객체들은 FloatingBox의 단락 컬렉션에 추가되고, 그 후 Page 인스턴스의 단락 컬렉션에 추가됩니다.

```cpp
void CreateMultiColumn() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("CreateMultiColumnPdf_out.pdf");

    // Create new document instance    
    auto document = MakeObject<Document>();

    // Specify the left margin info for the PDF file
    document->get_PageInfo()->get_Margin()->set_Left(40);

    // Specify the Right margin info for the PDF file
    document->get_PageInfo()->get_Margin()->set_Right(40);

    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->Add();

    auto graph1 = MakeObject<Aspose::Pdf::Drawing::Graph>(500, 2);

    // Add the line to paraphraphs collection of section object
    page->get_Paragraphs()->Add(graph1);

    // Specify the coordinates for the line
    auto posArr = MakeArray<float>({ 1, 2, 500, 2 });
    auto l1 = MakeObject<Aspose::Pdf::Drawing::Line>(posArr);
    graph1->get_Shapes()->Add(l1);

    // Create string variables with text containing html tags
    String s ("<span style=\"font-family: \"Times New Roman\", Times, serif;\" font-size=\"14pt\" \">\
<strong> How to Steer Clear of money scams</<strong> </span>");

    // Create text paragraphs containing HTML text

    auto heading_text = MakeObject<HtmlFragment>(s);
    page->get_Paragraphs()->Add(heading_text);

    auto box = MakeObject<FloatingBox>();

    // Add four columns in the section
    box->get_ColumnInfo()->set_ColumnCount(2);
    // Set the spacing between the columns
    box->get_ColumnInfo()->set_ColumnSpacing(u"5");

    box->get_ColumnInfo()->set_ColumnWidths(u"105 105");
    auto text1 = MakeObject<TextFragment>("By A Googler (The Official Google Blog)");
    text1->get_TextState()->set_FontSize(8);
    text1->get_TextState()->set_LineSpacing(2);
    text1->get_TextState()->set_FontSize(10);
    text1->get_TextState()->set_FontStyle(FontStyles::Italic);

    box->get_Paragraphs()->Add(text1);

    // Create a graphs object to draw a line
    auto graph2 = MakeObject<Aspose::Pdf::Drawing::Graph>(50, 10);
    // Specify the coordinates for the line
    auto posArr2 = MakeArray<float>({ 1, 10, 100, 10 });

    auto l2 = MakeObject<Aspose::Pdf::Drawing::Line>(posArr2);
    graph2->get_Shapes()->Add(l2);

    // Add the line to paragraphs collection of section object
    box->get_Paragraphs()->Add(graph2);

    auto text2 = MakeObject<TextFragment>(
        "Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. \
        Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue.\
        Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur \
        ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean \
        posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. \
        Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, \
        risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam \
        luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, \
        sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, \
        pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut,\
        iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus \
        mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla.\
        Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam,\
        iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique\
        ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\
        Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. \
        Praesent porttitor turpis eleifend ante. Morbi sodales.");
    box->get_Paragraphs()->Add(text2);

    page->get_Paragraphs()->Add(box);

    // Save PDF file
    document->Save(_dataDir + outputFileName);
}
```

## 사용자 지정 탭 위치 작업

탭 위치는 탭의 정지 지점입니다. 워드 프로세싱에서 각 라인은 정기적인 간격으로 배치된 여러 개의 탭 위치를 포함합니다(예: 매 반 인치마다). 그러나 대부분의 워드 프로세서는 원하는 곳에 탭 위치를 설정할 수 있도록 허용하므로 이를 변경할 수 있습니다. 탭 키를 누르면 커서 또는 삽입 포인트가 다음 탭 위치로 이동하는데, 이 자체는 보이지 않습니다. 탭 위치는 텍스트 파일에 존재하지 않지만, 워드 프로세서는 탭 키에 올바르게 반응할 수 있도록 이를 추적합니다.

다음은 사용자 지정 탭 위치를 설정하는 방법의 예입니다.

```cpp
void CustomTabStops() {
    String _dataDir("C:\\Samples\\");
    String outputFileName("CustomTabStops_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto ts = MakeObject<TabStops>();
    auto ts1 = ts->Add(100);

    ts1->set_AlignmentType(TabAlignmentType::Right);
    ts1->set_LeaderType(TabLeaderType::Solid);

    auto ts2 = ts->Add(200);
    ts2->set_AlignmentType(TabAlignmentType::Center);
    ts2->set_LeaderType(TabLeaderType::Dash);

    auto ts3 = ts->Add(300);
    ts3->set_AlignmentType(TabAlignmentType::Left);
    ts3->set_LeaderType(TabLeaderType::Dot);

    auto header = MakeObject<TextFragment>("This is a example of forming table with TAB stops", ts);
    auto text0 =  MakeObject<TextFragment>("#$TABHead1 #$TABHead2 #$TABHead3", ts);

    auto text1 = MakeObject<TextFragment>("#$TABdata11 #$TABdata12 #$TABdata13", ts);
    auto text2 = MakeObject<TextFragment>("#$TABdata21 ", ts);
    text2->get_Segments()->Add(MakeObject<TextSegment>("#$TAB"));
    text2->get_Segments()->Add(MakeObject<TextSegment>("data22 "));
    text2->get_Segments()->Add(MakeObject<TextSegment>("#$TAB"));
    text2->get_Segments()->Add(MakeObject<TextSegment>("data23"));
              
    page->get_Paragraphs()->Add(header);
    page->get_Paragraphs()->Add(text0);
    page->get_Paragraphs()->Add(text1);
    page->get_Paragraphs()->Add(text2);

    document->Save(_dataDir + outputFileName);
}
```

## PDF에 투명 텍스트 추가하는 방법

PDF 1.4(어크로뱃 5에서 지원하는 파일 형식)는 투명성을 지원한 첫 번째 PDF 버전입니다. 이 PDF는 Adobe Illustrator 9과 거의 같은 시기에 시장에 출시되었습니다.

PDF 파일은 이미지, 텍스트, 그래프, 첨부 파일, 주석 객체를 포함하며, TextFragment를 생성할 때 전경색, 배경색 정보와 텍스트 서식을 설정할 수 있습니다. Aspose.PDF for C++는 알파 색상 채널을 사용하여 텍스트를 추가하는 기능을 지원합니다. 다음의 코드 스니펫은 투명한 색상으로 텍스트를 추가하는 방법을 보여줍니다.

```cpp
void AddTransparentText() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("AddTransparentText_out.pdf");

    // 문서 인스턴스 생성
    auto document = MakeObject<Document>();    
    // PDF 파일의 페이지 컬렉션에 페이지 생성
    auto page = document->get_Pages()->Add();

    // Graph 객체 생성
    auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);

    // 특정 크기의 사각형 인스턴스 생성
    auto rect = MakeObject<Aspose::Pdf::Drawing::Rectangle>(100, 100, 400, 400);
    // 알파 색상 채널에서 색상 객체 생성
    int alpha = 10;
    int green = 0;
    int red = 100;
    int blue = 0;

    auto alphaColor = Color::FromArgb(alpha, red, green, blue);

    rect->get_GraphInfo()->set_FillColor(alphaColor);

    // Graph 객체의 도형 컬렉션에 사각형 추가
    canvas->get_Shapes()->Add(rect);

    // 페이지 객체의 단락 컬렉션에 그래프 객체 추가
    page->get_Paragraphs()->Add(canvas);

    // 그래프 객체의 위치를 변경하지 않도록 값 설정
    canvas->set_IsChangePosition(false);

    // 샘플 값으로 TextFragment 인스턴스 생성
    auto text = MakeObject<TextFragment>(
        "transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text ");
    // 알파 채널에서 색상 객체 생성
    alpha = 30;
    alphaColor = Color::FromArgb(alpha, red, green, blue);
    // 텍스트 인스턴스에 색상 정보 설정
    text->get_TextState()->set_ForegroundColor(alphaColor);
    // 페이지 인스턴스의 단락 컬렉션에 텍스트 추가
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## 폰트를 위한 줄 간격 지정

[Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options) 클래스는 특정 폰트 예: 입력 폰트 "HPSimplified.ttf"를 위해 설계된 [LineSpacingMode](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a240276fd8a270b7c134d3355c5fb1c91)라는 열거형을 가지고 있습니다. 또한 [Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options) 클래스에는 LineSpacingMode 유형의 [LineSpacing](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a240276fd8a270b7c134d3355c5fb1c91a9e120eead36071a90367e425c96b5eaf) 속성이 있습니다. 당신은 단지 LineSpacing을 LineSpacingMode.FullSize로 설정해야 합니다. 폰트를 올바르게 표시하기 위한 코드 스니펫은 다음과 같습니다:

```cpp
void SpecifyLineSpacingForFonts() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("SpecifyLineSpacing_out.pdf");

    String fontFile ("hp-simplified-265.ttf");

    // 입력 PDF 파일 로드
    auto document = MakeObject<Document>();
    
    // LineSpacingMode.FullSize를 가진 TextFormattingOptions 생성
    auto formattingOptions = MakeObject<TextFormattingOptions>();
    formattingOptions->set_LineSpacing(TextFormattingOptions::LineSpacingMode::FullSize);
    
    // 샘플 문자열로 텍스트 조각 생성
    auto textFragment = MakeObject<TextFragment>("Hello world");

    // TrueType 폰트를 스트림 객체로 로드
    auto fontStream = System::IO::File::OpenRead(_dataDir + fontFile);
    
    // 텍스트 문자열에 대한 폰트 이름 설정
    textFragment->get_TextState()->set_Font(FontRepository::OpenFont(fontStream, FontTypes::TTF));
    // 텍스트 조각의 위치 지정
    textFragment->set_Position(MakeObject<Position>(100, 600));
    // 현재 조각의 TextFormattingOptions를 미리 정의된 것으로 설정 (LineSpacingMode.FullSize를 가리킴)
    textFragment->get_TextState()->set_FormattingOptions(formattingOptions);
    
    // PDF 파일에 배치할 수 있도록 TextBuilder에 텍스트 추가    
    auto page = document->get_Pages()->Add();
    page->get_Paragraphs()->Add(textFragment);

    // 결과 PDF 문서 저장
    document->Save(_dataDir + outputFileName);
}
```

## 텍스트 너비 동적으로 가져오기

[Aspose.Pdf.Text.TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state) 클래스는 PDF 문서에서 텍스트 너비를 동적으로 가져오는 방법을 보여줍니다.

때때로 텍스트 너비를 동적으로 가져와야 할 때가 있습니다. Aspose.PDF for C++는 문자열 너비 측정을 위한 두 가지 방법을 포함하고 있습니다. Aspose.Pdf.Text.Font 또는 Aspose.Pdf.Text.TextState 클래스의 [MeasureString](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state#a084c1781028cd3483c82b4fd4cec4967) 메서드를 호출할 수 있습니다 (또는 둘 다). 아래의 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다.

```cpp
void GetTextWidthDynamicaly() {
    auto font = FontRepository::FindFont(u"Arial");
    auto ts = MakeObject<TextState>();

    ts->set_Font(font);
    ts->set_FontSize(14);

    if (Math::Abs(font->MeasureString(u"A", 14) - 9.337) > 0.001)
        Console::WriteLine(u"Unexpected font string measure!");

    if (Math::Abs(ts->MeasureString(u"z") - 7.0) > 0.001)
        Console::WriteLine(u"Unexpected font string measure!");

    for (char c = 'A'; c <= 'z'; c++) {
        String v(c);
        double fnMeasure = font->MeasureString(v, 14);
        double tsMeasure = ts->MeasureString(v);

        if (Math::Abs(fnMeasure - tsMeasure) > 0.001)
            Console::WriteLine(u"Font and state string measuring doesn't match!");
    }
}
```