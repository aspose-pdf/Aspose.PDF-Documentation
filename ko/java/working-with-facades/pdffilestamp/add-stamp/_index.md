---
title: PDF에 스탬프 추가
linktitle: PDF에 스탬프 추가
type: docs
weight: 40
url: /java/add-stamp/
description: PdfFileStamp 파사드를 사용하여 Java의 PDF 페이지에 이미지 스탬프를 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 PDF에 이미지 스탬프 추가
Abstract: PdfFileStamp 파사드를 사용하여 Java용 Aspose.PDF를 사용하여 PDF 문서에 스탬프 콘텐츠를 추가하는 방법을 알아보세요. 현재 Java 예제 세트는 `Stamp`을 생성하고, 이를 이미지 파일에 바인딩하고, 문서에 추가하고, 스탬프가 찍힌 PDF를 저장하는 방법을 보여줍니다.
---
## 
PDF에 스탬프 추가



이미지 기반 스탬프를 PDF에 적용해야 하는 경우 이 작업 과정을 사용하십시오.


### 
단계


1. 
`PdfFileStamp` 인스턴스를 생성하고 소스 PDF를 바인딩합니다.

2. 
`Stamp` 개체를 만듭니다.

3. 
`bindImage`을 사용하여 스탬프를 이미지 파일에 바인딩합니다.

4. 
`addStamp`을 사용하여 문서에 스탬프를 추가합니다.

5. 
출력을 저장하고 Facade 객체를 닫습니다.


### 
자바 예


```java
public static void addStampToPdf(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```


현재 `PdfFileStampExamples.java` 클래스에는 텍스트 전용 스탬프, 회전 또는 불투명도 구성을 위한 별도의 Java 샘플이 포함되어 있지 않습니다.
