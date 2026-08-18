---
title: استيراد وتصدير التعليقات التوضيحية باستخدام جافا
linktitle: استيراد وتصدير التعليقات التوضيحية
type: docs
weight: 80
url: /java/pdfannotationeditor-class/import-export-annotations/
description: تعرف على كيفية نسخ التعليقات التوضيحية من مستند PDF إلى مستند PDF آخر باستخدام Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: نقل التعليقات التوضيحية بتنسيق PDF بين المستندات في Java
Abstract: تشرح هذه المقالة كيفية نسخ التعليقات التوضيحية من ملف PDF مصدر وتصديرها إلى مستند PDF جديد باستخدام Java. يقوم سير العمل بتحميل الملف المصدر، وإنشاء المستند الوجهة، وإضافة صفحة، ونسخ التعليقات التوضيحية من الصفحة المصدر الأولى، وحفظ النتيجة.
---
## انسخ التعليقات التوضيحية من ملف PDF إلى آخر

1. افتح ملف PDF المصدر وقم بإنشاء مستند وجهة جديد بصفحة مستهدفة.
2. قم بتعداد التعليقات التوضيحية في الصفحة المصدر الأولى وأضف كل واحدة منها إلى الصفحة الوجهة.
3. احفظ المستند الوجهة للاحتفاظ بالتعليقات التوضيحية المنسوخة.

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
