---
title: Java에서 PDF 텍스트 회전
linktitle: PDF 내부의 텍스트 회전
type: docs
weight: 50
url: /java/rotate-text-inside-pdf/
description: Java에서 PDF 문서 내의 텍스트 조각과 단락을 회전하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 문서의 텍스트 조각 및 단락 회전
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서의 텍스트를 회전하는 방법을 설명합니다. 개별 텍스트 조각을 회전하고, 회전된 줄이 포함된 단락을 만들고, 다양한 레이아웃 시나리오에 맞게 전체 텍스트 단락을 회전하는 방법을 보여줍니다.
---
Aspose.PDF for Java를 사용하면 개별 텍스트 조각은 물론 전체 텍스트 단락도 회전할 수 있습니다.


## 
개별 텍스트 조각 회전



같은 줄에 있는 여러 텍스트 조각이 서로 다른 회전 각도를 사용해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
필요한 회전 값을 사용하여 텍스트 조각을 만듭니다.
1. `TextBuilder`을 추가하고 결과를 저장합니다.


```java
public static void rotateTextInsidePdf1(Path outputFile) {
       try (Document document = new Document()) {
           Page page = document.getPages().add();

           TextFragment textFragment1 = new TextFragment("main text");
           textFragment1.setPosition(new Position(100, 600));
           textFragment1.getTextState().setFontSize(12);
           textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

           TextFragment textFragment2 = new TextFragment("rotated text");
           textFragment2.setPosition(new Position(200, 600));
           textFragment2.getTextState().setFontSize(12);
           textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
           textFragment2.getTextState().setRotation(45);

           TextFragment textFragment3 = new TextFragment("rotated text");
           textFragment3.setPosition(new Position(300, 600));
           textFragment3.getTextState().setFontSize(12);
           textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
           textFragment3.getTextState().setRotation(90);

           TextBuilder builder = new TextBuilder(page);
           builder.appendText(textFragment1);
           builder.appendText(textFragment2);
           builder.appendText(textFragment3);

           document.save(outputFile.toString());
       }
   }
```

## 
텍스트 단락 내부의 줄 회전



단락에 일반 선과 회전된 선이 모두 포함되어야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
`TextParagraph`을 만들고 다양한 회전 설정으로 텍스트 조각을 추가합니다.
1. 페이지에 단락을 추가하고 문서를 저장합니다.


```java
public static void rotateTextInsidePdf2(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        TextParagraph paragraph = new TextParagraph();
        paragraph.setPosition(new Position(200, 600));

        TextFragment textFragment1 = new TextFragment("rotated text");
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment1.getTextState().setRotation(45);

        TextFragment textFragment2 = new TextFragment("main text");
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

        TextFragment textFragment3 = new TextFragment("another rotated text");
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setRotation(-45);

        paragraph.appendLine(textFragment1);
        paragraph.appendLine(textFragment2);
        paragraph.appendLine(textFragment3);

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendParagraph(paragraph);

        document.save(outputFile.toString());
    }
}
```

## 
명시적인 위치 없이 단락 조각 회전



일반 페이지 단락 흐름을 통해 회전된 텍스트를 추가해야 하는 경우 이 예를 사용합니다.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
회전 값이 다른 여러 텍스트 조각을 만듭니다.
1. 페이지 단락 컬렉션에 추가하고 PDF를 저장하세요.


```java
public static void rotateTextInsidePdf3(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment1 = new TextFragment("main text");
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

        TextFragment textFragment2 = new TextFragment("rotated text");
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setRotation(315);

        TextFragment textFragment3 = new TextFragment("rotated text");
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setRotation(270);

        page.getParagraphs().add(textFragment1);
        page.getParagraphs().add(textFragment2);
        page.getParagraphs().add(textFragment3);

        document.save(outputFile.toString());
    }
}
```

## 
전체 단락 회전



각 줄이 공유 스타일을 유지하면서 전체 단락 블록을 회전해야 하는 경우 이 예를 사용합니다.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
단락 수준 회전을 사용하여 여러 `TextParagraph` 개체를 만듭니다.
1. 공유 도우미 메서드를 사용하여 줄을 만들고 추가한 후 문서를 저장합니다.

```java
public static void rotateTextInsidePdf4(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        for (int i = 0; i < 4; i++) {
            TextParagraph paragraph = new TextParagraph();
            paragraph.setPosition(new Position(200, 600));
            paragraph.setRotation(i * 90 + 45);

            TextFragment textFragment1 = rotatedLine("Paragraph Text", false);
            TextFragment textFragment2 = rotatedLine("Second line of text", false);
            TextFragment textFragment3 = rotatedLine("And some more text...", true);

            paragraph.appendLine(textFragment1);
            paragraph.appendLine(textFragment2);
            paragraph.appendLine(textFragment3);

            TextBuilder builder = new TextBuilder(page);
            builder.appendParagraph(paragraph);
        }

        document.save(outputFile.toString());
    }
}

private static TextFragment rotatedLine(String text, boolean underline) {
    TextFragment fragment = new TextFragment(text);
    fragment.getTextState().setFontSize(12);
    fragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    fragment.getTextState().setBackgroundColor(Color.getLightGray());
    fragment.getTextState().setForegroundColor(Color.getBlue());
    fragment.getTextState().setUnderline(underline);
    return fragment;
}
```
