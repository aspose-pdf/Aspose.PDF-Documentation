---
title: PDF에서 텍스트 교체하기 C++ 사용
linktitle: PDF에서 텍스트 교체
type: docs
weight: 40
url: ko/cpp/replace-text-in-pdf/
description: PDF에서 텍스트를 교체하고 제거하는 다양한 방법에 대해 알아보세요. Aspose.PDF는 특정 영역이나 정규 표현식을 사용하여 텍스트를 교체할 수 있습니다.
lastmod: "2021-12-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

때때로 PDF 문서에서 텍스트를 교정하거나 교체해야 하는 작업이 나타나기도 합니다. 수작업으로 하려고 하면 번거로운 작업이 될 것이므로, 이 문제에 대한 해결책을 여기에 제시합니다.

솔직히 PDF 파일을 편집하는 것은 쉬운 작업이 아닙니다. 그래서 PDF 파일을 편집할 때 한 단어를 다른 단어로 찾아 교체해야 하는 상황이 발생하면, 그것은 매우 어려운 일이 될 것이며, 이를 완료하는 데 오랜 시간이 걸릴 것입니다. 게다가 출력물과 관련된 많은 문제들, 예를 들어 서식이 깨지거나 글꼴이 깨지는 문제를 겪을 수 있습니다. PDF 파일에서 텍스트를 쉽게 찾고 교체하려면, 우리는 Aspose.Pdf 라이브러리 소프트웨어를 사용할 것을 추천합니다. 이는 몇 분 안에 작업을 완료할 것입니다.

이 기사에서는 Aspose.PDF for C++를 사용하여 PDF 파일에서 텍스트를 성공적으로 찾고 교체하는 방법을 보여드리겠습니다.

## PDF 문서의 모든 페이지에서 텍스트 교체

{{% alert color="primary" %}}

