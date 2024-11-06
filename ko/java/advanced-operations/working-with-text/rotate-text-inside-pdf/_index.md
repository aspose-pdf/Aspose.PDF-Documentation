---
title: PDF 내 텍스트 회전 
linktitle: PDF 내 텍스트 회전
type: docs
weight: 50
url: ko/java/rotate-text-inside-pdf/
description: PDF에 텍스트를 회전시키는 다양한 방법을 배우세요. Aspose.PDF는 텍스트를 원하는 각도로 회전시키거나 텍스트 조각 또는 전체 단락을 회전시킬 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 회전 속성을 사용하여 PDF 내 텍스트 회전

[TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) 클래스의 [setRotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentState#setRotation-double-) 메서드를 사용하여 다양한 각도로 텍스트를 회전할 수 있습니다. 문서 생성의 다양한 시나리오에서 텍스트 회전을 사용할 수 있습니다. 필요한 대로 텍스트를 회전시키기 위해 각도를 도 단위로 지정할 수 있습니다. 텍스트 회전을 구현할 수 있는 다양한 시나리오를 확인해보세요.

## TextFragment 및 TextBuilder를 사용하여 회전 구현

```java
public class ExampleRotateText {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ImplementRotationUsingTextFragmentAndTextBuilder() {

        // 문서 객체 초기화
        Document pdfDocument = new Document();
        // 특정 페이지 가져오기
        Page pdfPage = pdfDocument.getPages().add();
        // 텍스트 조각 생성
        TextFragment textFragment1 = new TextFragment("main text");
        textFragment1.setPosition(new Position(100, 600));

        // 텍스트 속성 설정
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

        // 회전된 텍스트 조각 생성
        TextFragment textFragment2 = new TextFragment("rotated text");
        textFragment2.setPosition(new Position(200, 600));
        // 텍스트 속성 설정
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setRotation(45);

        // 회전된 텍스트 조각 생성
        TextFragment textFragment3 = new TextFragment("rotated text");
        textFragment3.setPosition(new Position(300, 600));

        // 텍스트 속성 설정
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setRotation(90);

        // TextBuilder 객체 생성
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // PDF 페이지에 텍스트 조각 추가
        textBuilder.appendText(textFragment1);
        textBuilder.appendText(textFragment2);
        textBuilder.appendText(textFragment3);

        // 문서 저장
        pdfDocument.save(_dataDir + "TextFragmentTests_Rotated1_out.pdf");
    }
}
```


## 텍스트 단락 및 텍스트 빌더를 사용하여 회전 구현 (회전된 조각들)

```java
public static void ImplementRotationUsingTextParagraphAndTextBuilder_RotatedFragments() {

    // 문서 객체 초기화
    Document pdfDocument = new Document();
    // 특정 페이지 가져오기
    Page pdfPage = (Page) pdfDocument.getPages().add();
    TextParagraph paragraph = new TextParagraph();
    paragraph.setPosition(new Position(200, 600));
    // 텍스트 조각 생성
    TextFragment textFragment1 = new TextFragment("rotated text");
    // 텍스트 속성 설정
    textFragment1.getTextState().setFontSize(12);
    textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    // 회전 설정
    textFragment1.getTextState().setRotation(45);

    // 텍스트 조각 생성
    TextFragment textFragment2 = new TextFragment("main text");
    // 텍스트 속성 설정
    textFragment2.getTextState().setFontSize(12);
    textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // 텍스트 조각 생성
    TextFragment textFragment3 = new TextFragment("another rotated text");
    // 텍스트 속성 설정
    textFragment3.getTextState().setFontSize(12);
    textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    // 회전 설정
    textFragment3.getTextState().setRotation(-45);

    // 텍스트 조각을 단락에 추가
    paragraph.appendLine(textFragment1);
    paragraph.appendLine(textFragment2);
    paragraph.appendLine(textFragment3);
    // 텍스트 빌더 객체 생성
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // 텍스트 단락을 PDF 페이지에 추가
    textBuilder.appendParagraph(paragraph);
    // 문서 저장
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated2_out.pdf");
}
```


## TextFragment 및 Page.Paragraphs를 사용하여 회전 구현

```csharp
public static void ImplementRotationUsingTextFragmentAndPageParagraphs() {
    // 문서 객체 초기화
    Document pdfDocument = new Document();
    // 특정 페이지 가져오기
    Page pdfPage = (Page) pdfDocument.getPages().add();
    // 텍스트 조각 생성
    TextFragment textFragment1 = new TextFragment("main text");
    // 텍스트 속성 설정
    textFragment1.getTextState().setFontSize(12);
    textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // 텍스트 조각 생성
    TextFragment textFragment2 = new TextFragment("rotated text");

    // 텍스트 속성 설정
    textFragment2.getTextState().setFontSize(12);
    textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // 회전 설정
    textFragment2.getTextState().setRotation(315);

    // 텍스트 조각 생성
    TextFragment textFragment3 = new TextFragment("rotated text");
    // 텍스트 속성 설정
    textFragment3.getTextState().setFontSize(12);
    textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // 회전 설정
    textFragment3.getTextState().setRotation(270);
    pdfPage.getParagraphs().add(textFragment1);
    pdfPage.getParagraphs().add(textFragment2);
    pdfPage.getParagraphs().add(textFragment3);

    // 문서 저장
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated3_out.pdf");
    }
```


## TextParagraph 및 TextBuilder를 사용하여 회전 구현 (전체 단락 회전)

```java
public static void ImplementRotationUsingTextParagraphAndTextBuilder() {

    // 문서 객체 초기화
    Document pdfDocument = new Document();
    // 특정 페이지 가져오기
    Page pdfPage = pdfDocument.getPages().add();
    for (int i = 0; i < 4; i++) {
        TextParagraph paragraph = new TextParagraph();
        paragraph.setPosition(new Position(200, 600));
        // 회전 지정
        paragraph.setRotation(i * 90 + 45);
        // 텍스트 조각 생성
        TextFragment textFragment1 = new TextFragment("단락 텍스트");
        // 텍스트 조각 생성
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment1.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment1.getTextState().setForegroundColor(Color.getBlue());

        // 텍스트 조각 생성
        TextFragment textFragment2 = new TextFragment("두 번째 줄의 텍스트");
        // 텍스트 속성 설정
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment2.getTextState().setForegroundColor(Color.getBlue());

        // 텍스트 조각 생성
        TextFragment textFragment3 = new TextFragment("그리고 더 많은 텍스트...");
        // 텍스트 속성 설정
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment3.getTextState().setForegroundColor(Color.getBlue());
        textFragment3.getTextState().setUnderline(true);

        paragraph.appendLine(textFragment1);
        paragraph.appendLine(textFragment2);
        paragraph.appendLine(textFragment3);
        // TextBuilder 객체 생성
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // PDF 페이지에 텍스트 조각 추가
        textBuilder.appendParagraph(paragraph);
    }
    // 문서 저장
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated4_out.pdf");
}
```