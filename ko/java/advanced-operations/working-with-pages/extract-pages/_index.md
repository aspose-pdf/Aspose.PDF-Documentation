---
title: Java에서 PDF 페이지 추출
linktitle: PDF 페이지 추출
type: docs
weight: 80
url: /java/extract-pages/
description: Java에서 단일 또는 여러 PDF 페이지를 새 파일로 추출하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 페이지를 새 문서로 추출
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 파일에서 페이지를 추출하는 방법을 설명합니다. 1 기반 페이지 인덱싱을 사용하여 단일 페이지를 복사하고 여러 페이지를 별도의 대상 문서로 추출하는 방법을 다룹니다.
---

Aspose.PDF for Java를 사용하면 선택한 페이지를 새 대상 문서로 복사할 수 있습니다.


## 
단일 페이지 추출



소스 PDF의 한 페이지를 별도의 문서로 저장해야 하는 경우 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 대상 문서를 만듭니다.

1. 
대상 페이지를 대상 페이지 컬렉션에 복사합니다.

1. 
새 PDF를 저장합니다.


```java
public static void extractPage(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        dstDocument.getPages().add(srcDocument.getPages().get_Item(2));
        dstDocument.save(outputFile.toString());
    }
}
```

## 
여러 페이지 추출



여러 페이지를 별도의 PDF로 복사해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 대상 문서를 만듭니다.

1. 
선택한 페이지 인덱스를 반복하여 대상에 추가합니다.

1. 
추출된 페이지 문서를 저장합니다.

```java
public static void extractBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString());
         Document anotherDocument = new Document()) {
        Integer[] pages = {2, 3};
        for (Integer pageIndex : pages) {
            anotherDocument.getPages().add(document.getPages().get_Item(pageIndex));
        }
        anotherDocument.save(outputFile.toString());
    }
}
```
