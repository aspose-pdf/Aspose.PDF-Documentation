---
title: إضافة الجداول إلى PDF في جافا
linktitle: إضافة الجداول
type: docs
weight: 10
url: /java/adding-tables/
description: تعرف على كيفية إضافة الجداول وتكوينها في مستندات PDF الموجودة في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة الجداول وتنسيقها في مستندات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية إضافة الجداول وتكوينها في مستندات PDF باستخدام Aspose.PDF لـ Java. وهو يغطي إنشاء الجدول، والحدود، والهوامش، والحشو، وامتدادات الصفوف والأعمدة، وسلوك الاحتواء التلقائي، وإدراج الصور في الخلايا، وتكرار الصفوف والأعمدة، وأجزاء HTML وLaTeX، والتحكم في العرض متعدد الصفحات.
---
يوفر Aspose.PDF for Java واجهة برمجة تطبيقات `Table` غنية لإنشاء الجداول مع تخصيص التخطيط والمحتوى.

## إنشاء جدول أساسي

استخدم هذا المثال عندما تحتاج إلى إضافة جدول بسيط بحدود موحدة وخلايا نصية.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. قم بإنشاء [جدول](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) وقم بتكوين حدوده.
1. أضف صفوفًا وخلايا، وأرفق الجدول بالصفحة، ثم احفظ المستند.

```java
public static void createTable(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 5, Color.getLightGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 5, Color.getLightGray()));
        for (int rowCount = 0; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add("Column (" + rowCount + ", 1)");
            row.getCells().add("Column (" + rowCount + ", 2)");
            row.getCells().add("Column (" + rowCount + ", 3)");
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## أضف خلايا ذات امتداد الصف وامتداد العمود

استخدم هذا المثال عندما يحتاج الجدول إلى خلايا مدمجة عبر الصفوف أو الأعمدة.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. قم بإنشاء [جدول](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) وأضف صفوفًا.
1. قم بتكوين `ColSpan` و`RowSpan` على الخلايا المستهدفة، ثم احفظ ملف PDF.

```java
public static void addRowspanOrColspan(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));

        Row row1 = table.getRows().add();
        for (int cellCount = 1; cellCount < 5; cellCount++) {
            row1.getCells().add("Test 1" + cellCount);
        }

        Row row2 = table.getRows().add();
        row2.getCells().add("Test 2 1");
        Cell cell = row2.getCells().add("Test 2 2");
        cell.setColSpan(2);
        row2.getCells().add("Test 2 4");

        Row row3 = table.getRows().add();
        row3.getCells().add("Test 3 1");
        row3.getCells().add("Test 3 2");
        row3.getCells().add("Test 3 3");
        row3.getCells().add("Test 3 4");

        Row row4 = table.getRows().add();
        row4.getCells().add("Test 4 1");
        cell = row4.getCells().add("Test 4 2");
        cell.setRowSpan(2);
        row4.getCells().add("Test 4 3");
        row4.getCells().add("Test 4 4");

        Row row5 = table.getRows().add();
        row5.getCells().add("Test 5 1");
        row5.getCells().add("Test 5 3");
        row5.getCells().add("Test 5 4");

        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## أضف حدود الجدول وحشو الخلايا

استخدم هذا المثال عندما تحتاج إلى تكوين الحدود والحشو وسلوك التفاف الخلايا.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. قم بإنشاء [جدول](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) وقم بتكوين العروض والحدود والحشوة.
1. أضف صفوفًا واحفظ المستند الناتج.

```java
public static void addBorders(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        page.getParagraphs().add(table);
        table.setColumnWidths("50 50 50");
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1f));
        table.setBorder(new BorderInfo(BorderSide.All, 1));
        table.setDefaultCellPadding(new MarginInfo(5, 5, 5, 5));

        Row row1 = table.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();
        row1.getCells().get_Item(2).getParagraphs().add(new TextFragment("col3 with large text string"));
        row1.getCells().get_Item(2).setWordWrapped(false);

        Row row2 = table.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");
        document.save(outputFile.toString());
    }
}
```

## تمكين تخطيط الجدول الملاءمة التلقائية

استخدم هذا المثال عندما يجب أن يتم ضبط الجدول تلقائيًا حسب عرض الصفحة المتوفر.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. قم بإنشاء [جدول](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) وقم بتعيين `ColumnAdjustment.AutoFitToWindow`.
1. أضف صفوفًا نموذجية واحفظ ملف PDF.

