---
title: PDF에서 텍스트 대체 
linktitle: PDF에서 텍스트 대체
type: docs
weight: 40
url: ko/java/replace-text-in-a-pdf-document/
description: PDF에서 텍스트를 대체하고 제거하는 다양한 방법에 대해 알아보세요. Aspose.PDF는 특정 영역에서 또는 정규 표현식을 사용하여 텍스트를 대체할 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서의 모든 페이지에서 텍스트 대체하기

{{% alert color="primary" %}}

Aspose.PDF를 사용하여 문서에서 텍스트를 찾고 대체하며, [이 링크](https://products.aspose.app/pdf/redaction)에서 온라인으로 결과를 확인할 수 있습니다.

{{% /alert %}}

[Aspose.PDF for Java](https://products.aspose.com/pdf/java)를 사용하여 PDF 문서의 모든 페이지에서 텍스트를 대체하려면:

1. 먼저 [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber)를 사용하여 대체할 특정 문구를 찾습니다.

1. 그런 다음 모든 [TextFragments](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber#getTextFragments--)를 통해 텍스트를 교체하고 다른 속성을 변경합니다.
1. 마지막으로 Document 클래스의 [save](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save--) 메서드를 사용하여 출력 PDF를 저장합니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleReplaceText {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void ReplaceTextOnAllPages() {
        Document pdfDocument = new Document(_dataDir+"sample.pdf");

        // 입력 검색 구문의 모든 인스턴스를 찾기 위해 TextAbsorber 객체를 생성합니다
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Web");
        
        // 문서의 첫 페이지에 대해 흡수기를 허용합니다
        pdfDocument.getPages().accept(textFragmentAbsorber);
        
        // 추출된 텍스트 조각을 컬렉션에 가져옵니다
        TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
        
        // 조각을 반복합니다
        for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
            // 텍스트 및 기타 속성을 업데이트합니다
            textFragment.setText("World Wide Web");
            textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setForegroundColor(Color.getBlue());
            textFragment.getTextState().setBackgroundColor(Color.getGray());
        }
        // 업데이트된 PDF 파일을 저장합니다
        pdfDocument.save(_dataDir+"Updated_Text.pdf");
    }
}
```


## 특정 페이지 영역의 텍스트 교체

특정 페이지 영역의 텍스트를 교체하기 위해서는 먼저 TextFragmentAbsorber 객체를 생성하고, [TextSearchOptions.setRectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextSearchOptions#setRectangle-com.aspose.pdf.Rectangle-)을 사용하여 페이지 영역을 지정한 다음 모든 TextFragment를 반복하여 텍스트를 교체해야 합니다. 이러한 작업이 완료되면 Document 객체의 save 메서드를 사용하여 출력 PDF를 저장하기만 하면 됩니다.

다음 코드 조각은 PDF 문서의 모든 페이지에서 텍스트를 교체하는 방법을 보여줍니다.

```java
 public static void ReplaceTextInParticularRegion(){
    // PDF 파일 로드
    Document pdfDocument = new Document(_dataDir+"sample.pdf");

    // TextFragment Absorber 객체 생성
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("PDF");

    // 페이지 경계 내에서 텍스트 검색
    textFragmentAbsorber.getTextSearchOptions().setLimitToPageBounds(true);

    // TextSearch 옵션에 대한 페이지 영역 지정
    textFragmentAbsorber.getTextSearchOptions().setRectangle(new Rectangle(100, 700, 400, 770));

    // PDF 파일의 첫 번째 페이지에서 텍스트 검색
    pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);

    // 개별 TextFragment 반복
    for(TextFragment tf : textFragmentAbsorber.getTextFragments())
    {
        // 텍스트를 "---"로 교체
        tf.setText("---");
    }

    // 업데이트된 PDF 파일 저장
    pdfDocument.save(_dataDir+"Updated_Text.pdf");
}
```


## 정규 표현식을 기반으로 텍스트 교체

정규 표현식을 기반으로 일부 구문을 교체하려면, 먼저 TextFragmentAbsorber를 사용하여 해당 정규 표현식과 일치하는 모든 구문을 찾아야 합니다. 정규 표현식을 TextFragmentAbsorber 생성자의 매개변수로 전달해야 합니다. 또한 정규 표현식이 사용되고 있는지를 지정하는 TextSearchOptions 객체를 생성해야 합니다. TextFragments에서 일치하는 구문을 얻은 후, 모든 구문을 반복하여 필요에 따라 업데이트해야 합니다. 마지막으로 Document 객체의 Save 메서드를 사용하여 업데이트된 PDF를 저장해야 합니다.

다음 코드 스니펫은 정규 표현식을 기반으로 텍스트를 교체하는 방법을 보여줍니다.

```java
public static void ReplaceTextWithRegularExpression() {
    // PDF 파일 로드
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    // 입력 검색 구문의 모든 인스턴스를 찾기 위해 TextAbsorber 객체 생성
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); 
    // 예: 1999-2000

    // 정규 표현식 사용을 지정하기 위해 텍스트 검색 옵션 설정
    TextSearchOptions textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(textSearchOptions);

    // 문서의 첫 페이지에 대해 Absorber 적용
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // 추출된 텍스트 조각을 컬렉션으로 가져옴
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

    // 조각을 반복 처리
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // 텍스트 및 기타 속성 업데이트
        textFragment.setText("ABCD-EFGH");
        textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
    }

    // 업데이트된 PDF 파일 저장
    pdfDocument.save(_dataDir + "Updated_Text.pdf");
}
```


## 기존 PDF 파일에서 폰트 교체

Aspose.PDF for Java는 PDF 문서에서 텍스트를 교체할 수 있는 기능을 지원합니다. 하지만 때로는 PDF 문서 내부에서 사용되는 폰트만 교체해야 하는 요구 사항이 있을 수 있습니다. 따라서 텍스트를 교체하는 대신 사용되는 폰트만 교체됩니다. TextFragmentAbsorber 생성자의 오버로드 중 하나는 TextEditOptions 객체를 인수로 받아들이며, 우리는 우리의 요구사항을 달성하기 위해 TextEditOptions.FontReplace 열거형에서 RemoveUnusedFonts 값을 사용할 수 있습니다.

다음 코드 스니펫은 PDF 문서 내부의 폰트를 교체하는 방법을 보여줍니다.

```java
public static void ReplaceFonts() {
    // Document 객체 인스턴스화
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // 텍스트 조각을 검색하고 편집 옵션을 사용되지 않는 폰트 제거로 설정
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(
            new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

    // 문서의 모든 페이지에 대한 absorber 수락
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // 모든 TextFragment를 순회
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection)
    {
        String fontName = textFragment.getTextState().getFont().getFontName();
        // 폰트 이름이 ArialMT이면 폰트 이름을 Arial로 교체
        if (fontName.equals("ArialMT")) {
            textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        }
    }

    // 업데이트된 PDF 파일 저장
    pdfDocument.save(_dataDir + "Updated_Text.pdf");
}
```


### 텍스트를 대체할 때 비영어(일본어) 폰트 사용

다음 코드 스니펫은 일본어 문자로 텍스트를 대체하는 방법을 보여줍니다. 일본어 텍스트를 추가하려면 일본어 문자를 지원하는 폰트(MSGothic 등)를 사용해야 합니다.

```java
public static void UseNonEnglishFontWhenReplacingText() {

    // Document 객체 인스턴스화
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // 모든 "page" 단어를 특정 폰트를 사용하여 일부 일본어 텍스트로 변경
    // 운영체제에 설치될 수 있는 TakaoMincho
    // 또한, 상형문자를 지원하는 다른 폰트일 수도 있음
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("page");

    // 텍스트 검색 옵션의 인스턴스 생성
    TextSearchOptions searchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(searchOptions);

    // 문서의 모든 페이지에 대해 흡수기 적용
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // 추출된 텍스트 조각을 컬렉션에 가져오기
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
    
    // 조각을 순회
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // 텍스트 및 기타 속성 업데이트
        textFragment.setText("ファイル");
        textFragment.getTextState().setFont(FontRepository.findFont("MSGothic"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
    }
    // 업데이트된 문서 저장
    pdfDocument.save(_dataDir + "Japanese_Text.pdf");
}
```


## 텍스트 교체는 페이지 내용을 자동으로 재배열해야 합니다

Aspose.PDF for Java는 PDF 파일 내에서 텍스트를 검색하고 교체하는 기능을 지원합니다. 하지만 최근 일부 고객들은 특정 TextFragment가 더 작은 내용으로 교체될 때 결과 PDF에 여분의 공백이 표시되거나 TextFragment가 더 긴 문자열로 교체될 때 단어가 기존 페이지 내용과 겹치는 문제를 겪었습니다. 따라서 PDF 문서 내의 텍스트가 교체되면 내용이 재배열되어야 한다는 요구가 있었습니다.

위에서 설명한 시나리오를 해결하기 위해, Aspose.PDF for Java는 PDF 파일 내에서 텍스트를 교체할 때 이러한 문제가 발생하지 않도록 개선되었습니다. 다음 코드 스니펫은 PDF 파일 내의 텍스트를 교체하고 페이지 내용이 자동으로 재배열되도록 하는 방법을 보여줍니다.

```java
public static void RearrangeContent() {
    // 소스 PDF 파일 불러오기
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // 정규 표현식으로 TextFragment Absorber 객체 생성
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[PDF,Web]");

    TextSearchOptions textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
    
    // 교체 후 현재 행이 너무 길거나 짧아질 경우 다음 또는 현재 행에서 텍스트를 줄바꿈하기 위해 ReplaceAdjustment.WholeWordsHyphenation 옵션을 지정할 수도 있습니다:
    //textFragmentAbsorber.getTextReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.WholeWordsHyphenation);

    // 문서의 모든 페이지에 대해 absorber를 수락
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // 추출된 텍스트 조각을 컬렉션으로 가져오기
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

    // 각 TextFragment 교체
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // 교체할 텍스트 조각의 글꼴 설정
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        // 글꼴 크기 설정
        textFragment.getTextState().setFontSize(10);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
        // 자리 표시자보다 큰 문자열로 텍스트 교체
        textFragment.setText("This is a larger string for the testing of this feature");
    }
    // 결과 PDF 저장
    pdfDocument.save(_dataDir + "RearrangeContentsUsingTextReplacement_out.pdf");
}
```


## PDF 생성 중 교체 가능한 기호 렌더링

교체 가능한 기호는 실행 시점에 해당 내용으로 대체될 수 있는 텍스트 문자열의 특수 기호입니다. 현재 Aspose.PDF 네임스페이스의 새로운 Document Object Model에서 지원하는 교체 가능한 기호는 `$P`, `$p`, `\n`, `\r`입니다. `$p`와 `$P`는 실행 시점의 페이지 번호를 처리하는 데 사용됩니다. `$p`는 현재 Paragraph 클래스가 있는 페이지의 번호로 대체됩니다. `$P`는 문서의 총 페이지 수로 대체됩니다. PDF 문서의 단락 컬렉션에 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXFragment)를 추가할 때 텍스트 내의 줄 바꿈을 지원하지 않습니다. 그러나 줄 바꿈이 있는 텍스트를 추가하려면 [TextParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextParagraph)와 함께 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXFragment)를 사용하십시오:

- 단일 "\n" 대신 TextFragment에서 "\r\n" 또는 Environment.NewLine을 사용하십시오;
- TextParagraph 객체를 생성하십시오.
 텍스트를 줄 바꿈으로 추가합니다;
- TextFragment를 TextParagraph.AppendLine으로 추가합니다;
- TextParagraph를 TextBuilder.AppendParagraph로 추가합니다.

```java
public static void RenderingReplaceableSymbols() {
    // PDF 파일 로드
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    Page page = pdfDocument.getPages().add();

    // 필요한 줄 바꿈 마커가 포함된 텍스트로 새로운 TextFragment 초기화
    TextFragment textFragment = new TextFragment("Applicant Name: " + System.lineSeparator() + " Joe Smoe");

    // 필요한 경우 텍스트 조각 속성 설정
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());

    // TextParagraph 객체 생성
    TextParagraph par = new TextParagraph();

    // 새로운 TextFragment를 단락에 추가
    par.appendLine(textFragment);

    // 단락 위치 설정
    par.setPosition (new Position(100, 600));

    // TextBuilder 객체 생성
    TextBuilder textBuilder = new TextBuilder(page);
    // TextBuilder를 사용하여 TextParagraph 추가
    textBuilder.appendParagraph(par);

    _dataDir = _dataDir + "RenderingReplaceableSymbols_out.pdf";
    pdfDocument.save(_dataDir);
}
```

## 머리글/바닥글 영역의 대체 가능한 기호

대체 가능한 기호는 PDF 파일의 머리글/바닥글 섹션에 배치될 수도 있습니다. 바닥글 섹션에 대체 가능한 기호를 추가하는 방법에 대한 자세한 내용은 다음 코드 스니펫을 참조하십시오.

```java
public static void ReplaceableSymbolsInHeaderFooterArea() {
    Document doc = new Document();
    Page page = doc.getPages().add();

    MarginInfo marginInfo = new MarginInfo();
    marginInfo.setTop(90);
    marginInfo.setBottom(50);
    marginInfo.setLeft(50);
    marginInfo.setRight(50);

    // marginInfo 인스턴스를 sec1.PageInfo의 Margin 속성에 할당합니다.
    page.getPageInfo().setMargin(marginInfo);

    HeaderFooter hfFirst = new HeaderFooter();
    page.setHeader(hfFirst);
    hfFirst.getMargin().setLeft(50);
    hfFirst.getMargin().setRight(50);

    // 머리글로 표시할 내용을 저장할 텍스트 단락을 인스턴스화합니다.
    TextFragment t1 = new TextFragment("report title");
    t1.getTextState().setFont(FontRepository.findFont("Arial"));
    t1.getTextState().setFontSize(16);
    t1.getTextState().setForegroundColor(Color.getBlack());
    t1.getTextState().setFontStyle(FontStyles.Bold);
    t1.getTextState().setHorizontalAlignment(HorizontalAlignment.Center);
    t1.getTextState().setLineSpacing(5f);
    hfFirst.getParagraphs().add(t1);

    TextFragment t2 = new TextFragment("Report_Name");
    t2.getTextState().setFont(FontRepository.findFont("Arial"));
    t2.getTextState().setForegroundColor(Color.getBlack());
    t2.getTextState().setHorizontalAlignment(HorizontalAlignment.Center);
    t2.getTextState().setLineSpacing(5f);
    t2.getTextState().setFontSize(12);
    hfFirst.getParagraphs().add(t2);

    // 섹션용 HeaderFooter 객체를 생성합니다.
    HeaderFooter hfFoot = new HeaderFooter();

    // HeaderFooter 객체를 홀수 및 짝수 바닥글로 설정합니다.
    page.setFooter(hfFoot);
    hfFoot.getMargin().setLeft(50);
    hfFoot.getMargin().setRight(50);

    // 전체 페이지 수의 현재 페이지 번호를 포함하는 텍스트 단락을 추가합니다.
    TextFragment t3 = new TextFragment("Generated on test date");
    TextFragment t4 = new TextFragment("report name ");
    TextFragment t5 = new TextFragment("Page $p of $P");

    // 테이블 객체를 인스턴스화합니다.
    Table tab2 = new Table();

    // 원하는 섹션의 단락 컬렉션에 테이블을 추가합니다.
    hfFoot.getParagraphs().add(tab2);

    // 테이블의 열 너비를 설정합니다.
    tab2.setColumnWidths("165 172 165");

    // 테이블에 행을 만들고 행에 셀을 추가합니다.
    Row row3 = tab2.getRows().add();

    row3.getCells().add();
    row3.getCells().add();
    row3.getCells().add();

    // 텍스트의 수직 정렬을 가운데로 설정합니다.
    row3.getCells().get_Item(0).setAlignment(HorizontalAlignment.Left);
    row3.getCells().get_Item(1).setAlignment(HorizontalAlignment.Center);
    row3.getCells().get_Item(2).setAlignment(HorizontalAlignment.Right);

    row3.getCells().get_Item(0).getParagraphs().add(t3);
    row3.getCells().get_Item(1).getParagraphs().add(t4);
    row3.getCells().get_Item(2).getParagraphs().add(t5);

    Table table = new Table();

    table.setColumnWidths("33% 33% 34%");
    table.setDefaultCellPadding(new MarginInfo());
    table.getDefaultCellPadding().setTop(10);
    table.getDefaultCellPadding().setBottom(10);

    // 원하는 섹션의 단락 컬렉션에 테이블을 추가합니다.
    page.getParagraphs().add(table);

    // BorderInfo 객체를 사용하여 기본 셀 테두리를 설정합니다.
    table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1f));

    // 또 다른 사용자 정의 BorderInfo 객체를 사용하여 테이블 테두리를 설정합니다.
    table.setBorder(new BorderInfo(BorderSide.All, 1f));

    table.setRepeatingRowsCount(1);

    // 테이블에 행을 만들고 행에 셀을 추가합니다.
    Row row1 = table.getRows().add();

    row1.getCells().add("col1");
    row1.getCells().add("col2");
    row1.getCells().add("col3");
    String CRLF = "\r\n";

    for (int i = 0; i <= 10; i++) {
        Row row = table.getRows().add();
        row.setRowBroken(true);
        for (int c = 0; c <= 2; c++) {
            Cell c1;
            if (c == 2)
                c1 = row.getCells().add(
                        "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a"
                                + CRLF
                                + "daily basis to ensure it contains the most up to date versions of each of our Java components. "
                                + CRLF
                                + "daily basis to ensure it contains the most up to date versions of each of our Java components. "
                                + CRLF
                                + "Using Aspose.Total for Java developers can create a wide range of applications.");
            else
                c1 = row.getCells().add("item1" + c);
            c1.setMargin(new MarginInfo());
            c1.getMargin().setLeft(30);
            c1.getMargin().setTop(10);
            c1.getMargin().setBottom(10);
        }
    }

    _dataDir = _dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
    doc.save(_dataDir);
}
```


## PDF 문서에서 모든 텍스트 제거

### 연산자를 사용하여 모든 텍스트 제거

일부 텍스트 작업에서는 PDF 문서에서 모든 텍스트를 제거해야 하며, 이를 위해 찾은 텍스트를 빈 문자열 값으로 설정해야 합니다. 문제는 다수의 텍스트 조각의 텍스트를 변경하는 것이 여러 검토 및 텍스트 위치 조정 작업을 유발한다는 점입니다. 이러한 작업은 텍스트 편집 시나리오에서 필수적입니다. 루프에서 처리되는 시나리오에서는 얼마나 많은 텍스트 조각이 제거될지 알 수 없다는 점이 어려움입니다.

따라서 PDF 페이지에서 모든 텍스트를 제거하는 시나리오에서는 다른 접근 방식을 사용할 것을 권장합니다. 다음의 매우 빠르게 작동하는 코드 스니펫을 고려해 보십시오.

```java
public static void RemoveAllTextUsingOperators() {
    // 문서 열기
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // PDF 문서의 모든 페이지를 순회
    for (int i = 1; i <= pdfDocument.getPages().size(); i++) {
        Page page = pdfDocument.getPages().get_Item(i);
        OperatorSelector operatorSelector = new OperatorSelector(new com.aspose.pdf.operators.TextShowOperator());
        // 페이지의 모든 텍스트 선택
        page.getContents().accept(operatorSelector);
        // 모든 텍스트 삭제
        page.getContents().delete(operatorSelector.getSelected());
    }
    // 문서 저장
    pdfDocument.save(_dataDir + "RemoveAllText_out.pdf");
}
```