---
title: Java에서 PDF 페이지 삭제
linktitle: PDF 페이지 삭제
type: docs
weight: 80
url: /java/delete-pages/
description: Java에서 PDF 파일의 페이지를 삭제하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 하나 이상의 PDF 페이지 삭제
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 파일에서 페이지를 제거하는 방법을 설명합니다. 페이지 컬렉션 API를 통해 단일 페이지 삭제와 여러 페이지를 한 번에 삭제하는 방법을 다룹니다.
---

PDF에서 하나 이상의 페이지를 제거해야 하는 경우 문서 페이지 컬렉션을 사용하세요.


## 
단일 페이지 삭제



색인별로 한 페이지를 제거해야 할 때 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지 컬렉션에서 대상 페이지를 삭제합니다.

1. 
업데이트된 문서를 저장합니다.


```java
public static void deletePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(2);
        document.save(outputFile.toString());
    }
}
```

## 
여러 페이지 삭제



한 번의 작업으로 여러 페이지를 제거해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지 컬렉션에서 삭제할 페이지 인덱스를 전달합니다.

1. 
수정된 PDF를 저장합니다.

```java
public static void deleteBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(new Integer[]{2, 3, 4});
        document.save(outputFile.toString());
    }
}
```
