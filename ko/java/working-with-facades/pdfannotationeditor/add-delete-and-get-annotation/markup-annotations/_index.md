---
title: Java를 사용한 마크업 주석
linktitle: 마크업 주석
type: docs
weight: 20
url: /java/pdfannotationeditor-class/markup-annotations/
description: Java를 사용하여 PDF 문서에서 강조 표시, 밑줄, 물결선 및 취소선 주석을 추가, 검사 및 삭제하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일의 마크업 주석 작업
Abstract: 이 문서에서는 Java를 사용하여 PDF 문서에서 텍스트 마크업 주석을 생성, 검사 및 제거하는 방법을 설명합니다. 저장소 Java 예제를 기반으로 강조 표시, 밑줄, 물결 모양 및 취소선 주석을 다룹니다.
---
## 강조 표시, 밑줄, 구불구불한 선 또는 취소선 주석 추가


1. 
입력 PDF를 열고 마크업 주석이 표시되어야 하는 페이지 영역을 선택합니다.

2. 
필요한 주석 유형을 생성하고 해당 메타데이터 또는 시각적 속성을 구성합니다.

3. 
페이지 컬렉션에 주석을 추가하고 문서를 저장합니다.

```java
public static void addTextHighlightAnnotation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HighlightAnnotation highlightAnnotation = new HighlightAnnotation(
                document.getPages().get_Item(1), new Rectangle(300, 750, 320, 770, true));
        document.getPages().get_Item(1).getAnnotations().add(highlightAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void addTextUnderlineAnnotation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline 1");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());
        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```
