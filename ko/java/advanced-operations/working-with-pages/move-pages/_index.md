---
title: Java에서 PDF 페이지 이동
linktitle: PDF 페이지 이동
type: docs
weight: 100
url: /java/move-pages/
description: 문서 내에서 또는 Java 문서 간에 PDF 페이지를 이동하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java 문서 간 PDF 페이지 이동
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF에서 페이지를 이동하는 방법을 설명합니다. 단일 페이지 또는 여러 페이지를 다른 문서로 이동하고 동일한 PDF 내에서 페이지 위치를 변경하는 방법을 다룹니다.
---

Aspose.PDF for Java를 사용하면 문서 간에 페이지를 이동하거나 동일한 PDF 내에서 페이지 위치를 변경할 수 있습니다.


## 
페이지를 다른 문서로 이동



소스 PDF에서 단일 페이지를 제거하고 별도의 문서에 저장해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 대상 문서를 만듭니다.

1. 
대상 페이지를 대상에 추가하고 소스에서 삭제합니다.

1. 
두 문서를 모두 저장합니다.


```java
public static void movePageFromOneDocumentToAnother(Path inputFile, Path sourceOutputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString());
         Document anotherDocument = new Document()) {
        anotherDocument.getPages().add(document.getPages().get_Item(2));
        document.getPages().delete(2);
        document.save(sourceOutputFile.toString());
        anotherDocument.save(outputFile.toString());
    }
}
```

## 
여러 페이지를 다른 문서로 이동



여러 페이지를 소스 PDF에서 새 문서로 전송해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 대상 문서를 만듭니다.

1. 
선택한 페이지를 대상 문서에 복사합니다.

1. 
원본에서 이동된 페이지를 삭제하고 두 파일을 모두 저장합니다.


```java
public static void moveBunchPagesFromOneDocumentToAnother(Path inputFile, Path sourceOutputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        Integer[] pages = {1, 2};
        for (Integer pageIndex : pages) {
            dstDocument.getPages().add(srcDocument.getPages().get_Item(pageIndex));
        }
        dstDocument.save(outputFile.toString());
        srcDocument.getPages().delete(pages);
        srcDocument.save(sourceOutputFile.toString());
    }
}
```

## 
동일한 문서 내에서 페이지 이동



동일한 PDF에서 페이지의 위치를 새 위치로 변경해야 하는 경우 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
대상 페이지를 새 위치에 복제하고 원본 페이지 항목을 제거합니다.

1. 
재정렬된 문서를 저장합니다.

```java
public static void movePageInNewLocationInSameDocument(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString())) {
        srcDocument.getPages().add(srcDocument.getPages().get_Item(2));
        srcDocument.getPages().delete(2);
        srcDocument.save(outputFile.toString());
    }
}
```
