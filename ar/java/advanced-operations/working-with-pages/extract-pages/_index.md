---
title: استخراج صفحات PDF في Java
linktitle: استخراج صفحات PDF
type: docs
weight: 80
url: /ar/java/extract-pages/
description: تعلم كيفية استخراج صفحة PDF واحدة أو عدة صفحات إلى ملفات جديدة في Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج صفحات PDF إلى مستندات جديدة باستخدام Java
Abstract: تشرح هذه المقالة كيفية استخراج الصفحات من ملفات PDF باستخدام Aspose.PDF for Java. وتغطي نسخ صفحة واحدة واستخراج عدة صفحات إلى مستند وجهة منفصل باستخدام ترقيم الصفحات بدءًا من 1.
---
يتيح لك Aspose.PDF for Java نسخ الصفحات المحددة إلى مستند وجهة جديد.

## استخراج صفحة واحدة

استخدم هذا المثال عندما تحتاج إلى حفظ صفحة واحدة من ملف PDF المصدر في مستند منفصل.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأنشئ مستند وجهة.
1. انسخ الصفحة المستهدفة إلى مجموعة صفحات الوجهة.
1. احفظ ملف PDF الجديد.

```java
public static void extractPage(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        dstDocument.getPages().add(srcDocument.getPages().get_Item(2));
        dstDocument.save(outputFile.toString());
    }
}
```

## استخراج صفحات متعددة

استخدم هذا المثال عندما تحتاج إلى نسخ عدة صفحات إلى ملف PDF منفصل.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأنشئ مستند وجهة.
1. مرّ على فهارس الصفحات المحددة وأضفها إلى الوجهة.
1. احفظ مستند الصفحات المستخرجة.

```java
public static void extractBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString());
         Document anotherDocument = new Document()) {
        Integer[] pages = {2, 3};
        for (Integer pageIndex : pages) {
            anotherDocument.getPages().add(document.getPages().get_Item(pageIndex));
        }
        anotherDocument.save(outputFile.toString());
    }
}
```
