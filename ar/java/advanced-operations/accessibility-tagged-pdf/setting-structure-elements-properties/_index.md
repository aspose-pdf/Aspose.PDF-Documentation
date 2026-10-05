---
title: تعيين خصائص عنصر بنية Tagged PDF في Java
linktitle: تعيين خصائص Structure Elements
type: docs
weight: 30
url: /ar/java/setting-structure-elements-properties/
description: تعلم كيفية تعيين خصائص عنصر بنية PDF الموسوم في Java مع Aspose.PDF، بما في ذلك العنوان، اللغة، النص الفعلي، النص البديل، نص التوسيع، الروابط، الملاحظات، وأسماء العلامات.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
تغطي هذه الصفحة أنماط ضبط الخصائص الشائعة لعناصر بنية PDF المرفقة في Java.

## تعيين خصائص العنصر الهيكلي المشتركة

استخدم هذا المثال عندما يجب أن يُظهر عنصر بنية مُوسَّم بيانات الوصوفية لإمكانية الوصول مثل العنوان، اللغة، النص الفعلي، والنص البديل.

1. أنشئ ملف PDF معلم [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وتهيئة بيانات التعريف للمحتوى الموسوم.
1. أنشئ قسم وعنصر رأس في شجرة الهيكل.
1. عيّن خصائص الرأس واحفظ المستند.

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

## تعيين عناصر النص

استخدم هذا المثال عندما تحتاج إلى إضافة عنصر فقرة بسيط إلى شجرة البنية الموسومة.

1. أنشئ ملف PDF معلم [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/) واضع نصه.
1. أضف الفقرة إلى العنصر الجذري واحفظ المستند.

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

## تعيين عناصر كتلة النص

هذا المثال ينشئ عناصر هيكلية متعددة على مستوى الكتلة، بما في ذلك عناوين من عدة مستويات وفقرة.

1. أنشئ ملف PDF معلم [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف عناصر العناوين للمستويات المطلوبة ثم أنشئ عنصر فقرة.
1. أضف عناصر الكتلة إلى بنية الجذر واحفظ المستند.

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

## تعيين العناصر المضمنة

استخدم هذا المثال عندما ينبغي لعناصر بنية الكتلة أن تحتوي على نطاقات مضمنة داخلية.

1. أنشئ ملف PDF معلم [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ عناصر العنوان وأرفق عناصر span الفرعية بها.
1. أنشئ فقرة تحتوي على عدة عناصر span واحفظ المستند.

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

## تعيين أسماء وسوم مخصصة

يقوم هذا المثال بتعيين أسماء علامات مخصصة لعناصر الفقرة وعناصر span في الهيكل الموسوم.

1. أنشئ ملف PDF معلم [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف عنصر قسم.
1. أنشئ فقرات وعناصر span، ثم تعيين أسماء علامات مخصصة لكل عنصر.
1. أضف العناصر إلى القسم واحفظ المستند.

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

## تعيين عناصر الرابط والشكل

استخدم هذا المثال عندما يجب أن تتضمن عناصر الروابط الموسومة أوصافًا بديلة وروابطًا تشعبية ومحتوى الشكل مع سمات التخطيط.

1. أنشئ ملف PDF معلم [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف عناصر الروابط داخل الفقرات.
1. اضبط أهداف الروابط التشعبية، والوصف البديل، وعنصر الشكل المرتبط.
1. عيّن سمة التخطيط المطلوبة واحفظ المستند.

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

## إضافة فقرات تحتوي على محتوى روابط مدمج

هذا المثال ينشئ عناصر فقرة تجمع بين النص العادي وعناصر span المتداخلة.

1. أنشئ ملف PDF معلم [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ عناصر الفقرة وأضف عناصر span كأطفال بنص مخصص.
1. أضف الفقرات إلى العنصر الجذري واحفظ المستند.

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

## تعيين عناصر الملاحظة

استخدم هذا المثال عندما يجب إنشاء عناصر بنية الملاحظة بمعرفات تلقائية أو صريحة.

1. أنشئ ملف PDF معلم [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف عنصر فقرة.
1. أنشئ عناصر الملاحظة وعيّن النص والمعرفات الخاصة بها حسب الحاجة.
1. أرفق الملاحظات إلى الفقرة واحفظ المستند.

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

## تعيين اللغة والعنوان للمحتوى متعدد اللغات

هذا المثال يعيّن بيانات تعريف على مستوى المستند ثم ينشئ فقرات ذات قيم لغوية مختلفة.

1. أنشئ ملف PDF معلم [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وضع عنوان المستند واللغة.
1. أضف عنصر رأس وأنشئ فقرات لكل عبارة مُحلية.
1. احفظ المستند الموسوم متعدد اللغات.

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

## إضافة مساعد فقرة للمحتوى الموسوم

تنشئ طريقة المساعد هذه فقرة، وتعيّن لغتها، وتضيفها إلى الهيكل الجذري.

1. أنشئ كائنًا من الفئة [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/).
1. عيّن النص واللغة للعنصر.
1. أضف الفقرة إلى عنصر الجذر للمحتوى الموسوم.

```java
private static void addParagraph(ITaggedContent taggedContent, String text, String language) {
    ParagraphElement paragraph = taggedContent.createParagraphElement();
    paragraph.setText(text);
    paragraph.setLanguage(language);
    taggedContent.getRootElement().appendChild(paragraph, true);
}
```
