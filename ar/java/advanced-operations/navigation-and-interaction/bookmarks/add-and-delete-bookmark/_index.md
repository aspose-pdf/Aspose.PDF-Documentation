---
title: إضافة وحذف إشارات PDF في Java
linktitle: إضافة وحذف إشارة مرجعية
type: docs
weight: 10
url: /ar/java/add-and-delete-bookmark/
description: تعلم كيفية إضافة وحذف الإشارات المرجعية في مستندات PDF باستخدام Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة أو إزالة الإشارات المرجعية في مستندات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إنشاء وحذف العلامات المرجعية باستخدام Aspose.PDF for Java. تُظهر الأمثلة إضافة علامة مرجعية على المستوى الأعلى، وإنشاء تسلسل هرمي للعلامات الفرعية، وحذف جميع العلامات المرجعية، وإزالة علامة مرجعية محددة وفقًا للعنوان.
---
استخدم مجموعة مخطط المستند لإدارة العلامات المرجعية برمجيًا.

## إضافة علامة مرجعية على المستوى الأعلى

استخدم هذا المثال عندما يجب أن يحتوي المستند على إدخال مخطط واحد على المستوى الأعلى.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) وَاضبط عنوانه، نمطه، وإجراءه.
1. أضف العلامة المرجعية إلى مخططات المستند واحفظ الملف.

```java
public static void addBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection pdfOutline = new OutlineItemCollection(document.getOutlines());
        pdfOutline.setTitle("Test Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);
        pdfOutline.setAction(new GoToAction(document.getPages().get_Item(1)));

        document.getOutlines().add(pdfOutline);
        document.save(outputFile.toString());
    }
}
```

## إضافة علامة مرجعية فرعية

هذا المثال ينشئ علامة مرجعية أصلية ويضع علامة مرجعية فرعية تحتها.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ أصل وفرعي كائنات [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/).
1. أضف العنصر الفرعي إلى العنصر الأب، أضف العنصر الأب إلى مجموعة المخطط، واحفظ المستند.

```java
public static void addChildBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection pdfOutline = new OutlineItemCollection(document.getOutlines());
        pdfOutline.setTitle("Parent Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        OutlineItemCollection pdfChildOutline = new OutlineItemCollection(document.getOutlines());
        pdfChildOutline.setTitle("Child Outline");
        pdfChildOutline.setItalic(true);
        pdfChildOutline.setBold(true);

        pdfOutline.add(pdfChildOutline);
        document.getOutlines().add(pdfOutline);
        document.save(outputFile.toString());
    }
}
```

## حذف جميع الإشارات المرجعية

استخدم هذا النهج عندما ينبغي إزالة مجموعة المخطط بالكامل من المستند.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احذف مجموعة المخططات الكاملة.
1. احفظ ملف الإخراج المنقّح.

```java
public static void deleteBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete();
        document.save(outputFile.toString());
    }
}
```

## حذف إشارة مرجعية محددة

استخدم هذا المثال عندما يجب إزالة إشارة مرجعية مسماة دون مسح شجرة الفهرس بأكملها.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احذف الإشارة المرجعية حسب العنوان من مجموعة المخططات.
1. احفظ المستند المحدث.

```java
public static void deleteBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete("Child Outline");
        document.save(outputFile.toString());
    }
}
```
