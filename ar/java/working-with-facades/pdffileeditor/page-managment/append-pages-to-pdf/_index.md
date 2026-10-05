---
title: إضافة صفحات إلى PDF
linktitle: إضافة صفحات إلى PDF
type: docs
weight: 10
url: /ar/java/append-pages-to-pdf/
description: إضافة صفحات من ملف PDF واحد إلى آخر في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة نطاق صفحات من مستند PDF إلى آخر باستخدام Java
Abstract: تعرف على كيفية إضافة صفحات إلى PDF باستخدام Aspose.PDF for Java. يستخدم مثال Java فئة PdfFileEditor لإضافة نطاق صفحات محدد من مستند آخر إلى نهاية ملف PDF الحالي.
---
## إضافة صفحات إلى PDF

يعتمد مثال Java على إضافة الصفحة 1 من ملف PDF ثانٍ إلى نهاية المستند الأول.

### خطوات

1. أنشئ مثيلًا `PdfFileEditor`.
2. اربط ملف PDF الرئيسي عن طريق تمرير مساره إلى `append`.
3. وفّر قائمة ملفات المصدر الثانوية ونطاق الصفحات للإضافة.
4. احفظ النتيجة المدمجة إلى ملف الإخراج.

### مثال Java

```java
public static void appendPagesToPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.append(inputFile.toString(), new String[] {sampleFile.toString()}, 1, 1, outputFile.toString());
}
```
