---
title: تقسيم ملف PDF إلى صفحات مفردة
linktitle: تقسيم ملف PDF إلى صفحات مفردة
type: docs
weight: 30
url: /java/split-pdf-into-single-pages/
description: قم بتقسيم ملف PDF إلى ملفات إخراج ذات صفحة واحدة في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتصدير كل صفحة من ملف PDF إلى ملف خاص بها باستخدام Java
Abstract: تعرف على كيفية تقسيم ملف PDF إلى ملفات ذات صفحة واحدة باستخدام Aspose.PDF لـ Java. يستخدم مثال Java PdfFileEditor لكتابة كل صفحة إلى ملف PDF فردي بناءً على نمط اسم الملف.
---
## تقسيم ملف PDF إلى صفحات واحدة

استخدم سير العمل هذا عندما يجب أن تصبح كل صفحة مصدر ملف PDF خاصًا بها.

### خطوات

1. قم بإنشاء مثيل `PdfFileEditor`.
2. قم بإعداد نمط ملف الإخراج الذي يتضمن عنصرًا نائبًا للصفحة مثل `%NUM%`.
3. اتصل `splitToPages` بالملف المصدر ونمط الإخراج.
4. احفظ الملفات ذات الصفحة الواحدة التي تم إنشاؤها.

```java
public static void splitPdfIntoSinglePages(Path inputFile, Path outputFilePattern) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToPages(inputFile.toString(), outputFilePattern.toString());
}
```
