---
title: 시청자 환경설정 가져오기
linktitle: 시청자 환경설정 가져오기
type: docs
weight: 10
url: /ko/java/get-viewer-preferences/
description: Aspose.PDF의 PdfContentEditor 파사드를 사용하여 Java에서 PDF 문서의 뷰어 기본 설정을 읽는 방법을 알아보세요.
lastmod: "2026-09-24"
TechArticle: true
AlternativeHeadline: Java에서 PDF 뷰어 기본 설정 읽기
Abstract: 이 문서에서는 Aspose.PDF for Java의 PdfContentEditor 외관을 사용하여 PDF를 바인딩하고 현재 뷰어 기본 설정 값을 인쇄하는 방법을 보여줍니다.
---
## 현재 시청자 환경설정 가져오기

1. 소스 PDF를 `PdfContentEditor` 파사드에 바인딩하세요.
2. 현재 값을 읽으려면 `getViewerPreference()`를 호출하세요.
3. 반환된 기본 설정 플래그를 검사하거나 인쇄하세요.

```java
public static void getViewerPreferences(Path inputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        System.out.println("Current viewer preference: " + editor.getViewerPreference());
    } finally {
        editor.close();
    }
}
```
