---
title: Java를 사용한 마크업 주석
linktitle: 마크업 주석
type: docs
weight: 30
url: /java/markup-annotations/
description: Java용 Aspose.PDF를 사용하여 PDF 문서에서 강조 표시, 밑줄, 물결선 및 취소선 주석을 추가, 검사 및 삭제하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일의 마크업 주석 작업을 수행합니다.
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 텍스트 마크업 주석을 생성, 검사 및 제거하는 방법을 설명합니다. 저장소 Java 예제를 기반으로 강조 표시, 밑줄, 물결 모양 및 취소선 주석을 다룹니다.
---

이 섹션의 마크업 주석 작업 흐름은 노트 스타일 주석, 캐럿 마커 및 그룹화된 교체-검토 시나리오에 중점을 둡니다.


## 
텍스트 주석 추가



페이지에 팝업 메타데이터가 포함된 스티커 메모 스타일 텍스트 주석을 배치해야 하는 경우 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[TextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/textannotation/)을 생성하고 제목, 내용, 아이콘, 팝업을 구성합니다.

1. 
페이지에 주석을 추가하고 문서를 저장합니다.


```java
public static void textAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextAnnotation textAnnotation = new TextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 613.664, 428.708, 680.769, true));
        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Sticky Note");
        textAnnotation.setContents("This is a text annotation added by Aspose.PDF for Java");
        textAnnotation.setFlags(AnnotationFlags.Print);
        textAnnotation.setColor(Color.getBlue());
        textAnnotation.setIcon(TextIcon.Help);

        PopupAnnotation popup = new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(428.708, 613.664, 528.708, 713.664, true));
        popup.setOpen(true);
        textAnnotation.setPopup(popup);

        document.getPages().get_Item(1).getAnnotations().add(textAnnotation, false);
        document.save(outputFile.toString());
    }
}
```

## 
텍스트 주석 받기



이 예에서는 페이지를 스캔하고 각 텍스트 주석의 직사각형을 인쇄합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지의 주석을 반복합니다.

1. 
[AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Text`으로 주석을 필터링하고 해당 직사각형을 인쇄합니다.


```java
public static void textAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Text) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## 
텍스트 주석 삭제



문서에서 기존 텍스트 주석을 제거해야 하는 경우 이 방법을 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Text` 유형의 주석을 수집합니다.

1. 
수집된 주석을 삭제하고 출력 파일을 저장합니다.


```java
public static void textAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Text) {
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
캐럿 주석 추가



캐럿 스타일 검토 주석으로 삽입된 텍스트를 표시해야 할 때 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[CaretAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/caretannotation/)을 생성하고 팝업 및 모양을 구성합니다.

1. 
페이지에 주석을 추가하고 문서를 저장합니다.


```java
public static void caretAnnotationsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        CaretAnnotation caretAnnotation = new CaretAnnotation(
                page,
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        caretAnnotation.setTitle("Aspose User");
        caretAnnotation.setSubject("Inserted text 1");
        caretAnnotation.setFlags(AnnotationFlags.Print);
        caretAnnotation.setColor(Color.getBlue());
        caretAnnotation.setPopup(new PopupAnnotation(
                page,
                new Rectangle(310, 713, 410, 730, true)));
        page.getAnnotations().add(caretAnnotation);

        document.save(outputFile.toString());
    }
}
```

## 
캐럿 주석 가져오기



이 예제는 기존 캐럿 주석을 읽고 해당 위치를 인쇄합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지 주석을 반복합니다.

1. 
[AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Caret`으로 주석을 필터링하고 해당 직사각형을 인쇄합니다.


```java
public static void caretAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.Caret) {
                System.out.println(annot.getRect());
            }
        }
    }
}
```

## 
캐럿 주석 삭제



페이지에서 캐럿 주석을 제거해야 하는 경우 이 접근 방식을 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
유형이 [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Caret`인 주석을 수집합니다.

