---
title: Java에서 PDF에 페이지 스탬프 추가
linktitle: 페이지 스탬프 추가
type: docs
weight: 30
url: /java/page-stamps-in-the-pdf-file/
description: Java에서 PDF 페이지 스탬프를 오버레이 또는 배경으로 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에 페이지 기반 스탬프 추가
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에 페이지 스탬프를 추가하는 방법을 설명합니다. 예제에서는 다른 PDF 페이지를 스탬프로 로드하고 배경으로 구성한 다음 대상 페이지에 적용합니다.
---

Java용 Aspose.PDF는 다른 PDF의 페이지를 스탬프로 적용하거나 페이지 번호 매기기 오버레이를 추가할 수 있습니다.


## 
다른 PDF에서 페이지 스탬프 추가



별도의 PDF 페이지를 배경 스탬프로 사용해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
외부 PDF 페이지에서 [PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfpagestamp/)를 만듭니다.

1. 
스탬프를 구성하고 대상 페이지에 추가한 후 결과를 저장합니다.


```java
public static void addPageStamp(Path inputFile, Path pageStampFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfPageStamp pageStamp = new PdfPageStamp(pageStampFile.toString(), 1);
        pageStamp.setBackground(true);
        document.getPages().get_Item(1).addStamp(pageStamp);
        document.save(outputFile.toString());
    }
}
```

## 
표준 페이지 번호 스탬프 추가



대상 페이지에 사용자 정의 텍스트 형식으로 현재 숫자를 표시해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/)를 생성하고 구성합니다.

1. 
페이지에 스탬프를 추가하고 문서를 저장하세요.


```java
public static void addPageNumStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + document.getPages().size());
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        document.getPages().get_Item(1).addStamp(pageNumberStamp);
        document.save(outputFile.toString());
    }
}
```

## 
로마 숫자 페이지 번호 스탬프 추가



페이지 번호 매기기가 사용자 정의 값에서 시작하고 대문자 로마 숫자를 사용해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/)를 생성하고 로마 숫자 번호 매기기를 구성합니다.

1. 
모든 페이지에 스탬프를 추가하고 PDF를 저장하세요.

```java
public static void addPageNumStampRoman(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(42);
        pageNumberStamp.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        for (Page page : document.getPages()) {
            page.addStamp(pageNumberStamp);
        }
        document.save(outputFile.toString());
    }
}
```
