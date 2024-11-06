---
title: PDF 내 텍스트 서식 
linktitle: PDF 내 텍스트 서식
type: docs
weight: 30
url: ko/java/text-formatting-inside-pdf/
description: 이 페이지는 PDF 파일 내에서 텍스트를 서식화하는 방법을 설명합니다. 줄 들여쓰기 추가, 텍스트 경계 추가, 밑줄 텍스트 추가, 추가된 텍스트 주위에 경계 추가, 플로팅 박스 내용의 텍스트 정렬 등을 포함합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF에 줄 들여쓰기 추가하는 방법

Aspose.PDF for Java는 [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions) 클래스에 SubsequentLinesIndent 속성을 제공합니다. 이 속성은 TextFragment 및 Paragraphs 컬렉션과 함께 PDF 생성 시나리오에서 줄 들여쓰기를 지정하는 데 사용할 수 있습니다.

다음 코드 스니펫을 사용하여 속성을 사용하는 방법을 참고하세요:

```java
public static void AddLineIndentToPDF() {
        // 새로운 문서 객체 생성
        Document document = new Document();
        Page page = document.getPages().add();

        TextFragment text = new TextFragment(
                "A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog.");

        // 텍스트 조각에 대한 TextFormattingOptions 초기화 및
        // SubsequentLinesIndent 값 지정
        TextFormattingOptions textOptions = new TextFormattingOptions();
        textOptions.setSubsequentLinesIndent(20);
        text.getTextState().setFormattingOptions(textOptions);

        page.getParagraphs().add(text);

        text = new TextFragment("Line2");
        page.getParagraphs().add(text);

        text = new TextFragment("Line3");
        page.getParagraphs().add(text);

        text = new TextFragment("Line4");
        page.getParagraphs().add(text);

        text = new TextFragment("Line5");
        page.getParagraphs().add(text);

        document.save(_dataDir + "SubsequentIndent_out.pdf");
    }
```


## 텍스트 테두리 추가 방법

다음 코드 스니펫은 TextBuilder를 사용하여 텍스트에 테두리를 추가하고 TextState의 DrawTextRectangleBorder 메서드를 설정하는 방법을 보여줍니다:

```java
public static void AddTextBorder() {
    // 새 문서 객체 생성
    Document pdfDocument = new Document();
    // 특정 페이지 가져오기
    Page pdfPage = pdfDocument.getPages().add();
    // 텍스트 조각 생성
    TextFragment textFragment = new TextFragment("main text");
    textFragment.setPosition(new Position(100, 600));
    // 텍스트 속성 설정
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    textFragment.getTextState().setBackgroundColor (Color.getLightGray());
    textFragment.getTextState().setForegroundColor (Color.getRed());
    // 텍스트 사각형 주위에 경계를 그리기 위해 setStrokingColor 사용
    textFragment.getTextState().setStrokingColor (Color.getDarkRed());
    // setDrawTextRectangleBorder 메서드를 사용하여 true 값을 설정
    textFragment.getTextState().setDrawTextRectangleBorder(true);
    TextBuilder tb = new TextBuilder(pdfPage);
    tb.appendText(textFragment);
    // 문서 저장
    pdfDocument.save(_dataDir + "PDFWithTextBorder_out.pdf");
}
```


## 밑줄 텍스트 추가 방법

다음 코드 스니펫은 새 PDF 파일을 생성할 때 밑줄 텍스트를 추가하는 방법을 보여줍니다.

```java
public static void AddUnderlineText(){
    // 문서 객체 생성
    Document pdfDocument = new Document();
    // PDF 문서에 페이지 추가
    Page page = pdfDocument.getPages().add();
    // 첫 번째 페이지에 대한 TextBuilder 생성
    TextBuilder tb = new TextBuilder(page);
    // 샘플 텍스트가 포함된 TextFragment
    TextFragment fragment = new TextFragment("밑줄 장식이 있는 텍스트");
    // TextFragment에 대한 폰트 설정
    fragment.getTextState().setFont(FontRepository.findFont("Arial"));
    fragment.getTextState().setFontSize(10);
    // 텍스트 형식을 밑줄로 설정
    fragment.getTextState().setUnderline(true);
    // TextFragment가 배치될 위치 지정
    fragment.setPosition(new Position(10, 800));
    // PDF 파일에 TextFragment 추가
    tb.appendText(fragment);

    // 결과 PDF 문서 저장
    pdfDocument.save(_dataDir + "AddUnderlineText_out.pdf");
}
```


## 텍스트에 추가된 테두리를 추가하는 방법

