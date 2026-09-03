---
title: 처음부터 PDF 분할
linktitle: 처음부터 PDF 분할
type: docs
weight: 10
url: /java/split-pdf-from-beginning/
description: PdfFileEditor 외관을 사용하여 Java에서 처음부터 PDF를 분할합니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF의 첫 페이지를 새 문서로 추출
Abstract: Java용 Aspose.PDF를 사용하여 처음부터 PDF를 분할하는 방법을 알아보세요. Java 예제에서는 PdfFileEditor를 사용하여 문서의 처음 세 페이지를 가져와 별도의 PDF로 저장합니다.
---
## 처음부터 PDF 분할



Java 샘플은 소스 문서에서 처음 세 페이지를 추출합니다.


### 
단계


1. 
`PdfFileEditor` 인스턴스를 생성합니다.

2. 
소스 파일, 보관할 페이지 수, 출력 파일과 함께 `splitFromFirst`을 호출하세요.
3. 새 PDF 문서를 저장합니다.

```java
public static void splitPdfFromBeginning(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitFromFirst(inputFile.toString(), 3, outputFile.toString());
}
```
