---
title: Java에서 PDF 책갈피 가져오기, 업데이트 및 확장
linktitle: 북마크 가져오기, 업데이트 및 확장
type: docs
weight: 20
url: /java/get-update-and-expand-bookmark/
description: Java를 사용하여 PDF 문서에서 북마크를 검색, 업데이트 및 확장하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 책갈피 속성을 검사하고 Java를 사용하여 PDF 파일의 개요를 확장합니다.
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 북마크를 읽고, 업데이트하고, 확장하는 방법을 설명합니다. 개요 항목 반복, PdfBookmarkEditor를 사용하여 책갈피 페이지 번호 추출, 하위 책갈피 읽기, 책갈피 제목 및 스타일 업데이트, 문서가 표시될 때 개요 강제 열기 등을 다룹니다.
---

Java용 Aspose.PDF는 문서 개요 모델과 `PdfBookmarkEditor` 외관을 통해 북마크를 노출합니다.


## 
북마크 속성 가져오기



문서 개요에서 최상위 책갈피 항목을 검사해야 할 때 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
개요 컬렉션을 반복합니다.

1. 
북마크 제목, 스타일, 색상 값을 읽고 인쇄합니다.


```java
public static void getBookmarks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection outlineItem = document.getOutlines().get_Item(i);
            System.out.println(outlineItem.getTitle());
            System.out.println(outlineItem.getItalic());
            System.out.println(outlineItem.getBold());
            System.out.println(outlineItem.getColor());
        }
    }
}
```

## 
북마크 페이지 번호 가져오기



이 예에서는 `PdfBookmarkEditor`을 사용하여 북마크 제목, 수준, 페이지 번호 및 작업을 추출합니다.


1. 
원본 PDF를 [PdfBookmarkEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdfbookmarkeditor/)에 바인딩합니다.

1. 
북마크 컬렉션을 추출하고 반복합니다.

1. 
각 북마크에 대한 레벨, 제목, 페이지 번호 및 작업 정보를 인쇄합니다.


```java
public static void getBookmarkPageNumber(Path inputFile) {
    PdfBookmarkEditor bookmarkEditor = new PdfBookmarkEditor();
    try {
        bookmarkEditor.bindPdf(inputFile.toString());
        for (Bookmark bookmark : bookmarkEditor.extractBookmarks()) {
            String levelSeparator = "";
            for (int i = 0; i < bookmark.getLevel(); i++) {
                levelSeparator += "----";
            }

            System.out.println(levelSeparator + " Title: " + bookmark.getTitle());
            System.out.println(levelSeparator + " Page Number: " + bookmark.getPageNumber());
            System.out.println(levelSeparator + " Page Action: " + bookmark.getAction());
        }
    } finally {
        bookmarkEditor.close();
    }
}
```

## 
어린이 북마크 받기



최상위 수준 항목과 중첩된 개요 항목을 모두 검사해야 하는 경우 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
최상위 개요를 반복하고 해당 속성을 인쇄합니다.

1. 
하위 북마크를 감지한 다음 이를 반복하고 해당 속성을 인쇄합니다.


```java
public static void getChildBookmarks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection outlineItem = document.getOutlines().get_Item(i);
            System.out.println(outlineItem.getTitle());
            System.out.println(outlineItem.getItalic());
            System.out.println(outlineItem.getBold());
            System.out.println(outlineItem.getColor());
            int count = outlineItem.size();
            if (count > 0) {
                System.out.println("Child Bookmarks");
                for (int j = 1; j <= outlineItem.size(); j++) {
                    OutlineItemCollection childOutlineItem = outlineItem.get_Item(j);
                    System.out.println(childOutlineItem.getTitle());
                    System.out.println(childOutlineItem.getItalic());
                    System.out.println(childOutlineItem.getBold());
                    System.out.println(childOutlineItem.getColor());
                }
            }
        }
    }
}
```

## 
북마크 업데이트



기존 북마크 제목과 스타일을 수정해야 하는 경우 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
대상 개요 항목과 해당 하위 책갈피에 액세스합니다.

1. 
책갈피 속성을 업데이트하고 문서를 저장합니다.


```java
public static void updateBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection outline = document.getOutlines().get_Item(1);
        OutlineItemCollection childOutline = outline.get_Item(1);
        childOutline.setTitle("Updated Outline");
        childOutline.setItalic(true);
        childOutline.setBold(true);

        document.save(outputFile.toString());
    }
}
```

## 
기본적으로 북마크 확장



책갈피 패널이 열려 문서가 표시될 때 확장된 개요 항목을 표시해야 하는 경우 이 예를 사용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
개요를 사용하도록 페이지 모드를 설정하고 각 개요 항목을 열린 것으로 표시합니다.

1. 
업데이트된 문서를 저장합니다.

```java
public static void expandedBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setPageMode(PageMode.UseOutlines);
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection item = document.getOutlines().get_Item(i);
            item.setOpen(true);
        }
        document.save(outputFile.toString());
    }
}
```
