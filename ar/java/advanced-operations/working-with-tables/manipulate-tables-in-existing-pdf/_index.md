---
title: معالجة الجداول في مستندات PDF الحالية
linktitle: معالجة الجداول
type: docs
weight: 40
url: /ar/java/manipulating-tables/
description: تعلم كيفية فحص وتعديل الجداول في مستندات PDF الحالية باستخدام Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: فحص وتعديل الجداول الموجودة في PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية معالجة الجداول الموجودة بالفعل في مستندات PDF باستخدام Aspose.PDF for Java. وتغطي تحديد الجداول باستخدام TableAbsorber، وتحديث النص داخل الخلية، واستبدال جدول مكتشف بكائن Table جديد.
---
استخدام `TableAbsorber` عندما تحتاج إلى تحديد مواقع الجداول الموجودة وتحديث محتواها.

## استبدال النص داخل خلية جدول

استخدم هذا المثال عندما يجب تحديث النص في خلية مكتشفة دون إعادة بناء الجدول بأكمله.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وزُر الصفحة التي تحتوي على [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. تحقق من أن جدول الهدف ومقاطع نص الخلية موجودة.
1. استبدل نص الخلية واحفظ المستند المحدث.

```java
public static void replaceCells(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        if (absorber.getTableList().isEmpty()) {
            throw new IllegalStateException("No tables were found on page 1.");
        }
        if (absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0).getTextFragments().size() == 0) {
            throw new IllegalStateException("The target cell has no text fragments.");
        }

        absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0)
                .getTextFragments().get_Item(1).setText("New Value");
        document.save(outputFile.toString());
    }
}
```

## استبدال جدول مكتشف بجدول جديد

استخدم هذا المثال عندما يجب استبدال الجدول الأصلي بالكامل بجدول تم إنشاؤه حديثًا.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) واكتشاف الجداول على الصفحة.
1. أنشئ جديد [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) بالهيكل المطلوب.
1. استبدل الجدول الممتص واحفظ ملف PDF الناتج.

```java
public static void replaceTable(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        if (absorber.getTableList().isEmpty()) {
            throw new IllegalStateException("No tables were found on page 1.");
        }

        AbsorbedTable oldTable = absorber.getTableList().get(0);
        Table newTable = new Table();
        newTable.setColumnWidths("100 100 100");
        newTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 1.0f));

        Row row = newTable.getRows().add();
        row.getCells().add("Col 1");
        row.getCells().add("Col 2");
        row.getCells().add("Col 3");
        row = newTable.getRows().add();
        row.getCells().add("Col 12");
        row.getCells().add("Col 22");
        row.getCells().add("Col 32");

        absorber.replace(document.getPages().get_Item(1), oldTable, newTable);
        document.save(outputFile.toString());
    }
}
```
