---
title: تقسيم PDF إلى صفحات منفردة
linktitle: تقسيم PDF إلى صفحات منفردة
type: docs
weight: 30
url: /ar/java/split-pdf-into-single-pages/
description: قسّم ملف PDF إلى ملفات إخراج من صفحة واحدة في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-10-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تصدير كل صفحة من PDF إلى ملفها الخاص باستخدام Java
Abstract: تعرّف على كيفية تقسيم PDF إلى ملفات صفحة واحدة باستخدام Aspose.PDF for Java. يستخدم المثال في Java فئة PdfFileEditor لكتابة كل صفحة إلى PDF إخراج منفرد بناءً على نمط اسم الملف.
---
## قسّم PDF إلى صفحات منفردة

استخدم هذا سير العمل عندما يجب أن تصبح كل صفحة مصدر ملف PDF خاص بها.

### خطوات

1. إنشاء `PdfFileEditor` مثيل.
2. قم بإعداد نمط ملف الإخراج الذي يتضمن عنصر نائب للصفحة مثل `%NUM%`.
3. اتصال `splitToPages` مع ملف المصدر ونمط الإخراج.
4. حفظ ملفات الصفحات المفردة المُنشأة.

```java
public static void splitPdfIntoSinglePages(Path inputFile, Path outputFilePattern) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToPages(inputFile.toString(), outputFilePattern.toString());
}
```