1. 
수집된 주석을 삭제하고 출력 문서를 저장합니다.


```java
public static void caretAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        List<Annotation> caretAnnotations = new ArrayList<>();
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.Caret) {
                caretAnnotations.add(annot);
            }
        }
        for (Annotation annot : caretAnnotations) {
            page.getAnnotations().delete(annot);
        }
        document.save(outputFile.toString());
    }
}
```

## 
그룹화된 대체 주석 추가



이 예는 캐럿 주석과 취소선 주석을 결합하여 교체 스타일 검토 주석을 나타냅니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
캐럿 주석 및 관련 [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/)을 생성합니다.

1. 
`setInReplyTo` 및 `setReplyType`을 통해 주석을 연결한 다음 문서를 저장합니다.


```java
public static void replaceAnnotationsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        CaretAnnotation caretAnnotation = new CaretAnnotation(
                page,
                new Rectangle(361.246, 727.908, 370.081, 735.107, true));
        caretAnnotation.setFlags(AnnotationFlags.Print);
        caretAnnotation.setSubject("Inserted text 2");
        caretAnnotation.setTitle("Aspose User");
        caretAnnotation.setColor(Color.getBlue());
        caretAnnotation.setPopup(new PopupAnnotation(
                page,
                new Rectangle(310, 713, 410, 730, true)));

        StrikeOutAnnotation strikeoutAnnotation = new StrikeOutAnnotation(
                page,
                new Rectangle(318.407, 727.826, 368.916, 740.098, true));
        strikeoutAnnotation.setColor(Color.getBlue());
        strikeoutAnnotation.setQuadPoints(new Point[]{
                new Point(321.66, 739.416),
                new Point(365.664, 739.416),
                new Point(321.66, 728.508),
                new Point(365.664, 728.508)
        });
        strikeoutAnnotation.setSubject("Cross-out");
        strikeoutAnnotation.setInReplyTo(caretAnnotation);
        strikeoutAnnotation.setReplyType(ReplyType.Group);

        page.getAnnotations().add(caretAnnotation);
        page.getAnnotations().add(strikeoutAnnotation);

        document.save(outputFile.toString());
    }
}
```

## 
그룹화된 대체 주석 가져오기



이 예에서는 그룹화된 교체 워크플로에 참여하는 취소선 주석을 감지합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지 주석을 반복하고 취소선 주석을 선택합니다.

1. 
응답 관계를 확인하고 일치하는 주석의 사각형을 인쇄합니다.


```java
public static void replaceAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.StrikeOut) {
                StrikeOutAnnotation sa = (StrikeOutAnnotation) annot;
                if (sa.getInReplyTo() != null && sa.getReplyType() == ReplyType.Group) {
                    System.out.println("Replace annotation rect: " + sa.getRect());
                }
            }
        }
    }
}
```

## 
그룹화된 대체 주석 삭제



교체-검토 취소선 주석을 페이지에서 제거해야 하는 경우 이 접근 방식을 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
교체 마크업을 나타내는 취소선 주석을 수집합니다.

1. 
수집된 주석을 삭제하고 업데이트된 문서를 저장합니다.


```java
public static void replaceAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        List<StrikeOutAnnotation> replaceAnnotations = new ArrayList<>();
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.StrikeOut) {
                replaceAnnotations.add((StrikeOutAnnotation) annot);
            }
        }
        for (StrikeOutAnnotation annot : replaceAnnotations) {
            page.getAnnotations().delete(annot);
        }
        document.save(outputFile.toString());
    }
}
```

## 
관련 주석 주제


- 
[텍스트 주석](/pdf/java/text-based-annotations/)

- 
[대화형 주석](/pdf/java/interactive-annotations/)

- 
[도형 주석](/pdf/java/shape-annotations/)

- 
[미디어 주석](/pdf/java/media-annotations/)

- 
[보안 주석](/pdf/java/security-annotations/)

- 
[워터마크 주석](/pdf/java/watermark-annotations/)