Aspose.PDF를 사용하여 문서에서 텍스트를 찾아 교체하고 온라인 결과를 이 [링크](https://products.aspose.app/pdf/redaction)에서 확인할 수 있습니다.

{{% /alert %}}

PDF 문서의 모든 페이지에서 텍스트를 교체하려면 먼저 교체하고자 하는 특정 구문을 찾기 위해 TextFragmentAbsorber를 사용해야 합니다. 그런 다음 모든 TextFragment를 통해 텍스트를 교체하고 다른 속성을 변경합니다. 완료한 후에는 Document 객체의 Save 메서드를 사용하여 출력 PDF를 저장하기만 하면 됩니다. 다음 코드 스니펫은 PDF 문서의 모든 페이지에서 텍스트를 교체하는 방법을 보여줍니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceTextOnAllPages() {

    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // 입력 검색 구문의 모든 인스턴스를 찾기 위해 TextAbsorber 객체 생성
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("Web");

    // 문서의 첫 페이지에 대하여 absorber를 수용
    document->get_Pages()->Accept(textFragmentAbsorber);

    // 추출된 텍스트 조각을 컬렉션으로 가져오기
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // 조각을 반복
    for (auto textFragment : textFragmentCollection) {
        // 텍스트 및 기타 속성 업데이트
        textFragment->set_Text(u"World Wide Web");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }
    // 업데이트된 PDF 파일 저장
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## 특정 페이지 영역의 텍스트 교체

특정 페이지 영역의 텍스트를 교체하기 위해서는 먼저 TextFragmentAbsorber 객체를 인스턴스화하고, TextSearchOptions.Rectangle 속성을 사용하여 페이지 영역을 지정한 다음, 모든 TextFragments를 반복하여 텍스트를 교체해야 합니다. 이러한 작업이 완료되면 Document 객체의 Save 메서드를 사용하여 출력 PDF를 저장하기만 하면 됩니다. 다음 코드 스니펫은 PDF 문서의 모든 페이지에서 텍스트를 교체하는 방법을 보여줍니다.

```cpp
void ReplaceTextInParticularRegion() {

    String _dataDir("C:\\Samples\\");

    // PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // TextFragment Absorber 객체 인스턴스화
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("PDF");

    // 페이지 경계 내의 텍스트 검색
    textFragmentAbsorber->get_TextSearchOptions()->set_LimitToPageBounds(true);

    // 텍스트 검색 옵션에 대한 페이지 영역 지정
    textFragmentAbsorber->get_TextSearchOptions()->set_Rectangle(new Rectangle(100, 700, 400, 770));

    // PDF 파일의 첫 번째 페이지에서 텍스트 검색
    document->get_Pages()->idx_get(1)->Accept(textFragmentAbsorber);

    // 개별 TextFragment 반복
    for (auto tf : textFragmentAbsorber->get_TextFragments()) {
        // 텍스트를 "---"로 교체
        tf->set_Text(u"---");
    }

    // 업데이트된 PDF 파일 저장
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## 정규 표현식을 기반으로 텍스트 대체

정규 표현식을 기반으로 일부 구문을 대체하려면 먼저 TextFragmentAbsorber를 사용하여 해당 특정 정규 표현식과 일치하는 모든 구문을 찾아야 합니다. 정규 표현식을 TextFragmentAbsorber 생성자의 매개변수로 전달해야 합니다. 또한 정규 표현식을 사용할지 여부를 지정하는 TextSearchOptions 객체를 생성해야 합니다. TextFragments에서 일치하는 구문을 얻으면 모두 반복하여 필요에 따라 업데이트해야 합니다. 마지막으로, 문서 객체의 Save 메서드를 사용하여 업데이트된 PDF를 저장해야 합니다. 다음 코드 스니펫은 정규 표현식을 기반으로 텍스트를 대체하는 방법을 보여줍니다.

```cpp
void ReplaceTextWithRegularExpression() {

    String _dataDir("C:\\Samples\\");

    // load PDF file
    auto document = MakeObject<Document>(_dataDir + u"Sample.pdf");
    // Create TextAbsorber object to find all instances of the input search phrase
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("\\d{4}-\\d{4}");
    // like 1999-2000

    // Set text search option to specify regular expression usage
    auto textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // Accept the absorber for first page of document
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Get the extracted text fragments into collection
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Loop through the fragments
    for (auto textFragment : textFragmentCollection) {
        // Update text and other properties
        textFragment->set_Text(u"ABCD-EFGH");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }

    // Save the updated PDF file
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## 기존 PDF 파일에서 글꼴 교체

Aspose.PDF for C++는 PDF 문서에서 텍스트를 교체하는 기능을 지원합니다. 그러나 때로는 PDF 문서 내에서 사용되는 글꼴만 교체해야 하는 요구사항이 있을 수 있습니다. 따라서 텍스트를 교체하는 대신 사용되는 글꼴만 교체됩니다. TextFragmentAbsorber 생성자의 오버로드 중 하나는 TextEditOptions 객체를 인수로 받아들이며, TextEditOptions.FontReplace 열거형에서 RemoveUnusedFonts 값을 사용하여 우리의 요구사항을 충족할 수 있습니다. 다음 코드 스니펫은 PDF 문서 내의 글꼴을 교체하는 방법을 보여줍니다.

```cpp
void ReplaceFonts() {
    String _dataDir("C:\\Samples\\");

    // 문서 객체 인스턴스화
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // 텍스트 조각 검색 및 편집 옵션을 사용하지 않는 글꼴 제거로 설정
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>(
        MakeObject<TextEditOptions>(TextEditOptions::FontReplace::RemoveUnusedFonts));

    // 문서의 모든 페이지에 흡수기 적용
    document->get_Pages()->Accept(textFragmentAbsorber);

    // 모든 텍스트 조각을 순회
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();
    for (auto textFragment : textFragmentCollection) {
        String fontName = textFragment->get_TextState()->get_Font()->get_FontName();
        // 글꼴 이름이 ArialMT인 경우 글꼴 이름을 Arial로 교체
        if (fontName.Equals(u"ArialMT")) {
            textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        }
    }

    // 업데이트된 PDF 파일 저장
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

다음 코드 스니펫에서는 텍스트를 교체할 때 비영어 폰트를 사용하는 방법을 볼 수 있습니다:

```cpp
void UseNonEnglishFontWhenReplacingText() {

    String _dataDir("C:\\Samples\\");

    // Document 객체 인스턴스화
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // "PDF"라는 모든 단어를 특정 폰트의 일본어 텍스트로 변경
    // OS에 설치되어 있을 수 있는 MSGothic
    // 또한, 히에로글리프를 지원하는 다른 폰트일 수 있음
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("PDF");

    // 텍스트 검색 옵션의 인스턴스 생성
    auto searchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(searchOptions);

    // 문서의 모든 페이지에 대해 흡수기를 적용
    document->get_Pages()->Accept(textFragmentAbsorber);

    // 추출된 텍스트 조각을 컬렉션에 가져옴
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // 조각을 반복
    for (auto textFragment : textFragmentCollection) {
        // 텍스트 및 기타 속성을 업데이트
        textFragment->set_Text(u"ファイル");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"TakaoMincho"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }
    // 업데이트된 문서 저장
    document->Save(_dataDir + u"Japanese_Text.pdf");
}
```

## 텍스트 교체는 페이지 내용을 자동으로 재배열해야 합니다

Aspose.PDF for C++는 PDF 파일 내에서 텍스트를 찾고 교체하는 기능을 지원합니다. 그러나 최근 일부 클라이언트는 텍스트를 교체할 때 문제가 발생했습니다. 특정 TextFragment가 더 작은 내용으로 교체된 후 결과 PDF에 여분의 공백이 표시되거나, TextFragment가 더 긴 문자열로 교체되면 단어가 기존 페이지 콘텐츠와 겹치는 문제가 있었습니다. 따라서 PDF 문서 내의 텍스트를 교체한 후에 콘텐츠를 재배열하는 메커니즘을 도입해야 했습니다.

위에서 언급한 시나리오를 해결하기 위해, PDF 파일 내에서 텍스트를 교체할 때 이러한 문제가 발생하지 않도록 Aspose.PDF for C++가 개선되었습니다. 다음 코드 스니펫은 PDF 파일 내에서 텍스트를 교체하고 페이지 내용이 자동으로 재정렬되어야 하는 방법을 보여줍니다.

```cpp
void RearrangeContent() {
    String _dataDir("C:\\Samples\\");

    // Document 객체를 인스턴스화합니다.
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // 정규 표현식으로 TextFragment Absorber 객체를 생성합니다.
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("[PDF,Web]");

    auto textSearchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // 텍스트 교체 후 현재 줄이 너무 길거나 짧아질 경우 다음 또는 현재 줄에 텍스트를 감싸는
    // ReplaceAdjustment.WholeWordsHyphenation 옵션을 지정할 수도 있습니다:
    //textFragmentAbsorber->get_TextReplaceOptions()->set_ReplaceAdjustmentAction(TextReplaceOptions::ReplaceAdjustment::WholeWordsHyphenation);

    // 문서의 모든 페이지에 대해 absorber를 수락합니다.
    document->get_Pages()->Accept(textFragmentAbsorber);

    // 추출된 텍스트 프래그먼트를 컬렉션에 가져옵니다.
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // 각 TextFragment를 교체합니다.
    for (auto textFragment : textFragmentCollection) {
        // 교체되는 텍스트 프래그먼트의 폰트를 설정합니다.
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        // 폰트 크기를 설정합니다.
        textFragment->get_TextState()->set_FontSize(10);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
        // 플레이스홀더보다 더 큰 문자열로 텍스트를 교체합니다.
        textFragment->set_Text(u"This is a larger string for the testing of this feature");
    }
    // 결과 PDF를 저장합니다.
    document->Save(_dataDir + u"RearrangeContentsUsingTextReplacement_out.pdf");
}
```

## PDF 생성 중 대체 가능한 심볼 렌더링

대체 가능한 심볼은 실행 시간에 해당 내용으로 대체될 수 있는 텍스트 문자열 내의 특별한 심볼입니다. 현재 Aspose.PDF 네임스페이스의 새로운 문서 객체 모델에서 지원하는 대체 가능한 심볼은 `$P`, `$p,` `\n`, `\r`입니다. `$p`와 `$P`는 실행 시간에 페이지 번호를 처리하는 데 사용됩니다. `$p`는 현재 Paragraph 클래스가 위치한 페이지의 번호로 대체됩니다. `$P`는 문서의 총 페이지 수로 대체됩니다. PDF 문서의 단락 컬렉션에 `TextFragment`를 추가할 때 텍스트 내에서 줄 바꿈을 지원하지 않습니다. 그러나 줄 바꿈이 있는 텍스트를 추가하려면 `TextFragment`를 `TextParagraph`와 함께 사용하십시오:

- 단일 "\n" 대신 TextFragment에서 "\r\n" 또는 Environment.NewLine을 사용하십시오;
- TextParagraph 개체를 생성합니다. 텍스트를 줄 단위로 분할하여 추가합니다;
- TextFragment를 TextParagraph.AppendLine으로 추가합니다;
- TextBuilder.AppendParagraph로 TextParagraph를 추가합니다.

## 헤더/푸터 영역의 교체 가능한 기호

교체 가능한 기호는 PDF 파일의 헤더/푸터 섹션 내부에도 배치할 수 있습니다. 푸터 섹션에 교체 가능한 기호를 추가하는 방법을 보려면 다음 코드 스니펫을 검토하십시오.

```csharp
void ReplaceableSymbolsInHeaderFooterArea() {

    auto document = MakeObject<Document>();
    auto page = doc.getPages().add();

    auto marginInfo = MakeObject<MarginInfo>();
    marginInfo->set_Top(90);
    marginInfo->set_Bottom(50);
    marginInfo->set_Left(50);
    marginInfo->set_Right(50);

    // 페이지 정보의 여백 속성에 marginInfo 인스턴스 할당
    page.getPageInfo()->set_Margin(marginInfo);

    auto hfFirst = MakeObject<HeaderFooter>();
    page->set_Header(hfFirst);
    hfFirst->get_Margin()->set_Left(50);
    hfFirst->get_Margin()->set_Right(50);

    // 헤더로 표시할 콘텐츠를 저장할 텍스트 단락 인스턴스화
    auto t1 = MakeObject<TextFragment>("보고서 제목");
    t1->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    t1->get_TextState()->set_FontSize(16);
    t1->get_TextState()->set_ForegroundColor(Color::get_Black());
    t1->get_TextState()->set_FontStyle(FontStyles::Bold);
    t1->get_TextState()->set_HorizontalAlignment(HorizontalAlignment::Center);
    t1->get_TextState()->set_LineSpacing(5.0f);
    hfFirst->get_Paragraphs()->Add(t1);

    auto t2 = MakeObject<TextFragment>("보고서_이름");
    t2->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    t2->get_TextState()->set_ForegroundColor(Color::get_Black());
    t2->get_TextState()->set_HorizontalAlignment(HorizontalAlignment::Center);
    t2->get_TextState()->set_LineSpacing(5.0f);
    t2->get_TextState()->set_FontSize(12);
    hfFirst->get_Paragraphs()->Add(t2);

    // 섹션을 위한 HeaderFooter 객체 생성
    auto hfFoot = MakeObject<HeaderFooter>();

    // 홀수 및 짝수 푸터에 HeaderFooter 객체 설정
    page->set_Footer(hfFoot);
    hfFoot->get_Margin()->set_Left(50);
    hfFoot->get_Margin()->set_Right(50);

    // 총 페이지 수 중 현재 페이지 번호를 포함하는 텍스트 단락 추가
    auto t3 = MakeObject<TextFragment>("생성된 테스트 날짜");
    auto t4 = MakeObject<TextFragment>("보고서 이름 ");
    auto t5 = MakeObject<TextFragment>("페이지 $p / $P");

    // 테이블 객체 인스턴스화
    auto tab2 = MakeObject<Table>();

    // 원하는 섹션의 단락 컬렉션에 테이블 추가
    hfFoot->get_Paragraphs()->Add(tab2);

    // 테이블 열 너비 설정
    tab2->set_ColumnWidths(u"165 172 165");

    // 테이블에 행 생성 후 행에 셀 생성
    auto row3 = tab2->get_Rows()->Add();

    row3->get_Cells()->Add();
    row3->get_Cells()->Add();
    row3->get_Cells()->Add();

    // 텍스트의 수직 정렬을 중앙 정렬로 설정
    row3->get_Cells()->idx_get(0)->set_Alignment(HorizontalAlignment::Left);
    row3->get_Cells()->idx_get(1)->set_Alignment(HorizontalAlignment::Center);
    row3->get_Cells()->idx_get(2)->set_Alignment(HorizontalAlignment::Right);

    row3->get_Cells()->idx_get(0)->get_Paragraphs()->Add(t3);
    row3->get_Cells()->idx_get(1)->get_Paragraphs()->Add(t4);
    row3->get_Cells()->idx_get(2)->get_Paragraphs()->Add(t5);

    auto table = MakeObject<Table>();

    table->set_ColumnWidths(u"33% 33% 34%");
    table->set_DefaultCellPadding(new MarginInfo());
    table->get_DefaultCellPadding()->set_Top(10);
    table->get_DefaultCellPadding()->set_Bottom(10);

    // 원하는 섹션의 단락 컬렉션에 테이블 추가
    page.getParagraphs().add(table);

    // BorderInfo 객체를 사용하여 기본 셀 테두리 설정
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.1f));

    // 다른 맞춤형 BorderInfo 객체를 사용하여 테이블 테두리 설정
    table->set_Border(MakeObject<BorderInfo>(BorderSide::All, 1.0f));

    table->set_RepeatingRowsCount(1);

    // 테이블에 행 생성 후 행에 셀 생성
    auto row1 = table->get_Rows()->Add();

    row1->get_Cells()->Add(u"열1");
    row1->get_Cells()->Add(u"열2");
    row1->get_Cells()->Add(u"열3");

    String CRLF ("\r\n");

    for (int i = 0; i <= 10; i++) {
        auto row = table->get_Rows()->Add();
        row->set_IsRowBroken(true);
        for (int c = 0; c <= 2; c++) {
            SharedPtr<Cell> c1;
            if (c == 2)
                c1 = row->get_Cells()->Add(
                    u"Aspose.Total for C++는 Aspose에서 제공하는 모든 Java 구성 요소의 컴필레이션입니다. 이는 최신 버전을 포함하도록 "
                    + CRLF
                    + u"매일 컴파일됩니다. "
                    + CRLF
                    + u"매일 컴파일됩니다. "
                    + CRLF
                    + u"Aspose.Total for C++를 사용하여 개발자는 다양한 응용 프로그램을 만들 수 있습니다.");
            else
                c1 = row->get_Cells()->Add(u"항목1" + c);
            c1->set_Margin(new MarginInfo());
            c1->get_Margin()->set_Left(30);
            c1->get_Margin()->set_Top(10);
            c1->get_Margin()->set_Bottom(10);
        }
    }

    _dataDir = _dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
    doc.save(_dataDir);
}
```

## PDF 문서에서 모든 텍스트 제거

### 연산자를 사용하여 모든 텍스트 제거

일부 텍스트 작업에서는 PDF 문서에서 모든 텍스트를 제거해야 하며, 이를 위해 발견된 텍스트를 빈 문자열 값으로 설정해야 합니다. 사실은, 텍스트 조각 세트에 대해 텍스트를 변경하면 여러 작업이 텍스트의 위치를 확인하고 조정해야 합니다. 이는 텍스트 편집 스크립트에서 필요합니다. 문제는 루프에서 처리되는 스크립트에서 얼마나 많은 텍스트 조각이 삭제될지 알 수 없다는 점에 있습니다.

따라서 PDF 페이지에서 모든 텍스트를 제거하는 시나리오에 대해 다른 접근 방식을 사용하는 것이 좋습니다.

다음 코드 스니펫은 이 작업을 빠르게 해결하는 방법을 보여줍니다.