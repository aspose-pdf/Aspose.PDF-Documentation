---
title: Java를 사용한 대화형 주석
linktitle: 대화형 주석
type: docs
weight: 60
url: /java/interactive-annotations/
description: Aspose.PDF for Java를 사용하여 PDF 문서에서 링크 주석을 추가, 검사 및 삭제하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 대화형 PDF 주석을 사용하여 작업합니다.
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 파일에서 대화형 링크 주석 작업을 수행하는 방법을 설명합니다. 텍스트 찾기, 일치하는 텍스트 영역 위에 링크 주석 생성, 기존 링크 주석 읽기 및 삭제에 대해 다룹니다.
---

이 섹션의 대화형 주석은 PDF 뷰어 내부의 사용자 작업에 응답하는 링크 및 버튼 기반 작업 흐름에 중점을 둡니다.


## 
링크 주석 추가



페이지에 있는 텍스트 위에 클릭 가능한 링크를 배치해야 하는 경우 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
대상 텍스트 조각을 찾아 해당 사각형 위에 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/)을 만듭니다.

1. 
[GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/)을 할당하고 업데이트된 문서를 저장합니다.


```java
public static void linkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("file");
        document.getPages().get_Item(1).accept(textFragmentAbsorber);

        var phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);
        LinkAnnotation linkAnnotation = new LinkAnnotation(
                document.getPages().get_Item(1),
                phoneNumberFragment.getRectangle());
        linkAnnotation.setAction(new GoToURIAction("https://www.aspose.com"));

        document.getPages().get_Item(1).getAnnotations().add(linkAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 
링크 주석 받기



이 예에서는 페이지 주석 컬렉션을 검색하고 각 링크 주석의 위치를 보고합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
대상 페이지의 주석을 반복합니다.

1. 
[AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link`으로 주석을 필터링하고 해당 직사각형을 인쇄합니다.


```java
public static void linkGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## 
링크 주석 삭제



기존 링크 주석을 페이지에서 제거해야 하는 경우 이 접근 방식을 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
유형이 [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link`인 주석을 수집합니다.

1. 
수집된 주석을 삭제하고 출력 파일을 저장합니다.


```java
public static void linkDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
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
선 주석 추가



이 예에서는 화살표 스타일, 테두리 설정 및 팝업 메모를 사용하여 대화형 선 주석을 만듭니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
시작점과 끝점이 있는 [LineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/)을 만듭니다.

1. 
모양과 팝업 주석을 구성한 다음 문서를 저장합니다.


```java
public static void lineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        LineAnnotation lineAnnotation = new LineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(550, 93, 562, 439, true),
                new Point(556, 99),
                new Point(556, 443));

        lineAnnotation.setTitle("John Smith");
        lineAnnotation.setColor(Color.getRed());
        lineAnnotation.setStartingStyle(LineEnding.OpenArrow);
        lineAnnotation.setEndingStyle(LineEnding.OpenArrow);

        Border border = new Border(lineAnnotation);
        border.setWidth(3);
        lineAnnotation.setBorder(border);

        PopupAnnotation popup = new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(842, 124, 1021, 266, true));
        lineAnnotation.setPopup(popup);

        document.getPages().get_Item(1).getAnnotations().add(lineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 
탐색 버튼 추가



대화형 탐색을 위해 PDF에 이전 페이지 및 다음 페이지 버튼이 포함되어야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 문서에 필요한 페이지가 있는지 확인하세요.

1. 
사전 정의된 탐색 작업을 사용하여 [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) 컨트롤을 만듭니다.

1. 
양식 컬렉션에 버튼을 추가하고 업데이트된 문서를 저장합니다.


```java
public static void navigationButtonsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();

        record ButtonConfig(String name, double xPos, PredefinedAction action) {}
        List<ButtonConfig> buttonConfigs = List.of(
                new ButtonConfig("Previous Page", 120.0, PredefinedAction.PrevPage),
                new ButtonConfig("Next Page", 230.0, PredefinedAction.NextPage));

        for (Page page : document.getPages()) {
            for (ButtonConfig config : buttonConfigs) {
                Rectangle rect = new Rectangle(config.xPos(), 10.0, config.xPos() + 100, 40.0, true);
                ButtonField button = new ButtonField(page, rect);
                button.setPartialName(config.name());
                button.setValue(config.name());
                button.getCharacteristics().setBorder(Color.getRed());
                button.getCharacteristics().setBackground(Color.getOrange().toRgb());
                button.getAnnotationActions().setOnReleaseMouseBtn(new NamedAction(config.action()));
                document.getForm().add(button);
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 
인쇄 버튼 추가



이 예제에서는 사용자가 클릭할 때 인쇄 명령을 트리거하는 버튼을 만듭니다.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 페이지를 추가하세요.

1. 
[ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/)를 생성하고 사전 정의된 인쇄 작업을 할당합니다.

1. 
버튼 테두리와 배경을 구성하고 양식에 추가한 후 문서를 저장합니다.

```java
public static void printButtonAdd(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle rect = new Rectangle(72, 748, 164, 768, true);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setAlternateName("Print current document");
        printButton.setColor(Color.getBlack());
        printButton.setPartialName("printBtn1");
        printButton.setValue("Print Document");
        printButton.getAnnotationActions().setOnReleaseMouseBtn(
                new NamedAction(PredefinedAction.File_Print));

        Border border = new Border(printButton);
        border.setStyle(BorderStyle.Solid);
        border.setWidth(2);
        printButton.setBorder(border);

        printButton.getCharacteristics().setBorder(Color.getBlue());
        printButton.getCharacteristics().setBackground(Color.getLightBlue().toRgb());

        document.getForm().add(printButton);
        document.save(outputFile.toString());
    }
}
```
