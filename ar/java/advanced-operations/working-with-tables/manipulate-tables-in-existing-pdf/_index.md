---
title: Manipulate Tables in existing PDF
linktitle: Manipulate Tables
type: docs
weight: 30
url: /ar/java/manipulate-tables-in-existing-pdf/
description: التلاعب بالجداول في ملف PDF موجود واستبدال الجدول القديم بآخر جديد في مستند PDF باستخدام Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## التلاعب بالجداول في ملف PDF موجود

إحدى الميزات الأولى التي يدعمها Aspose.PDF for Java هي قدراته على العمل مع الجداول وتوفر دعمًا كبيرًا لإضافة الجداول في ملفات PDF التي يتم إنشاؤها من البداية أو أي ملفات PDF موجودة.
   لديك أيضًا القدرة على دمج الجدول مع قاعدة البيانات (DOM) لإنشاء جداول ديناميكية بناءً على محتويات قاعدة البيانات. في هذا الإصدار الجديد، قمنا بتنفيذ ميزة جديدة للبحث وتحليل الجداول البسيطة التي توجد بالفعل على صفحة من مستند PDF. توفر فئة جديدة باسم **Aspose.PDF.Text.TableAbsorber** هذه القدرات. استخدام TableAbsorber مشابه جدًا لفئة TextFragmentAbsorber الموجودة.

يوضح مقتطف الكود التالي الخطوات اللازمة لتحديث المحتويات في خلية جدول معينة.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleManipulate {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ManipulateTables() {

        // تحميل ملف PDF الموجود
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        // إنشاء كائن TableAbsorber للعثور على الجداول
        TableAbsorber absorber = new TableAbsorber();

        // زيارة الصفحة الأولى مع الامتصاص
        absorber.visit(pdfDocument.getPages().get_Item(1));

        // الوصول إلى الجدول الأول في الصفحة، الخلية الأولى وشظايا النص فيها
        TextFragment fragment = absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0)
                .getTextFragments().get_Item(1);

        // تغيير نص الشظية النصية الأولى في الخلية
        fragment.setText("hi world");

        pdfDocument.save(_dataDir + "ManipulateTable_out.pdf");
    }
```

## استبدال الجدول القديم بآخر جديد في مستند PDF

في حالة الحاجة إلى العثور على جدول معين واستبداله بالجدول المطلوب، يمكنك استخدام الطريقة Replace() من فئة [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) للقيام بذلك.

المثال التالي يوضح الوظيفة لاستبدال الجدول داخل مستند PDF:

```java
public static void ReplaceOldTableWithNew() {

        // تحميل مستند PDF الحالي
        Document pdfDocument = new Document(_dataDir + "Table_input2.pdf");

        // إنشاء كائن TableAbsorber للعثور على الجداول
        TableAbsorber absorber = new TableAbsorber();

        Page page = pdfDocument.getPages().get_Item(1);

        // زيارة الصفحة الأولى باستخدام الماص
        absorber.visit(page);

        // الحصول على الجدول الأول في الصفحة
        AbsorbedTable table = absorber.getTableList().get(0);

        // إنشاء جدول جديد
        Table newTable = new Table();
        newTable.setColumnWidths("100 100 100");
        newTable.setDefaultCellBorder (new BorderInfo(BorderSide.All, 1F));

        Row row = newTable.getRows().add();
        row.getCells().add("Col 1");
        row.getCells().add("Col 2");
        row.getCells().add("Col 3");

        // استبدال الجدول بالجدول الجديد
        absorber.replace(page, table, newTable);

        // حفظ المستند
        pdfDocument.save(_dataDir + "TableReplaced_out.pdf");
        
    }

}
```