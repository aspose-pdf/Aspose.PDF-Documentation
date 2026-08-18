---
title: الاستخراج على أساس المنطقة باستخدام Java
linktitle: الاستخراج على أساس المنطقة
type: docs
weight: 20
url: /java/region-based-extraction/
description: تعرف على كيفية استخراج النص من منطقة صفحة معينة أو فحص هندسة الفقرة في مستندات PDF باستخدام Aspose.PDF لـ Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## استخراج النص من منطقة صفحة مستطيلة

استخدم `TextSearchOptions` مع `Rectangle` لتقييد الاستخراج بمنطقة محددة في الصفحة.

1. افتح ملف PDF المصدر في مثيل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [TextAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) لتجميع النص من منطقة الصفحة المحددة.
1. أنشئ [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsearchoptions/) للهدف [المستطيل](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) وقم بتمكين `setLimitToPageBounds(true)` بحيث يبقى الاستخراج داخل مربع الصفحة المرئي.
1. قم بتطبيق خيارات البحث المكونة على أداة الامتصاص وقم بزيارة الهدف [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. اكتب المخزن المؤقت للنص المستخرج إلى ملف الإخراج.

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

## استخراج الفقرات بالمعلومات الهندسية

استخدم `ParagraphAbsorber` لفحص مستطيلات القسم ومضلعات الفقرة مع النص المستخرج.

1. افتح ملف PDF المصدر في مثيل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [ParagraphAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) وقم بزيارة [الصفحة] المستهدفة (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) لإنشاء معلومات ترميز الصفحة.
1. اقرأ نتيجة ترميز الصفحة الأولى وكررها عبر أقسامها وفقراتها.
1. قم بتجميع مستطيل القسم ومضلع الفقرة ونص الفقرة المعاد بناؤه من أسطر [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. أنشئ تقرير الإخراج باستخدام الأشكال الهندسية وتفاصيل النص المستخرج.
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
