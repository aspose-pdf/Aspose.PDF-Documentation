---
title: إنشاء أو إضافة جدول في PDF 
linktitle: إنشاء أو إضافة جدول
type: docs
weight: 10
url: /ar/java/add-table-in-existing-pdf-document/
description: تعلم كيفية إنشاء أو إضافة جدول إلى مستند PDF، تطبيق نمط الخلية، تقسيم الجدول على الصفحات وتخصيص الصفوف والأعمدة إلخ.
lastmod: "2021-12-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إنشاء الجدول

تحتوي مساحة الأسماء Aspose.PDF على فئات باسم [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table)، [Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/cell)، و[Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/row) والتي توفر وظائف لإنشاء الجداول عند إنشاء مستندات PDF من الصفر.

يمكن إنشاء جدول عن طريق إنشاء كائن من فئة الجدول.

```java
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### إضافة جدول في مستند PDF موجود

لإضافة جدول إلى ملف PDF موجود باستخدام Aspose.PDF لـ Java، اتبع الخطوات التالية:

1. قم بتحميل الملف المصدر.

1. تهيئة جدول وتعيين أعمدته وصفوفه.
1. تعيين إعدادات الجدول (قمنا بتعيين الحدود).
1. ملء الجدول.
1. إضافة الجدول إلى صفحة.
1. حفظ الملف.

تُظهر مقتطفات الشيفرة التالية كيفية إضافة نص في ملف PDF موجود.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddTable {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void CreateTable() {
        Document doc = new Document(_dataDir + "input.pdf");
        // تهيئة مثيل جديد من الجدول
        Table table = new Table();
        // تعيين لون حدود الجدول كرمادي فاتح
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // تعيين الحدود لخلايا الجدول
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // إنشاء حلقة لإضافة 10 صفوف
        for (int row_count = 1; row_count < 10; row_count++) {
            // إضافة صف إلى الجدول
            Row row = table.getRows().add();
            // إضافة خلايا الجدول
            row.getCells().add("عمود (" + row_count + ", 1)");
            row.getCells().add("عمود (" + row_count + ", 2)");
            row.getCells().add("عمود (" + row_count + ", 3)");
        }
        // إضافة كائن الجدول إلى الصفحة الأولى من المستند المدخل
        doc.getPages().get_Item(1).getParagraphs().add(table);
        // حفظ المستند المحدث الذي يحتوي على كائن الجدول
        doc.save(_dataDir + "document_with_table.pdf");
    }
```


### ColSpan و RowSpan في جداول Aspose.PDF باستخدام Java

يوفر Aspose.PDF for Java طريقة [setColSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setColSpan-int-) لدمج الأعمدة في الجدول وطريقة [setRowSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setRowSpan-int-) لدمج الصفوف.

نستخدم طرق [setColSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setColSpan-int-) أو [setRowSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setRowSpan-int-) على كائن [Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell) الذي ينشئ خلية الجدول. بعد تطبيق الخصائص المطلوبة، يمكن إضافة الخلية المنشأة إلى الجدول.

```java
public static void AddTable_RowColSpan() {
        // تحميل مستند PDF المصدر
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // تهيئة مثيل جديد من الجدول
        Table table = new Table();
        // تعيين لون حدود الجدول كـ LightGray
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getBlack()));
        // تعيين الحدود لخلايا الجدول
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getBlack()));
        // إضافة الصف الأول إلى الجدول
        Row row1 = table.getRows().add();
        for (int cellCount = 1; cellCount < 5; cellCount++) {
            // إضافة خلايا الجدول
            row1.getCells().add("اختبار 1 " + cellCount);
        }

        // إضافة الصف الثاني إلى الجدول
        Row row2 = table.getRows().add();
        row2.getCells().add("اختبار 2 1");
        Cell cell = row2.getCells().add("اختبار 2 2");
        cell.setColSpan(2);
        row2.getCells().add("اختبار 2 4");

        // إضافة الصف الثالث إلى الجدول
        Row row3 = table.getRows().add();
        row3.getCells().add("اختبار 3 1");
        row3.getCells().add("اختبار 3 2");
        row3.getCells().add("اختبار 3 3");
        row3.getCells().add("اختبار 3 4");

        // إضافة الصف الرابع إلى الجدول
        Row row4 = table.getRows().add();
        row3.getCells().add("اختبار 4 1");
        cell = row3.getCells().add("اختبار 4 2");
        cell.setRowSpan(2);
        row3.getCells().add("اختبار 4 3");
        row3.getCells().add("اختبار 4 4");

        // إضافة الصف الخامس إلى الجدول
        row4 = table.getRows().add();
        row4.getCells().add("اختبار 5 1");
        row4.getCells().add("اختبار 5 3");
        row4.getCells().add("اختبار 5 4");

        // إضافة كائن الجدول إلى الصفحة الأولى من المستند المدخل
        page.getParagraphs().add(table);

        // حفظ المستند المحدث الذي يحتوي على كائن الجدول
        pdfDocument.save(_dataDir + "document_with_table_out.pdf");
    }
```


