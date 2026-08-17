---
title: Java에서 PDF 링크 업데이트
linktitle: 링크 업데이트
type: docs
weight: 20
url: /java/update-links/
description: Java에서 PDF 링크 모양과 대상을 업데이트하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일의 링크 주석 모양 및 웹 대상 업데이트
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 기존 링크 주석을 업데이트하는 방법을 보여줍니다. 예제에서는 링크에 포함된 텍스트 색상 변경, 링크 주석 색상 업데이트, 웹 링크의 대상 URI 교체를 보여줍니다.
---

기존 링크는 페이지에서 링크 주석을 찾아 해당 모양이나 작업을 업데이트하여 편집할 수 있습니다.


## 
연결된 텍스트 색상 업데이트



링크 주석으로 덮힌 텍스트 영역을 다시 칠해야 할 때 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
링크 주석을 찾고 각 주석 영역에서 텍스트 검색 직사각형을 만듭니다.

1. 
일치하는 텍스트 조각을 다시 칠하고 문서를 저장합니다.


```java
public static void linkAnnotationUpdateTextColor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                TextFragmentAbsorber absorber = new TextFragmentAbsorber();
                Rectangle rect = annotation.getRect();
                rect.setLLX(rect.getLLX() - 2);
                rect.setLLY(rect.getLLY() - 2);
                rect.setURX(rect.getURX() + 2);
                rect.setURY(rect.getURY() + 2);
                absorber.setTextSearchOptions(new TextSearchOptions(rect));
                absorber.visit(document.getPages().get_Item(1));
                for (TextFragment textFragment : absorber.getTextFragments()) {
                    textFragment.getTextState().setForegroundColor(Color.getRed());
                }
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 
링크 테두리 색상 업데이트



기존 링크 주석의 표시 색상을 변경해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지 주석을 반복하고 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) 개체를 필터링합니다.

1. 
링크 주석 색상을 업데이트하고 문서를 저장합니다.


```java
public static void linkAnnotationUpdateBorder(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                linkAnnotation.setColor(Color.getRed());
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 
웹 링크 대상 업데이트



기존 웹 링크가 새 URI를 가리켜야 하는 경우 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
작업이 [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/)인 링크 주석을 찾습니다.

1. 
URI를 바꾸고 업데이트된 문서를 저장합니다.

```java
public static void linkAnnotationUpdateWebDestination(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                if (linkAnnotation.getAction() instanceof GoToURIAction) {
                    GoToURIAction action = (GoToURIAction) linkAnnotation.getAction();
                    action.setURI("https://www.aspose.com");
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```
