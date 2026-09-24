---
title: Java에서 PDF 페이지 크기 변경
linktitle: 페이지 크기 변경
type: docs
weight: 40
url: /java/change-page-size/
description: Java에서 PDF 페이지 크기를 읽고 변경하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 페이지 크기 및 상자 읽기 및 업데이트
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 페이지 크기를 읽고 수정하는 방법을 보여줍니다. 페이지 크기 가져오기, 회전이 적용된 페이지 크기 측정, 변경 전후의 상자 치수를 인쇄하는 동안 첫 번째 페이지를 새 크기로 업데이트하는 방법을 다룹니다.
---
Aspose.PDF for Java는 페이지 크기를 보고하고 업데이트할 수 있습니다.


## 
페이지 크기 변경



기존 페이지의 크기를 조정하고 변경 전후의 페이지 상자를 검사해야 할 때 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)을 가져오고 현재 상자 값을 인쇄합니다.
1. 새 페이지 크기를 설정하고 문서를 저장합니다.

```java
public static void setPageSize(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        printBoxes("Before set", page);
        page.setPageSize(597.6, 842.4);
        printBoxes("After set", page);
        document.save(outputFile.toString());
    }
}
```

## 페이지 크기 가져오기

페이지의 표시되는 크기를 읽어야 할 때 이 예를 사용하십시오.

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.
1. 회전 처리가 활성화된 페이지 직사각형을 가져옵니다.
1. 페이지 너비와 높이를 출력합니다.


```java
public static void getPageSize(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rectangle = document.getPages().get_Item(1).getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```

## 
회전이 적용된 페이지 크기 가져오기



회전을 고려하기 전과 후에 페이지 크기를 비교해야 할 때 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)을 회전합니다.
1. 회전 처리 유무와 관계없이 페이지 직사각형을 읽고 두 값을 모두 출력합니다.

```java
public static void getPageSizeRotation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.setRotate(Rotation.on90);
        Rectangle rectangle = page.getPageRect(false);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
        rectangle = page.getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```
