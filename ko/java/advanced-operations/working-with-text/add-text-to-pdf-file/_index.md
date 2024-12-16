---
title: PDF 파일에 텍스트 추가
linktitle: PDF 파일에 텍스트 추가
type: docs
weight: 10
url: /ko/java/add-text-to-pdf-file/
description: 이 문서는 Aspose.PDF에서 텍스트 작업의 다양한 측면을 설명합니다. PDF에 텍스트를 추가하고, HTML 조각을 추가하거나, 사용자 정의 OTF 글꼴을 사용하는 방법을 배웁니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

기존 PDF 파일에 텍스트를 추가하려면:

1. Document 객체를 사용하여 입력 PDF를 엽니다.
2. 텍스트를 추가하려는 특정 페이지를 가져옵니다.
3. 입력 텍스트와 기타 텍스트 속성과 함께 TextFragment 객체를 생성합니다. 텍스트를 추가하려는 특정 페이지에서 생성된 TextBuilder 객체는 AppendText 메서드를 사용하여 TextFragment 객체를 페이지에 추가할 수 있게 합니다.
4. Document 객체의 Save 메서드를 호출하여 출력 PDF 파일을 저장합니다.

## 텍스트 추가

다음 코드 스니펫은 기존 PDF 파일에 텍스트를 추가하는 방법을 보여줍니다.

```java
public static void AddingText() {
    // PDF 파일 로드
    Document document = new Document(_dataDir + "sample.pdf");

    // 특정 페이지 가져오기
    Page pdfPage = document.getPages().get_Item(1);
    // 텍스트 조각 생성
    TextFragment textFragment = new TextFragment("Aspose.PDF");
    textFragment.setPosition(new Position(80, 700));

    // 텍스트 속성 설정
    textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
    textFragment.getTextState().setFontSize(14);
    textFragment.getTextState().setForegroundColor(Color.getBlue());
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());

    // TextBuilder 객체 생성
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // PDF 페이지에 텍스트 조각 추가
    textBuilder.appendText(textFragment);

    // 결과 PDF 문서 저장
    document.save(_dataDir + "AddText_out.pdf");
}
```


## 스트림에서 폰트 로드

다음 코드 스니펫은 PDF 문서에 텍스트를 추가할 때 스트림 객체에서 폰트를 로드하는 방법을 보여줍니다.

```java
import com.aspose.pdf.*;
import com.aspose.pdf.text.FontTypes;

import java.io.FileInputStream;
import java.io.FileNotFoundException;  
//...
public static void LoadingFontFromStream() throws FileNotFoundException{
    
    String fontFile = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf";

    // 입력 PDF 파일 로드
    Document doc = new Document(_dataDir + "input.pdf");
    // 문서의 첫 페이지에 대한 텍스트 빌더 객체 생성
    TextBuilder textBuilder = new TextBuilder(doc.getPages().get_Item(1));
    // 샘플 문자열로 텍스트 조각 생성
    TextFragment textFragment = new TextFragment("Hello world");
    
    if (fontFile != "")
    {
        // 스트림 객체에 트루타입 폰트 로드
        FileInputStream fontStream=new FileInputStream(fontFile);            
        // 텍스트 문자열에 대한 폰트 이름 설정
        textFragment.getTextState().setFont (FontRepository.openFont(fontStream, FontTypes.TTF));
        // 텍스트 조각의 위치 지정
        textFragment.setPosition(new Position(10, 10));
        // 텍스트를 TextBuilder에 추가하여 PDF 파일 위에 배치할 수 있도록 함
        textBuilder.appendText(textFragment);
        
        _dataDir = _dataDir + "LoadingFontFromStream_out.pdf";
    
        // 결과 PDF 문서를 저장합니다.
        doc.save(_dataDir); 
    }       
}
```


## TextParagraph를 사용하여 텍스트 추가

다음 코드 스니펫은 [TextParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextParagraph) 클래스를 사용하여 PDF 문서에 텍스트를 추가하는 방법을 보여줍니다.

```java
public static void AddTextUsingTextParagraph() {
    // 문서 열기
    Document doc = new Document();
    // Document 객체의 페이지 컬렉션에 페이지 추가
    Page page = doc.getPages().add();
    TextBuilder builder = new TextBuilder(page);
    // 텍스트 단락 생성
    TextParagraph paragraph = new TextParagraph();
    // 후속 줄 들여쓰기 설정
    paragraph.setSubsequentLinesIndent (20);
    // TextParagraph를 추가할 위치 지정
    paragraph.setRectangle(new Rectangle(100, 300, 200, 700));
    // 단어 줄 바꿈 모드 지정
    paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
    // 텍스트 조각 생성
    TextFragment fragment1 = new TextFragment("the quick brown fox jumps over the lazy dog");
    fragment1.getTextState().setFont (FontRepository.findFont("Times New Roman"));
    fragment1.getTextState().setFontSize (12);
    // 단락에 조각 추가
    paragraph.appendLine(fragment1);
    // 단락 추가
    builder.appendParagraph(paragraph);

    _dataDir = _dataDir + "AddTextUsingTextParagraph_out.pdf";

    // 결과 PDF 문서 저장
    doc.save(_dataDir);        
}
```


## 텍스트 세그먼트에 하이퍼링크 추가

PDF 페이지는 하나 이상의 TextFragment 객체로 구성될 수 있으며, 각 TextFragment 객체는 하나 이상의 TextSegment 인스턴스를 가질 수 있습니다. TextSegment에 하이퍼링크를 설정하기 위해서는 Aspose.Pdf.WebHyperlink 인스턴스의 객체를 제공하면서 TextSegment 클래스의 Hyperlink 속성을 사용할 수 있습니다. 이 요구 사항을 충족시키기 위해 다음의 코드 스니펫을 사용해 보십시오.

