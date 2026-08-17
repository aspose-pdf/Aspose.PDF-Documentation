---
title: PDF에서 페이지 삭제
linktitle: PDF에서 페이지 삭제
type: docs
weight: 20
url: /java/delete-pages-from-pdf/
description: PdfFileEditor 파사드를 사용하여 Java의 PDF에서 선택한 페이지를 삭제합니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 문서에서 특정 페이지 제거
Abstract: Java용 Aspose.PDF를 사용하여 PDF에서 페이지를 삭제하는 방법을 알아보세요. Java 예제에서는 PdfFileEditor를 사용하여 정의된 페이지 번호 집합을 제거하고 나머지 페이지를 새 문서로 저장합니다.
---
## 
PDF에서 페이지 삭제



Java 샘플은 소스 문서에서 2페이지와 4페이지를 제거합니다.


### 
단계


1. 
`PdfFileEditor` 인스턴스를 생성합니다.

2. 
제거할 페이지 번호로 배열을 만듭니다.

3. 
입력 파일, 페이지 배열 및 출력 파일을 사용하여 `delete`을 호출합니다.

4. 
결과 PDF를 저장합니다.


### 
자바 예

```java
public static void deletePagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.delete(inputFile.toString(), new int[] {2, 4}, outputFile.toString());
}
```
