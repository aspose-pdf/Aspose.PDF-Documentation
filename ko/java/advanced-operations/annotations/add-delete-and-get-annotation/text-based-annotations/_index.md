---
title: Java를 사용한 텍스트 기반 주석
linktitle: 텍스트 주석
type: docs
weight: 10
url: /java/text-based-annotations/
description: Java용 Aspose.PDF를 사용하여 PDF 문서에서 텍스트, 자유 텍스트 및 취소선 주석을 추가, 검사 및 삭제하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 텍스트 PDF 주석을 사용하여 작업합니다.
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 텍스트 기반 주석을 만들고 읽고 제거하는 방법을 설명합니다. Java 예제 구현을 기반으로 하는 텍스트 주석, 자유 텍스트 주석 및 취소선 주석을 다룹니다.
---

이 섹션의 텍스트 기반 주석 작업 흐름은 자유 텍스트, 강조 표시, 취소선, 물결선 및 밑줄 시나리오를 다룹니다.


## 
자유 텍스트 주석 추가, 가져오기 및 삭제



편집 가능한 텍스트 메모를 배치하거나 검사하거나 페이지에서 제거해야 할 때 다음 예제를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지에서 [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/freetextannotation/) 개체를 생성, 검색, 수집합니다.

1. 
주석을 추가하거나 삭제할 때 업데이트된 문서를 저장하세요.


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

```java
public static void freeTextAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FreeText) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void freeTextAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FreeText) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## 
하이라이트 주석 추가, 가져오기 및 삭제



이 예에서는 강조 마크업을 생성하고 기존 강조 주석을 검사하고 제거하는 방법을 보여줍니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지에서 [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) 개체를 사용하여 작업합니다.

1. 
주석을 추가하거나 삭제한 후 문서를 저장하세요.


```java
public static void textHighlightAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HighlightAnnotation highlightAnnotation = new HighlightAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(300, 750, 320, 770, true));

        document.getPages().get_Item(1).getAnnotations().add(highlightAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void textHighlightAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void textHighlightAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## 
취소선 주석 추가, 가져오기, 삭제



텍스트 범위에 대한 검토 스타일 취소선 마크업이 필요한 경우 다음 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/) 개체를 생성, 검사, 수집합니다.

1. 
변경 사항을 적용한 후 문서를 저장합니다.


```java
public static void textStrikeoutAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        StrikeOutAnnotation strikeoutAnnotation = new StrikeOutAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        strikeoutAnnotation.setTitle("Aspose User");
        strikeoutAnnotation.setSubject("Inserted text 1");
        strikeoutAnnotation.setFlags(AnnotationFlags.Print);
        strikeoutAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(strikeoutAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void textStrikeoutAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.StrikeOut) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void textStrikeoutAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.StrikeOut) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## 
구불구불한 주석 추가, 가져오기 및 삭제



이러한 예는 검토 중에 텍스트를 강조하는 데 사용되는 구불구불한 마크업과 함께 작동합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[SquigglyAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/squigglyannotation/) 객체를 생성, 검사, 수집합니다.

1. 
주석을 추가하거나 삭제한 후 문서를 저장하세요.


```java
public static void textSquigglyAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        SquigglyAnnotation squigglyAnnotation = new SquigglyAnnotation(
                page,
                new Rectangle(67, 317, 261, 459, true));
        squigglyAnnotation.setTitle("John Smith");
        squigglyAnnotation.setColor(Color.getBlue());

        page.getAnnotations().add(squigglyAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void textSquigglyAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Squiggly) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void textSquigglyAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Squiggly) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## 
밑줄 주석 추가, 가져오기 및 삭제



주석 API를 통해 텍스트에 밑줄을 긋거나 검사하거나 제거해야 하는 경우 다음 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지에서 [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) 개체를 사용하여 작업합니다.

1. 
주석을 추가하거나 삭제한 후 문서를 저장하세요.


```java
public static void textUnderlineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline 1");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void textUnderlineAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void textUnderlineAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## 
쿼드 포인트로 밑줄 주석 추가



이 예에서는 직사각형에서 파생된 쿼드 포인트를 통해 밑줄 영역을 명시적으로 정의합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/)을 만들고 쿼드 포인트를 계산합니다.

1. 
페이지에 주석을 추가하고 문서를 저장합니다.


```java
public static void textUnderlineWithQuadPointsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rect = new Rectangle(299.988, 713.664, 308.708, 720.769, true);
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1), rect);
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline with Quad Points");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());
        underlineAnnotation.setQuadPoints(new com.aspose.pdf.Point[]{
                new com.aspose.pdf.Point(rect.getLLX(), rect.getLLY()),
                new com.aspose.pdf.Point(rect.getURX(), rect.getLLY()),
                new com.aspose.pdf.Point(rect.getURX(), rect.getURY()),
                new com.aspose.pdf.Point(rect.getLLX(), rect.getURY())
        });

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 
밑줄 주석에서 표시된 텍스트 가져오기



이러한 예제는 전체 문자열 또는 개별 조각으로 밑줄 주석과 관련된 텍스트 콘텐츠를 읽습니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지의 밑줄 주석을 반복합니다.

1. 
`getMarkedText()` 또는 `getMarkedTextFragments()`을 읽고 결과를 인쇄합니다.


```java
public static void textUnderlineMarkedTextGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                System.out.println("Marked text: " + ua.getMarkedText());
            }
        }
    }
}
```

```java
public static void textUnderlineMarkedFragmentsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                for (TextFragment fragment : ua.getMarkedTextFragments()) {
                    System.out.println("Fragment text: " + fragment.getText());
                }
            }
        }
    }
}
```

## 
제목별 밑줄 주석 삭제



메타데이터를 기반으로 밑줄 주석을 선택적으로 제거해야 하는 경우 이 접근 방식을 사용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
제목별로 밑줄 주석을 필터링합니다.

1. 
일치하는 주석을 삭제하고 업데이트된 문서를 저장합니다.


```java
public static void textUnderlineByTitleDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<UnderlineAnnotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                if ("Aspose User".equals(ua.getTitle())) {
                    toDelete.add(ua);
                }
            }
        }
        for (UnderlineAnnotation ua : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(ua);
        }
        document.save(outputFile.toString());
    }
}
```

## 
밑줄 주석 추가 및 병합



이 예에서는 밑줄 주석을 추가하고 이를 즉시 정적 페이지 콘텐츠로 병합합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지에 [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/)을 추가합니다.

1. 
주석에서 `flatten()`을 호출하고 출력 파일을 저장합니다.


```java
public static void textUnderlineFlattenAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline to Flatten");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        underlineAnnotation.flatten();

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
[워터마크 주석](/pdf/java/watermark-annotations/)

- 
[주석 가져오기 및 내보내기](/pdf/java/import-export-annotations/)
