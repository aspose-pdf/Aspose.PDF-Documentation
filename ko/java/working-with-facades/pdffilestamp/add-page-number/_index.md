---
title: PDF에 페이지 번호 추가
linktitle: PDF에 페이지 번호 추가
type: docs
weight: 30
url: /java/page-number/
description: PdfFileStamp 파사드를 사용하여 Java에서 PDF 문서에 페이지 번호를 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 PDF에 페이지 번호 추가
Abstract: PdfFileStamp 파사드를 사용하여 Java용 Aspose.PDF로 PDF 문서에 페이지 번호를 추가하는 방법을 알아보세요. Java 예제에서는 기본 배치, 명시적 좌표, 여백에 따른 정렬 배치, 사용자 정의 시작 번호가 있는 로마자 번호 매기기 출력을 다룹니다.
---
## 
PDF에 페이지 번호 추가



PDF 콘텐츠가 이미 생성된 후 페이지 번호 매기기를 적용해야 하는 경우 `PdfFileStamp`을 사용합니다.


### 
단계


1. 
`PdfFileStamp` 인스턴스를 생성하고 소스 PDF를 바인딩합니다.

2. 
필요한 페이지 번호 배치 전략을 선택하세요.

3. 
선택적으로 스탬핑하기 전에 번호 매기기 스타일과 시작 번호를 설정합니다.

4. 
필요한 오버로드로 `addPageNumber`을 호출하세요.

5. 
출력을 저장하고 Facade 객체를 닫습니다.


### 
자바 예제

```java
public static void addPageNumbersDefault(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #");
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersAtCoordinates(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #", 300, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersWithPositionAndMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #", PdfFileStamp.POS_BOTTOM_RIGHT, 10, 10, 10, 10);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersWithRomanStyle(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);
        pdfStamper.setStartingNumber(42);
        pdfStamper.addPageNumber("Page #", PdfFileStamp.POS_UPPER_RIGHT);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
