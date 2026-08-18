---
title: إضافة وحذف إشارات PDF المرجعية في Java
linktitle: إضافة وحذف إشارة مرجعية
type: docs
weight: 10
url: /java/add-and-delete-bookmark/
description: تعرف على كيفية إضافة الإشارات المرجعية وحذفها في مستندات PDF باستخدام Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإضافة أو إزالة الإشارات المرجعية في مستندات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إنشاء الإشارات المرجعية وحذفها باستخدام Aspose.PDF لـ Java. توضح الأمثلة إضافة إشارة مرجعية ذات مستوى أعلى، وإنشاء تسلسل هرمي للإشارات المرجعية الفرعية، وحذف كافة الإشارات المرجعية، وإزالة إشارة مرجعية محددة حسب العنوان.
---
استخدم مجموعة المخطط التفصيلي للمستندات لإدارة الإشارات المرجعية برمجيًا.

## أضف إشارة مرجعية ذات مستوى أعلى

استخدم هذا المثال عندما يجب أن يتضمن المستند إدخال مخطط تفصيلي واحد عالي المستوى.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) وقم بتكوين عنوانه ونمطه وإجراءاته.
1. أضف الإشارة المرجعية إلى الخطوط العريضة للمستند واحفظ الملف.

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

## أضف إشارة مرجعية فرعية

يقوم هذا المثال بإنشاء إشارة مرجعية أصلية ويدمج إشارة مرجعية فرعية تحتها.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء كائنات [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) الأصلية والفرعية.
1. أضف الطفل إلى الأصل، وأضف الأصل إلى مجموعة المخطط التفصيلي، ثم احفظ المستند.

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

## حذف كافة الإشارات المرجعية

استخدم هذا الأسلوب عندما يجب إزالة مجموعة المخطط التفصيلي بالكامل من المستند.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. حذف مجموعة الخطوط العريضة الكاملة.
1. احفظ ملف الإخراج الذي تم تنظيفه.

```java
public static void deleteBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete();
        document.save(outputFile.toString());
    }
}
```

## حذف إشارة مرجعية محددة

استخدم هذا المثال عندما يجب إزالة إشارة مرجعية مسماة دون مسح شجرة المخطط التفصيلي بالكامل.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بحذف الإشارة المرجعية حسب العنوان من مجموعة الخطوط العريضة.
1. احفظ المستند المحدث.

```java
public static void deleteBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete("Child Outline");
        document.save(outputFile.toString());
    }
}
```
