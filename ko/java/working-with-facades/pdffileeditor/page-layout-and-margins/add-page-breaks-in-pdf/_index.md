---
title: PDF에 페이지 나누기 추가
linktitle: PDF에 페이지 나누기 추가
type: docs
weight: 20
url: /java/add-page-breaks-in-pdf/
description: PdfFileEditor 파사드를 사용하여 Java에서 PDF에 페이지 나누기를 삽입합니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 문서의 고정 위치에 페이지 나누기 삽입
Abstract: Java용 Aspose.PDF를 사용하여 페이지 나누기를 추가하는 방법을 알아보세요. Java 예제에서는 PdfFileEditor.PageBreak를 사용하여 특정 수직 위치에서 페이지를 분할하고 결과를 새 PDF로 저장합니다.
---
## PDF에 페이지 나누기 추가



페이지를 알려진 Y 위치에서 여러 페이지로 분할해야 하는 경우 이 작업 흐름을 사용합니다.


### 
단계


1. 
`PdfFileEditor` 인스턴스를 생성합니다.

2. 
페이지 번호와 구분 위치를 사용하여 하나 이상의 `PdfFileEditor.PageBreak` 항목을 만듭니다.
3. 페이지 나누기 배열을 `addPageBreak`에 전달합니다.

4. 
업데이트된 PDF 문서를 저장합니다.


### 
자바 예

```java
public static void addPageBreaksInPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addPageBreak(inputFile.toString(), outputFile.toString(), new PdfFileEditor.PageBreak[] {
            new PdfFileEditor.PageBreak(1, 400)
    });
}
```
