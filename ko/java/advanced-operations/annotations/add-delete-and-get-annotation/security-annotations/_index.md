---
title: Java를 사용한 보안 주석
linktitle: 보안 주석
type: docs
weight: 75
url: /java/security-annotations/
description: Java용 Aspose.PDF를 사용하여 텍스트 수정을 표시하고, 수정 주석을 적용하고, PDF 파일에서 선택한 페이지 영역을 수정하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 보안 주석을 사용하여 Java에서 민감한 PDF 콘텐츠를 수정합니다.
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 편집 주석 작업을 수행하는 방법을 설명합니다. 교정 주석으로 일치하는 텍스트를 표시하고, 교정을 영구적으로 적용하고, 감지된 이미지 배치 직사각형을 기반으로 선택한 영역을 교정하는 방법을 다룹니다.
---

이 섹션의 보안 주석 작업 흐름은 중요한 PDF 콘텐츠에 대한 수정 준비 및 적용에 중점을 둡니다.


## 
교정 주석으로 텍스트 표시



교정이 영구적으로 적용되기 전에 교정 주석으로 일치하는 텍스트를 덮어야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
대상 텍스트를 검색하고 각 일치 항목에 대해 [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/)을 만듭니다.

1. 
교정 모양을 구성하고 문서를 저장합니다.


```java
public static void markTextRedaction(Path inputFile, Path outputFile, String searchTerm) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(searchTerm);
        TextSearchOptions textSearchOptions = new TextSearchOptions(true);
        textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
        document.getPages().accept(textFragmentAbsorber);

        for (var textFragment : textFragmentAbsorber.getTextFragments()) {
            Page page = textFragment.getPage();
            RedactionAnnotation redactionAnnotation = new RedactionAnnotation(page, textFragment.getRectangle());
            redactionAnnotation.setFillColor(Color.getGray());
            redactionAnnotation.setBorderColor(Color.getRed());
            redactionAnnotation.setColor(Color.getWhite());
            redactionAnnotation.setOverlayText("REDACTED");
            redactionAnnotation.setTextAlignment(HorizontalAlignment.Center);
            redactionAnnotation.setRepeat(true);
            page.getAnnotations().add(redactionAnnotation, true);
        }
        document.save(outputFile.toString());
    }
}
```

## 
기존 수정 적용



이 예에서는 페이지에 이미 존재하는 수정 주석을 영구적으로 적용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Redaction` 유형의 주석을 수집합니다.

1. 
수집된 각 주석에 대해 `redact()`을 호출하고 업데이트된 파일을 저장합니다.


```java
public static void applyRedaction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<RedactionAnnotation> redactionAnnotations = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Redaction) {
                redactionAnnotations.add((RedactionAnnotation) annotation);
            }
        }
        for (RedactionAnnotation redactionAnnotation : redactionAnnotations) {
            redactionAnnotation.redact();
        }
        document.save(outputFile.toString());
    }
}
```

## 
선택한 페이지 영역 수정



대상 콘텐츠가 일치하는 텍스트가 아닌 위치로 식별되는 경우 이 접근 방식을 사용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
예를 들어 이미지 배치에서 페이지의 대상 직사각형을 감지합니다.

1. 
해당 영역에 대한 [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/)을 만들고 문서를 저장합니다.


```java
public static void redactArea(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber imagePlacementAbsorber = new ImagePlacementAbsorber();
        Page page = document.getPages().get_Item(1);
        page.accept(imagePlacementAbsorber);

        com.aspose.pdf.Rectangle targetRect = imagePlacementAbsorber.getImagePlacements().get_Item(2).getRectangle();
        RedactionAnnotation redactionAnnotation = new RedactionAnnotation(page, targetRect);
        redactionAnnotation.setFillColor(Color.getGray());
        redactionAnnotation.setBorderColor(Color.getRed());
        redactionAnnotation.setColor(Color.getWhite());
        redactionAnnotation.setOverlayText("REDACTED");
        redactionAnnotation.setTextAlignment(HorizontalAlignment.Center);
        redactionAnnotation.setRepeat(true);

        page.getAnnotations().add(redactionAnnotation, true);
        document.save(outputFile.toString());
    }
}
```

## 
관련 주석 주제


- 
[대화형 주석](/pdf/java/interactive-annotations/)

- 
[마크업 주석](/pdf/java/markup-annotations/)

- 
[도형 주석](/pdf/java/shape-annotations/)

- 
[텍스트 주석](/pdf/java/text-based-annotations/)

- 
[워터마크 주석](/pdf/java/watermark-annotations/)

- 
[주석 가져오기 및 내보내기](/pdf/java/import-export-annotations/)
