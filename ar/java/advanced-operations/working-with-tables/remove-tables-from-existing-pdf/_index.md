---
title: إزالة الجداول من مستندات PDF الموجودة
linktitle: إزالة الجداول
description: تعرف على كيفية إزالة جدول واحد أو أكثر من مستندات PDF الموجودة في Java.
lastmod: "2026-06-09"
type: docs
weight: 50
url: /java/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: احذف جدولًا واحدًا أو عدة جدول من ملفات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية إزالة الجداول من مستندات PDF الموجودة باستخدام Aspose.PDF لـ Java. يقدم TableAbsorter لتحديد موقع الجداول ويوضح كيفية حذف جدول واحد أو إزالة جميع الجداول المكتشفة من الصفحة.
---
استخدم `TableAbsorber` عندما تحتاج إلى حذف واحد أو أكثر من الجداول المكتشفة من ملف PDF موجود.

## قم بإزالة جدول واحد تم اكتشافه

استخدم هذا المثال عندما يجب حذف الجدول المطابق الأول في الصفحة فقط.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بزيارة الصفحة المستهدفة باستخدام [TableAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. قم بإزالة أول جدول تم اكتشافه واحفظ المستند.

```java
public static void removeOneTable(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        absorber.remove(absorber.getTableList().get(0));
        document.save(outputFile.toString());
    }
}
```

## إزالة كافة الجداول المكتشفة من الصفحة

استخدم هذا المثال عندما يجب إزالة كل جدول مطابق في الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بزيارة الصفحة المستهدفة باستخدام [TableAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) وانسخ الجداول المكتشفة إلى القائمة.
1. قم بإزالة كل جدول تم اكتشافه واحفظ ملف PDF المحدث.

```java
public static void removeAllTables(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        List<AbsorbedTable> tables = new ArrayList<>(absorber.getTableList());
        for (AbsorbedTable table : tables) {
            absorber.remove(table);
        }
        document.save(outputFile.toString());
    }
}
```
