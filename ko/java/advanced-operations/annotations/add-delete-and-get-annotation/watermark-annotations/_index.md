---
title: Java를 사용한 워터마크 주석
linktitle: 워터마크 주석
type: docs
weight: 70
url: /java/watermark-annotations/
description: Java용 Aspose.PDF를 사용하여 PDF 문서에서 워터마크 주석을 추가, 검사 및 삭제하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일의 워터마크 주석 작업을 수행합니다.
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 워터마크 주석을 생성, 검사 및 제거하는 방법을 설명합니다. 사용자 정의 텍스트 상태 및 불투명도로 텍스트 워터마크 주석 추가, 기존 워터마크 주석 영역 읽기 및 워터마크 주석 삭제를 다룹니다.
---

워터마크 주석을 사용하면 페이지에 재사용 가능한 오버레이 콘텐츠를 배치하는 동시에 주석 컬렉션을 통해 관리할 수 있습니다.


## 
워터마크 주석 추가



사용자 정의 글꼴 설정 및 불투명도가 포함된 텍스트 워터마크 주석이 필요한 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkannotation/)을 생성하여 페이지에 추가하세요.

1. 
[TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/), 워터마크 텍스트, 불투명도를 설정한 후 문서를 저장하세요.


```java
public static void watermarkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        WatermarkAnnotation watermarkAnnotation = new WatermarkAnnotation(
                page,
                new Rectangle(100, 100, 400, 200, true));

        page.getAnnotations().add(watermarkAnnotation);

        TextState textState = new TextState();
        textState.setForegroundColor(Color.getBlue());
        textState.setFontSize(25);
        textState.setFont(FontRepository.findFont("Arial"));

        watermarkAnnotation.setOpacity(0.5);
        watermarkAnnotation.setTextAndState(new String[]{"HELLO", "Line 1", "Line 2"}, textState);

        document.save(outputFile.toString());
    }
}
```

## 
워터마크 주석 받기



이 예에서는 주석 컬렉션을 스캔하고 각 워터마크 주석의 직사각형을 인쇄합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
대상 페이지의 주석을 반복합니다.

1. 
[AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark`으로 주석을 필터링하고 해당 직사각형을 인쇄합니다.


```java
public static void watermarkGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation a : document.getPages().get_Item(1).getAnnotations()) {
            if (a.getAnnotationType() == AnnotationType.Watermark) {
                System.out.println(a.getRect());
            }
        }
    }
}
```

## 
워터마크 주석 삭제



문서에서 기존 워터마크 주석을 제거해야 하는 경우 이 방법을 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark` 유형의 주석을 수집합니다.

1. 
수집된 주석을 삭제하고 출력 파일을 저장합니다.


```java
public static void watermarkDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation a : document.getPages().get_Item(1).getAnnotations()) {
            if (a.getAnnotationType() == AnnotationType.Watermark) {
                toDelete.add(a);
            }
        }
        for (Annotation a : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(a);
        }
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
[보안 주석](/pdf/java/security-annotations/)

- 
[도형 주석](/pdf/java/shape-annotations/)

- 
[텍스트 주석](/pdf/java/text-based-annotations/)

- 
[주석 가져오기 및 내보내기](/pdf/java/import-export-annotations/)
