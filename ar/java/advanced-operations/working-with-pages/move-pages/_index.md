---
title: نقل صفحات PDF في جافا
linktitle: نقل صفحات PDF
type: docs
weight: 100
url: /java/move-pages/
description: تعرف على كيفية نقل صفحات PDF داخل مستند أو بين المستندات في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: نقل صفحات PDF بين المستندات في Java
Abstract: تشرح هذه المقالة كيفية نقل الصفحات في ملفات PDF باستخدام Aspose.PDF لـ Java. ويغطي نقل صفحة واحدة أو عدة صفحات إلى مستند آخر، وإعادة تحديد موضع الصفحة داخل نفس ملف PDF.
---
يتيح لك Aspose.PDF for Java نقل الصفحات بين المستندات أو تغيير موضع الصفحات داخل ملف PDF نفسه.

## نقل صفحة إلى مستند آخر

استخدم هذا المثال عندما يجب إزالة صفحة واحدة من ملف PDF المصدر وحفظها في مستند منفصل.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وقم بإنشاء مستند وجهة.
1. إضافة الصفحة المستهدفة إلى الوجهة وحذفها من المصدر.
1. احفظ كلا الوثيقتين.

```java
public static void movePageFromOneDocumentToAnother(Path inputFile, Path sourceOutputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString());
         Document anotherDocument = new Document()) {
        anotherDocument.getPages().add(document.getPages().get_Item(2));
        document.getPages().delete(2);
        document.save(sourceOutputFile.toString());
        anotherDocument.save(outputFile.toString());
    }
}
```

## نقل صفحات متعددة إلى مستند آخر

استخدم هذا المثال عندما يجب نقل عدة صفحات من ملف PDF المصدر إلى مستند جديد.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وقم بإنشاء المستند الوجهة.
1. انسخ الصفحات المحددة إلى المستند الوجهة.
1. احذف الصفحات المنقولة من المصدر واحفظ كلا الملفين.

```java
public static void moveBunchPagesFromOneDocumentToAnother(Path inputFile, Path sourceOutputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        Integer[] pages = {1, 2};
        for (Integer pageIndex : pages) {
            dstDocument.getPages().add(srcDocument.getPages().get_Item(pageIndex));
        }
        dstDocument.save(outputFile.toString());
        srcDocument.getPages().delete(pages);
        srcDocument.save(sourceOutputFile.toString());
    }
}
```

## نقل صفحة داخل نفس المستند

استخدم هذا المثال عندما يجب تغيير موضع الصفحة إلى موقع جديد في نفس ملف PDF.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بتكرار الصفحة المستهدفة في الموضع الجديد وقم بإزالة إدخال الصفحة الأصلية.
1. احفظ المستند المعاد ترتيبه.

```java
public static void movePageInNewLocationInSameDocument(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString())) {
        srcDocument.getPages().add(srcDocument.getPages().get_Item(2));
        srcDocument.getPages().delete(2);
        srcDocument.save(outputFile.toString());
    }
}
```
