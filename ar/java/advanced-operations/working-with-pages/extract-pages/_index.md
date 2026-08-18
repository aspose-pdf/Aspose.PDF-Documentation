---
title: استخراج صفحات PDF في جافا
linktitle: استخراج صفحات PDF
type: docs
weight: 80
url: /java/extract-pages/
description: تعرف على كيفية استخراج صفحات PDF فردية أو متعددة إلى ملفات جديدة في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم باستخراج صفحات PDF إلى مستندات جديدة باستخدام Java
Abstract: تشرح هذه المقالة كيفية استخراج الصفحات من ملفات PDF باستخدام Aspose.PDF لـ Java. ويغطي نسخ صفحة واحدة واستخراج صفحات متعددة في مستند وجهة منفصل باستخدام فهرسة الصفحة الواحدة.
---
يتيح لك Aspose.PDF for Java نسخ الصفحات المحددة إلى مستند وجهة جديد.

## استخراج صفحة واحدة

استخدم هذا المثال عندما تحتاج إلى حفظ صفحة واحدة من ملف PDF المصدر في مستند منفصل.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وقم بإنشاء مستند وجهة.
1. انسخ الصفحة المستهدفة إلى مجموعة الصفحات الوجهة.
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

استخدم هذا المثال عندما تحتاج إلى نسخ عدة صفحات في ملف PDF منفصل.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وقم بإنشاء مستند وجهة.
1. قم بالتكرار خلال فهارس الصفحات المحددة وأضفها إلى الوجهة.
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
