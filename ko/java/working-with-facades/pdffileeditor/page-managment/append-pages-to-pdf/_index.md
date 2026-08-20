---
title: PDF에 페이지 추가
linktitle: PDF에 페이지 추가
type: docs
weight: 10
url: /java/append-pages-to-pdf/
description: PdfFileEditor 외관을 사용하여 Java에서 한 PDF의 페이지를 다른 PDF에 추가합니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 한 PDF 문서의 페이지 범위를 다른 PDF 문서에 추가합니다.
Abstract: Java용 Aspose.PDF를 사용하여 PDF에 페이지를 추가하는 방법을 알아보세요. Java 예제에서는 PdfFileEditor를 사용하여 다른 문서에서 선택한 페이지 범위를 현재 PDF 끝에 추가합니다.
---
## PDF에 페이지 추가



Java 샘플은 두 번째 PDF의 1페이지를 첫 번째 문서의 끝에 추가합니다.


### 
단계


1. 
`PdfFileEditor` 인스턴스를 생성합니다.

2. 
해당 경로를 `append`에 전달하여 기본 입력 PDF를 바인딩합니다.
3. 추가할 보조 소스 파일 목록과 페이지 범위를 제공합니다.

4. 
병합된 결과를 출력 파일에 저장합니다.


### 
자바 예

```java
public static void appendPagesToPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.append(inputFile.toString(), new String[] {sampleFile.toString()}, 1, 1, outputFile.toString());
}
```
