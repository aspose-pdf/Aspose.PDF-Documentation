---
title: Java에서 PDF 문서 조작
linktitle: PDF 문서 조작
type: docs
weight: 20
url: /java/manipulate-pdf-document/
description: TOC 관리 및 PDF/A 검사를 포함하여 Java에서 PDF 문서를 검증, 구성 및 수정하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 문서 검증, 재구성 및 평면화
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서를 조작하는 방법을 설명합니다. PDF/A 준수 확인, 목차 추가 및 사용자 정의, TOC 페이지 번호 숨기기 또는 사용자 정의, 만료 스크립트 할당, 대화형 양식 필드 평면화 등을 다룹니다.
---

Aspose.PDF for Java에는 단순한 페이지 편집 이상의 문서 구조 작업이 포함되어 있습니다.


## 
PDF/A-1a 규정 준수 여부 확인



문서가 PDF/A-1a 보관 표준을 충족하는지 확인해야 할 때 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
필수 [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) 대상에 대해 유효성 검사를 실행합니다.

1. 
검증 보고서를 지정된 출력 경로에 저장합니다.


```java
public static void validatePdfaStandardA1a(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1A);
    }
}
```

## 
PDF/A-1b 규정 준수 확인



이 변형은 PDF/A-1b 적합성 수준에 대해 동일한 소스 문서의 유효성을 검사합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
PDF/A-1b의 경우 [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) 값을 사용하여 유효성 검사 방법을 호출합니다.

1. 
검증 결과를 출력 보고서 파일에 기록합니다.


```java
public static void validatePdfaStandardA1b(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1B);
    }
}
```

## 
목차 추가



