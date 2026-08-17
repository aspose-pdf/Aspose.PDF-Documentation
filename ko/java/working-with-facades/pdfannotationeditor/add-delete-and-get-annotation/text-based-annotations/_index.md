---
title: Java를 사용한 텍스트 기반 주석
linktitle: 텍스트 주석
type: docs
weight: 10
url: /java/pdfannotationeditor-class/text-based-annotations/
description: Java를 사용하여 PDF 문서에서 텍스트, 자유 텍스트 및 취소선 주석을 추가, 검사 및 삭제하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java에서 텍스트 PDF 주석 작업
Abstract: 이 문서에서는 Java를 사용하여 PDF 문서에서 텍스트 기반 주석을 만들고 읽고 제거하는 방법을 설명합니다. Java 예제 구현을 기반으로 하는 텍스트 주석, 자유 텍스트 주석 및 취소선 주석을 다룹니다.
---
## 
텍스트 주석 추가


1. 
입력 PDF를 열고 텍스트 주석을 배치할 페이지를 대상으로 지정합니다.

2. 
`TextAnnotation`을 만들고 직사각형을 정의하고 제목, 제목, 플래그 및 색상을 설정합니다.

3. 
페이지에 주석을 추가하고 업데이트된 문서를 저장합니다.


```java
public static void textAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextAnnotation textAnnotation = new TextAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 613.664, 428.708, 680.769, true));
        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Inserted text 1");
        textAnnotation.setFlags(AnnotationFlags.Print);
        textAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(textAnnotation, false);
        document.save(outputFile.toString());
    }
}
```

## 
자유 텍스트 주석 추가


1. 
소스 PDF를 로드하고 자유 텍스트 메모의 대상 페이지와 직사각형을 선택합니다.

2. 
`FreeTextAnnotation`을 생성하고 기본 모양을 초기화한 다음 제목과 색상을 설정합니다.

3. 
페이지에 주석을 추가하고 결과를 저장합니다.

```java
public static void freeTextAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299, 713, 308, 720, true),
                new DefaultAppearance());
        freeTextAnnotation.setTitle("Aspose User");
        freeTextAnnotation.setColor(Color.getLightGreen());

        document.getPages().get_Item(1).getAnnotations().add(freeTextAnnotation);
        document.save(outputFile.toString());
    }
}
```
