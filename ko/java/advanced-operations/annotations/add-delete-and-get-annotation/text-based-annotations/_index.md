---
title: Java를 사용한 텍스트 기반 주석
linktitle: 텍스트 주석
type: docs
weight: 10
url: /java/text-based-annotations/
description: 자유 텍스트, 강조 표시, 취소선, 물결선 및 밑줄 마크업을 포함하여 Java용 Aspose.PDF를 사용하여 텍스트 기반 PDF 주석을 생성, 검사 및 삭제하는 방법을 알아보세요.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 텍스트 PDF 주석을 사용하여 작업합니다.
Abstract: 이 문서에서는 자유 텍스트, 강조 표시, 취소선, 구불구불한 주석 및 밑줄 주석을 포함하여 Java용 Aspose.PDF의 5가지 텍스트 기반 주석 유형으로 작업하는 방법을 보여줍니다. 주석을 추가, 검색 및 삭제하는 방법과 텍스트 표시 및 대화형 마크업 병합과 같은 고급 기술을 알아보세요.
---
텍스트 기반 주석을 사용하면 검토자와 개발자는 핵심 내용을 변경하지 않고도 PDF 문서에 대화형 메모, 강조 표시 및 마크업을 추가할 수 있습니다. 이 섹션에서는 문서 검토 워크플로, 규정 준수 시나리오 및 협업 피드백 주기에 사용되는 5가지 실용적인 주석 유형을 다룹니다.


## 
빠른 참조: 주석 유형



이 문서에서는 다음과 같은 텍스트 기반 주석 유형을 다룹니다.


- 
**자유 텍스트**: 메모 및 설명 추가를 위한 편집 가능한 텍스트 상자

- 
**하이라이트**: 중요한 텍스트 구절을 시각적으로 강조합니다.
- **취소선**: 검토 중 텍스트에 삭제 또는 수정 표시

- 
**구불구불한**: 오류나 문제를 나타내는 물결 모양 밑줄

- 
**밑줄**: 선택적인 쿼드 포인트 정밀도를 사용한 기존 밑줄 강조


## 
자유 텍스트 주석 추가, 가져오기 및 삭제



자유 텍스트 주석은 문서 구조에 영향을 주지 않고 편집할 수 있는 부동 텍스트 상자 역할을 합니다. 다음 예제를 사용하여 설명 상자를 추가하고 해당 속성을 검사하거나 제거합니다.

### 자유 텍스트 주석 추가


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
직사각형과 모양 설정을 사용하여 [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/freetextannotation/)을 만듭니다.

1. 
페이지에 주석을 추가하고 문서를 저장합니다.


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

### 
무료 텍스트 주석 받기

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지의 주석을 반복하고 [AnnotationType.FreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/)로 필터링합니다.

1. 
주석 속성 또는 경계를 검색합니다.


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

### 
자유 텍스트 주석 삭제


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.
1. 페이지 주석을 반복하고 유형별로 필터링하여 자유 텍스트 주석을 찾으세요.

1. 
삭제 목록에 일치하는 주석을 추가하고 페이지에서 제거합니다.

1. 
업데이트된 문서를 저장합니다.


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



강조 표시 주석은 반투명 오버레이로 중요한 구절을 표시합니다. 이러한 예를 사용하여 문서 검토를 위한 하이라이트를 만들고, 기존 하이라이트를 찾고, 마크업을 정리합니다.

### 하이라이트 주석 추가


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
강조 영역을 정의하는 직사각형을 사용하여 [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/)을 만듭니다.

1. 
페이지에 주석을 추가하고 문서를 저장합니다.


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

### 
하이라이트 주석 받기

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
주석을 반복하고 [AnnotationType.Highlight](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/)를 기준으로 필터링합니다.

1. 
경계 또는 색상과 같은 주석 속성을 읽습니다.


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

### 
하이라이트 주석 삭제


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.
1. 유형별로 주석을 필터링하여 하이라이트 주석을 수집합니다.

1. 
페이지에서 각 주석을 제거합니다.