```java
public static void AddHyperlinkToTextSegment() {
    // 문서 인스턴스 생성
    Document doc = new Document();
    // PDF 파일의 페이지 컬렉션에 페이지 추가
    Page page1 = doc.getPages().add();

    // TextFragment 인스턴스 생성
    TextFragment tf = new TextFragment("샘플 텍스트 프래그먼트");
    // TextFragment의 수평 정렬 설정
    tf.setHorizontalAlignment(HorizontalAlignment.Right);

    // 샘플 텍스트로 텍스트 세그먼트 생성
    TextSegment segment = new TextSegment(" ... 텍스트 세그먼트 1...");
    // TextFragment의 세그먼트 컬렉션에 세그먼트 추가
    tf.getSegments().add(segment);

    // 새로운 TextSegment 생성
    segment = new TextSegment("구글로 링크");
    // TextFragment의 세그먼트 컬렉션에 세그먼트 추가

    tf.getSegments().add(segment);

    // TextSegment에 하이퍼링크 설정
    segment.setHyperlink(new com.aspose.pdf.WebHyperlink("www.aspose.com"));

    // 텍스트 세그먼트의 전경색 설정
    segment.getTextState().setForegroundColor(com.aspose.pdf.Color.getBlue());

    // 텍스트 서식을 이탤릭체로 설정
    segment.getTextState().setFontStyle(FontStyles.Italic);

    // 또 다른 TextSegment 객체 생성
    segment = new TextSegment("하이퍼링크 없는 텍스트 세그먼트");

    // TextFragment의 세그먼트 컬렉션에 세그먼트 추가
    tf.getSegments().add(segment);

    // 페이지 객체의 문단 컬렉션에 TextFragment 추가
    page1.getParagraphs().add(tf);

    _dataDir = _dataDir + "AddHyperlinkToTextSegment_out.pdf";

    // 결과 PDF 문서 저장.
    doc.save(_dataDir);

}
```


## OTF 폰트 사용

Aspose.PDF for Java는 PDF 파일 내용을 생성/조작할 때 기본 시스템 폰트가 아닌 다른 내용으로 표시되도록 사용자 지정/트루타입 폰트를 사용할 수 있는 기능을 제공합니다. Aspose.PDF for Java 10.4.0 버전부터 Open Type Fonts에 대한 지원을 제공합니다.

```java
public static void UseOTFFont() {
    // 새로운 문서 인스턴스 생성
    Document pdfDocument = new Document();
    // PDF 파일의 페이지 컬렉션에 페이지 추가
    Page page = pdfDocument.getPages().add();
    // 샘플 텍스트로 TextFragment 인스턴스 생성
    TextFragment fragment = new TextFragment("OTF 폰트의 샘플 텍스트");
    // 시스템 디렉토리에 있는 OTF 폰트의 경로를 지정할 수도 있습니다.
    fragment.getTextState().setFont(FontRepository.openFont("/home/aspose/.fonts/Montserrat-Black.otf"));
    // PDF 파일 내에 폰트를 포함하도록 지정하여,
    // 특정 폰트가 대상 기계에 설치되지 않더라도 올바르게 표시되도록 합니다.
    fragment.getTextState().getFont().setEmbedded(true);
    // 페이지 인스턴스의 단락 컬렉션에 TextFragment 추가
    page.getParagraphs().add(fragment);
    // 결과 PDF 문서 저장
    pdfDocument.save(_dataDir + "OTFFont_out.pdf");
}
```


## DOM을 사용하여 HTML 문자열 추가하기

Aspose.Pdf.Generator.Text 클래스에는 IsHtmlTagSupported라는 속성이 있으며, 이 속성은 PDF 파일에 HTML 태그/컨텐츠를 추가할 수 있게 합니다. 추가된 컨텐츠는 단순한 텍스트 문자열로 나타나는 대신 본래의 HTML 태그로 렌더링됩니다. Aspose.Pdf 네임스페이스의 새로운 문서 개체 모델(DOM)에서 유사한 기능을 지원하기 위해 HtmlFragment 클래스가 도입되었습니다.

[HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlFragment) 인스턴스를 사용하여 PDF 파일 내부에 배치할 HTML 컨텐츠를 지정할 수 있습니다. TextFragment와 유사하게 HtmlFragment는 단락 수준의 객체이며 페이지 객체의 단락 모음에 추가할 수 있습니다. 다음 코드 스니펫은 DOM 접근 방식을 사용하여 PDF 파일 내부에 HTML 컨텐츠를 배치하는 단계를 보여줍니다.

```java
public static void AddingHtmlString() {
    // Document 객체 인스턴스화
    Document doc = new Document();
    // PDF 파일의 페이지 모음에 페이지 추가
    Page page = doc.getPages().add();
    // HTML 컨텐츠로 HtmlFragment 인스턴스화
    HtmlFragment title = new HtmlFragment("<h1 style=\"color:blue\"><strong>HTML 문자열 데모</strong></h1>");
    // 여백 세부사항을 위한 MarginInfo 설정
    MarginInfo Margin = new MarginInfo();
    Margin.setBottom(10);
    Margin.setTop(200);
    // 여백 정보 설정
    title.setMargin(Margin);
    // 페이지의 단락 모음에 HTML Fragment 추가
    page.getParagraphs().add(title);
    // PDF 파일 저장
    doc.save(_dataDir + "sample_html_out.pdf");
}
```


