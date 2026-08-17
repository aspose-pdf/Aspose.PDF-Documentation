---
title: Java에서 PDF 책갈피 추가 및 삭제
linktitle: 북마크 추가 및 삭제
type: docs
weight: 10
url: /java/add-and-delete-bookmark/
description: Java를 사용하여 PDF 문서에 책갈피를 추가하고 삭제하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 문서에 책갈피 추가 또는 제거
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 북마크를 만들고 삭제하는 방법을 보여줍니다. 예제에서는 최상위 책갈피 추가, 하위 책갈피 계층 생성, 모든 책갈피 삭제 및 제목별로 특정 책갈피 제거를 보여줍니다.
---

프로그래밍 방식으로 책갈피를 관리하려면 문서 개요 컬렉션을 사용하세요.


## 
최상위 북마크 추가



문서에 단일 최상위 개요 항목이 포함되어야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/)을 만들고 제목, 스타일, 작업을 구성합니다.

1. 
문서 개요에 책갈피를 추가하고 파일을 저장합니다.


```java
public static void addBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection pdfOutline = new OutlineItemCollection(document.getOutlines());
        pdfOutline.setTitle("Test Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);
        pdfOutline.setAction(new GoToAction(document.getPages().get_Item(1)));

        document.getOutlines().add(pdfOutline);
        document.save(outputFile.toString());
    }
}
```

## 
하위 북마크 추가



이 예에서는 상위 책갈피를 만들고 그 아래에 하위 책갈피를 중첩합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
상위 및 하위 [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) 개체를 만듭니다.

1. 
상위 항목에 하위 항목을 추가하고 개요 컬렉션에 상위 항목을 추가한 후 문서를 저장합니다.


```java
public static void addChildBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection pdfOutline = new OutlineItemCollection(document.getOutlines());
        pdfOutline.setTitle("Parent Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        OutlineItemCollection pdfChildOutline = new OutlineItemCollection(document.getOutlines());
        pdfChildOutline.setTitle("Child Outline");
        pdfChildOutline.setItalic(true);
        pdfChildOutline.setBold(true);

        pdfOutline.add(pdfChildOutline);
        document.getOutlines().add(pdfOutline);
        document.save(outputFile.toString());
    }
}
```

## 
모든 북마크 삭제



문서에서 전체 개요 컬렉션을 제거해야 하는 경우 이 방법을 사용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
전체 개요 컬렉션을 삭제합니다.

1. 
정리된 출력 파일을 저장합니다.


```java
public static void deleteBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete();
        document.save(outputFile.toString());
    }
}
```

## 
특정 북마크 삭제



전체 개요 트리를 지우지 않고 이름이 지정된 하나의 책갈피를 제거해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
개요 컬렉션에서 제목별로 책갈피를 삭제합니다.

1. 
업데이트된 문서를 저장합니다.

```java
public static void deleteBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete("Child Outline");
        document.save(outputFile.toString());
    }
}
```
