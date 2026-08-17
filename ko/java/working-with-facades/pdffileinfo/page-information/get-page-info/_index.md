---
title: 페이지 정보 얻기
linktitle: 페이지 정보 얻기
type: docs
weight: 10
url: /java/get-page-info/
description: PdfFileInfo 파사드를 사용하여 Java에서 페이지 너비, 높이 및 회전을 검사하는 방법을 알아보세요.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java용 Aspose.PDF를 사용하여 PDF 페이지 정보 얻기
Abstract: Aspose.PDF for Java를 사용하여 페이지 정보를 검색하는 방법을 알아보세요. Java 예제에서는 PdfFileInfo를 사용하여 페이지 1의 너비, 높이 및 회전을 읽으므로 추가 처리 전에 레이아웃을 검사할 수 있습니다.
---
## 
페이지 정보 가져오기



이 예에서는 페이지 1의 주요 기하학적 속성을 읽습니다.


### 
단계


1. 
소스 PDF에 대한 `PdfFileInfo` 개체를 만듭니다.

2. 
검사하려는 페이지에 대해 `getPageWidth`, `getPageHeight`, `getPageRotation`로 전화하세요.

3. 
반환된 값을 사용하거나 인쇄합니다.

4. 
`PdfFileInfo` 인스턴스를 닫습니다.


### 
자바 예

```java
public static void getPageInformation(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page Width: " + pdfInfo.getPageWidth(1));
    System.out.println("Page Height: " + pdfInfo.getPageHeight(1));
    System.out.println("Page Rotation: " + pdfInfo.getPageRotation(1));
    pdfInfo.close();
}
```