다음 코드 스니펫은 문서에 HTML 순서 목록을 추가하는 방법을 보여줍니다:

```java
public static void AddHTMLOrderedListIntoDocuments() {
    // Document 객체 인스턴스화
    Document doc = new Document();
    // 관련 HTML 조각으로 HtmlFragment 객체 인스턴스화
    HtmlFragment t = new HtmlFragment(
            "<div style=\"font-family: sans-serif\"><ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li><li>Fifth</li></ul><p>Text after the list.</p><p>Next line<br/>Last line</p></div>");
    // Pages 컬렉션에 페이지 추가
    Page page = doc.getPages().add();
    // 페이지 안에 HtmlFragment 추가
    page.getParagraphs().add(t);
    // 결과 PDF 파일 저장
    doc.save(_dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf");
}
```

다음과 같이 TextState 객체를 사용하여 HTML 문자열 서식을 설정할 수도 있습니다:

```java
public static void AddHTMLStringFormatting() {
    // Document 객체 인스턴스화
    Document doc = new Document();
    // PDF 파일의 페이지 컬렉션에 페이지 추가
    Page page = doc.getPages().add();
    // HTML 내용을 가진 HtmlFragment 인스턴스화
    HtmlFragment title = new HtmlFragment("<h1><strong>HTML String Demo</strong></h1>");
    TextState textState = new TextState(12);
    textState.setFont(FontRepository.findFont("Calibri"));
    textState.setForegroundColor(Color.getGreen());
    textState.setBackgroundColor(Color.getCoral());
    title.setTextState(textState);

    // 페이지의 단락 컬렉션에 HTML 조각 추가
    page.getParagraphs().add(title);
    // PDF 파일 저장
    doc.save(_dataDir + "sample_html_out.pdf");
}
```


일부 텍스트 속성 값을 HTML 마크업을 통해 설정한 후, 동일한 값을 TextState 속성에서 제공하면 TextState 인스턴스의 속성 형식으로 HTML 매개변수를 덮어쓰게 됩니다. 다음 코드 스니펫은 설명된 동작을 보여줍니다.

```java
public static void AddHTMLUsingDOMAndOverwrite() {
    // Document 객체 인스턴스화
    Document doc = new Document();
    // PDF 파일의 페이지 컬렉션에 페이지 추가
    Page page = doc.getPages().add();
    // HTML 콘텐츠로 HtmlFragment 인스턴스화
    HtmlFragment title = new HtmlFragment("<p style='font-family: Verdana'><b><i>Table contains text</i></b></p>");
    // 'Verdana'의 글꼴이 'Arial'로 재설정됩니다
    title.setTextState(new TextState("Arial Black"));
    title.setTextState(new TextState(20));
    // 아래쪽 여백 정보 설정
    title.getMargin().setBottom(10);
    // 위쪽 여백 정보 설정
    title.getMargin().setTop(400);
    // 페이지의 단락 컬렉션에 HTML Fragment 추가
    page.getParagraphs().add(title);
    // PDF 파일 저장
    doc.save(_dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf");
}
```


## 각주 및 미주 (DOM)

각주는 논문 본문의 텍스트에 연속된 위첨자 숫자를 사용하여 주석을 표시합니다. 실제 주석은 들여쓰기되어 페이지 하단에 각주로 나타날 수 있습니다.

### 각주 추가하기

각주 참조 시스템에서는 다음과 같이 참조를 표시합니다:

- 소스 자료 바로 뒤에 작은 숫자를 줄 위에 놓습니다. 이 숫자는 주석 식별자로 불리며, 텍스트 줄 약간 위에 위치합니다.
- 동일한 숫자를 페이지 하단에 소스의 인용과 함께 기재합니다. 각주는 숫자 순서대로, 첫 번째 참조는 1, 두 번째는 2, 계속해서 진행됩니다.

각주의 장점은 독자가 관심 있는 참조의 출처를 쉽게 페이지 아래로 눈을 내려 확인할 수 있다는 것입니다.

다음에 지정된 단계에 따라 각주를 작성하십시오:

- Document 인스턴스를 생성합니다
- Page 객체를 생성합니다
- TextFragment 객체를 생성합니다

- Note 인스턴스를 생성하고 그 값을 TextFragment.FootNote 속성에 전달합니다
- 페이지 인스턴스의 문단 컬렉션에 TextFragment 추가

### 각주에 대한 사용자 지정 선 스타일

다음 예제는 PDF 페이지 하단에 각주를 추가하고 사용자 지정 선 스타일을 정의하는 방법을 보여줍니다.

```java
public static void AddFootNote() {
    // Document 인스턴스 생성
    Document document = new Document(_dataDir + "sample.pdf");

    Page page = document.getPages().get_Item(1);
    TextFragmentAbsorber tfa = new TextFragmentAbsorber("Portable Document Format");
    tfa.visit(page);

    TextFragment t = tfa.getTextFragments().get_Item(1);
    Note note = new Note();
    note.setText("데모");
    t.setFootNote(note);

    // TextFragment 인스턴스 생성
    TextFragment text = new TextFragment("Hello World");
    // TextFragment에 FootNote 값 설정
    text.setFootNote(new Note("테스트 텍스트 1에 대한 각주"));
    // 문서의 첫 번째 페이지에 있는 문단 컬렉션에 TextFragment 추가
    page.getParagraphs().add(text);
    // 두 번째 TextFragment 생성
    text = new TextFragment("Aspose.Pdf for Java");
    // 두 번째 텍스트 조각에 각주 설정
    text.setFootNote(new Note("테스트 텍스트 2에 대한 각주"));
    // PDF 파일의 문단 컬렉션에 두 번째 텍스트 조각 추가
    page.getParagraphs().add(text);

    document.save(_dataDir + "sample_footnote.pdf");
}
```


