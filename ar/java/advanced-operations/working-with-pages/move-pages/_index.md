---
title: نقل صفحات PDF في Java
linktitle: نقل صفحات PDF
type: docs
weight: 100
url: /ar/java/move-pages/
description: تعلم كيفية نقل صفحات PDF داخل مستند أو بين المستندات في Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: نقل صفحات PDF بين المستندات في Java
Abstract: تشرح هذه المقالة كيفية نقل الصفحات في ملفات PDF باستخدام Aspose.PDF for Java. تغطي نقل صفحة واحدة أو عدة صفحات إلى مستند آخر، وإعادة تموضع صفحة داخل نفس ملف PDF.
---
يتيح لك Aspose.PDF for Java نقل الصفحات بين المستندات أو إعادة تموضع الصفحات داخل نفس ملف PDF.

## نقل صفحة إلى مستند آخر

استخدم هذا المثال عندما يجب إزالة صفحة واحدة من ملف PDF المصدر وحفظها في مستند منفصل.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) واخلق مستندًا هدفًا.
1. أضف الصفحة المستهدفة إلى المستند الوجهة واحذفها من المصدر.
1. احفظ كلا المستندين.

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

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأنشئ المستند الوجهة.
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

استخدم هذا المثال عندما يجب إعادة تموضع صفحة إلى موقع جديد في نفس ملف PDF.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. انسخ الصفحة المستهدفة إلى الموضع الجديد وأزل إدخال الصفحة الأصلي.
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
