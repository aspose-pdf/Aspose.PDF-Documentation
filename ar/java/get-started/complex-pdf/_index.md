---
title: إنشاء ملف PDF معقد
linktitle: إنشاء ملف PDF معقد
type: docs
weight: 30
url: /ar/java/complex-pdf-example/
description: يتيح Aspose.PDF for Java إنشاء مستندات PDF أكثر تعقيدًا تحتوي على صور، قطع نصية، وجداول في ملف واحد.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إنشاء ملف PDF معقد باستخدام Java
Abstract: توضح هذه المقالة كيفية إنشاء ملف PDF أكثر تعقيدًا في Java باستخدام Aspose.PDF. يضيف المثال صورة، عنوانًا منسقًا، كتلة نصية وصفية، وجدولًا بخلايا رأسية منسقة وصفوف جدولية مُولدة، ثم يحفظ النتيجة كملف PDF.
---
الـ [مرحبًا بالعالم](/pdf/ar/java/hello-world-example/) يوضح المثال أبسط مسار لإنشاء PDF. يبني هذا المثال على سير العمل هذا وينشئ مستندًا أغنى يجمع بين الرسومات والنصوص والمحتوى الجدولي.

لإنشاء مستند PDF أكثر تعقيدًا في Java:

1. إنشاء [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وإضافة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. أضف صورة إلى [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) مع `page.addImage(...)` وهدف [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. إنشاء رأس [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) وقم بتعيين الخط والحجم والمحاذاة و [Position](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/).
1. إنشاء ثانٍ [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) للفقرة الوصفية.
1. بناء [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) مع حدود، حشو، وتنسيق الرأس.
1. إضافة صفوف الجدول الزمني المُولَّدة إلى [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/).
1. إلحاق الـ [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) إلى الـ [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) الفقرات.
1. احفظ ملف PDF الناتج [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

الكود Java التالي مبني على `GetStartedExamples.java`.

```java
public static void complexExample(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        page.addImage(imageFile.toString(), new Rectangle(20, 730, 120, 830, true));

        TextFragment header = new TextFragment("New ferry routes in Fall 2029");
        header.getTextState().setFont(FontRepository.findFont("Arial"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment(HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        String descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. "
                + "Ferry service is operating at half capacity and on a reduced schedule. "
                + "Expect lineups.";
        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);

        page.getParagraphs().add(createScheduleTable());

        document.save(outputFile.toString());
    }
}
```

يستخدم المثال نفسه طريقة مساعدة لإعداد جدول المواعيد مع تنسيق العنوان وتوقيتات المغادرة المُولدة:

```java
private static Table createScheduleTable() {
    Table table = new Table();
    table.setColumnWidths("200 200");
    table.setBorder(new BorderInfo(BorderSide.Box, 1.0f, Color.getDarkSlateGray()));
    table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
    table.setDefaultCellPadding(new MarginInfo(4.5, 4.5, 4.5, 4.5));
    table.getMargin().setBottom(10);
    table.getDefaultCellTextState().setFont(FontRepository.findFont("Helvetica"));

    Row headerRow = table.getRows().add();
    Cell departsCityCell = headerRow.getCells().add("Departs City");
    Cell departsIslandCell = headerRow.getCells().add("Departs Island");
    styleHeaderCell(departsCityCell);
    styleHeaderCell(departsIslandCell);

    Duration time = Duration.ofHours(6);
    Duration increment = Duration.ofMinutes(30);
    for (int index = 0; index < 10; index++) {
        Row dataRow = table.getRows().add();
        dataRow.getCells().add(formatTime(time));
        time = time.plus(increment);
        dataRow.getCells().add(formatTime(time));
    }

    return table;
}
```
