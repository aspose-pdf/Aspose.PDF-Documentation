---
title: استخراج قائم على المنطقة باستخدام Java
linktitle: استخراج قائم على المنطقة
type: docs
weight: 20
url: /ar/java/region-based-extraction/
description: تعلم كيفية استخراج النص من منطقة صفحة محددة أو فحص هندسة الفقرات في مستندات PDF باستخدام Aspose.PDF for Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## استخراج النص من منطقة صفحة مستطيلة

استخدام `TextSearchOptions` مع `Rectangle` لتقييد الاستخراج إلى مساحة محددة على الصفحة.

1. افتح ملف PDF المصدر في [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. أنشئ كائنًا من الفئة [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) لجمع النص من منطقة الصفحة المحددة.
1. أنشئ كائنًا من الفئة [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsearchoptions/) للهدف [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) وفعّل `setLimitToPageBounds(true)` لذا يظل الاستخراج داخل صندوق الصفحة المرئي.
1. طبّق خيارات البحث المكوّنة على absorber وزُر الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. اكتب مخزن النص المستخرج إلى ملف الخرج.

```java
public static void extractTextFromRegion(Path inputFile, Path outputFile, int pageNumber, Rectangle rectangle)
        throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber absorber = new TextAbsorber();
        TextSearchOptions options = new TextSearchOptions(rectangle);
        options.setLimitToPageBounds(true);
        absorber.setTextSearchOptions(options);
        document.getPages().get_Item(pageNumber).accept(absorber);
        Files.writeString(outputFile, absorber.getText());
    }
}
```

## استخراج الفقرات مع معلومات الهندسة

استخدام `ParagraphAbsorber` لفحص مستطيلات الأقسام ومضلعات الفقرات مع النص المستخرج.

1. افتح ملف PDF المصدر في [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. أنشئ كائنًا من الفئة [ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) وزيارة الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) لبناء معلومات ترميز الصفحة.
1. اقرأ نتيجة ترميز الصفحة الأولى وتكرّر عبر أقسامها وفقراتها.
1. اجمع كل مستطيل قسم، ومضلع الفقرة، ونص الفقرة المعاد بناؤه من [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) خطوط.
1. أنشئ تقرير الإخراج مع تفاصيل الهندسة والنص المستخرج.
1. اكتب التفاصيل المستخرجة إلى ملف الإخراج.

```java
public static void extractParagraphsWithGeometry(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        PageMarkup pageMarkup = absorber.getPageMarkups().get(0);
        StringBuilder text = new StringBuilder();
        int sectionIndex = 1;
        for (MarkupSection section : pageMarkup.getSections()) {
            text.append("Section ").append(sectionIndex)
                    .append(": rectangle = ").append(section.getRectangle()).append("\n");
            int paragraphIndex = 1;
            for (MarkupParagraph paragraph : section.getParagraphs()) {
                text.append("  Paragraph ").append(paragraphIndex)
                        .append(": polygon = ").append(Arrays.toString(paragraph.getPoints())).append("\n");
                StringBuilder paragraphText = new StringBuilder();
                for (List<TextFragment> line : paragraph.getLines()) {
                    for (TextFragment fragment : line) {
                        paragraphText.append(fragment.getText());
                    }
                    paragraphText.append("\r\n");
                }
                text.append("    Text: ").append(paragraphText).append("\n\n");
                paragraphIndex++;
            }
            sectionIndex++;
        }

        Files.writeString(outputFile, text.toString());
    }
}
```
