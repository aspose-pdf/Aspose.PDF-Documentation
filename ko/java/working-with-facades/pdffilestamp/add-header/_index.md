---
title: PDF에 헤더 추가
linktitle: PDF에 헤더 추가
type: docs
weight: 20
url: /java/add-header/
description: PdfFileStamp 파사드를 사용하여 Java의 PDF 페이지에 텍스트 및 이미지 헤더를 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 PDF에 텍스트 및 이미지 헤더 추가
Abstract: PdfFileStamp 파사드를 사용하여 Java용 Aspose.PDF를 사용하여 PDF 문서에 헤더 내용을 추가하는 방법을 알아보세요. Java 예제는 일반 텍스트 헤더, 스트림에서 로드된 이미지 헤더, 명시적인 여백 값이 있는 스타일 헤더를 다룹니다.
---
## 
PDF에 헤더 추가



각 페이지에 반복되는 헤더 내용이 필요한 경우 `PdfFileStamp`을 사용하세요.


### 
단계


1. 
`PdfFileStamp` 인스턴스를 생성하고 소스 PDF를 바인딩합니다.

2. 
헤더 콘텐츠를 `FormattedText`으로 빌드하거나 이미지 스트림에서 로드합니다.

3. 
적절한 `addHeader` 오버로드를 호출하세요.

4. 
출력을 저장하고 Facade 객체를 닫습니다.


### 
자바 예제

```java
public static void addTextHeader(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("Sample Header");
        pdfStamper.addHeader(text, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addImageHeader(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addHeader(imageStream, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addHeaderWithMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText(
                "Sample Header",
                Color.BLUE,
                FontStyle.Helvetica,
                EncodingType.Winansi,
                true,
                12.0f);
        pdfStamper.addHeader(text, 20, 20, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
