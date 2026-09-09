---
title: 스탬프 목록
linktitle: 스탬프 목록
type: docs
weight: 20
url: /java/list-stamps/
description: Aspose.PDF의 PdfContentEditor 외관을 사용하여 Java 페이지에 도장을 나열하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java로 PDF 고무 스탬프 나열
Abstract: 이 문서에서는 PDF를 바인딩하고, 페이지에서 스탬프를 검색하고, Aspose.PDF for Java의 PdfContentEditor 파사드를 사용하여 결과 컬렉션을 검사하는 방법을 보여줍니다.
---
## 페이지에 스탬프 나열


1. 
소스 PDF를 `PdfContentEditor` 파사드에 바인딩합니다.

2. 
대상 페이지의 스탬프를 검색하려면 `getStamps(pageNumber)`으로 전화하세요.

3. 
결과 `StampInfo[]` 컬렉션을 검사합니다.

```java
public static void listStamps(Path inputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        StampInfo[] stamps = editor.getStamps(1);
        System.out.println("Stamps on page 1: " + stamps.length);
    } finally {
        editor.close();
    }
}
```