1. 
업데이트된 문서를 저장합니다.


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



취소선 주석은 텍스트에 줄을 그어 삭제, 거부 또는 개정을 나타냅니다. 문서 검토 중에 취소선 마크업을 적용하고, 표시된 텍스트를 찾고, 취소선 주석을 제거하려면 다음 예를 사용하세요.

### 삼진 주석 추가


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
직사각형, 제목, 색상을 포함하는 [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/)을 만듭니다.

1. 
페이지에 주석을 추가하고 문서를 저장합니다.


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

### 
삼진 주석 받기

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
주석을 반복하고 [AnnotationType.StrikeOut](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/)을 기준으로 필터링합니다.

1. 
주석 메타데이터 또는 경계를 읽습니다.


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

### 
삼진 주석 삭제


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.
1. 유형별로 필터링하여 삼진 주석을 수집하세요.

1. 
페이지에서 각 주석을 제거합니다.

1. 
업데이트된 문서를 저장합니다.


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



구불구불한 주석(물결 모양의 밑줄)은 잠재적인 오류, 문제 또는 주의가 필요한 항목을 강조합니다. 다음 예를 사용하여 문제가 있는 텍스트를 표시하고, 구불구불한 주석을 검사하고, 문서에서 제거하세요.

### 구불구불한 주석 추가


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
직사각형과 제목이 있는 [SquigglyAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/squigglyannotation/)을 만듭니다.

1. 
페이지에 주석을 추가하고 문서를 저장합니다.


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

### 
구불구불한 주석 받기

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
주석을 반복하고 [AnnotationType.Squiggly](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/)를 기준으로 필터링합니다.

1. 
주석 경계 또는 메타데이터를 읽습니다.


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

### 
구불구불한 주석 삭제


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.
1. 유형별로 필터링하여 구불구불한 주석을 수집하세요.

1. 
페이지에서 각 주석을 제거합니다.

1. 
업데이트된 문서를 저장합니다.


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



밑줄 주석은 전통적인 밑줄을 사용하여 중요한 구절을 강조합니다. 이러한 예를 사용하여 밑줄을 만들고, 표시된 텍스트 내용을 읽고, 페이지에서 밑줄 주석을 삭제합니다.

### 밑줄 주석 추가


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
직사각형과 색상을 사용하여 [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/)을 만듭니다.

1. 
페이지에 주석을 추가하고 문서를 저장합니다.


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

### 
밑줄 주석 가져오기

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
주석을 반복하고 [AnnotationType.Underline](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/)을 기준으로 필터링합니다.

1. 
주석 속성 또는 경계를 읽습니다.


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

### 
밑줄 주석 삭제


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.
1. 유형별로 필터링하여 밑줄 주석을 수집합니다.

1. 
페이지에서 각 주석을 제거합니다.

1. 
업데이트된 문서를 저장합니다.


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

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

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



밑줄 주석으로 덮인 실제 텍스트 내용을 검색합니다. 이 예에서는 표시된 전체 텍스트를 단일 문자열로 읽거나 자세한 분석을 위해 텍스트 조각을 개별적으로 처리하는 두 가지 접근 방식을 보여줍니다.

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

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



제목과 같은 메타데이터 속성을 필터링하여 선택적으로 주석을 제거합니다. 이 접근 방식을 사용하면 작성자 또는 목적별로 주석을 대상으로 정리할 수 있습니다.

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

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



대화형 밑줄 주석을 병합하여 영구 페이지 콘텐츠로 변환합니다. 이렇게 하면 모든 PDF 뷰어에서 밑줄 모양을 유지하면서 추가 편집을 방지할 수 있습니다.

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

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
- [마크업 주석](/pdf/java/markup-annotations/)

- 
[보안 주석](/pdf/java/security-annotations/)

- 
[도형 주석](/pdf/java/shape-annotations/)

- 
[워터마크 주석](/pdf/java/watermark-annotations/)

- 
[주석 가져오기 및 내보내기](/pdf/java/import-export-annotations/)
