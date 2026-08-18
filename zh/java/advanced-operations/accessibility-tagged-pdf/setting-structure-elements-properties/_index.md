---
title: 在 Java 中设置标记的 PDF 结构元素属性
linktitle: 设置结构元素属性
type: docs
weight: 30
url: /java/setting-structure-elements-properties/
description: 了解如何使用 Aspose.PDF 在 Java 中设置标记的 PDF 结构元素属性，包括标题、语言、实际文本、替代文本、扩展文本、链接、注释和标记名称。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
本页介绍了 Java 中标记的 PDF 结构元素的常见属性设置模式。

## 设置公共结构元素属性

当标记的结构元素应公开可访问性元数据（例如标题、语言、实际文本和替代文本）时，请使用此示例。

1. 创建新的带标签的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并初始化带标签的内容元数据。
1. 在结构树中创建节和标题元素。
1. 设置标题属性并保存文档。

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

## 设置文本元素

当您需要将简单的段落元素添加到标记结构树时，请使用此示例。

1. 创建一个新的带标签的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建一个 [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/) 并设置其文本。
1. 将段落附加到根元素并保存文档。

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

## 设置文本块元素

此示例创建多个块级结构元素，包括多个级别的标题和一个段落。

1. 创建一个新的带标签的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 添加所需级别的标题元素，然后创建段落元素。
1. 将块元素附加到根结构并保存文档。

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

## 设置内联元素

当块结构元素应包含嵌套的内联跨度时，请使用此示例。

1. 创建一个新的带标签的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 构建标题元素并向其附加 span 子元素。
1. 创建一个具有多个跨度的段落并保存文档。

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

## 设置自定义标签名称

此示例将自定义标签名称分配给标记结构中的段落和跨度元素。

1. 创建一个新的带标签的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个部分元素。
1. 创建段落和跨度，然后为每个元素设置自定义标签名称。
1. 将元素附加到该部分并保存文档。

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

## 设置链接和图形元素

当标记的链接元素应包括备用描述、超链接和具有布局属性的图形内容时，请使用此示例。

1. 创建一个新的带标签的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并在段落内添加链接元素。
1. 配置超链接目标、备用描述和链接的图形元素。
1. 设置所需的布局属性并保存文档。

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

## 添加包含内嵌链接相关内容的段落

此示例创建组合纯文本和嵌套 span 元素的段落元素。

1. 创建一个新的带标签的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建段落元素并添加带有自定义文本的跨度子元素。
1. 将段落附加到根元素并保存文档。

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

## 设置注释元素

当应使用自动或显式 ID 创建注释结构元素时，请使用此示例。

1. 创建一个新的带标签的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加段落元素。
1. 创建注释元素并根据需要设置其文本和 ID。
1. 将注释附加到该段落并保存文档。

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

## 设置多语言内容的语言和标题

此示例分配文档级元数据，然后创建具有不同语言值的段落。

1. 创建一个新的带标签的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并设置文档标题和语言。
1. 添加标题元素并为每个本地化短语创建段落。
1. 保存多语言标记文档。

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

## 为标记内容添加段落助手

此帮助器方法创建一个段落，分配其语言，并将其附加到根结构。

1. 创建一个 [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/)。
1. 设置元素的文本和语言。
1. 将段落附加到标记的内容根元素。

```java
private static void addParagraph(ITaggedContent taggedContent, String text, String language) {
    ParagraphElement paragraph = taggedContent.createParagraphElement();
    paragraph.setText(text);
    paragraph.setLanguage(language);
    taggedContent.getRootElement().appendChild(paragraph, true);
}
```