우리는 다음과 같이 TextState 객체를 사용하여 각주 레이블(참고 식별자) 형식을 설정할 수 있습니다:

```java
public static void AddCustomFootNoteLabel() {
    // Document 인스턴스 생성
    Document document = new Document(_dataDir + "sample.pdf");

    Page page = document.getPages().get_Item(1);
    TextFragmentAbsorber tfa = new TextFragmentAbsorber("Portable Document Format");
    tfa.visit(page);

    TextFragment t = tfa.getTextFragments().get_Item(1);
    Note note = new Note();
    note.setText("Demo");
    t.setFootNote(note);

    // TextFragment 인스턴스 생성
    TextFragment text = new TextFragment("Hello World");
    // TextFragment에 대한 각주 값 설정
    text.setFootNote(new Note("test text 1에 대한 각주"));
    text.getFootNote().setText("21");
    TextState ts = new TextState();
    ts.setForegroundColor(Color.getBlue());
    ts.setFontStyle(FontStyles.Italic);
    text.getFootNote().setTextState(ts);

    // 문서의 첫 페이지의 단락 컬렉션에 TextFragment 추가
    page.getParagraphs().add(text);
    // 두 번째 TextFragment 생성
    text = new TextFragment("Aspose.Pdf for Java");
    // 두 번째 텍스트 조각에 대한 각주 설정
    text.setFootNote(new Note("test text 2에 대한 각주"));
    // PDF 파일의 단락 컬렉션에 두 번째 텍스트 조각 추가
    page.getParagraphs().add(text);

    document.save(_dataDir + "sample_footnote.pdf");
}
```


### 각주 레이블 사용자 지정

기본적으로 각주 번호는 1부터 증가합니다. 그러나 사용자 지정 각주 레이블을 설정해야 하는 경우가 있습니다. 이 요구 사항을 충족하려면 다음 코드 스니펫을 사용해 보세요.

```java
public static void CustomFootNote_Label() {
    // Document 인스턴스 생성
    Document document = new Document();
    // PDF의 페이지 컬렉션에 페이지 추가
    Page page = document.getPages().add();
    // GraphInfo 객체 생성
    GraphInfo graph = new GraphInfo();
    // 선 너비를 2로 설정
    graph.setLineWidth(2);
    // graph 객체의 색상 설정
    graph.setColor(Color.getRed());
    // 대시 배열 값을 3으로 설정
    graph.setDashArray(new int[] { 3 });
    // 대시 위상 값을 1로 설정
    graph.setDashPhase(1);
    // 페이지의 각주 선 스타일을 graph로 설정
    page.setNoteLineStyle(graph);

    // TextFragment 인스턴스 생성
    TextFragment text = new TextFragment("Hello World");
    // TextFragment에 각주 값 설정
    text.setFootNote(new Note("foot note for test text 1"));
    // 각주에 대한 사용자 지정 레이블 지정
    text.getFootNote().setText(" Aspose(2021)");
    // 문서의 첫 번째 페이지의 단락 컬렉션에 TextFragment 추가
    page.getParagraphs().add(text);

    document.save(_dataDir + "CustomizeFootNoteLabel_out.pdf");
}
```


## 이미지 및 테이블을 각주에 추가하기

이전 릴리스 버전에서는 TextFragment 객체에만 각주 지원이 제공되었습니다. 그러나 Aspose.PDF for Java 10.7.0 릴리스부터는 PDF 문서 내의 테이블, 셀 등 다른 객체에도 각주를 추가할 수 있습니다. 다음 코드 스니펫은 TextFragment 객체에 각주를 추가한 다음 각주 섹션의 단락 컬렉션에 이미지 및 테이블 객체를 추가하는 단계를 보여줍니다.

```java
public static void AddingImageAndTableToFootnote() {
    // 문서 인스턴스 생성
    Document document = new Document();
    // PDF의 페이지 컬렉션에 페이지 추가
    Page page = document.getPages().add();
    // TextFragment 인스턴스 생성
    TextFragment text = new TextFragment("Hello World");

    page.getParagraphs().add(text);

    text.setFootNote(new Note());
    Image image = new Image();
    image.setFile(_dataDir + "aspose-logo.jpg");
    image.setFixHeight(20);
    text.getFootNote().getParagraphs().add(image);
    TextFragment footNote = new TextFragment("footnote text");
    footNote.getTextState().setFontSize(20);
    footNote.setInLineParagraph(true);
    text.getFootNote().getParagraphs().add(footNote);
    Table table = new Table();
    table.getRows().add().getCells().add().getParagraphs().add(new TextFragment("Row 1 Cell 1"));
    text.getFootNote().getParagraphs().add(table);

    page.getParagraphs().add(text);

    document.save(_dataDir + "AddImageAndTable_out.pdf");
}
```


## EndNotes 생성 방법

EndNote는 독자에게 논문 끝부분의 특정 위치를 참조하여 논문에서 인용되거나 언급된 정보 또는 단어의 출처를 찾을 수 있도록 하는 출처 인용입니다. 각주를 사용할 때, 인용하거나 패러프레이즈한 문장 또는 요약된 자료 뒤에 위첨자 번호가 따라옵니다.

다음 예제는 Pdf 페이지에 EndNote를 추가하는 방법을 보여줍니다.

