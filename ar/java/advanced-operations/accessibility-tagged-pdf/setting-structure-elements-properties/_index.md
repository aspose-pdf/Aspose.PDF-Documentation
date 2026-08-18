---
title: قم بتعيين خصائص عنصر بنية PDF ذات العلامات في Java
linktitle: ضبط خصائص عناصر الهيكل
type: docs
weight: 30
url: /java/setting-structure-elements-properties/
description: تعرف على كيفية تعيين خصائص عنصر بنية PDF ذات العلامات في Java باستخدام Aspose.PDF، بما في ذلك العنوان واللغة والنص الفعلي والنص البديل ونص التوسيع والارتباطات والملاحظات وأسماء العلامات.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
تغطي هذه الصفحة أنماط إعداد الخصائص الشائعة لعناصر بنية PDF ذات علامات تمييز في Java.

## تعيين خصائص عنصر الهيكل المشترك

استخدم هذا المثال عندما يجب أن يعرض عنصر البنية المميزة بيانات تعريف إمكانية الوصول مثل العنوان واللغة والنص الفعلي والنص البديل.

1. قم بإنشاء ملف PDF [مستند] جديد بعلامات تمييز (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وقم بتهيئة البيانات التعريفية للمحتوى المميز بعلامات.
1. قم بإنشاء قسم وعنصر رأس في شجرة الهيكل.
1. قم بتعيين خصائص الرأس واحفظ المستند.

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

استخدم هذا المثال عندما تحتاج إلى إضافة عنصر فقرة بسيط إلى شجرة البنية ذات العلامات.

1. قم بإنشاء ملف PDF [مستند] جديد بعلامات تمييز (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/) وقم بتعيين النص الخاص به.
1. قم بإلحاق الفقرة بالعنصر الجذر واحفظ المستند.

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

يقوم هذا المثال بإنشاء عناصر بنية متعددة على مستوى الكتلة، بما في ذلك عناوين عدة مستويات وفقرة.

1. قم بإنشاء ملف PDF [مستند] جديد بعلامات تمييز (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف عناصر الرأس للمستويات المطلوبة ثم قم بإنشاء عنصر فقرة.
1. قم بإلحاق عناصر الكتلة بالبنية الجذرية واحفظ المستند.

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

استخدم هذا المثال عندما يجب أن تحتوي عناصر بنية الكتلة على امتدادات مضمنة متداخلة.

1. قم بإنشاء ملف PDF [مستند] جديد بعلامات تمييز (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم ببناء عناصر الرأس وإلحاق العناصر الفرعية بها.
1. أنشئ فقرة ذات امتدادات متعددة واحفظ المستند.

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

## تعيين أسماء العلامات المخصصة

يقوم هذا المثال بتعيين أسماء علامات مخصصة لعناصر الفقرة والامتداد في البنية ذات العلامات.

1. قم بإنشاء ملف PDF [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) بعلامة جديدة وأضف عنصر القسم.
1. قم بإنشاء فقرات وامتدادات، ثم قم بتعيين أسماء علامات مخصصة لكل عنصر.
1. قم بإلحاق العناصر بالقسم وحفظ المستند.

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

## تعيين عناصر الارتباط والشكل

استخدم هذا المثال عندما يجب أن تتضمن عناصر الارتباط ذات العلامات أوصافًا بديلة وارتباطات تشعبية ومحتوى شكل مع سمات التخطيط.

1. قم بإنشاء ملف PDF [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) بعلامة جديدة وأضف عناصر الارتباط داخل الفقرات.
1. قم بتكوين أهداف الارتباط التشعبي والأوصاف البديلة وعنصر الشكل المرتبط.
1. قم بتعيين سمة التخطيط المطلوبة واحفظ المستند.

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

## أضف فقرات ذات محتوى مضمن مرتبط بالارتباط

يقوم هذا المثال بإنشاء عناصر فقرة تجمع بين النص العادي وعناصر الامتداد المتداخلة.

1. قم بإنشاء ملف PDF [مستند] جديد بعلامات تمييز (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ عناصر فقرة وأضف عناصر فرعية بنص مخصص.
1. قم بإلحاق الفقرات بالعنصر الجذر واحفظ المستند.

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

## ضبط عناصر الملاحظة

استخدم هذا المثال عندما يجب إنشاء عناصر بنية الملاحظة بمعرفات تلقائية أو صريحة.

1. قم بإنشاء ملف PDF [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) بعلامة جديدة وأضف عنصر فقرة.
1. قم بإنشاء عناصر الملاحظة وقم بتعيين النص والمعرفات الخاصة بها حسب الحاجة.
1. قم بإلحاق الملاحظات بالفقرة واحفظ المستند.

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

يقوم هذا المثال بتعيين بيانات التعريف على مستوى المستند ثم إنشاء فقرات بقيم لغة مختلفة.

1. قم بإنشاء ملف PDF [مستند] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) بعلامة جديدة وقم بتعيين عنوان المستند ولغته.
1. أضف عنصر رأس وأنشئ فقرات لكل عبارة مترجمة.
1. احفظ المستند متعدد اللغات الذي تم وضع علامة عليه.

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

تقوم هذه الطريقة المساعدة بإنشاء فقرة، وتعيين لغتها، وإلحاقها بالبنية الجذرية.

1. قم بإنشاء [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/).
1. قم بتعيين النص واللغة للعنصر.
1. قم بإلحاق الفقرة بالعنصر الجذر للمحتوى المميز بعلامة.

```java
private static void addParagraph(ITaggedContent taggedContent, String text, String language) {
    ParagraphElement paragraph = taggedContent.createParagraphElement();
    paragraph.setText(text);
    paragraph.setLanguage(language);
    taggedContent.getRootElement().appendChild(paragraph, true);
}
```
