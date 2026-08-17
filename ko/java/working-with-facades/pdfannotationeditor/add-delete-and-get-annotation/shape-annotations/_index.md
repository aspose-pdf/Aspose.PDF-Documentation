---
title: Java를 통한 모양 주석
linktitle: 모양 주석
type: docs
weight: 40
url: /java/pdfannotationeditor-class/shape-annotations/
description: Java를 사용하여 PDF 문서에서 정사각형, 원, 다각형 및 폴리라인 주석을 추가, 검사 및 삭제하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java에서 기하학적 PDF 주석 작업
Abstract: 이 문서에서는 Java를 사용하여 PDF 문서에서 기하학적 주석을 생성, 검사 및 제거하는 방법을 설명합니다. 색상, 불투명도, 팝업 및 점 구성을 통해 정사각형, 원, 다각형 및 폴리라인 주석을 다룹니다.
---
## 
모양 주석 추가


1. 
입력 PDF를 열고 모양 주석을 포함할 페이지와 직사각형을 선택합니다.

2. 
필요한 모양 주석을 생성한 다음 필요할 때 제목, 색상, 불투명도 및 점을 설정합니다.

3. 
페이지에 주석을 추가하고 수정된 PDF를 저장합니다.

```java
public static void squareAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SquareAnnotation squareAnnotation = new SquareAnnotation(
                document.getPages().get_Item(1), new Rectangle(60, 600, 250, 450, true));
        squareAnnotation.setTitle("John Smith");
        squareAnnotation.setColor(Color.getBlue());
        squareAnnotation.setInteriorColor(Color.getBlueViolet());
        squareAnnotation.setOpacity(0.25);

        document.getPages().get_Item(1).getAnnotations().add(squareAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void polygonAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PolygonAnnotation polygonAnnotation = new PolygonAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(200, 300, 400, 400, true),
                new Point[]{
                        new Point(200, 300),
                        new Point(220, 300),
                        new Point(250, 330),
                        new Point(300, 304),
                        new Point(300, 400)
                });
        polygonAnnotation.setTitle("John Smith");
        polygonAnnotation.setColor(Color.getBlue());
        polygonAnnotation.setInteriorColor(Color.getBlueViolet());
        polygonAnnotation.setOpacity(0.25);

        document.getPages().get_Item(1).getAnnotations().add(polygonAnnotation);
        document.save(outputFile.toString());
    }
}
```
