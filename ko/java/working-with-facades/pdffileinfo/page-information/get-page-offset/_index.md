---
title: 페이지 오프셋 가져오기
linktitle: 페이지 오프셋 가져오기
type: docs
weight: 20
url: /java/get-page-offset/
description: PdfFileInfo 파사드를 사용하여 Java에서 페이지 X 및 Y 오프셋을 검사하는 방법을 알아보세요.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 페이지 오프셋 가져오기
Abstract: Java용 Aspose.PDF를 사용하여 페이지 오프셋을 검색하는 방법을 알아보세요. Java 예제에서는 PdfFileInfo를 사용하여 페이지 1의 X 및 Y 오프셋을 읽고 더 쉬운 레이아웃 분석을 위해 포인트 값을 인치로 변환합니다.
---
## 
페이지 오프셋 가져오기



페이지 내용이 PDF 원본을 기준으로 배치되는 방식을 이해해야 할 때 이 작업 과정을 사용하십시오.


### 
단계


1. 
입력 PDF에 대한 `PdfFileInfo` 개체를 만듭니다.

2. 
대상 페이지는 `getPageXOffset` 및 `getPageYOffset`로 전화하세요.

3. 
`72.0`으로 나누어 포인트 값을 인치로 변환합니다.

4. 
변환된 값을 사용하거나 인쇄합니다.

5. 
`PdfFileInfo` 인스턴스를 닫습니다.


### 
자바 예

```java
public static void getPageOffsets(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page X Offset: " + (pdfInfo.getPageXOffset(1) / 72.0) + " inches");
    System.out.println("Page Y Offset: " + (pdfInfo.getPageYOffset(1) / 72.0) + " inches");
    pdfInfo.close();
}
```
