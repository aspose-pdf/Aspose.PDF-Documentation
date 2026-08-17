---
title: PDF 소책자 만들기
linktitle: PDF 소책자 만들기
type: docs
weight: 20
url: /java/create-pdf-booklet/
description: PdfFileEditor 외관을 사용하여 Java의 기존 문서에서 소책자용 PDF를 만듭니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java로 PDF 문서에서 소책자 출력 생성
Abstract: Aspose.PDF for Java를 사용하여 PDF 소책자를 만드는 방법을 알아보세요. Java 예제에서는 PdfFileEditor를 사용하여 소책자 인쇄를 위해 페이지를 재정렬하고 간단한 성공 확인을 위한 부울 반환 변형도 포함합니다.
---
## 
PDF 소책자 만들기



`PdfFileEditor.makeBooklet`을 사용하여 기존 PDF의 페이지를 소책자 순서로 재정렬합니다.


### 
단계


1. 
`PdfFileEditor` 인스턴스를 생성합니다.

2. 
원본 PDF 및 출력 파일을 사용하여 `makeBooklet`으로 전화하세요.

3. 
소책자 문서를 저장합니다.

4. 
반환 상태를 확인하려면 boolean-return 변형을 사용하고 실패한 결과를 처리하세요.


### 
자바 예

```java
public static void createPdfBooklet(Path inputFile, Path outputFile) {
    PdfFileEditor bookletMaker = new PdfFileEditor();
    bookletMaker.makeBooklet(inputFile.toString(), outputFile.toString());
}

public static void tryCreatePdfBooklet(Path inputFile, Path outputFile) {
    PdfFileEditor bookletMaker = new PdfFileEditor();
    if (!bookletMaker.makeBooklet(inputFile.toString(), outputFile.toString())) {
        System.out.println("Failed to create booklet.");
    }
}
```