```java
public static void autoFit(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        page.getParagraphs().add(table);
        table.setColumnWidths("50 50 50");
        table.setColumnAdjustment(ColumnAdjustment.AutoFitToWindow);
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1f));
        table.setBorder(new BorderInfo(BorderSide.All, 1));
        table.setDefaultCellPadding(new MarginInfo(5, 5, 5, 5));

        Row row1 = table.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add("col3");
        Row row2 = table.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");
        document.save(outputFile.toString());
    }
}
```

## إضافة صورة داخل خلية جدول

استخدم هذا المثال عندما يحتاج الجدول إلى عرض محتوى الصورة النقطية داخل إحدى خلاياه.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. قم بإنشاء [جدول](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) وأضف صفًا يحتوي على خلايا نصية وصورة.
1. قم بتكوين حجم [الصورة](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) واحفظ المستند.

```java
public static void addImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setColumnWidths("200 100");

        Row row = table.getRows().add();
        row.getCells().add().getParagraphs().add(new TextFragment(imageFile.toString()));
        Image image = new Image();
        image.setFile(imageFile.toString());
        image.setFixWidth(50);
        image.setFixHeight(50);
        row.getCells().add().getParagraphs().add(image);

        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## أضف صور SVG داخل خلايا الجدول

استخدم هذا المثال عندما يجب أن يعرض الجدول ملفات SVG صفًا تلو الآخر.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. قم بإنشاء [جدول](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) وقم بالتكرار عبر ملفات SVG.
1. أضف صفًا واحدًا لكل صورة، وقم بتكوين SVG [صورة](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/)، واحفظ ملف PDF.

```java
public static void addSvgImage(List<Path> imageFiles, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setColumnWidths("200 100");
        for (Path imageFile : imageFiles) {
            Row row = table.getRows().add();
            row.getCells().add().getParagraphs().add(new TextFragment(imageFile.toString()));
            Image image = new Image();
            image.setFileType(ImageFileType.Svg);
            image.setFile(imageFile.toString());
            image.setFixWidth(50);
            image.setFixHeight(50);
            row.getCells().add().getParagraphs().add(image);
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## إضافة أجزاء HTML إلى خلايا الجدول

استخدم هذا المثال عندما يجب أن يتضمن محتوى الجدول تنسيق HTML المضمن.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. قم بإنشاء [جدول](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) وقم بتكوين الحدود.
1. أضف كائنات [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlfragment/) إلى الخلايا واحفظ المستند.

```java
public static void addHtmlFragments(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray()));
        for (int rowCount = 1; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add().getParagraphs().add(new HtmlFragment("Column <strong>(" + rowCount + ", 1)</strong>"));
            row.getCells().add().getParagraphs().add(new HtmlFragment("Column <span style='color:red'>(" + rowCount + ", 2)</span>"));
            row.getCells().add().getParagraphs().add(new HtmlFragment("Column <span style='text-decoration: underline'>(" + rowCount + ", 3)</span>"));
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## أضف أجزاء LaTeX إلى خلايا الجدول

استخدم هذا المثال عندما يجب أن يعرض محتوى الجدول تعبيرات TeX أو LaTeX.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. قم بإنشاء [جدول](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) بحدود.
1. أضف كائنات [TeXFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/texfragment/) إلى الخلايا واحفظ ملف الإخراج.

```java
public static void addLatexFragments(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray()));
        for (int rowCount = 1; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add().getParagraphs().add(new TeXFragment("Column $\\mathbf{(" + rowCount + ", 1)}$"));
            row.getCells().add().getParagraphs().add(new TeXFragment("Column $\\textcolor{red}{(" + rowCount + ", 2)}$"));
            row.getCells().add().getParagraphs().add(new TeXFragment("Column $\\underline{(" + rowCount + ", 3)}$"));
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## فرض جدول على صفحة جديدة

استخدم هذا المثال عندما يجب أن يبدأ الجدول الثاني على صفحة منفصلة بعد جدول كبير.

1. قم بإنشاء [مستند] PDF جديد (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وقم بتكوين إعدادات الصفحة.
1. أنشئ أول [جدول] كبير (https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) وأضفه إلى الصفحة.
1. قم بإنشاء جدول ثانٍ، وقم بتعيين `InNewPage`، واحفظ المستند.

```java
public static void addTableOnNewPage(Path outputFile) {
    try (Document document = new Document()) {
        document.getPageInfo().getMargin().setLeft(37);
        document.getPageInfo().getMargin().setRight(37);
        document.getPageInfo().getMargin().setTop(37);
        document.getPageInfo().getMargin().setBottom(37);
        document.getPageInfo().setLandscape(true);

        Page page = document.getPages().add();
        Table table = new Table();
        table.setColumnWidths("50 100");
        for (int i = 1; i < 121; i++) {
            Row row = table.getRows().add();
            row.setFixedRowHeight(15);
            row.getCells().add().getParagraphs().add(new TextFragment("Content 1"));
            row.getCells().add().getParagraphs().add(new TextFragment("Content 2"));
        }
        page.getParagraphs().add(table);

        Table table1 = new Table();
        table1.setColumnWidths("100 100");
        for (int i = 1; i < 11; i++) {
            Row row = table1.getRows().add();
            row.getCells().add().getParagraphs().add(new TextFragment("Content 3"));
            row.getCells().add().getParagraphs().add(new TextFragment("Content 4"));
        }
        table1.setInNewPage(true);
        page.getParagraphs().add(table1);
        document.save(outputFile.toString());
    }
}
```

## أنشئ جدولًا مكسورًا رأسيًا بأعمدة متكررة

استخدم هذا المثال عندما يستمر جدول عريض عموديًا ويكرر أعمدة المفاتيح.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. قم بإنشاء [جدول](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) وقم بتكوين الفصل الرأسي باستخدام الأعمدة المتكررة.
1. أضف صفوف الرأس والبيانات، ثم احفظ المستند.

```java
public static void addTableHideBorders(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBroken(TableBroken.Vertical);
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All));
        table.setRepeatingColumnsCount(2);
        page.getParagraphs().add(table);

        Row row = table.getRows().add();
        Cell cell = row.getCells().add("header 1");
        cell.setColSpan(2);
        cell.setBackgroundColor(Color.getLightGray());
        row.getCells().add("header 3");
        Cell cell2 = row.getCells().add("header 4");
        cell2.setColSpan(2);
        cell2.setBackgroundColor(Color.getLightBlue());
        row.getCells().add("header 6");
        Cell cell3 = row.getCells().add("header 7");
        cell3.setColSpan(2);
        cell3.setBackgroundColor(Color.getLightGreen());
        Cell cell4 = row.getCells().add("header 9");
        cell4.setColSpan(3);
        cell4.setBackgroundColor(Color.getLightCoral());
        for (int i = 12; i < 18; i++) {
            row.getCells().add("header " + i);
        }

        for (int rowCounter = 0; rowCounter < 3; rowCounter++) {
            Row row1 = table.getRows().add();
            for (int i = 1; i < 18; i++) {
                row1.getCells().add("col " + rowCounter + ", " + i);
            }
        }
        document.save(outputFile.toString());
    }
}
```

## إعادة استخدام الحدود والمثال الحشو

استخدم هذا المساعد عندما يجب تفويض سيناريو الهوامش والحشو إلى مثال الحدود المشتركة.

1. استدعاء حدود الجدول الموجود وطريقة الحشو.
1. أعد استخدام نفس منطق تخطيط الجدول دون تكرار التعليمات البرمجية.

```java
public static void addMarginsOrPadding(Path outputFile) {
    addBorders(outputFile);
}
```

## قم بإنشاء جدول بزوايا مستديرة

استخدم هذا المثال عندما يجب أن يستخدم الجدول نمط الزوايا المستديرة بدلاً من الحدود المستطيلة القياسية.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. قم بإنشاء [جدول](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) وقم بتكوين إعدادات الحدود المستديرة.
1. أضف صفوفًا إلى الجدول واحفظ ملف PDF.

```java
public static void createTableWithRoundCorner(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        BorderInfo borderInfo = new BorderInfo(BorderSide.All);
        borderInfo.setRoundedBorderRadius(15);
        table.setCornerStyle(BorderCornerStyle.Round);
        table.setBorder(borderInfo);
        for (int rowCount = 0; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add("Column (" + rowCount + ", 1)");
            row.getCells().add("Column (" + rowCount + ", 2)");
            row.getCells().add("Column (" + rowCount + ", 3)");
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## إضافة صفوف رأس متكررة

استخدم هذا المثال عندما يجب أن تكرر الجداول متعددة الصفحات صفوف رؤوسها في كل صفحة متابعة.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. قم بإنشاء [جدول] (https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) منقسم رأسيًا وقم بتكوين عدد الصفوف والنمط المتكرر.
1. أضف صفوف الرأس وصفوف البيانات، ثم احفظ المستند.

```java
public static void addRepeatingRows(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBroken(TableBroken.Vertical);
        table.setRepeatingRowsCount(2);
        TextState textState = new TextState();
        textState.setFontSize(12);
        textState.setFont(FontRepository.findFont("TimesNewRoman"));
        textState.setForegroundColor(Color.getRed());
        table.setRepeatingRowsStyle(textState);
        table.setColumnWidths("100 100 100");
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));
        table.setBorder(new BorderInfo(BorderSide.All, 1, Color.getBlack()));

        Row headerRow1 = table.getRows().add();
        headerRow1.getCells().add("Header 1-1");
        headerRow1.getCells().add("Header 1-2");
        headerRow1.getCells().add("Header 1-3");
        for (Cell cell : headerRow1.getCells()) {
            cell.setBackgroundColor(Color.getLightGray());
        }
        Row headerRow2 = table.getRows().add();
        headerRow2.getCells().add("Header 2-1");
        headerRow2.getCells().add("Header 2-2");
        headerRow2.getCells().add("Header 2-3");
        for (Cell cell : headerRow2.getCells()) {
            cell.setBackgroundColor(Color.getLightBlue());
        }
        for (int i = 1; i < 101; i++) {
            Row row = table.getRows().add();
            row.getCells().add("Data " + i + "-1");
            row.getCells().add("Data " + i + "-2");
            row.getCells().add("Data " + i + "-3");
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## إضافة أعمدة متكررة في جدول واسع

استخدم هذا المثال عندما يجب أن تتكرر الأعمدة الأولى بينما ينكسر الجدول عموديًا على نفس الصفحة.

1. قم بإنشاء [مستند] PDF جديد (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وقم بتكوين حجم الصفحة.
1. قم بإنشاء [جدول](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) وقم بتعيين الأعمدة المتكررة بالإضافة إلى سلوك الاحتواء التلقائي.
1. قم بإضافة صفوف الرأس والبيانات، ثم احفظ ملف PDF.

```java
public static void addRepeatingColumns(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(PageSize.getA5().getHeight(), PageSize.getA5().getWidth());
        BorderInfo border = new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray());
        Table table = new Table();
        table.setBroken(TableBroken.VerticalInSamePage);
        table.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);
        table.setRepeatingColumnsCount(5);
        table.setBorder(border);
        table.setDefaultCellBorder(border);
        page.getParagraphs().add(table);

        Row row = table.getRows().add();
        for (int i = 1; i < 6; i++) {
            Cell cell = row.getCells().add("header " + i);
            cell.setBackgroundColor(Color.getLightGray());
        }
        for (int i = 6; i < 18; i++) {
            row.getCells().add("header " + i);
        }

        for (int rowCounter = 1; rowCounter < 6; rowCounter++) {
            row = table.getRows().add();
            for (int i = 1; i < 6; i++) {
                Cell cell = row.getCells().add("cell " + rowCounter + "," + i);
                cell.setBackgroundColor(Color.getLightGray());
            }
            for (int i = 6; i < 18; i++) {
                row.getCells().add("cell " + rowCounter + "," + i);
            }
        }
        document.save(outputFile.toString());
    }
}
```

## إدراج فواصل الصفحات بين صفوف الجدول

استخدم هذا المثال عندما يجب أن تبدأ صفوف جدول معينة في صفحة جديدة.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. قم بإنشاء [جدول](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) وقم بتعبئة العديد من الصفوف.
1. قم بتمييز الصفوف المحددة بـ `InNewPage` واحفظ المستند.

```java
public static void insertPageBreak(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, Color.getRed()));
        table.setColumnWidths("100 100");
        for (int counter = 0; counter < 201; counter++) {
            Row row = new Row();
            table.getRows().add(row);
            row.getCells().add().getParagraphs().add(new TextFragment("Cell " + counter + ", 0"));
            row.getCells().add().getParagraphs().add(new TextFragment("Cell " + counter + ", 1"));
            if (counter % 10 == 0 && counter != 0) {
                row.setInNewPage(true);
            }
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## تدوير النص داخل خلايا الجدول

استخدم هذا المثال عندما يجب عرض نص الخلية بزوايا دوران مختلفة.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. قم بإنشاء [جدول](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) وأضف صفًا يحتوي على خلايا متعددة.
1. قم بإنشاء كائنات [TextFragment] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) تم تدويرها، وأضفها إلى الخلايا، واحفظ ملف PDF.

```java
public static void rotatedTextTable(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));
        Row row = table.getRows().add();
        row.setMinRowHeight(200);
        for (int cellCount = 0; cellCount < 4; cellCount++) {
            Cell cell = row.getCells().add();
            TextFragment textFragment = new TextFragment("Cell 1 " + (cellCount - 1));
            textFragment.getTextState().setRotation(90 * cellCount);
            textFragment.setHorizontalAlignment(HorizontalAlignment.Center);
            cell.getParagraphs().add(textFragment);
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```
