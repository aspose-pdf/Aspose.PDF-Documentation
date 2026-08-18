---
title: إنشاء ملف PDF معقد
linktitle: إنشاء ملف PDF معقد
type: docs
weight: 30
url: /java/complex-pdf-example/
description: يتيح لك Aspose.PDF for Java إنشاء مستندات PDF أكثر تعقيدًا تحتوي على صور وأجزاء نصية وجداول في ملف واحد.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإنشاء ملف PDF معقد باستخدام Java
Abstract: توضح هذه المقالة كيفية إنشاء ملف PDF أكثر تعقيدًا في Java باستخدام Aspose.PDF. يضيف المثال صورة، وعنوانًا منسقًا، وكتلة نص وصفية، وجدولًا يحتوي على خلايا رأس ذات نمط وصفوف جدول تم إنشاؤها، ثم يحفظ النتيجة كمستند PDF.
---
يغطي مثال [Hello World](/pdf/java/hello-world-example/) أبسط مسار لإنشاء ملف PDF. يعتمد هذا المثال على سير العمل هذا ويقوم بإنشاء مستند أكثر ثراءً يجمع بين الرسومات والنص والمحتوى الجدولي.

لإنشاء مستند PDF أكثر تعقيدًا في Java:

1. أنشئ [مستندًا](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. أضف صورة إلى [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) باستخدام `page.addImage(...)` وهدف [مستطيل](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. قم بإنشاء رأس [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) وقم بتعيين الخط والحجم والمحاذاة و[الموضع](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/).
1. قم بإنشاء [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) ثانيًا لفقرة الوصف.
1. قم بإنشاء [جدول](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) باستخدام الحدود والحشو وتصميم الرأس.
1. أضف صفوف الجدول التي تم إنشاؤها إلى [الجدول](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/).
1. قم بإلحاق [الجدول](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) بفقرات [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. احفظ ملف PDF الناتج [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

يعتمد كود Java التالي على `GetStartedExamples.java`.

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

يستخدم نفس المثال طريقة مساعدة لإعداد جدول الجدول بتنسيق الرأس وأوقات المغادرة التي تم إنشاؤها:

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
