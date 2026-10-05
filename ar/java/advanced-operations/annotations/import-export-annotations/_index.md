---
title: استيراد وتصدير التعليقات التوضيحية باستخدام Java
linktitle: استيراد وتصدير التعليقات التوضيحية
type: docs
weight: 80
url: /ar/java/import-export-annotations/
description: تعلم كيفية نسخ التعليقات التوضيحية من مستند PDF إلى مستند PDF آخر باستخدام Aspose.PDF for Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: نقل تعليقات PDF التوضيحية بين المستندات في Java.
Abstract: تشرح هذه المقالة كيفية نسخ التعليقات التوضيحية من ملف PDF مصدر وتصديرها إلى مستند PDF جديد باستخدام Aspose.PDF for Java. يقوم سير العمل بتحميل الملف المصدر، إنشاء مستند الوجهة، إضافة صفحة، نسخ التعليقات التوضيحية من الصفحة المصدر الأولى، وحفظ النتيجة.
---
## نسخ التعليقات التوضيحية من PDF إلى آخر

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى الوجهة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف كل [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) إلى الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. اقرأ أو التكرار عبر [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) العناصر على الصفحة المستهدفة.
1. احفظ ملف PDF المحدّث [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. عدّ [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) العناصر في صفحة المصدر الأولى وأضف كل واحدة إلى صفحة الوجهة.

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
