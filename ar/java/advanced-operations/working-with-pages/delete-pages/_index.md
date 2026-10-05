---
title: حذف صفحات PDF في Java
linktitle: حذف صفحات PDF
type: docs
weight: 80
url: /ar/java/delete-pages/
description: تعلم كيفية حذف الصفحات من ملفات PDF في Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: حذف صفحة واحدة أو أكثر من صفحات PDF في Java
Abstract: تشرح هذه المقالة كيفية إزالة الصفحات من ملفات PDF باستخدام Aspose.PDF for Java. تغطي حذف صفحة واحدة وحذف عدة صفحات في آنٍ واحد عبر واجهة برمجة تطبيقات مجموعة الصفحات.
---
استخدم مجموعة صفحات المستند عندما تحتاج إلى إزالة صفحة واحدة أو أكثر من PDF.

## حذف صفحة واحدة

استخدم هذا المثال عندما تحتاج إلى إزالة صفحة واحدة بحسب فهرستها.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احذف الصفحة المستهدفة من مجموعة الصفحات.
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

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. مرّر مؤشرات الصفحات لحذفها من مجموعة الصفحات.
1. احفظ ملف PDF المعدل.

```java
public static void deleteBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(new Integer[]{2, 3, 4});
        document.save(outputFile.toString());
    }
}
```
