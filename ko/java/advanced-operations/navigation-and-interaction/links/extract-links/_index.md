---
title: Java에서 PDF 링크 추출
linktitle: 링크 추출
type: docs
weight: 30
url: /java/extract-links/
description: Java의 PDF 문서에서 링크 주석과 하이퍼링크를 추출하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에서 링크 주석 및 URI 대상 추출
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 링크 주석을 추출하는 방법을 설명합니다. 페이지의 링크 주석을 열거하고, 페이지 색인과 직사각형을 읽고, GoToURIAction 인스턴스에서 URI 대상을 추출하는 방법을 보여줍니다.
---
페이지 주석을 반복하고 `AnnotationType.Link`을 필터링하여 PDF 링크를 검사할 수 있습니다.


## 
링크 주석 추출



페이지의 링크 주석에 대한 위치 및 페이지 정보가 필요한 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지 주석을 반복하고 링크 주석을 필터링합니다.
1. 일치하는 각 링크에 대한 페이지 색인과 직사각형을 읽습니다.


```java
public static void extractLinkAnnotation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                System.out.println("Page: " + linkAnnotation.getPageIndex()
                        + ", location: " + linkAnnotation.getRect());
            }
        }
    }
}
```

## 
하이퍼링크 대상 추출



웹 링크 주석에서 대상 URI를 읽어야 할 때 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
작업이 [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/)인 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) 개체를 찾습니다.
1. 각 하이퍼링크에 대한 페이지 색인과 URI 대상을 인쇄합니다.

```java
public static void extractHyperlinks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                if (linkAnnotation.getAction() instanceof GoToURIAction) {
                    GoToURIAction action = (GoToURIAction) linkAnnotation.getAction();
                    System.out.println("Page " + linkAnnotation.getPageIndex() + ", URI:" + action.getURI());
                }
            }
        }
    }
}
```
