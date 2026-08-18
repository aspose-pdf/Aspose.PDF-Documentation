---
title: إلحاق الصفحات بملف PDF
linktitle: إلحاق الصفحات بملف PDF
type: docs
weight: 10
url: /java/append-pages-to-pdf/
description: قم بإلحاق صفحات من ملف PDF إلى آخر في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إلحاق نطاق صفحات من مستند PDF إلى آخر باستخدام Java
Abstract: تعرف على كيفية إلحاق الصفحات بملف PDF باستخدام Aspose.PDF لـ Java. يستخدم مثال Java PdfFileEditor لإلحاق نطاق صفحات محدد من مستند آخر إلى نهاية ملف PDF الحالي.
---
## إلحاق الصفحات بملف PDF

يقوم نموذج Java بإلحاق الصفحة 1 من ملف PDF الثاني بنهاية المستند الأول.

### خطوات

1. قم بإنشاء مثيل `PdfFileEditor`.
2. قم بربط ملف PDF المدخل الرئيسي عن طريق تمرير مساره إلى `append`.
3. قم بتوفير قائمة الملفات المصدر الثانوية ونطاق الصفحات المراد إلحاقه.
4. احفظ النتيجة المدمجة في ملف الإخراج.

### مثال جافا

```java
public static void appendPagesToPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.append(inputFile.toString(), new String[] {sampleFile.toString()}, 1, 1, outputFile.toString());
}
```
