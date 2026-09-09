---
title: PDF에 페이지 삽입
linktitle: PDF에 페이지 삽입
type: docs
weight: 40
url: /java/insert-pages-into-pdf/
description: PdfFileEditor 외관을 사용하여 한 PDF에서 선택한 페이지를 Java의 다른 PDF에 삽입합니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 선택한 위치에 다른 PDF의 페이지 삽입
Abstract: Java용 Aspose.PDF를 사용하여 PDF에 페이지를 삽입하는 방법을 알아보세요. Java 예제에서는 PdfFileEditor를 사용하여 대상 PDF의 지정된 페이지 번호 뒤에 두 번째 문서에서 선택한 페이지를 삽입합니다.
---
## PDF에 페이지 삽입



Java 샘플은 대상 PDF의 2페이지 뒤에 보조 문서의 1페이지와 2페이지를 삽입합니다.


### 
단계


1. 
`PdfFileEditor` 인스턴스를 생성합니다.

2. 
대상 문서에서 삽입 지점을 선택합니다.
3. 원본 문서에서 복사할 페이지 번호를 선택합니다.

4. 
대상 파일, 삽입 지점, 소스 파일, 페이지 배열 및 출력 파일을 사용하여 `insert`을 호출합니다.

5. 
업데이트된 PDF를 저장합니다.


### 
자바 예

```java
public static void insertPagesIntoPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.insert(inputFile.toString(), 2, sampleFile.toString(), new int[] {1, 2}, outputFile.toString());
}
```
