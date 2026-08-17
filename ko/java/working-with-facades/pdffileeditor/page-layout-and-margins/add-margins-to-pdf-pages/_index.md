---
title: PDF 페이지에 여백 추가
linktitle: PDF 페이지에 여백 추가
type: docs
weight: 10
url: /java/add-margins-to-pdf-pages/
description: PdfFileEditor 외관을 사용하여 Java에서 선택한 PDF 페이지에 여백을 추가합니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 문서의 특정 페이지에 여백 추가
Abstract: Java용 Aspose.PDF를 사용하여 선택한 페이지에 여백을 추가하는 방법을 알아보세요. Java 예제에서는 PdfFileEditor를 사용하여 개별 페이지 번호를 대상으로 하고 동일한 위쪽, 아래쪽, 왼쪽 및 오른쪽 여백 값을 적용합니다.
---
## 
PDF 페이지에 여백 추가



Java 샘플은 소스 문서의 1페이지와 3페이지에 36포인트 여백을 추가합니다.


### 
단계


1. 
`PdfFileEditor` 인스턴스를 생성합니다.

2. 
새 여백을 적용할 페이지 번호를 선택하세요.

3. 
입력 파일, 출력 파일, 페이지 목록 및 여백 값을 사용하여 `addMargins`을 호출합니다.

4. 
업데이트된 PDF를 저장합니다.


### 
자바 예

```java
public static void addMarginsToPdfPages(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addMargins(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 36, 36, 36, 36);
}
```
