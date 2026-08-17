---
title: Java에서 PDF 페이지 추가
linktitle: 페이지 추가
type: docs
weight: 10
url: /java/add-pages/
description: Java로 PDF 문서에 페이지를 추가하거나 삽입하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 페이지 추가 또는 삽입
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 파일에 페이지를 추가하는 방법을 설명합니다. 특정 위치에 빈 페이지를 삽입하고, 문서 끝에 페이지를 추가하고, 다른 PDF에서 페이지를 가져오는 방법을 다룹니다.
---

Aspose.PDF for Java를 사용하면 빈 페이지를 삽입하거나 다른 문서에서 페이지를 가져올 수 있습니다.


## 
특정 위치에 빈 페이지 삽입



기존 PDF 중간에 빈 페이지를 추가해야 할 때 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지 컬렉션의 대상 위치에 새 페이지를 삽입합니다.

1. 
업데이트된 문서를 저장합니다.


```java
public static void insertEmptyPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().insert(2);
        document.save(outputFile.toString());
    }
}
```

## 
끝에 빈 페이지 추가



새로운 빈 마지막 페이지로 문서를 확장해야 할 때 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지 컬렉션 끝에 새 페이지를 추가합니다.

1. 
수정된 PDF를 저장합니다.


```java
public static void addEmptyPageToEnd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();
        document.save(outputFile.toString());
    }
}
```

## 
다른 문서의 페이지 추가



한 PDF의 페이지를 다른 PDF로 가져오려는 경우 이 예를 사용하십시오.


1. 
대상 [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 생성하고 원본 문서를 엽니다.

1. 
필요한 대상 콘텐츠를 추가하고 소스 PDF에서 대상 페이지를 가져옵니다.

1. 
결과 문서를 저장합니다.

```java
public static void addPageFromAnotherDocument(Path inputFile, Path outputFile) {
    try (Document document = new Document();
         Document anotherDocument = new Document(inputFile.toString())) {
        document.getPages().add().getParagraphs().add(new TextFragment("This is first page!"));
        document.getPages().add(anotherDocument.getPages().get_Item(1));
        document.save(outputFile.toString());
    }
}
```
