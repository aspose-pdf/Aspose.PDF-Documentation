---
title: استيراد وتصدير التعليقات التوضيحية باستخدام Java
linktitle: استيراد وتصدير التعليقات التوضيحية
type: docs
weight: 80
url: /ar/java/pdfannotationeditor-class/import-export-annotations/
description: تعرف على كيفية نسخ التعليقات التوضيحية من مستند PDF واحد إلى مستند PDF آخر باستخدام Java.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: نقل تعليقات PDF التوضيحية بين المستندات في Java
Abstract: تشرح هذه المقالة كيفية نسخ التعليقات التوضيحية من ملف PDF المصدر وتصديرها إلى مستند PDF جديد باستخدام Java. يقوم سير العمل بتحميل الملف المصدر، وإنشاء مستند الوجهة، وإضافة صفحة، ونسخ التعليقات التوضيحية من الصفحة المصدر الأولى، ثم حفظ النتيجة.
---
## نسخ التعليقات التوضيحية من PDF إلى آخر

1. افتح ملف PDF المصدر وأنشئ مستند وجهة جديدًا بصفحة هدف.
2. عدّد التعليقات التوضيحية في الصفحة الأولى من المصدر وأضف كل واحدة إلى صفحة الوجهة.
3. احفظ مستند الوجهة لتثبيت التعليقات التوضيحية المنقولة.

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
