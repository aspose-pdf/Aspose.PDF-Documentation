---
title: حذف صفحات PDF في جافا
linktitle: حذف صفحات PDF
type: docs
weight: 80
url: /java/delete-pages/
description: تعرف على كيفية حذف الصفحات من ملفات PDF في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: احذف صفحة PDF واحدة أو أكثر في Java
Abstract: تشرح هذه المقالة كيفية إزالة الصفحات من ملفات PDF باستخدام Aspose.PDF لـ Java. ويغطي حذف صفحة واحدة وحذف صفحات متعددة مرة واحدة من خلال واجهة برمجة تطبيقات مجموعة الصفحات.
---
استخدم مجموعة صفحات المستند عندما تحتاج إلى إزالة صفحة واحدة أو أكثر من ملف PDF.

## حذف صفحة واحدة

استخدم هذا المثال عندما تحتاج إلى إزالة صفحة واحدة من خلال فهرسها.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. حذف الصفحة المستهدفة من مجموعة الصفحات.
1. احفظ المستند المحدث.

```java
public static void deletePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(2);
        document.save(outputFile.toString());
    }
}
```

## حذف صفحات متعددة

استخدم هذا المثال عندما يجب إزالة عدة صفحات في عملية واحدة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بتمرير فهارس الصفحات لحذفها من مجموعة الصفحات.
1. احفظ ملف PDF المعدل.

```java
public static void deleteBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(new Integer[]{2, 3, 4});
        document.save(outputFile.toString());
    }
}
```
