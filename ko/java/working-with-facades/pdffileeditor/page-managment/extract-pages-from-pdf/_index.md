---
title: PDF에서 페이지 추출
linktitle: PDF에서 페이지 추출
type: docs
weight: 30
url: /java/extract-pages-from-pdf/
description: PdfFileEditor 파사드를 사용하여 Java의 PDF에서 선택한 페이지를 추출합니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 선택한 PDF 페이지를 새 문서로 추출
Abstract: Java용 Aspose.PDF를 사용하여 PDF에서 페이지를 추출하는 방법을 알아보세요. Java 예제에서는 PdfFileEditor를 사용하여 특정 페이지 번호를 수집하고 이를 별도의 출력 PDF에 기록합니다.
---
## 
PDF에서 페이지 추출



Java 샘플은 페이지 1, 4, 3을 새 PDF 문서로 추출합니다.


### 
단계


1. 
`PdfFileEditor` 인스턴스를 생성합니다.

2. 
추출할 페이지 번호를 정의합니다.

3. 
소스 파일, 페이지 배열 및 출력 파일을 사용하여 `extract`을 호출합니다.

4. 
추출된 페이지를 새 PDF로 저장합니다.


### 
자바 예

```java
public static void extractPagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.extract(inputFile.toString(), new int[] {1, 4, 3}, outputFile.toString());
}
```
