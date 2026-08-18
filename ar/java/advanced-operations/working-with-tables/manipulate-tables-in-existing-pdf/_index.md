---
title: التعامل مع الجداول في وثائق PDF الموجودة
linktitle: التعامل مع الجداول
type: docs
weight: 40
url: /java/manipulating-tables/
description: تعرف على كيفية فحص الجداول وتعديلها في مستندات PDF الموجودة باستخدام Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: فحص وتعديل جداول PDF الموجودة باستخدام Java
Abstract: تشرح هذه المقالة كيفية التعامل مع الجداول الموجودة بالفعل في مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي تحديد موقع الجداول باستخدام TableAbsorter، وتحديث النص داخل الخلية، واستبدال الجدول المكتشف بكائن جدول جديد.
---
استخدم `TableAbsorber` عندما تحتاج إلى تحديد موقع الجداول الموجودة وتحديث محتواها.

## استبدال النص داخل خلية الجدول

استخدم هذا المثال عندما يجب تحديث النص الموجود في الخلية المكتشفة دون إعادة بناء الجدول بأكمله.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وقم بزيارة الصفحة باستخدام [TableAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. التحقق من وجود الجدول الهدف وأجزاء نص الخلية.
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

## استبدال الجدول الذي تم اكتشافه بجدول جديد

استخدم هذا المثال عندما يجب استبدال الجدول الأصلي بالكامل بجدول تم إنشاؤه حديثًا.

1. افتح ملف PDF [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) المصدر واكتشف الجداول الموجودة في الصفحة.
1. قم بإنشاء [جدول](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) جديد بالبنية المطلوبة.
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
