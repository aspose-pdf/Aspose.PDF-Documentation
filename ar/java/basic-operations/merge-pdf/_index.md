---
title: دمج ملفات PDF في Java
linktitle: دمج ملفات PDF
type: docs
weight: 50
url: /ar/java/merge-pdf/
description: تعرف على كيفية دمج ملفات PDF متعددة في مستند واحد في Java باستخدام Aspose.PDF.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: دمج صفحات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية دمج مستندين PDF في Java باستخدام Aspose.PDF. يفتح المثال مستندين مصدرين، يضيف صفحات المستند الثاني إلى الأول، ويحفظ النتيجة المدمجة كملف PDF جديد.
---
يكون دمج ملفات PDF مفيدًا عندما تحتاج إلى جمع المستندات ذات الصلة في ملف واحد للتوزيع أو الأرشفة أو المعالجة.

## مثال حي

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) هو تطبيق مجاني عبر الإنترنت لاختبار دمج ملفات PDF في المتصفح.

يوضح هذا الموضوع كيفية دمج ملفات PDF متعددة في مستند واحد باستخدام Java:

1. افتح كلا المستندين المصدرين باستخدام [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) المنشئ.
1. إلحاق الـ [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) المجموعة من الثانية [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) إلى الأول مع `document1.getPages().add(document2.getPages())`.
1. حفظ المدمج [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) إلى مسار الإخراج.

## دمج مستندين PDF

المثال التالي بلغة Java مبني على `MergeDocumentExamples.java`.

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```
