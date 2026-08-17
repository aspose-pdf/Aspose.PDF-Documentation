---
title: Java를 사용한 워터마크 주석
linktitle: 워터마크 주석
type: docs
weight: 70
url: /java/pdfannotationeditor-class/watermark-annotations/
description: Java를 사용하여 PDF 문서에서 워터마크 주석을 추가, 검사 및 삭제하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일의 워터마크 주석 작업
Abstract: 이 문서에서는 Java를 사용하여 PDF 문서에서 워터마크 주석을 생성, 검사 및 제거하는 방법을 설명합니다. 사용자 정의 텍스트 상태 및 불투명도로 텍스트 워터마크 주석 추가, 기존 워터마크 주석 영역 읽기 및 워터마크 주석 삭제를 다룹니다.
---
## 
워터마크 주석 추가


1. 
입력 PDF를 열고 워터마크 주석이 배치될 직사각형을 정의합니다.

2. 
`WatermarkAnnotation`을 생성하여 페이지에 추가하고 워터마크 텍스트 상태와 불투명도를 구성합니다.

3. 
워터마크 텍스트 줄을 적용하고 수정된 PDF를 저장합니다.

```java
public static void watermarkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        WatermarkAnnotation watermarkAnnotation = new WatermarkAnnotation(
                document.getPages().get_Item(1), new Rectangle(100, 0, 400, 100, true));

        document.getPages().get_Item(1).getAnnotations().add(watermarkAnnotation);

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