نتيجة تنفيذ الكود أدناه هي الجدول الموضح في الصورة التالية:

![عرض تجريبي لـ ColSpan و RowSpan](colspan_rowspan.png)

## العمل مع الحدود والهوامش والحشو

يسمح Aspose.PDF لـ Java للمطورين بإنشاء جداول في مستندات PDF. وفقًا لنموذج كائن المستند الخاص بـ Aspose.PDF، يُعتبر الجدول عنصراً على مستوى الفقرة.

يرجى ملاحظة أنه يدعم أيضًا ميزة تعيين نمط الحدود والهوامش وحشو الخلايا للجداول. قبل الدخول في التفاصيل الفنية، من المهم فهم مفاهيم الحدود والهوامش والحشو التي يتم تقديمها أدناه في مخطط:

![الحدود والهوامش والحشو](set-border-style-margins-and-padding-of-table_1.png)

في الشكل أعلاه، يمكنك أن ترى أن حدود الجدول والصف والخلية تتداخل. باستخدام Aspose.PDF، يمكن أن يحتوي الجدول على هوامش ويمكن أن تحتوي الخلايا على حشوات. لتعيين هوامش الخلايا، يجب علينا تعيين حشو الخلية.

## الحدود

لتعيين حدود كائنات [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#setBorder-com.aspose.pdf.BorderInfo-)، [Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/Row#setBorder-com.aspose.pdf.BorderInfo-) و[Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setBorder-com.aspose.pdf.BorderInfo-)، استخدم طرق [Table.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#setBorder-com.aspose.pdf.BorderInfo-)، [Row.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Row#setBorder-com.aspose.pdf.BorderInfo-) و[Cell.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setBorder-com.aspose.pdf.BorderInfo-).
 يمكن أيضاً تحديد حدود الخلايا باستخدام طريقة [DefaultCellBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Row#setDefaultCellBorder-com.aspose.pdf.BorderInfo-) من صف [Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/row) أو [جدول](https://reference.aspose.com/pdf/java/com.aspose.pdf/table). جميع الخصائص المتعلقة بالحدود التي تمت مناقشتها أعلاه تُسند إلى مثيل لفئة الصف، التي يتم إنشاؤها عن طريق استدعاء مُنشئها. تحتوي فئة الصف على العديد من التحميلات التي تأخذ تقريباً جميع المعلمات المطلوبة لتخصيص الحدود.

## الهوامش أو الحشوة

يمكن إدارة حشوة الخلايا باستخدام طريقة [DefaultCellPadding](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#setDefaultCellPadding-com.aspose.pdf.MarginInfo-) لفئة الجدول. جميع الخصائص المتعلقة بالهوامش يتم تعيينها كنسخة من فئة [MarginInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/MarginInfo) التي تأخذ معلومات حول المعلمات `Left` و`Right` و`Top` و`Bottom` لإنشاء هوامش مخصصة.

في المثال التالي، يتم تعيين عرض حدود الخلية إلى 0.1 نقطة، وعرض حدود الجدول إلى 1 نقطة ويتم تعيين حشو الخلية إلى 5 نقاط.

![الهامش والحدود في جدول PDF](margin-border.png)

```java
public static void MargingPadding() {
        // إنشاء كائن الوثيقة باستدعاء منشئه الفارغ
        Document doc = new Document();
        Page page = doc.getPages().add();
        // إنشاء كائن الجدول
        Table tab1 = new Table();
        // إضافة الجدول في مجموعة الفقرات للقسم المطلوب
        page.getParagraphs().add(tab1);
        // تعيين عرض أعمدة الجدول
        tab1.setColumnWidths ("50 50 50");
        // تعيين حدود الخلية الافتراضية باستخدام كائن BorderInfo
        tab1.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1F));
        // تعيين حدود الجدول باستخدام كائن BorderInfo مخصص آخر
        tab1.setBorder (new BorderInfo(BorderSide.All, 1F));

        // إنشاء كائن MarginInfo وتعيين هوامشه اليسرى والسفلى واليمنى والعلوية
        MarginInfo margin = new MarginInfo();
        margin.setTop (5f);
        margin.setLeft (5f);
        margin.setRight (5f);
        margin.setBottom (5f);

        // تعيين حشو الخلية الافتراضي لكائن MarginInfo
        tab1.setDefaultCellPadding(margin);

        // إنشاء صفوف في الجدول ثم خلايا في الصفوف
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();

        TextFragment mytext = new TextFragment("col3 مع نص طويل");

        row1.getCells().get_Item(2).getParagraphs().add(mytext);
        row1.getCells().get_Item(2).setWordWrapped(false);

        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // حفظ ملف PDF
        doc.save(_dataDir + "MarginsOrPadding_out.pdf");
    }
}
```

لإنشاء جدول بزوايا مستديرة، استخدم قيمة `RoundedBorderRadius` لفئة [BorderInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/BorderInfo) واضبط نمط زوايا الجدول ليكون مستديرًا.

```java
    public static void RoundedBorderRadius() {
        Document doc = new Document();
        Page page = doc.getPages().add();

        // إنشاء كائن جدول
        Table tab1 = new Table();

        // إضافة الجدول إلى مجموعة الفقرات في القسم المطلوب
        page.getParagraphs().add(tab1);

        GraphInfo graph = new GraphInfo();
        graph.setColor(Color.getRed());
        // إنشاء كائن BorderInfo فارغ
        BorderInfo bInfo = new BorderInfo(BorderSide.All, graph);
        // ضبط الحدود لتكون مستديرة حيث يكون نصف القطر 15
        bInfo.setRoundedBorderRadius(15);
        // ضبط نمط زوايا الجدول ليكون مستديرًا.
        tab1.setCornerStyle(BorderCornerStyle.Round);
        // ضبط معلومات حدود الجدول
        tab1.setBorder(bInfo);
        // إنشاء صفوف في الجدول ثم خلايا في الصفوف
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();

        TextFragment mytext = new TextFragment("col3 with large text string");

        row1.getCells().get_Item(2).getParagraphs().add(mytext);
        row1.getCells().get_Item(2).setWordWrapped(false);

        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // حفظ ملف PDF
        doc.save(_dataDir + "BorderRadius_out.pdf");
    }
```


### خاصية AutoFitToWindow في تعداد ColumnAdjustmentType

```java
 public static void AutoFitToWindowProperty() {
        // إنشاء كائن Pdf عن طريق استدعاء منشئه الفارغ
        Document doc = new Document();
        // إنشاء القسم في كائن Pdf
        Page sec1 = doc.getPages().add();

        // إنشاء كائن جدول
        Table tab1 = new Table();
        // إضافة الجدول في مجموعة الفقرات للقسم المطلوب
        sec1.getParagraphs().add(tab1);

        // ضبط عرض الأعمدة في الجدول
        tab1.setColumnWidths("50 50 50");
        tab1.setColumnAdjustment(ColumnAdjustment.AutoFitToWindow);

        // ضبط الحدود الافتراضية للخلية باستخدام كائن BorderInfo
        tab1.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1F));

        // ضبط حدود الجدول باستخدام كائن BorderInfo آخر مخصص
        tab1.setBorder(new BorderInfo(BorderSide.All, 1F));

        // إنشاء كائن MarginInfo وضبط الهوامش اليسرى والسفلية واليمنى والعليا
        MarginInfo margin = new MarginInfo();
        margin.setTop(5f);
        margin.setLeft(5f);
        margin.setRight(5f);
        margin.setBottom(5f);

        // ضبط الحشوة الافتراضية للخلية إلى كائن MarginInfo
        tab1.setDefaultCellPadding(margin);

        // إنشاء صفوف في الجدول ثم خلايا في الصفوف
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add("col3");
        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // حفظ المستند المحدث الذي يحتوي على كائن الجدول
        doc.save(_dataDir + "AutoFitToWindow_out.pdf");
    }
```


### الحصول على عرض الجدول

في بعض الأحيان، يكون من الضروري الحصول على عرض الجدول ديناميكيًا. تحتوي فئة Aspose.PDF.Table على طريقة [GetWidth](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#getWidth--) لهذا الغرض. على سبيل المثال، لم تقم بتعيين عرض أعمدة الجدول بشكل صريح وقمت بتعيين [ColumnAdjustment](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColumnAdjustment) إلى AutoFitToContent. في هذه الحالة، يمكنك الحصول على عرض الجدول كما يلي.

```java
public static void GetTableWidth() {
        // إنشاء مستند جديد
        Document doc = new Document();
        // إضافة صفحة في المستند
        Page page = doc.getPages().add();

        // تهيئة جدول جديد
        Table table = new Table();

        // إضافة الجدول في مجموعة الفقرات للقسم المطلوب
        page.getParagraphs().add(table);
        table.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);

        // إضافة صف في الجدول
        Row row = table.getRows().add();
        // إضافة خلية في الجدول
        row.getCells().add("نص الخلية 1");
        row.getCells().add("نص الخلية 2");
        // الحصول على عرض الجدول
        System.out.println(table.getWidth());
    }
```


## إضافة كائن SVG إلى خلية الجدول

يدعم Aspose.PDF لـ Java ميزة إضافة خلية جدول إلى ملف PDF. أثناء إنشاء جدول، من الممكن إضافة نص أو صور إلى الخلايا. علاوة على ذلك، تقدم الـ API أيضًا ميزة تحويل ملفات SVG إلى تنسيق PDF. باستخدام مزيج من هذه الميزات، من الممكن تحميل صورة SVG وإضافتها إلى خلية جدول.

يُظهر مقتطف الشيفرة التالي الخطوات اللازمة لإنشاء مثيل جدول وإضافة صورة SVG داخل خلية جدول.

```java
 public static void AddSVGObjectToTableCell() {
        // إنشاء كائن المستند
        Document doc = new Document();
        // إنشاء مثيل للصورة
        com.aspose.pdf.Image img = new com.aspose.pdf.Image();
        // تعيين نوع الصورة كـ SVG
        img.setFileType (com.aspose.pdf.ImageFileType.Svg);
        // مسار ملف المصدر
        img.setFile (_dataDir + "SVGToPDF.svg");
        // تعيين العرض لمثيل الصورة
        img.setFixWidth (50);
        // تعيين الارتفاع لمثيل الصورة
        img.setFixHeight (50);
        // إنشاء مثيل الجدول
        com.aspose.pdf.Table table = new com.aspose.pdf.Table();
        // تعيين العرض لخلايا الجدول
        table.setColumnWidths ("100 100");
        // إنشاء كائن الصف وإضافته إلى مثيل الجدول
        com.aspose.pdf.Row row = table.getRows().add();
        // إنشاء كائن الخلية وإضافته إلى مثيل الصف
        com.aspose.pdf.Cell cell = row.getCells().add();
        // إضافة جزء نص إلى مجموعة الفقرات في كائن الخلية
        cell.getParagraphs().add(new TextFragment("First cell"));
        // إضافة خلية أخرى إلى كائن الصف
        cell = row.getCells().add();
        // إضافة صورة SVG إلى مجموعة الفقرات في مثيل الخلية المضاف حديثًا
        cell.getParagraphs().add(img);
        // إنشاء كائن الصفحة وإضافته إلى مجموعة الصفحات في مثيل المستند
        Page page = doc.getPages().add();
        // إضافة الجدول إلى مجموعة الفقرات في كائن الصفحة
        page.getParagraphs().add(table);
        // حفظ ملف PDF
        doc.save(_dataDir + "AddSVGObject_out.pdf");
    }
```


## إضافة علامات HTML داخل الجدول

يسمح Aspose.PDF لـ Java بإضافة جزء HTML جديد داخل فقرة من ملف PDF الخاص بك.

{{% alert color="primary" %}}

يرجى أخذ في الاعتبار أن استخدام علامات HTML داخل عنصر الجدول يزيد من وقت إنشاء المستند، حيث يحتاج API إلى معالجة علامات HTML وفقًا لذلك وعرضها في مستند PDF الناتج.

{{% /alert %}}

```java
  public static void AddHTMLFragmentToTableCell() {
        Document doc = new Document(_dataDir + "input.pdf");
        // يهيئ مثيلًا جديدًا من الجدول
        Table table = new Table();
        // تعيين لون حدود الجدول كرمادي فاتح
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // تعيين الحدود لخلايا الجدول
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // إنشاء حلقة لإضافة 10 صفوف
        for (int row_count = 1; row_count < 10; row_count++) {
            Cell cell;
            // إضافة صف إلى الجدول
            Row row = table.getRows().add();
            // إضافة خلايا الجدول
            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Column <strong>(" + row_count + ", 1)</strong>"));

            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Column <span style='color:red'>(" + row_count + ", 2)</span>"));

            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Column <span style='text-decoration: underline'>(" + row_count + ", 3)</span>"));
        }
        // إضافة كائن الجدول إلى الصفحة الأولى من المستند المدخل
        doc.getPages().get_Item(1).getParagraphs().add(table);
        // حفظ المستند المحدث الذي يحتوي على كائن الجدول
        doc.save(_dataDir + "AddHTMLObject_out.pdf");
    }

}
```


## إدراج فاصل صفحات بين صفوف الجدول

كسلوك افتراضي، عند إنشاء جدول داخل ملف PDF، يتدفق الجدول إلى الصفحات التالية عندما يصل إلى هامش الجدول السفلي. ومع ذلك، قد يكون لدينا حاجة لإدراج فاصل صفحات قسرًا عندما يتم إضافة عدد معين من الصفوف للجدول. يُظهر مقتطف الشفرة التالي الخطوات لإدراج فاصل صفحات عندما يتم إضافة 10 صفوف للجدول.

```java
    public static void InsertPageBreak() {
        // إنشاء مثيل للمستند
        Document doc = new Document();
        // إضافة صفحة إلى مجموعة الصفحات لملف PDF
        Page page = doc.getPages().add();
        // إنشاء مثيل للجدول
        Table tab = new Table();
        // تعيين نمط الحدود للجدول
        tab.setBorder (new BorderInfo(BorderSide.All, Color.getRed()));
        // تعيين نمط الحدود الافتراضي للجدول بلون الحدود كأحمر
        tab.setDefaultCellBorder (new BorderInfo(BorderSide.All, Color.getRed()));
        // تحديد عرض أعمدة الجدول
        tab.setColumnWidths ("100 100");
        // إنشاء حلقة لإضافة 200 صف للجدول
        for (int counter = 0; counter <= 200; counter++) {
            Row row = new Row();
            tab.getRows().add(row);
            Cell cell1 = new Cell();
            cell1.getParagraphs().add(new TextFragment("Cell " + counter + ", 0"));
            row.getCells().add(cell1);
            Cell cell2 = new Cell();
            cell2.getParagraphs().add(new TextFragment("Cell " + counter + ", 1"));
            row.getCells().add(cell2);
            // عند إضافة 10 صفوف، يتم عرض الصف الجديد في صفحة جديدة
            if (counter % 10 == 0 && counter != 0)
                row.setInNewPage(true);
        }
        // إضافة الجدول إلى مجموعة الفقرات لملف PDF
        page.getParagraphs().add(tab);

        // حفظ مستند PDF
        doc.save(_dataDir + "InsertPageBreak_out.pdf");
    }
```


## إخفاء حدود الخلايا الممتدة

أثناء إضافة الخلايا إلى جدول، قد تظهر حدود الخلية الممتدة عندما تنكسر إلى صف آخر. يمكن جعل هذه الحدود الممتدة مخفية كما هو موضح في نموذج الكود التالي.

```java
Document doc = new Document();
com.aspose.pdf.Page page = doc.getPages().add();

//Instantiate a table object that will be nested inside outerTable that will break
//inside the same page
com.aspose.pdf.Table mytable = new com.aspose.pdf.Table();
mytable.setBroken(TableBroken.Vertical);
mytable.setDefaultCellBorder(new BorderInfo(BorderSide.All));
mytable.setRepeatingColumnsCount(2);
page.getParagraphs().add(mytable);

//Add header Row
com.aspose.pdf.Row row = mytable.getRows().add();
Cell cell = row.getCells().add("header 1");
cell.setColSpan(2);
cell.setBackgroundColor(Color.getLightGray());
Cell header3 = row.getCells().add("header 3");
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
row.getCells().add("header 12");
row.getCells().add("header 13");
row.getCells().add("header 14");
row.getCells().add("header 15");
row.getCells().add("header 16");
row.getCells().add("header 17");

for (int rowCounter = 0; rowCounter < 1; rowCounter++)
{
  //Create rows in the table and then cells in the rows
  com.aspose.pdf.Row row1 = mytable.getRows().add();
  row1.getCells().add("col "+rowCounter+", 1");
  row1.getCells().add("col "+rowCounter+", 2");
  row1.getCells().add("col "+rowCounter+", 3");
  row1.getCells().add("col "+rowCounter+", 4");
  row1.getCells().add("col "+rowCounter+", 5");
  row1.getCells().add("col "+rowCounter+", 6");
  row1.getCells().add("col "+rowCounter+", 7");
  row1.getCells().add("col "+rowCounter+", 8");
  row1.getCells().add("col "+rowCounter+", 9");
  row1.getCells().add("col "+rowCounter+", 10");
  row1.getCells().add("col "+rowCounter+", 11");
  row1.getCells().add("col "+rowCounter+", 12");
  row1.getCells().add("col "+rowCounter+", 13");
  row1.getCells().add("col "+rowCounter+", 14");
  row1.getCells().add("col "+rowCounter+", 15");
  row1.getCells().add("col "+rowCounter+", 16");
  row1.getCells().add("col "+rowCounter+", 17");
}
doc.save(dataDir + "3_out.pdf");
```