```java
public static void HowToCreateEndNotes() {
    Document doc = new Document();
    // PDF의 페이지 컬렉션에 페이지 추가
    Page page = doc.getPages().add();
    // TextFragment 인스턴스 생성
    TextFragment text = new TextFragment("Hello World");
    // TextFragment에 대한 EndNote 값 설정
    text.setEndNote(new Note("sample End note"));
    // FootNote에 대한 사용자 정의 레이블 지정
    text.getEndNote().setText(" Aspose(2021)");
    // 문서의 첫 번째 페이지의 단락 컬렉션에 TextFragment 추가
    page.getParagraphs().add(text);
    // PDF 파일 저장
    doc.save(_dataDir + "EndNote.pdf");
}
```


## 텍스트와 이미지 인라인 문단으로 추가

PDF 파일의 기본 레이아웃은 흐름 레이아웃(상단 왼쪽에서 하단 오른쪽)입니다. 따라서 PDF 파일에 추가되는 모든 새로운 요소는 하단 오른쪽 흐름에 추가됩니다. 그러나 이미지와 텍스트 등 다양한 페이지 요소를 동일한 수준에서 표시해야 할 수도 있습니다(연이어). 한 가지 방법은 테이블 인스턴스를 생성하고 두 요소를 개별 셀 객체에 추가하는 것입니다. 그러나 또 다른 방법은 인라인 문단일 수 있습니다. 이미지와 텍스트의 IsInLineParagraph 속성을 true로 설정하면 이러한 문단이 다른 페이지 요소와 인라인으로 나타납니다.

다음 코드 스니펫은 PDF 파일에 텍스트와 이미지를 인라인 문단으로 추가하는 방법을 보여줍니다.

```java
 public static void TextAndImageAsInLineParagraph() {
    // Document 인스턴스 생성
    Document doc = new Document();
    // Document 인스턴스의 페이지 컬렉션에 페이지 추가
    Page page = doc.getPages().add();
    // TextFragmnet 생성
    TextFragment text = new TextFragment("Hello World.. ");
    // TextFragment를 Page 객체의 문단 컬렉션에 추가
    page.getParagraphs().add(text);
    // 이미지 인스턴스 생성
    Image image = new Image();
    // 이미지를 인라인 문단으로 설정하여
    // 이전 문단 객체(TextFragment) 바로 뒤에 나타나도록 설정
    image.setInLineParagraph (true);
    // 이미지 파일 경로 지정
    image.setFile(_dataDir + "aspose-logo.jpg");
    // 이미지 높이 설정 (선택 사항)
    image.setFixHeight(30);
    // 이미지 너비 설정 (선택 사항)
    image.setFixWidth(100);
    // 페이지 객체의 문단 컬렉션에 이미지 추가
    page.getParagraphs().add(image);
    // 다른 내용으로 TextFragment 객체 재초기화
    text = new TextFragment(" Hello Again..");
    // TextFragment를 인라인 문단으로 설정
    text.setInLineParagraph (true);
    // 새로 생성된 TextFragment를 페이지의 문단 컬렉션에 추가
    page.getParagraphs().add(text);
    
    doc.save(_dataDir+"TextAndImageAsParagraph_out.pdf");
}
```


## 텍스트 추가 시 문자 간격 지정

텍스트는 TextFragment 인스턴스를 사용하거나 TextParagraph 객체를 사용하여 PDF 파일의 단락 모음에 추가할 수 있으며, TextStamp 클래스를 사용하여 PDF 안에 텍스트를 스탬프로 찍을 수도 있습니다. 텍스트를 추가할 때 텍스트 객체에 대한 문자 간격을 지정해야 하는 경우가 있을 수 있습니다. 이 요구 사항을 충족하기 위해 CharacterSpacing이라는 새로운 속성이 도입되었습니다. 이 요구 사항을 충족하는 다음 접근 방식을 참조하십시오.

다음 접근 방식은 PDF 문서 안에 텍스트를 추가할 때 문자 간격을 지정하는 단계를 보여줍니다.

## TextBuilder 및 TextFragment 사용

```java
 public static void CharacterSpacing_TextFragment(){
    // Document 인스턴스 생성
    Document pdfDocument = new Document();
    // 문서의 페이지 컬렉션에 페이지 추가
    Page page = pdfDocument.getPages().add();
    // TextBuilder 인스턴스 생성
    TextBuilder builder = new TextBuilder(page);
    // 샘플 내용으로 텍스트 조각 인스턴스 생성
    TextFragment wideFragment = new TextFragment("문자 간격이 증가된 텍스트");
    wideFragment.getTextState().applyChangesFrom(new TextState("Arial", 12));
    // TextFragment에 대한 문자 간격 지정
    wideFragment.getTextState().setCharacterSpacing(2.0f);
    // TextFragment의 위치 지정
    wideFragment.setPosition(new Position(100, 650));
    // TextBuilder 인스턴스에 TextFragment 추가
    builder.appendText(wideFragment);        
    // 결과 PDF 문서 저장.
    pdfDocument.save(_dataDir+ "CharacterSpacingUsingTextBuilderAndFragment_out.pdf");
}
```


## TextBuilder 및 TextParagraph 사용

