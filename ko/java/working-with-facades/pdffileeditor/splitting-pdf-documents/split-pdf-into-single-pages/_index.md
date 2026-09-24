---
title: PDF를 단일 페이지로 분할
linktitle: PDF를 단일 페이지로 분할
type: docs
weight: 30
url: /java/split-pdf-into-single-pages/
description: PdfFileEditor 파사드를 사용하여 PDF를 Java의 단일 페이지 출력 파일로 분할합니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF의 각 페이지를 자체 파일로 내보내기
Abstract: Java용 Aspose.PDF를 사용하여 PDF를 단일 페이지 파일로 분할하는 방법을 알아보세요. Java 예제에서는 PdfFileEditor를 사용하여 파일 이름 패턴을 기반으로 각 페이지를 개별 출력 PDF에 기록합니다.
---
## PDF를 단일 페이지로 분할



각 소스 페이지가 자체 PDF 파일이 되어야 하는 경우 이 워크플로우를 사용하십시오.


### 
단계


1. 
`PdfFileEditor` 인스턴스를 생성합니다.

2. 
`%NUM%`과 같은 페이지 자리 표시자가 포함된 출력 파일 패턴을 준비합니다.
3. 소스 파일과 출력 패턴을 사용하여 `splitToPages`을 호출합니다.

4. 
생성된 단일 페이지 파일을 저장합니다.

```java
public static void splitPdfIntoSinglePages(Path inputFile, Path outputFilePattern) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToPages(inputFile.toString(), outputFilePattern.toString());
}
```
