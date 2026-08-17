---
title: Java에서 PDF 파일 병합
linktitle: PDF 파일 병합
type: docs
weight: 50
url: /java/merge-pdf/
description: Aspose.PDF를 사용하여 Java에서 여러 PDF 파일을 단일 문서로 병합하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 페이지 결합
Abstract: 이 문서에서는 Aspose.PDF를 사용하여 Java에서 두 PDF 문서를 병합하는 방법을 설명합니다. 이 예제에서는 두 개의 소스 문서를 열고 두 번째 문서의 페이지를 첫 번째 문서에 추가한 다음 병합된 결과를 새 PDF 파일로 저장합니다.
---

PDF 파일 병합은 배포, 보관 또는 처리를 위해 관련 문서를 단일 파일로 결합해야 할 때 유용합니다.


## 
실제 사례



[Aspose.PDF Merger](https://products.aspose.app/pdf/merger)는 브라우저에서 PDF 병합을 테스트하기 위한 무료 온라인 애플리케이션입니다.



이 항목에서는 Java에서 여러 PDF 파일을 단일 문서로 병합하는 방법을 보여줍니다.


1. 
[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 생성자를 사용하여 두 소스 문서를 모두 엽니다.

1. 
`document1.getPages().add(document2.getPages())`을 사용하여 두 번째 [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)의 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 컬렉션을 첫 번째 컬렉션에 추가합니다.

1. 
병합된 [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 출력 경로에 저장합니다.


## 
두 개의 PDF 문서 병합



다음 Java 예제는 `MergeDocumentExamples.java`을 기반으로 합니다.

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```
