---
title: Установка свойств элемента структуры PDF с тегами в Java
linktitle: Настройка свойств элементов структуры
type: docs
weight: 30
url: /java/setting-structure-elements-properties/
description: Узнайте, как установить свойства элемента структуры PDF с тегами в Java с помощью Aspose.PDF, включая заголовок, язык, фактический текст, альтернативный текст, текст расширения, ссылки, примечания и имена тегов.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
На этой странице описаны общие шаблоны настройки свойств для размеченных элементов структуры PDF в Java.

## Установите общие свойства элемента структуры

Используйте этот пример, когда элемент структуры с тегами должен предоставлять метаданные доступности, такие как заголовок, язык, фактический текст и альтернативный текст.

1. Создайте новый PDF-файл с тегами [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и инициализируйте метаданные содержимого с тегами.
1. Создайте раздел и элемент заголовка в дереве структуры.
1. Установите свойства заголовка и сохраните документ.

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

## Установите текстовые элементы

Используйте этот пример, когда вам нужно добавить простой элемент абзаца в дерево структуры с тегами.

1. Создайте новый PDF-файл с тегами [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/) и задайте его текст.
1. Добавьте абзац к корневому элементу и сохраните документ.

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

## Установите элементы текстового блока

В этом примере создается несколько элементов структуры уровня блока, включая заголовки нескольких уровней и абзац.

1. Создайте новый PDF-файл с тегами [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте элементы заголовка для необходимых уровней, а затем создайте элемент абзаца.
1. Добавьте элементы блока в корневую структуру и сохраните документ.

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

## Установите встроенные элементы

Используйте этот пример, когда элементы блочной структуры должны содержать вложенные строчные промежутки.

1. Создайте новый PDF-файл с тегами [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте элементы заголовка и добавьте к ним дочерние элементы диапазона.
1. Создайте абзац с несколькими интервалами и сохраните документ.

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

## Задайте имена пользовательских тегов

В этом примере имена пользовательских тегов назначаются элементам абзаца и диапазона в структуре тегов.

1. Создайте новый PDF-файл с тегом [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте элемент раздела.
1. Создавайте абзацы и интервалы, а затем задавайте собственные имена тегов для каждого элемента.
1. Добавьте элементы в раздел и сохраните документ.

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

## Установите элементы ссылки и фигуры

Используйте этот пример, когда помеченные элементы ссылки должны включать альтернативные описания, гиперссылки и содержимое рисунка с атрибутами макета.

1. Создайте новый PDF-файл с тегом [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте элементы ссылок внутри абзацев.
1. Настройте цели гиперссылок, альтернативные описания и элемент связанной фигуры.
1. Установите необходимый атрибут макета и сохраните документ.

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

## Добавляйте абзацы со встроенным контентом, связанным со ссылками.

В этом примере создаются элементы абзаца, сочетающие в себе простой текст и вложенные элементы диапазона.

1. Создайте новый PDF-файл с тегами [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создавайте элементы абзаца и добавляйте дочерние элементы с произвольным текстом.
1. Добавьте абзацы к корневому элементу и сохраните документ.

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

## Установите элементы заметки

Используйте этот пример, когда элементы структуры примечаний должны создаваться с автоматическими или явными идентификаторами.

1. Создайте новый PDF-файл с тегом [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте элемент абзаца.
1. Создайте элементы заметки и задайте их текст и идентификаторы по мере необходимости.
1. Добавьте примечания к абзацу и сохраните документ.

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

## Установите язык и заголовок для многоязычного контента

В этом примере назначаются метаданные уровня документа, а затем создаются абзацы с разными языковыми значениями.

1. Создайте новый PDF-файл с тегом [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и установите заголовок и язык документа.
1. Добавьте элемент заголовка и создайте абзацы для каждой локализованной фразы.
1. Сохраните многоязычный документ с тегами.

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

## Добавьте помощник абзаца для содержимого с тегами

Этот вспомогательный метод создает абзац, назначает его язык и добавляет его к корневой структуре.

1. Создайте [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/).
1. Установите текст и язык для элемента.
1. Добавьте абзац к корневому элементу содержимого с тегами.

```java
private static void addParagraph(ITaggedContent taggedContent, String text, String language) {
    ParagraphElement paragraph = taggedContent.createParagraphElement();
    paragraph.setText(text);
    paragraph.setLanguage(language);
    taggedContent.getRootElement().appendChild(paragraph, true);
}
```
