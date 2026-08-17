---
title: Java를 사용한 주석 및 특수 텍스트
linktitle: 주석 및 특수 텍스트
type: docs
weight: 40
url: /java/annotation-and-special-text/
description: Java용 Aspose.PDF를 사용하여 PDF 문서의 스탬프 주석, 강조 표시된 텍스트, 위 첨자 또는 아래 첨자 내용에서 텍스트를 추출하는 방법을 알아보세요.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 
강조 표시된 텍스트 추출



페이지 주석을 반복하고 `HighlightAnnotation`에서 표시된 텍스트를 읽습니다.


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)의 [주석](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 개체를 반복합니다.

1. 
각 주석을 입력된 주석 클래스로 캐스팅하기 전에 각 주석이 [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/)인지 확인하세요.

1. 
각 강조 표시 주석에서 표시된 텍스트를 읽고 콘솔에 인쇄합니다.


```java
public static void extractHighlightedText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation instanceof HighlightAnnotation) {
                HighlightAnnotation highlightAnnotation = (HighlightAnnotation) annotation;
                System.out.println(highlightAnnotation.getMarkedText());
            }
        }
    }
}
```

## 
스탬프 주석에서 텍스트 추출



스탬프 주석에서 일반 모양 스트림을 읽고 `TextAbsorber`을 통해 전달합니다.


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)의 [주석](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 개체를 반복합니다.

1. 
유형이 `Stamp`인 주석으로 주석을 필터링합니다.

1. 
[TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/)를 생성하고 스탬프 주석 모양 사전에서 일반 모양 항목을 요청합니다.

1. 
모양 [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/)을 방문하여 추출된 텍스트를 인쇄합니다.


```java
public static void extractStampText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Stamp) {
                TextAbsorber absorber = new TextAbsorber();
                Object[] xforms = new Object[1];
                if (annotation.getAppearance().tryGetValue("N", xforms) && xforms[0] instanceof XForm) {
                    absorber.visit((XForm) xforms[0]);
                    System.out.println(absorber.getText());
                }
            }
        }
    }
}
```

## 
위 첨자 및 아래 첨자 텍스트 세부정보 추출



추출된 텍스트와 각 조각의 위 첨자 또는 아래 첨자 플래그가 모두 필요한 경우 `TextFragmentAbsorber`을 사용하세요.


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
조각 수준 텍스트 분석을 위해 [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/)를 만듭니다.

1. 
대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 방문하여 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 개체를 수집합니다.

1. 
해당 조각을 반복하고 `fragment.getTextState()`의 위 첨자 및 아래 첨자 플래그와 함께 텍스트를 읽습니다.

1. 
추출된 세부정보를 출력 파일에 씁니다.

```java
public static void extractSuperSubDetails(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().get_Item(pageNumber).accept(absorber);
        StringBuilder details = new StringBuilder();
        for (TextFragment fragment : absorber.getTextFragments()) {
            details.append("Text: '").append(fragment.getText())
                    .append("' | Superscript: ").append(fragment.getTextState().isSuperscript())
                    .append(" | Subscript: ").append(fragment.getTextState().isSubscript())
                    .append(System.lineSeparator());
        }
        Files.writeString(outputFile, details.toString());
    }
}
```