```java
public static void CharacterSpacing_TextParagraph() {
    // Document 인스턴스 생성
    Document pdfDocument = new Document();
    // Document의 페이지 컬렉션에 페이지 추가
    Page page = pdfDocument.getPages().add();
    // TextBuilder 인스턴스 생성
    TextBuilder builder = new TextBuilder(page);
    // TextParagraph 인스턴스 생성
    TextParagraph paragraph = new TextParagraph();
    // 폰트 이름과 크기를 지정하기 위해 TextState 인스턴스 생성
    TextState state = new TextState("Arial", 12);
    // 문자 간격 지정
    state.setCharacterSpacing (1.5f);
    // TextParagraph 객체에 텍스트 추가
    paragraph.appendLine("문자 간격이 있는 단락입니다", state);
    // TextParagraph의 위치 지정
    paragraph.setPosition (new Position(100, 550));
    // TextBuilder 인스턴스에 TextParagraph 추가
    builder.appendParagraph(paragraph);
    // 결과 PDF 문서를 저장
    pdfDocument.save(_dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf");
}
```


## 텍스트 스탬프 사용하기

```java
public static void CharacterSpacing_TextStamp() {
    // Document 인스턴스 생성
    Document pdfDocument = new Document();
    // Document의 페이지 컬렉션에 페이지 추가
    Page page = pdfDocument.getPages().add();
    // 샘플 텍스트로 TextStamp 인스턴스화
    TextStamp stamp = new TextStamp("This is text stamp with character spacing");
    // Stamp 객체에 대한 글꼴 이름 지정
    stamp.getTextState().setFont(FontRepository.findFont("Arial"));
    // TextStamp에 대한 글꼴 크기 지정
    stamp.getTextState().setFontSize(12);
    // 문자 간격을 1f로 지정
    stamp.getTextState().setCharacterSpacing (1f);
    // 스탬프의 XIndent 설정
    stamp.setXIndent(100);
    // 스탬프의 YIndent 설정
    stamp.setYIndent(500);
    // 페이지 인스턴스에 텍스트 스탬프 추가
    stamp.put(page);        
    // 결과 PDF 문서를 저장
    pdfDocument.save(_dataDir+"CharacterSpacingUsingTextStamp_out.pdf");        
}
```

## 다중 열 PDF 문서 생성하기

잡지와 신문에서는 뉴스가 책에서처럼 왼쪽에서 오른쪽으로 전체 페이지에 텍스트 단락이 인쇄되는 대신 주로 단일 페이지에 여러 열로 표시됩니다.
 Microsoft Word 및 Adobe Acrobat Writer와 같은 많은 문서 처리 애플리케이션은 사용자가 단일 페이지에 여러 열을 만들고 데이터를 추가할 수 있도록 합니다.

Aspose.PDF for Java는 PDF 문서의 페이지 내에 여러 열을 생성하는 기능도 제공합니다. 다중 열 PDF 파일을 생성하기 위해 Aspose.Pdf.FloatingBox 클래스를 사용할 수 있습니다. 이 클래스는 ColumnInfo.ColumnCount 속성을 제공하여 FloatingBox 내부의 열 수를 지정할 수 있으며, ColumnInfo.ColumnSpacing 및 ColumnInfo.ColumnWidths 속성을 사용하여 열 간격과 열 너비를 각각 지정할 수도 있습니다. FloatingBox는 문서 객체 모델 내의 요소이며 상대적 위치 지정(예: 텍스트, 그래프, 이미지 등)과 비교하여 별도의 위치를 가질 수 있음을 참고하세요.
열 간격은 열 사이의 공간을 의미하며, 기본 열 간격은 1.25cm입니다. 열 너비가 지정되지 않으면 Aspose.PDF for Java는 페이지 크기와 열 간격에 따라 각 열의 너비를 자동으로 계산합니다.

아래 예제는 두 개의 열을 Graphs 객체(Line)로 생성하는 방법을 보여주며, 이 객체들은 FloatingBox의 단락 컬렉션에 추가되고, 이후 Page 인스턴스의 단락 컬렉션에 추가됩니다.

```java
public static void CreateMultiColumn() {
    Document doc = new Document();
    // PDF 파일의 왼쪽 여백 정보 지정
    doc.getPageInfo().getMargin().setLeft(40);
    
    // PDF 파일의 오른쪽 여백 정보 지정
    doc.getPageInfo().getMargin().setRight(40);
    
    Page page = doc.getPages().add();

    com.aspose.pdf.drawing.Graph graph1 = new com.aspose.pdf.drawing.Graph(500, 2);
    
    // 섹션 객체의 단락 컬렉션에 선 추가
    page.getParagraphs().add(graph1);

    // 선의 좌표 지정
    float[] posArr = new float[] { 1, 2, 500, 2 };
    com.aspose.pdf.drawing.Line l1 = new com.aspose.pdf.drawing.Line(posArr);
    graph1.getShapes().add(l1);
    
    // HTML 태그가 포함된 텍스트로 문자열 변수 생성
    String s = "<span style=\"font-family: \"Times New Roman\", Times, serif;\" font-size=\"14pt\" \">"
                +"<strong> How to Steer Clear of money scams</<strong> </span>";
    
    // HTML 텍스트를 포함하는 텍스트 단락 생성

    HtmlFragment heading_text = new HtmlFragment(s);
    page.getParagraphs().add(heading_text);

    FloatingBox box = new FloatingBox();
    
    // 섹션에 네 개의 열 추가
    box.getColumnInfo().setColumnCount(2);
    // 열 사이의 간격 설정
    box.getColumnInfo().setColumnSpacing("5");

    box.getColumnInfo().setColumnWidths("105 105");
    TextFragment text1 = new TextFragment("By A Googler (The Official Google Blog)");
    text1.getTextState().setFontSize (8);
    text1.getTextState().setLineSpacing (2);
    text1.getTextState().setFontSize (10);
    text1.getTextState().setFontStyle (FontStyles.Italic);

    box.getParagraphs().add(text1);
    
    // 선을 그리기 위한 그래프 객체 생성
    com.aspose.pdf.drawing.Graph graph2 = new com.aspose.pdf.drawing.Graph(50, 10);
    // 선의 좌표 지정
    float[] posArr2 = new float[] { 1, 10, 100, 10 };
    com.aspose.pdf.drawing.Line l2 = new com.aspose.pdf.drawing.Line(posArr2);
    graph2.getShapes().add(l2);

    // 섹션 객체의 단락 컬렉션에 선 추가
    box.getParagraphs().add(graph2);

    TextFragment text2 = new TextFragment("Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. "
    +"Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue."
    +"Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur "
    +"ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean "
    +"posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. "
    +"Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, "
    +"risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam "
    +"luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, "
    +"sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, "
    +"pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut,"
    +"iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus "
    +"mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla."
    +"Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam,"
    +"iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique"
    +"ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
    +"Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. "
    +"Praesent porttitor turpis eleifend ante. Morbi sodales.");
    box.getParagraphs().add(text2);

    page.getParagraphs().add(box);

    // PDF 파일 저장
    doc.save(_dataDir + "CreateMultiColumnPdf_out.pdf");        
}
```


