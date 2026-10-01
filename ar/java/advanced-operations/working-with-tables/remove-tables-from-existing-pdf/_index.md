---
title: إزالة الجداول من مستندات PDF الحالية
linktitle: إزالة الجداول
description: تعلم كيفية إزالة جدول واحد أو أكثر من مستندات PDF الحالية باستخدام Java.
lastmod: "2026-10-01"
type: docs
weight: 50
url: /ar/java/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: حذف جدول واحد أو عدة جداول من ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إزالة الجداول من مستندات PDF الحالية باستخدام Aspose.PDF for Java. تُعرّف بـ TableAbsorber لتحديد مواقع الجداول وتُظهر كيفية حذف جدول واحد أو إزالة جميع الجداول المكتشفة من صفحة.
---
استخدم `TableAbsorber` عندما تحتاج إلى حذف جدول واحد أو أكثر تم اكتشافه من ملف PDF موجود.

## إزالة جدول مكتشف واحد

استخدم هذا المثال عندما يجب حذف الجدول المتطابق الأول فقط في الصفحة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بزيارة الصفحة الهدف باستخدام [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. إزالة الجدول الأول المكتشف وحفظ المستند.

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

## إزالة جميع الجداول المكتشفة من صفحة

استخدم هذا المثال عندما يجب إزالة كل جدول متطابق على الصفحة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بزيارة الصفحة الهدف باستخدام [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) ونسخ الجداول المكتشفة إلى قائمة.
1. إزالة كل جدول مكتشف وحفظ ملف PDF المحدث.

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
