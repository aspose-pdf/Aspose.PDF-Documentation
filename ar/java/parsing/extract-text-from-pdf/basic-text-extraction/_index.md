---
title: استخراج النص الأساسي باستخدام Java
linktitle: استخراج النص الأساسي
type: docs
weight: 10
url: /ar/java/basic-text-extraction/
description: تعلم كيفية استخراج النص من مستندات PDF في Java باستخدام Aspose.PDF من جميع الصفحات، أو من صفحة محددة، أو حسب هيكل الفقرات.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
استخراج النص الأساسي هو نقطة الانطلاق لقراءة محتوى PDF في Java. يوفر Aspose.PDF نهجين شائعين:

- استخدم `TextAbsorber` عندما تحتاج إلى نتيجة نصية عادية من مستند أو صفحة.
- استخدم `ParagraphAbsorber` عند الحاجة إلى الحفاظ على تجميع الصفحة، القسم، الفقرة، السطر، والجزء

صفحات PDF لا تخزن النص مثل مستند معالجة النصوص، لذلك يعتمد ترتيب الاستخراج على تيار محتوى الصفحة وتنسيقها. لاستخراج مخصص حسب المنطقة، تفاصيل الهندسة، تخطيطات متعددة الأعمدة، التعليقات التوضيحية، النص المميز، أو اكتشاف النص العلوي والسفلي، استخدم المقالات المتعلقة بالاستخراج في هذا القسم.

## استخراج النص من جميع الصفحات

استخدم `TextAbsorber` لجمع تدفق نص مسطح من كامل المستند وكتابته إلى ملف. هذا هو أبسط خيار عندما تحتاج فقط إلى محتوى النص القابل للقراءة ولا تحتاج إلى حدود الفقرات أو الإحداثيات.

1. افتح ملف PDF المصدر في مثيل [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) لتجميع النص عبر المستند بأكمله.
1. استدعِ `document.getPages().accept(textAbsorber)` إذن كل [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) الصفحة تم زيارتها بواسطة الممتص.
1. اكتب مخزن النص المستخرج إلى ملف الإخراج.

```java
public static void extractTextFromAllPages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## استخراج النص من صفحة محددة

طبق absorber فقط على الصفحة التي تحتاجها. أرقام الصفحات في الـ مجموعة `Document` الصفحات تبدأ من 1، لذا `get_Item(1)` يقرأ الصفحة الأولى.

1. افتح ملف PDF المصدر في مثيل [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) لاستخراج صفحة واحدة.
1. استدعِ `accept(textAbsorber)` على الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) تم الاختيار حسب رقم الصفحة.
1. اكتب مخزن النص المستخرج إلى ملف الإخراج.

```java
public static void extractTextFromPage(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().get_Item(pageNumber).accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## استخراج النص حسب بنية الفقرة

استخدم `ParagraphAbsorber` عندما تحتاج إلى تجميع هيكلي بدلاً من تدفق نص عادي واحد. يُعيد علامات الصفحات مع الأقسام والفقرات والأسطر، و الكائنات `TextFragment`، وهي مفيدة عندما يجب أن يحافظ الإخراج على كتل من النص المنطقي.

1. افتح ملف PDF المصدر في مثيل [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) وزيارة المستند بالكامل لبناء نتائج ترميز الصفحة.
1. مرّ على علامات الصفحة، الأقسام، الفقرات، الأسطر، و الكائنات [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) المكشوفة من قبل absorber..
1. أنشئ نص الإخراج مع ترقيم صريح للصفحة والقسم والفقرة لضمان الحفاظ على تجميع البنية.
1. اكتب نص الفقرة المستخرجة إلى ملف الإخراج.

```java
public static void extractParagraphsFromPdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(document);

        StringBuilder text = new StringBuilder();
        for (PageMarkup pageMarkup : absorber.getPageMarkups()) {
            int sectionIndex = 1;
            for (MarkupSection section : pageMarkup.getSections()) {
                int paragraphIndex = 1;
                for (MarkupParagraph paragraph : section.getParagraphs()) {
                    StringBuilder paragraphText = new StringBuilder();
                    for (List<TextFragment> line : paragraph.getLines()) {
                        for (TextFragment fragment : line) {
                            paragraphText.append(fragment.getText());
                        }
                        paragraphText.append("\r\n");
                    }
                    text.append("Page ").append(pageMarkup.getNumber())
                            .append(", Section ").append(sectionIndex)
                            .append(", Paragraph ").append(paragraphIndex)
                            .append(":\n");
                    text.append(paragraphText).append("\n");
                    paragraphIndex++;
                }
                sectionIndex++;
            }
        }

        Files.writeString(outputFile, text.toString());
    }
}
```
