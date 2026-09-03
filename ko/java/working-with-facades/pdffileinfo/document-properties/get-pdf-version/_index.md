---
title: PDF 버전 받기
linktitle: PDF 버전 받기
type: docs
weight: 20
url: /java/get-pdf-version/
description: PdfFileInfo 파사드를 사용하여 Java에서 PDF 문서 버전을 검색하는 방법을 알아보세요.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java용 Aspose.PDF를 사용하여 PDF 버전 검색
Abstract: Java용 Aspose.PDF를 사용하여 PDF 버전을 검색하는 방법을 알아보세요. Java 예제에서는 PdfFileInfo 객체를 생성하고 `getPdfVersion()`이 포함된 버전 문자열을 읽고 결과를 인쇄하고 파일 정보 객체를 닫습니다.
---
## PDF 버전 받기



버전별 처리 로직을 통해 파일 호환성을 확인하거나 문서를 라우팅해야 하는 경우 이 워크플로를 사용하세요.


### 
단계


1. 
PDF 파일에 대한 `PdfFileInfo` 개체를 만듭니다.

2. 
보고된 버전을 검색하려면 `getPdfVersion()`으로 전화하세요.
3. 버전 값을 사용하거나 인쇄하십시오.

4. 
`PdfFileInfo` 인스턴스를 닫습니다.


### 
자바 예

```java
public static void getPdfVersion(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println();
    System.out.println("PDF Version: " + pdfInfo.getPdfVersion());
    pdfInfo.close();
}
```
