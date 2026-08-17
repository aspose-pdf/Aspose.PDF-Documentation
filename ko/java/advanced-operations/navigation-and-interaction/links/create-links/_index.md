---
title: Java에서 PDF 링크 만들기
linktitle: 링크 생성
type: docs
weight: 10
url: /java/create-links/
description: Java로 내부, 외부 및 원격 PDF 링크를 만드는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에 링크 주석 만들기
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 링크 주석을 만드는 방법을 보여줍니다. LinkAnnotation 개체에 작업을 연결하여 실행 작업, 원격 문서 탐색, 문서 내 페이지 탐색 및 URI 기반 웹 링크를 다룹니다.
---

Aspose.PDF for Java는 `LinkAnnotation`을 작업 개체와 함께 사용하여 링크 동작을 정의합니다.


## 
실행-작업 링크 생성



링크 주석이 외부 파일이나 대상을 시작해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 대상 페이지를 선택합니다.

1. 
[LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/)을 생성하고 테두리와 색상을 구성합니다.

1. 
[LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/launchaction/)을 할당하고 문서를 저장합니다.


```java
public static void createLinkAnnotationLaunchAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        Border border = new Border(link);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        link.setBorder(border);
        link.setColor(Color.getGreen());
        link.setAction(new LaunchAction(document, inputFile.toString()));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## 
원격 이동 링크 만들기



링크가 다른 PDF 문서의 페이지를 열어야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
대상 페이지에 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/)을 생성합니다.

1. 
[GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoremoteaction/)을 할당하고 출력 파일을 저장합니다.


```java
public static void createLinkAnnotationGoToRemoteAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        link.setColor(Color.getGreen());
        link.setAction(new GoToRemoteAction(inputFile.toString(), 1));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## 
내부 이동 링크 만들기



링크가 동일한 PDF 문서 내의 다른 페이지로 이동해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/)을 생성하고 모양을 구성합니다.

1. 
대상 페이지에 [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/)을 할당하고 문서를 저장합니다.


```java
public static void createLinkAnnotationGoToAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        Border border = new Border(link);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        link.setBorder(border);
        link.setColor(Color.getGreen());
        if (document.getPages().size() >= 4) {
            link.setAction(new GoToAction(document.getPages().get_Item(4)));
        } else {
            link.setAction(new GoToAction(document.getPages().get_Item(document.getPages().size())));
        }
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## 
URI 링크 만들기



링크가 URI 작업을 통해 웹 리소스를 열어야 하는 경우 이 예를 사용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지에 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/)을 생성하세요.

1. 
[GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/)을 할당하고 출력 파일을 저장합니다.

```java
public static void createLinkAnnotationGoToUriAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        link.setColor(Color.getGreen());
        link.setAction(new GoToURIAction("https://docs.aspose.com/pdf/python"));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```
