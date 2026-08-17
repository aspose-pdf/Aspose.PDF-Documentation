---
title: PDF 페이지 내용 크기 조정
linktitle: PDF 페이지 내용 크기 조정
type: docs
weight: 30
url: /java/resize-pdf-page-contents/
description: PdfFileEditor 외관을 사용하여 Java에서 선택한 PDF 페이지의 내용 크기를 조정합니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 문서의 기존 페이지 내용 크기 조정
Abstract: Java용 Aspose.PDF를 사용하여 페이지 내용의 크기를 조정하는 방법을 알아보세요. Java 예제에서는 PdfFileEditor를 사용하여 특정 페이지를 대상으로 지정하고, 새로운 콘텐츠 너비와 높이를 적용하고, 크기 조정 작업이 실패할 경우 워크플로를 중지합니다.
---
## 
PDF 페이지 내용 크기 조정



Java 샘플은 1페이지와 3페이지의 콘텐츠 영역 크기를 조정하고 부울 반환 값을 확인합니다.


### 
단계


1. 
`PdfFileEditor` 인스턴스를 생성합니다.

2. 
콘텐츠 크기를 조정해야 하는 페이지를 선택합니다.

3. 
대상 너비와 높이를 사용하여 `resizeContents`을 호출하세요.

4. 
계속하기 전에 반환 값을 확인하고 실패를 처리하십시오.

5. 
업데이트된 문서를 저장합니다.


### 
자바 예

```java
public static void resizePdfPageContents(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    if (!pdfEditor.resizeContents(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 400, 750)) {
        throw new IllegalStateException("Failed to resize PDF page contents.");
    }
}
```
