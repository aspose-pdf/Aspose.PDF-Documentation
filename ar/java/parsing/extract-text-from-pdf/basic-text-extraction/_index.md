---
title: استخراج النص الأساسي باستخدام جافا
linktitle: استخراج النص الأساسي
type: docs
weight: 10
url: /java/basic-text-extraction/
description: تعرف على كيفية استخراج النص من مستندات PDF في Java باستخدام Aspose.PDF من جميع الصفحات، أو من صفحة معينة، أو حسب بنية الفقرة.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
يعد استخراج النص الأساسي نقطة البداية لقراءة محتوى PDF في Java. يوفر Aspose.PDF طريقتين شائعتين:

- استخدم `TextAbsorber` عندما تحتاج إلى نتيجة نص عادي من مستند أو صفحة.
- استخدم `ParagraphAbsorber` عندما تحتاج إلى الاحتفاظ بتجميع الصفحات والقسم والفقرة والأسطر والأجزاء.

لا تقوم صفحات PDF بتخزين النص مثل مستند معالجة النصوص، لذا يعتمد الترتيب المستخرج على تدفق محتوى الصفحة وتخطيطها. بالنسبة للاستخراج الخاص بالمنطقة، أو تفاصيل الهندسة، أو التخطيطات متعددة الأعمدة، أو التعليقات التوضيحية، أو النص المميز، أو اكتشاف الحروف المرتفعة والمنخفضة، استخدم مقالات الاستخراج ذات الصلة في هذا القسم.

## استخراج النص من كافة الصفحات

استخدم `TextAbsorber` لتجميع دفق نص ثابت من المستند بأكمله وكتابته في ملف. هذا هو الخيار الأبسط عندما تحتاج فقط إلى محتوى النص المقروء ولا تحتاج إلى حدود الفقرة أو إحداثياتها.

1. افتح ملف PDF المصدر في مثيل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [TextAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) لتجميع النص عبر المستند بأكمله.
1. اتصل بـ`document.getPages().accept(textAbsorber)` حتى تتم زيارة كل [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) بواسطة الممتص.
1. اكتب المخزن المؤقت للنص المستخرج إلى ملف الإخراج.

```java
public static void extractTextFromAllPages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## استخراج النص من صفحة معينة

قم بتطبيق الممتص على الصفحة التي تحتاجها فقط. أرقام الصفحات في مجموعة الصفحات `Document` تعتمد على الرقم 1، لذلك يقرأ `get_Item(1)` الصفحة الأولى.

1. افتح ملف PDF المصدر في مثيل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [TextAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) لاستخراج صفحة واحدة.
1. اتصل بـ `accept(textAbsorber)` على [الصفحة] المستهدفة (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) المحددة حسب رقم الصفحة.
1. اكتب المخزن المؤقت للنص المستخرج إلى ملف الإخراج.

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

استخدم `ParagraphAbsorber` عندما تحتاج إلى تجميع هيكلي بدلاً من دفق نص عادي واحد. تقوم بإرجاع علامات الصفحة التي تحتوي على الأقسام والفقرات والسطور وكائنات `TextFragment`، وهو أمر مفيد عندما يجب أن يحافظ الإخراج على الكتل المنطقية للنص.

1. افتح ملف PDF المصدر في مثيل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [ParagraphAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) وقم بزيارة المستند بأكمله لإنشاء نتائج ترميز الصفحة.
1. قم بالتكرار من خلال علامات الصفحة والأقسام والفقرات والأسطر وكائنات [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) التي تم الكشف عنها بواسطة أداة الامتصاص.
1. أنشئ نص الإخراج باستخدام ترقيم صريح للصفحات والأقسام والفقرات بحيث يتم الحفاظ على التجميع الهيكلي.
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