문서에 콘텐츠 페이지 링크가 포함된 생성된 목차 페이지가 포함되어야 하는 경우 이 접근 방식을 사용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
새 TOC [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 삽입하고 해당 [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/)를 구성합니다.

1. 
대상 페이지를 가리키는 [제목](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) 항목을 만듭니다.

1. 
업데이트된 문서를 저장합니다.


```java
public static void addTableOfContents(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().insert(1);
        TocInfo tocInfo = new TocInfo();
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(20);
        title.getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.setTitle(title);
        tocPage.setTocInfo(tocInfo);

        String[] titles = {"First page", "Second page"};
        for (int index = 0; index < titles.length && index + 2 <= document.getPages().size(); index++) {
            Heading heading = new Heading(1);
            TextSegment segment = new TextSegment(titles[index]);
            heading.setTocPage(tocPage);
            heading.getSegments().add(segment);
            Page destinationPage = document.getPages().get_Item(index + 2);
            heading.setDestinationPage(destinationPage);
            heading.setTop(destinationPage.getRect().getHeight());
            tocPage.getParagraphs().add(heading);
        }

        document.save(outputFile.toString());
    }
}
```

## 
TOC 수준 및 형식 지정



이 예에서는 여러 목차 수준에 서로 다른 시각적 설정을 할당하는 방법을 보여줍니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
TOC [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가하고 [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/) 형식 배열을 구성합니다.

1. 
다양한 수준의 샘플 [제목](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) 항목을 만듭니다.

1. 
형식이 지정된 TOC로 문서를 저장합니다.


```java
public static void setTocLevels(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().add();
        TocInfo tocInfo = new TocInfo();
        tocInfo.setLineDash(TabLeaderType.Solid);
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(30);
        tocInfo.setTitle(title);
        tocPage.setTocInfo(tocInfo);

        tocInfo.setFormatArrayLength(4);
        tocInfo.getFormatArray()[0].getMargin().setLeft(0);
        tocInfo.getFormatArray()[0].getMargin().setRight(30);
        tocInfo.getFormatArray()[0].setLineDash(TabLeaderType.Dot);
        tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        tocInfo.getFormatArray()[1].getMargin().setLeft(10);
        tocInfo.getFormatArray()[1].getMargin().setRight(30);
        tocInfo.getFormatArray()[1].setLineDash(3);
        tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
        tocInfo.getFormatArray()[2].getMargin().setLeft(20);
        tocInfo.getFormatArray()[2].getMargin().setRight(30);
        tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.getFormatArray()[3].setLineDash(TabLeaderType.Solid);
        tocInfo.getFormatArray()[3].getMargin().setLeft(30);
        tocInfo.getFormatArray()[3].getMargin().setRight(30);
        tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

        try (Page page = document.getPages().add()) {
            for (int level = 1; level < 5; level++) {
                Heading heading = new Heading(level);
                heading.setAutoSequence(true);
                heading.setTocPage(tocPage);
                heading.getTextState().setFont(FontRepository.findFont("Arial"));
                heading.getSegments().add(new TextSegment("Sample Heading" + level));
                heading.setInList(true);
                page.getParagraphs().add(heading);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 
목차에서 페이지 번호 숨기기



목차에 페이지 번호 없이 항목 제목을 표시해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
목차 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가하고 [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/)에서 페이지 번호를 비활성화합니다.

1. 
필수 [제목](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) 항목을 생성하고 콘텐츠 페이지에 추가합니다.

1. 
업데이트된 문서를 저장합니다.


```java
public static void hidePageNumbersInToc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page;
        Heading heading;
        try (Page tocPage = document.getPages().add()) {
            TocInfo tocInfo = new TocInfo();
            TextFragment title = new TextFragment("Table Of Contents");
            title.getTextState().setFontSize(20);
            title.getTextState().setFontStyle(FontStyles.Bold);
            tocInfo.setTitle(title);
            tocInfo.setShowPageNumbers(false);
            tocPage.setTocInfo(tocInfo);

            tocInfo.setFormatArrayLength(4);
            tocInfo.getFormatArray()[0].getMargin().setRight(0);
            tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
            tocInfo.getFormatArray()[1].getMargin().setLeft(30);
            tocInfo.getFormatArray()[1].getTextState().setUnderline(true);
            tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
            tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
            tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

            page = document.getPages().add();
            heading = new Heading(1);
            heading.setTocPage(tocPage);
        }
        heading.setAutoSequence(true);
        heading.setInList(true);
        heading.getSegments().add(new TextSegment("this is heading of level 1"));
        page.getParagraphs().add(heading);

        document.save(outputFile.toString());
    }
}
```

## 
TOC 페이지 번호 접두사 사용자 정의



이 예에서는 생성된 목차에 표시되는 페이지 번호에 사용자 정의 접두어를 추가합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
목차 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 삽입하고 [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/)에 원하는 페이지 번호 접두어를 설정합니다.

1. 
각 페이지를 가리키는 [제목](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) 항목을 만듭니다.

1. 
업데이트된 문서를 저장합니다.


```java
public static void customizePageNumbersInToc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().insert(1);
        TocInfo tocInfo = new TocInfo();
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(20);
        title.getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.setTitle(title);
        tocInfo.setPageNumbersPrefix("P");
        tocPage.setTocInfo(tocInfo);

        for (int index = 1; index <= document.getPages().size(); index++) {
            Page page = document.getPages().get_Item(index);
            Heading heading = new Heading(1);
            heading.setTocPage(tocPage);
            heading.setDestinationPage(page);
            heading.setTop(page.getRect().getHeight());
            heading.getSegments().add(new TextSegment("Page " + index));
            tocPage.getParagraphs().add(heading);
        }

        document.save(outputFile.toString());
    }
}
```

## 
PDF 만료 스크립트 추가



문서가 열릴 때 JavaScript를 실행하고 특정 날짜 이후 만료 경고를 표시해야 하는 경우 이 접근 방식을 사용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 필요한 내용을 추가합니다.

1. 
만료 논리를 사용하여 [JavascriptAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/javascriptaction/)을 만듭니다.

1. 
스크립트를 문서 열기 작업으로 할당하고 출력 파일을 저장합니다.


```java
public static void setPdfExpiryDate(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        try (Page page = document.getPages().add()) {
            page.getParagraphs().add(new TextFragment("Hello World..."));
        }
        JavascriptAction script = new JavascriptAction(
                "var year=2017;"
                        + "var month=5;"
                        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
                        + "expiry = new Date(year, month);"
                        + "if (today.getTime() > expiry.getTime())"
                        + "app.alert('The file is expired. You need a new one.');");
        document.setOpenAction(script);
        document.save(outputFile.toString());
    }
}
```

## 
채울 수 있는 PDF 양식 병합



이 예에서는 대화형 양식 필드를 정적 페이지 콘텐츠로 변환하므로 결과 문서는 더 이상 양식으로 편집할 수 없습니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
문서에 양식 위젯이 포함되어 있는지 확인하세요.

1. 
[WidgetAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/)으로 표시되는 각 [필드](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/)를 평면화합니다.

1. 
병합된 문서를 저장합니다.

```java
public static void flattenFillablePdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getForm() != null && document.getForm().size() > 0) {
            for (WidgetAnnotation annotation : document.getForm()) {
                if (annotation instanceof Field field) {
                    field.flatten();
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```
