---
title: Java에서 태그가 있는 PDF 구조 요소 속성 설정
linktitle: 구조 요소 속성 설정
type: docs
weight: 30
url: /java/setting-structure-elements-properties/
description: 제목, 언어, 실제 텍스트, 대체 텍스트, 확장 텍스트, 링크, 메모 및 태그 이름을 포함하여 Aspose.PDF를 사용하여 Java에서 태그가 지정된 PDF 구조 요소 속성을 설정하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

이 페이지에서는 Java의 태그가 지정된 PDF 구조 요소에 대한 일반적인 속성 설정 패턴을 다룹니다.


## 
공통 구조 요소 속성 설정



태그가 지정된 구조 요소가 제목, 언어, 실제 텍스트, 대체 텍스트와 같은 접근성 메타데이터를 노출해야 하는 경우 이 예를 사용하세요.


1. 
새로운 태그가 있는 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 생성하고 태그가 있는 콘텐츠 메타데이터를 초기화합니다.

1. 
구조 트리에 섹션과 헤더 요소를 생성합니다.

1. 
헤더 속성을 설정하고 문서를 저장합니다.


```java
public static void setProperties(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        StructureElement rootElement = taggedContent.getRootElement();
        SectElement sectionElement = taggedContent.createSectElement();
        rootElement.appendChild(sectionElement, true);

        HeaderElement headerElement = taggedContent.createHeaderElement(1);
        sectionElement.appendChild(headerElement, true);
        headerElement.setText("The Header");

        headerElement.setTitle("Title");
        headerElement.setLanguage("en-US");
        headerElement.setAlternativeText("Alternative Text");
        headerElement.setExpansionText("Expansion Text");
        headerElement.setActualText("Actual Text");

        document.save(outputFile.toString());
    }
}
```

## 
텍스트 요소 설정



태그가 지정된 구조 트리에 간단한 단락 요소를 추가해야 할 때 이 예를 사용하십시오.


1. 
새 태그가 있는 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
[ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/)를 생성하고 텍스트를 설정합니다.

1. 
단락을 루트 요소에 추가하고 문서를 저장합니다.


```java
public static void setTextElements(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        ParagraphElement paragraphElement = taggedContent.createParagraphElement();
        paragraphElement.setText("Paragraph.");
        taggedContent.getRootElement().appendChild(paragraphElement, true);

        document.save(outputFile.toString());
    }
}
```

## 
텍스트 블록 요소 설정



이 예에서는 여러 수준의 제목과 단락을 포함하여 여러 블록 수준 구조 요소를 만듭니다.


1. 
새 태그가 있는 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
필요한 수준에 대한 헤더 요소를 추가한 다음 단락 요소를 만듭니다.

1. 
블록 요소를 루트 구조에 추가하고 문서를 저장합니다.


```java
public static void setTextBlockElements(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        for (int level = 1; level <= 6; level++) {
            HeaderElement header = taggedContent.createHeaderElement(level);
            header.setText("H" + level + ". Header of Level " + level);
            taggedContent.getRootElement().appendChild(header, true);
        }

        ParagraphElement p = taggedContent.createParagraphElement();
        p.setText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                + "Aenean nec lectus ac sem faucibus imperdiet.");
        taggedContent.getRootElement().appendChild(p, true);

        document.save(outputFile.toString());
    }
}
```

## 
인라인 요소 설정



블록 구조 요소에 중첩된 인라인 범위가 포함되어야 하는 경우 이 예를 사용하십시오.


1. 
새 태그가 있는 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
헤더 요소를 빌드하고 해당 요소에 범위 하위 요소를 추가합니다.

1. 
여러 범위로 단락을 만들고 문서를 저장합니다.


