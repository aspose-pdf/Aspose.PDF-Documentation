---
title: Установить свойства элементов структуры Tagged PDF в Java
linktitle: Настройка свойств Structure Elements
type: docs
weight: 30
url: /ru/java/setting-structure-elements-properties/
description: Узнайте, как установить свойства элементов структуры Tagged PDF в Java с Aspose.PDF, включая заголовок, язык, фактический текст, альтернативный текст, расширяющийся текст, ссылки, примечания и имена тегов.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
На этой странице рассматриваются типичные шаблоны установки свойств для структурных элементов помеченного PDF в Java.

## Установите общие свойства элементов структуры

Используйте этот пример, когда элемент теговой структуры должен раскрывать метаданные доступности, такие как заголовок, язык, основной текст и альтернативный текст.

1. Создайте новый Tagged PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и инициализировать метаданные помеченного содержимого.
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

Используйте этот пример, когда вам нужно добавить простой элемент абзаца в дерево теговой структуры.

1. Создайте новый Tagged PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/) и установить его текст.
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

Этот пример создает несколько элементов структуры блочного уровня, включая заголовки нескольких уровней и абзац.

1. Создайте новый Tagged PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте элементы заголовков для необходимых уровней, а затем создайте элемент абзаца.
1. Добавьте блочные элементы в корневую структуру и сохраните документ.

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

Используйте этот пример, когда блочные структурные элементы должны содержать вложенные встроенные спаны.

1. Создайте новый Tagged PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте элементы заголовков и добавьте к ним дочерние элементы span.
1. Создайте абзац с несколькими спанами и сохраните документ.

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

## Установите пользовательские имена тегов

В этом примере пользовательские имена тегов присваиваются элементам paragraph и span в помеченной структуре.

1. Создайте новый Tagged PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавить элемент раздела.
1. Создайте абзацы и спаны, затем установите пользовательские имена тегов для каждого элемента.
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

## Установите элементы link и figure

Используйте этот пример, когда помеченные элементы ссылки должны включать альтернативные описания, гиперссылки и содержимое фигур с атрибутами макета.

1. Создайте новый Tagged PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавить элементы ссылок внутри абзацев.
1. Настройте цели гиперссылок, альтернативные описания и связанным элементом рисунка.
1. Установите требуемый атрибут компоновки и сохраните документ.

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

## Добавьте абзацы со встроенным содержимым ссылок

Этот пример создает элементы абзаца, которые объединяют обычный текст и вложенные элементы span.

1. Создайте новый Tagged PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте элементы абзаца и добавьте дочерние элементы span с пользовательским текстом.
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

Используйте этот пример, когда элементы структуры заметок должны создаваться с автоматическими или явными идентификаторами.

1. Создайте новый Tagged PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавить элемент абзаца.
1. Создайте элементы заметок и установите их текст и идентификаторы по мере необходимости.
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

В этом примере задаются метаданные уровня документа, а затем создаются абзацы с разными значениями языка.

1. Создайте новый Tagged PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и установить название документа и язык.
1. Добавьте элемент заголовка и создайте абзацы для каждой локализованной фразы.
1. Сохраните многоязычный тегированный документ.

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

## Добавьте помощник абзаца для помеченного контента

Этот вспомогательный метод создает абзац, задает его язык и добавляет его к корневой структуре.

1. Создайте [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/).
1. Установите текст и язык для элемента.
1. Добавьте абзац к корневому элементу помеченного содержимого.

```java
private static void addParagraph(ITaggedContent taggedContent, String text, String language) {
    ParagraphElement paragraph = taggedContent.createParagraphElement();
    paragraph.setText(text);
    paragraph.setLanguage(language);
    taggedContent.getRootElement().appendChild(paragraph, true);
}
```