## 사용자 정의 탭 정지점 작업

탭 정지점은 탭의 정지 지점입니다. 워드 프로세싱에서 각 줄은 일정한 간격(예: 반 인치마다)으로 배치된 여러 개의 탭 정지점을 포함합니다. 그러나 대부분의 워드 프로세서에서는 원하는 위치에 탭 정지점을 설정할 수 있도록 허용하므로 변경할 수 있습니다. Tab 키를 누르면 커서 또는 삽입 지점이 다음 탭 정지점으로 이동하며, 이는 보이지 않습니다. 탭 정지점은 텍스트 파일에 존재하지 않지만, 워드 프로세서는 Tab 키에 올바르게 반응할 수 있도록 이를 추적합니다.

[Aspose.PDF for Java](https://docs.aspose.com/pdf/java/)는 개발자들이 PDF 문서에서 사용자 정의 탭 정지점을 사용할 수 있도록 합니다. Aspose.Pdf.Text.TabStop 클래스는 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) 클래스에서 사용자 정의 탭 정지점을 설정하는 데 사용됩니다.

[Aspose.PDF for Java](https://docs.aspose.com/pdf/java/)는 또한 TabLeaderType이라는 열거형으로 미리 정의된 몇 가지 탭 리더 유형을 제공합니다. 이의 미리 정의된 값과 설명은 아래와 같습니다.

|**탭 리더 유형**|**설명**|
| :- | :- |
|None|탭 리더 없음|
|Solid|실선 탭 리더|
|Dash|대시 탭 리더|
|Dot|점 탭 리더|

여기 사용자 정의 탭 정지 설정 예제가 있습니다.

```java
public static void CustomTabStops() {
    Document pdfdocument = new Document();
    Page page = pdfdocument.getPages().add();

    com.aspose.pdf.TabStops ts = new com.aspose.pdf.TabStops();
    com.aspose.pdf.TabStop ts1 = ts.add(100);
    ts1.setAlignmentType(TabAlignmentType.Right);
    ts1.setLeaderType (TabLeaderType.Solid);
    
    com.aspose.pdf.TabStop ts2 = ts.add(200);
    ts2.setAlignmentType(TabAlignmentType.Center);
    ts2.setLeaderType (TabLeaderType.Dash);

    com.aspose.pdf.TabStop ts3 = ts.add(300);
    ts3.setAlignmentType(TabAlignmentType.Left);
    ts3.setLeaderType (TabLeaderType.Dot);

    TextFragment header = new TextFragment("이것은 TAB 정지를 사용하여 테이블을 형성하는 예제입니다", ts);
    TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts);

    TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts);
    TextFragment text2 = new TextFragment("#$TABdata21 ", ts);
    text2.getSegments().add(new TextSegment("#$TAB"));
    text2.getSegments().add(new TextSegment("data22 "));
    text2.getSegments().add(new TextSegment("#$TAB"));
    text2.getSegments().add(new TextSegment("data23"));

    page.getParagraphs().add(header);
    page.getParagraphs().add(text0);
    page.getParagraphs().add(text1);
    page.getParagraphs().add(text2);
    
    pdfdocument.save(_dataDir + "CustomTabStops_out.pdf"); 
}
```


## PDF에 투명 텍스트 추가하는 방법

PDF 파일은 이미지, 텍스트, 그래프, 첨부 파일, 주석 객체를 포함하며, TextFragment를 생성할 때 전경, 배경색 정보뿐만 아니라 텍스트 서식을 설정할 수 있습니다. Aspose.PDF for Java는 알파 색상 채널과 함께 텍스트를 추가하는 기능을 지원합니다. 다음 코드 스니펫은 투명 색상으로 텍스트를 추가하는 방법을 보여줍니다.

```java
  public static void AddTransparentText() {
    // Document 인스턴스 생성
    Document pdfdocument = new Document();
    // PDF 파일의 페이지 컬렉션에 페이지 생성
    Page page = pdfdocument.getPages().add();

    // Graph 객체 생성
    Graph canvas = new Graph(100, 400);
    // 특정 크기의 사각형 인스턴스 생성
    com.aspose.pdf.drawing.Rectangle rect = new com.aspose.pdf.drawing.Rectangle(100, 100, 400, 400);
    // 알파 색상 채널에서 색상 객체 생성
    int alpha = 10;
    int green = 0;
    int red = 100;
    int blue = 0;
    Color alphaColor = Color.fromArgb(alpha, red, green, blue);
    rect.getGraphInfo().setFillColor(alphaColor);
    // 사각형을 Graph 객체의 도형 컬렉션에 추가
    canvas.getShapes().add(rect);
    // Graph 객체를 페이지 객체의 단락 컬렉션에 추가
    page.getParagraphs().add(canvas);
    // Graph 객체의 위치 변경하지 않도록 설정
    canvas.setChangePosition(false);

    // 샘플 값으로 TextFragment 인스턴스 생성
    TextFragment text = new TextFragment(
            "transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text ");
    // 알파 채널에서 색상 객체 생성
    alpha = 30;
    alphaColor = Color.fromArgb(alpha, red, green, blue);
    // 텍스트 인스턴스에 색상 정보 설정
    text.getTextState().setForegroundColor (alphaColor);
    // 페이지 인스턴스의 단락 컬렉션에 텍스트 추가
    page.getParagraphs().add(text);
    
    pdfdocument.save(_dataDir + "AddTransparentText_out.pdf");
}
```


## 글꼴의 줄 간격 지정

모든 글꼴에는 추상적인 사각형이 있으며, 그 높이는 동일한 글꼴 크기의 유형 사이의 줄 간격을 나타냅니다. 이 사각형은 `em square`라고 불리며, 글리프 윤곽이 정의되는 디자인 그리드입니다. 입력 글꼴의 많은 문자는 글꼴의 `em square` 경계를 벗어난 곳에 포인트가 배치되어 있으므로, 글꼴을 올바르게 표시하기 위해서는 특별한 설정의 사용이 필요합니다. 객체 TextFragment는 [TextState.getFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentState#getFormattingOptions--) 메소드를 통해 접근할 수 있는 텍스트 서식 옵션 세트를 가지고 있습니다. 이 메소드는 [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions) 클래스를 반환합니다.
 이 클래스에는 특정 글꼴을 위해 설계된 열거형 [LineSpacingMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions.LineSpacingMode)가 있습니다. 예를 들어 입력 글꼴 "HPSimplified.ttf"가 있습니다. 또한 클래스 [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions)에는 LineSpacingMode 유형의 메소드 [setLineSpacing](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions#setLineSpacing-int-)가 있습니다. 그냥 LineSpacing을 LineSpacingMode.FullSize로 설정하면 됩니다. 글꼴이 올바르게 표시되도록 하는 코드 스니펫은 다음과 같습니다:

```java
public static void SpecifyLineSpacingForFonts() {
    String fontFile = _dataDir + "hp-simplified.ttf";
    // 입력 PDF 파일 로드
    Document doc = new Document();
    // LineSpacingMode.FullSize로 TextFormattingOptions 생성
    TextFormattingOptions formattingOptions = new TextFormattingOptions();
    formattingOptions.setLineSpacing(TextFormattingOptions.LineSpacingMode.FullSize);

    // 문서의 첫 페이지에 대한 텍스트 빌더 객체 생성
    // TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
    // 샘플 문자열로 텍스트 조각 생성
    TextFragment textFragment = new TextFragment("Hello world");

    // TrueType 글꼴을 스트림 객체에 로드
    FileInputStream fontStream;
    try {
        fontStream = new FileInputStream(fontFile);
    } catch (FileNotFoundException e) {
        e.printStackTrace();
        return;
    }

    // 텍스트 문자열의 글꼴 이름 설정
    textFragment.getTextState().setFont(FontRepository.openFont(fontStream, FontTypes.TTF));
    // 텍스트 조각의 위치 지정
    textFragment.setPosition(new Position(100, 600));
    // 현재 조각의 TextFormattingOptions를 사전 정의된 것으로 설정(이는 LineSpacingMode.FullSize를 가리킴)
    textFragment.getTextState().setFormattingOptions(formattingOptions);
    // 텍스트를 TextBuilder에 추가하여 PDF 파일 위에 배치할 수 있도록 함
    // textBuilder.AppendText(textFragment);
    Page page = doc.getPages().add();
    page.getParagraphs().add(textFragment);

    // 결과 PDF 문서 저장
    doc.save(_dataDir + "SpecifyLineSpacing_out.pdf");
}
```

## 텍스트 너비 동적으로 가져오기

때때로, 텍스트 너비를 동적으로 가져와야 할 때가 있습니다. Aspose.PDF for Java는 문자열 너비 측정을 위한 두 가지 메서드를 포함하고 있습니다. com.aspose.pdf.Font 또는 com.aspose.pdf.TextState 클래스(또는 둘 다)의 [MeasureString](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState#measureString--) 메서드를 호출할 수 있습니다. 아래의 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다.

```java
public static void GetTextWidthDynamicaly() {
    Font font = FontRepository.findFont("Arial");
    TextState ts = new TextState();
        ts.setFont(font);
        ts.setFontSize(14);
        if (Math.abs(font.measureString("A", 14) - 9.337) > 0.001)
            System.out.println("예상치 못한 폰트 문자열 측정!");

        if (Math.abs(ts.measureString("z") - 7.0) > 0.001)
        System.out.println("예상치 못한 폰트 문자열 측정!");

        for (char c = 'A'; c <= 'z'; c++)
        {
            double fnMeasure = font.measureString(String.valueOf(c), 14);
            double tsMeasure = ts.measureString(String.valueOf(c));

            if (Math.abs(fnMeasure - tsMeasure) > 0.001)
                System.out.println("폰트와 상태 문자열 측정이 일치하지 않습니다!");
        }
}
```