```java
public static void setInlineElements(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        for (int level = 1; level <= 6; level++) {
            HeaderElement header = taggedContent.createHeaderElement(level);
            taggedContent.getRootElement().appendChild(header, true);

            SpanElement span1 = taggedContent.createSpanElement();
            span1.setText("H" + level + ". ");
            header.appendChild(span1, true);

            SpanElement span2 = taggedContent.createSpanElement();
            span2.setText("Level " + level + " Header");
            header.appendChild(span2, true);
        }

        ParagraphElement paragraphElement = taggedContent.createParagraphElement();
        paragraphElement.setText("P. ");
        taggedContent.getRootElement().appendChild(paragraphElement, true);

        for (int index = 1; index <= 10; index++) {
            SpanElement span = taggedContent.createSpanElement();
            span.setText("Span " + index + ". ");
            paragraphElement.appendChild(span, true);
        }

        document.save(outputFile.toString());
    }
}
```

## 
맞춤 태그 이름 설정



이 예에서는 태그가 지정된 구조의 단락 및 범위 요소에 사용자 정의 태그 이름을 할당합니다.


1. 
새 태그가 있는 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 섹션 요소를 추가합니다.

1. 
단락과 범위를 만든 다음 각 요소에 대한 사용자 정의 태그 이름을 설정하세요.

1. 
섹션에 요소를 추가하고 문서를 저장합니다.


```java
public static void setTagName(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        SectElement sectionElement = taggedContent.createSectElement();
        taggedContent.getRootElement().appendChild(sectionElement, true);

        String[] paragraphTags = {"P1", "Para", "Para", "Paragraph"};
        String[] spanTags = {"SPAN", "Sp", "Sp", "TheSpan"};

        for (int index = 0; index < 4; index++) {
            ParagraphElement paragraph = taggedContent.createParagraphElement();
            paragraph.setText("P" + (index + 1) + ". ");
            paragraph.setTag(paragraphTags[index]);

            SpanElement span = taggedContent.createSpanElement();
            span.setText("Span " + (index + 1) + ".");
            span.setTag(spanTags[index]);

            paragraph.appendChild(span, true);
            sectionElement.appendChild(paragraph, true);
        }

        document.save(outputFile.toString());
    }
}
```

## 
링크 및 그림 요소 설정



태그된 링크 요소에 레이아웃 속성이 있는 대체 설명, 하이퍼링크 및 그림 콘텐츠가 포함되어야 하는 경우 이 예를 사용하십시오.


1. 
새로운 태그가 있는 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 단락 안에 링크 요소를 추가하세요.

1. 
하이퍼링크 대상, 대체 설명, 연결된 그림 요소를 구성합니다.

1. 
필요한 레이아웃 속성을 설정하고 문서를 저장합니다.


```java
public static void setElements(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Link Elements Example");
        taggedContent.setLanguage("en-US");

        for (int index = 1; index <= 4; index++) {
            ParagraphElement paragraph = taggedContent.createParagraphElement();
            taggedContent.getRootElement().appendChild(paragraph, true);

            LinkElement link = taggedContent.createLinkElement();
            paragraph.appendChild(link, true);
            link.setHyperlink(new WebHyperlink("http://google.com"));
            link.setText(index == 4 ? "The multiline link: Google Google Google Google" : "Google");
            link.setAlternateDescriptions("Link to Google");
        }

        ParagraphElement paragraph = taggedContent.createParagraphElement();
        taggedContent.getRootElement().appendChild(paragraph, true);

        LinkElement link = taggedContent.createLinkElement();
        paragraph.appendChild(link, true);
        link.setHyperlink(new WebHyperlink("http://google.com"));

        FigureElement figure = taggedContent.createFigureElement();
        figure.setImage(imageFile.toString(), 1200);
        figure.setAlternativeText("Google icon");

        StructureAttributes linkLayoutAttributes = link.getAttributes().getAttributes(AttributeOwnerStandard.Layout);
        StructureAttribute placementAttribute = new StructureAttribute(AttributeKey.Placement);
        placementAttribute.setNameValue(AttributeName.Placement_Block);
        linkLayoutAttributes.setAttribute(placementAttribute);

        link.appendChild(figure, true);
        link.setAlternateDescriptions("Link to Google");

        document.save(outputFile.toString());
    }
}
```

## 
인라인 링크 관련 콘텐츠가 포함된 단락 추가