추가한 텍스트의 외관을 제어할 수 있습니다. 아래 예시는 추가한 텍스트 주위에 사각형을 그려 테두리를 추가하는 방법을 보여줍니다. [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 클래스에 대해 더 알아보세요.

```java
public static void AddBorderAroundAddedText() {
    PdfContentEditor editor = new PdfContentEditor();
    editor.bindPdf(_dataDir + "input.pdf");
    LineInfo lineInfo = new LineInfo();
    lineInfo.setLineWidth(2);
    lineInfo.setVerticeCoordinate (new float[] { 0, 0, 100, 100, 50, 100 });
    lineInfo.setVisibility(true);
    editor.createPolygon(lineInfo, 1, new java.awt.Rectangle(0, 0, 0, 0), "");

    // 결과 PDF 문서를 저장합니다.
    editor.save(_dataDir + "AddingBorderAroundAddedText_out.pdf");
}
```

## 줄바꿈 추가하는 방법

TextFragment는 텍스트 내에서 줄바꿈을 지원하지 않습니다.
 하지만 줄 바꿈이 있는 텍스트를 추가하려면 TextFragment와 TextParagraph를 사용하세요:

- 단일 “\n” 대신 TextFragment에서 "\r\n" 또는 Environment.NewLine을 사용합니다;
- TextParagraph 객체를 생성합니다. 이것은 텍스트를 줄 나누기로 추가합니다;
- TextFragment를 TextParagraph.AppendLine과 함께 추가합니다;
- TextParagraph를 TextBuilder.AppendParagraph와 함께 추가합니다.
아래 코드 스니펫을 사용하세요.

```java
public static void AddNewLineFeed() {        
    Document pdfDocument = new Document();
    Page page = pdfDocument.getPages().add();

    // 필요한 줄 바꿈 표시가 포함된 텍스트로 새 TextFragment 초기화
    TextFragment textFragment = new TextFragment("Applicant Name: " + System.lineSeparator() + " Joe Smoe");

    // 필요시 텍스트 프래그먼트 속성 설정
    textFragment.getTextState().setFontSize (12);
    textFragment.getTextState().setFont(FontRepository.findFont("DejaVu Serif"));
    textFragment.getTextState().setBackgroundColor (Color.getLightGray());
    textFragment.getTextState().setForegroundColor (Color.getRed());

    // TextParagraph 객체 생성
    TextParagraph par = new TextParagraph();

    // 새 TextFragment를 단락에 추가
    par.appendLine(textFragment);

    // 단락 위치 설정
    par.setPosition (new Position(100, 600));

    // TextBuilder 객체 생성
    TextBuilder textBuilder = new TextBuilder(page);
    // TextBuilder를 사용하여 TextParagraph 추가
    textBuilder.appendParagraph(par);

    // 결과 PDF 문서 저장.
    pdfDocument.save(_dataDir + "AddNewLineFeed_out.pdf");
}
```

## StrikeOut 텍스트 추가 방법

TextState 클래스는 PDF 문서에 배치되는 TextFragments의 서식을 설정할 수 있는 기능을 제공합니다. 이 클래스를 사용하여 텍스트 서식을 굵게, 기울임꼴, 밑줄로 설정할 수 있으며, 이번 릴리스부터는 텍스트 서식을 취소선으로 표시할 수 있는 기능이 제공됩니다. 다음 코드 스니펫을 사용하여 취소선 서식이 있는 TextFragment를 추가해 보세요.

전체 코드 스니펫을 사용하세요:

```java
public static void AddStrikeOutText(){
    // 문서 열기
    Document pdfDocument = new Document();
    // 특정 페이지 가져오기
    Page pdfPage = (Page)pdfDocument.getPages().add();

    // 텍스트 조각 생성
    TextFragment textFragment = new TextFragment("main text");
    textFragment.setPosition (new Position(100, 600));

    // 텍스트 속성 설정
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("DejaVu Serif"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());
    // setStrikeOut 메서드를 사용하여 취소선 텍스트 활성화
    textFragment.getTextState().setStrikeOut(true);
    // 텍스트를 굵게 표시
    textFragment.getTextState().setFontStyle(FontStyles.Bold);

    // TextBuilder 객체 생성
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // PDF 페이지에 텍스트 조각 추가
    textBuilder.appendText(textFragment);

    // 결과 PDF 문서 저장
    pdfDocument.save(_dataDir + "AddStrikeOutText_out.pdf");        
}
```


## 텍스트에 그라데이션 음영 적용

텍스트 편집 시나리오를 위한 API에서 텍스트 서식이 더욱 향상되어 이제 PDF 문서 내에 패턴 색상 공간으로 텍스트를 추가할 수 있습니다. com.aspose.pdf.Color 클래스는 텍스트에 음영 색상을 지정할 수 있는 새로운 메서드 `setPatternColorSpace`를 도입하여 더욱 향상되었습니다. 이 새로운 메서드는 다음 코드 스니펫에 표시된 대로 축 음영, 방사형 (타입 3) 음영 등 텍스트에 다양한 그라데이션 음영을 추가합니다:

```java
public static void ApplyGradientShading() {
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("항상 올바르게 인쇄");
    pdfDocument.getPages().accept(absorber);

    TextFragment textFragment = absorber.getTextFragments().get_Item(1);

    Color foregroundColor = new com.aspose.pdf.Color();
    foregroundColor.setPatternColorSpace(new GradientAxialShading(Color.getRed(), Color.getBlue()));

    // 패턴 색상 공간으로 새로운 색상 생성
    textFragment.getTextState().setForegroundColor (foregroundColor);

    textFragment.getTextState().setUnderline(true);

    pdfDocument.save(_dataDir + "text_out.pdf");
}
```


방사형 그라디언트를 적용하려면 위 코드 스니펫에서 `GradientRadialShading(startingColor, endingColor)`과 같은 `setPatternColorSpace` 메소드를 사용할 수 있습니다.

```java
public static void ApplyGradientShadingRadial() {
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("항상 올바르게 인쇄");
    pdfDocument.getPages().accept(absorber);

    TextFragment textFragment = absorber.getTextFragments().get_Item(1);

    Color foregroundColor = new com.aspose.pdf.Color();
    foregroundColor.setPatternColorSpace(new GradientRadialShading(Color.getRed(), Color.getBlue()));

    // 패턴 색상 공간을 가진 새로운 색상 생성
    textFragment.getTextState().setForegroundColor (foregroundColor);

    textFragment.getTextState().setUnderline(true);

    pdfDocument.save(_dataDir + "text_out.pdf");
}
```

## 플로팅 콘텐츠에 텍스트 정렬하는 방법

Aspose.PDF는 플로팅 박스 요소 내부의 콘텐츠에 대한 텍스트 정렬 설정을 지원합니다.
 Aspose.Pdf.FloatingBox 인스턴스의 정렬 속성은 다음 코드 샘플과 같이 이를 달성하는 데 사용할 수 있습니다.

```java
public static void AlignTextToFloatContent() {
    Document pdfDocument = new Document();
    Page page = pdfDocument.getPages().add();

    FloatingBox floatBox = new FloatingBox(100, 100);
    floatBox.setVerticalAlignment(VerticalAlignment.Bottom); // 수직 정렬을 아래로 설정
    floatBox.setHorizontalAlignment (HorizontalAlignment.Right); // 수평 정렬을 오른쪽으로 설정
    floatBox.getParagraphs().add(new TextFragment("FloatingBox_bottom")); // 텍스트 추가
    floatBox.setBorder(new BorderInfo(BorderSide.All, Color.getBlue())); // 테두리 설정
    
    page.getParagraphs().add(floatBox);

    FloatingBox floatBox1 = new FloatingBox(100, 100);
    floatBox1.setVerticalAlignment(VerticalAlignment.Center); // 수직 정렬을 중앙으로 설정
    floatBox1.setHorizontalAlignment (HorizontalAlignment.Right); // 수평 정렬을 오른쪽으로 설정
    floatBox1.getParagraphs().add(new TextFragment("FloatingBox_center")); // 텍스트 추가
    floatBox1.setBorder (new BorderInfo(BorderSide.All, Color.getBlue())); // 테두리 설정
    page.getParagraphs().add(floatBox1);

    FloatingBox floatBox2 = new FloatingBox(100, 100);
    floatBox2.setVerticalAlignment(VerticalAlignment.Top); // 수직 정렬을 위로 설정
    floatBox2.setHorizontalAlignment (HorizontalAlignment.Right); // 수평 정렬을 오른쪽으로 설정
    floatBox2.getParagraphs().add(new TextFragment("FloatingBox_top")); // 텍스트 추가
    floatBox2.setBorder (new BorderInfo(BorderSide.All, Color.getBlue())); // 테두리 설정
    page.getParagraphs().add(floatBox2);

    pdfDocument.save(_dataDir + "FloatingBox_alignment_review_out.pdf"); // 문서 저장        
}
```