---
title: PDF에 바닥글 추가
linktitle: PDF에 바닥글 추가
type: docs
weight: 10
url: /java/add-footer/
description: PdfFileStamp 파사드를 사용하여 Java의 PDF 페이지에 텍스트 및 이미지 바닥글을 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 PDF에 텍스트 및 이미지 바닥글 추가
Abstract: PdfFileStamp 파사드를 사용하여 Java용 Aspose.PDF를 사용하여 PDF 문서에 바닥글 콘텐츠를 추가하는 방법을 알아보세요. Java 예제에서는 일반 텍스트 바닥글, 스트림에서 로드된 이미지 바닥글, 명시적인 왼쪽, 오른쪽 및 아래쪽 여백이 있는 텍스트 바닥글을 다룹니다.
---
## PDF에 바닥글 추가



문서의 모든 페이지에 반복되는 바닥글 내용이 필요한 경우 `PdfFileStamp`을 사용하세요.


### 
단계


1. 
`PdfFileStamp` 인스턴스를 생성하고 소스 PDF를 바인딩합니다.

2. 
`FormattedText` 또는 이미지 스트림으로 바닥글 콘텐츠를 작성합니다.
3. 적절한 `addFooter` 오버로드를 호출하세요.

4. 
업데이트된 파일을 저장하고 Facade 객체를 닫습니다.


### 
자바 예제

```java
public static void addTextFooter(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("Sample Footer");
        pdfStamper.addFooter(text, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addImageFooter(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addFooter(imageStream, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addFooterWithMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("This footer has margins on all sides.");
        pdfStamper.addFooter(text, 20, 20, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
