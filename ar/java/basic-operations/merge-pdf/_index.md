---
title: دمج ملفات PDF في جافا
linktitle: دمج ملفات PDF
type: docs
weight: 50
url: /java/merge-pdf/
description: تعرف على كيفية دمج ملفات PDF متعددة في مستند واحد في Java باستخدام Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: دمج صفحات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية دمج مستندي PDF في Java باستخدام Aspose.PDF. يفتح المثال مستندين مصدرين، ويلحق صفحات المستند الثاني بالوثيقة الأولى، ويحفظ النتيجة المدمجة كملف PDF جديد.
---
يعد دمج ملفات PDF مفيدًا عندما تحتاج إلى دمج المستندات ذات الصلة في ملف واحد للتوزيع أو الأرشفة أو المعالجة.

## مثال حي

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) هو تطبيق مجاني عبر الإنترنت لاختبار دمج ملفات PDF في المتصفح.

يوضح هذا الموضوع كيفية دمج ملفات PDF متعددة في مستند واحد في Java:

1. افتح كلا المستندين المصدرين باستخدام مُنشئ [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإلحاق مجموعة [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) من [المستند] الثاني(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) بالمجموعة الأولى باستخدام `document1.getPages().add(document2.getPages())`.
1. احفظ [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) المدمج في مسار الإخراج.

## دمج وثيقتين PDF

يستند مثال Java التالي إلى `MergeDocumentExamples.java`.

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```
