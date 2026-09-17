---
title: PDF를 끝까지 분할
linktitle: PDF를 끝까지 분할
type: docs
weight: 40
url: /java/split-pdf-to-end/
description: PdfFileEditor 외관을 사용하여 선택한 페이지에서 Java 끝까지 PDF를 분할합니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF의 시작 지점부터 끝까지 페이지를 추출합니다.
Abstract: Java용 Aspose.PDF를 사용하여 PDF를 끝까지 분할하는 방법을 알아보세요. Java 예제에서는 PdfFileEditor를 사용하여 2페이지부터 소스 문서 끝까지 모든 페이지를 추출합니다.
---
## PDF를 분할하여 종료



Java 샘플은 2페이지부터 모든 페이지를 추출합니다.


### 
단계


1. 
`PdfFileEditor` 인스턴스를 생성합니다.

2. 
소스 파일, 시작 페이지 번호, 출력 파일을 포함하여 `splitToEnd`을 호출하세요.
3. 결과 PDF 문서를 저장합니다.

```java
public static void splitPdfToEnd(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToEnd(inputFile.toString(), 2, outputFile.toString());
}
```