이 예에서는 일반 텍스트와 중첩된 범위 요소를 결합하는 단락 요소를 만듭니다.


1. 
새 태그가 있는 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
단락 요소를 만들고 사용자 정의 텍스트로 범위 하위 항목을 추가합니다.

1. 
루트 요소에 단락을 추가하고 문서를 저장합니다.


```java
public static void addLinkElement(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Text Elements Example");
        taggedContent.setLanguage("en-US");

        for (int paragraphIndex = 1; paragraphIndex <= 4; paragraphIndex++) {
            ParagraphElement paragraph = taggedContent.createParagraphElement();
            taggedContent.getRootElement().appendChild(paragraph, true);

            SpanElement span1 = taggedContent.createSpanElement();
            span1.setText("Span_" + paragraphIndex + "1");
            SpanElement span2 = taggedContent.createSpanElement();
            span2.setText(" and Span_" + paragraphIndex + "2.");

            paragraph.setText("Paragraph with ");
            paragraph.appendChild(span1, true);
            paragraph.appendChild(span2, true);
        }

        document.save(outputFile.toString());
    }
}
```

## 
메모 요소 설정



자동 또는 명시적 ID를 사용하여 메모 구조 요소를 생성해야 하는 경우 이 예를 사용하십시오.


1. 
새 태그가 있는 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 단락 요소를 추가합니다.

1. 
메모 요소를 생성하고 필요에 따라 텍스트와 ID를 설정합니다.

1. 
단락에 메모를 추가하고 문서를 저장합니다.


```java
public static void setNoteElement(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Sample of Note Elements");
        taggedContent.setLanguage("en-US");

        ParagraphElement paragraph = taggedContent.createParagraphElement();
        taggedContent.getRootElement().appendChild(paragraph, true);

        NoteElement note1 = taggedContent.createNoteElement();
        paragraph.appendChild(note1, true);
        note1.setText("Note with auto generate ID. ");

        NoteElement note2 = taggedContent.createNoteElement();
        paragraph.appendChild(note2, true);
        note2.setText("Note with ID = 'note_002'. ");
        note2.setId("note_002");

        NoteElement note3 = taggedContent.createNoteElement();
        paragraph.appendChild(note3, true);
        note3.setText("Note with ID = 'note_003'. ");
        note3.setId("note_003");

        document.save(outputFile.toString());
    }
}
```

## 
다국어 콘텐츠의 언어 및 제목 설정



이 예에서는 문서 수준 메타데이터를 할당한 다음 다른 언어 값을 사용하여 단락을 만듭니다.


1. 
새 태그가 있는 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 문서 제목과 언어를 설정합니다.

1. 
헤더 요소를 추가하고 현지화된 각 문구에 대한 단락을 만듭니다.

1. 
다국어 태그가 지정된 문서를 저장합니다.


```java
public static void setLanguageAndTitle(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example Tagged Document");
        taggedContent.setLanguage("en-US");

        HeaderElement header = taggedContent.createHeaderElement(1);
        header.setText("Phrase on different languages");
        taggedContent.getRootElement().appendChild(header, true);

        addParagraph(taggedContent, "Hello, World!", "en-US");
        addParagraph(taggedContent, "Hallo Welt!", "de-DE");
        addParagraph(taggedContent, "Bonjour le monde!", "fr-FR");
        addParagraph(taggedContent, "Hola Mundo!", "es-ES");

        document.save(outputFile.toString());
    }
}
```

## 
태그된 콘텐츠에 대한 단락 도우미 추가



이 도우미 메서드는 단락을 만들고 해당 언어를 할당한 후 루트 구조에 추가합니다.


1. 
[ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/)를 만듭니다.

1. 
요소의 텍스트와 언어를 설정합니다.

1. 
태그가 지정된 콘텐츠 루트 요소에 단락을 추가합니다.

```java
private static void addParagraph(ITaggedContent taggedContent, String text, String language) {
    ParagraphElement paragraph = taggedContent.createParagraphElement();
    paragraph.setText(text);
    paragraph.setLanguage(language);
    taggedContent.getRootElement().appendChild(paragraph, true);
}
```
