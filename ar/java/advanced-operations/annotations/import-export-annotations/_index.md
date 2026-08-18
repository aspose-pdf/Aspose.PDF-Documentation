---
title: استيراد وتصدير التعليقات التوضيحية باستخدام جافا
linktitle: استيراد وتصدير التعليقات التوضيحية
type: docs
weight: 80
url: /java/import-export-annotations/
description: تعرف على كيفية نسخ التعليقات التوضيحية من مستند PDF إلى مستند PDF آخر باستخدام Aspose.PDF لـ Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: نقل التعليقات التوضيحية بتنسيق PDF بين المستندات في Java.
Abstract: تشرح هذه المقالة كيفية نسخ التعليقات التوضيحية من ملف PDF مصدر وتصديرها إلى مستند PDF جديد باستخدام Aspose.PDF لـ Java. يقوم سير العمل بتحميل الملف المصدر، وإنشاء المستند الوجهة، وإضافة صفحة، ونسخ التعليقات التوضيحية من الصفحة المصدر الأولى، وحفظ النتيجة.
---
## انسخ التعليقات التوضيحية من ملف PDF إلى آخر

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى الوجهة [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف كل [تعليق توضيحي](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) إلى [الصفحة] المستهدفة(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. اقرأ أو كرر عناصر [التعليق التوضيحي](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) الموجودة في الصفحة المستهدفة.
1. احفظ ملف PDF المحدث [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بتعداد عناصر [التعليق التوضيحي](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) في الصفحة المصدر الأولى وأضف كل منها إلى الصفحة الوجهة.

```java
public static void importExport(Path inputFile, Path outputFile) {
    try (Document sourceDocument = new Document(inputFile.toString());
         Document destinationDocument = new Document()) {
        Page page = destinationDocument.getPages().add();

        for (Annotation annotation : sourceDocument.getPages().get_Item(1).getAnnotations()) {
            page.getAnnotations().add(annotation, true);
        }

        destinationDocument.save(outputFile.toString());
    }
}
```
