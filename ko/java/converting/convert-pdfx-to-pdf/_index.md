---
title: Java에서 PDF/A 및 PDF/UA를 PDF로 변환
linktitle: PDF/A 및 PDF/UA를 PDF로 변환
type: docs
weight: 120
url: /java/convert-pdf_x-to-pdf/
lastmod: "2026-06-16"
description: Java의 표준 기반 PDF 파일에서 PDF/A 및 PDF/UA 규정 준수를 제거하고 이를 표준 PDF 문서로 저장하는 방법을 알아보세요.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Java에서 PDF/A 및 PDF/UA를 표준 PDF로 변환하는 방법
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 표준 기반 PDF 문서에서 PDF/A 및 PDF/UA 규격을 제거한 다음 결과를 표준 PDF 파일로 저장하는 방법을 설명합니다.
---

Java용 Aspose.PDF는 표준을 준수하는 PDF 변형을 다시 일반 PDF 문서로 변환할 수 있습니다.


## 
PDF/A를 표준 PDF로 변환



보관 PDF/A 문서를 표준 PDF로 다운그레이드해야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF/A 파일을 엽니다.

1. 
로드된 문서에서 보관 규정 준수 프로필을 분리하려면 `removePdfaCompliance()`으로 전화하세요.

1. 
PDF/A 제한 세트 없이 결과 표준 PDF 파일을 저장합니다.


```java
public static void convertPdfAToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfaCompliance();
        document.save(outputFile.toString());
    }
}
```

## 
PDF/UA를 표준 PDF로 변환



액세스 가능한 PDF/UA 문서를 표준 PDF로 다시 변환해야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF/UA 파일을 엽니다.

1. 
문서 메타데이터 및 구조 요구 사항에서 접근성 규정 준수 프로필을 제거하려면 `removePdfUaCompliance()`으로 전화하세요.

1. 
결과 PDF 문서를 일반 PDF 파일로 저장합니다.

```java
public static void convertPdfUaToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfUaCompliance();
        document.save(outputFile.toString());
    }
}
```
