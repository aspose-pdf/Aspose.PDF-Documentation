---
title: إضافة ختم إلى PDF
linktitle: إضافة ختم إلى PDF
type: docs
weight: 40
url: /java/add-stamp/
description: تعرف على كيفية إضافة ختم صورة إلى صفحات PDF في Java باستخدام واجهة PdfFileStamp.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة طوابع الصور إلى PDF في Java
Abstract: تعرف على كيفية إضافة محتوى الطوابع إلى مستندات PDF باستخدام Aspose.PDF لـ Java باستخدام واجهة PdfFileStamp. توضح مجموعة أمثلة Java الحالية كيفية إنشاء `Stamp` وربطه بملف صورة وإضافته إلى المستند وحفظ ملف PDF المختوم.
---
## إضافة ختم إلى PDF

استخدم سير العمل هذا عندما يجب تطبيق ختم قائم على الصورة على ملف PDF.

### خطوات

1. قم بإنشاء مثيل `PdfFileStamp` واربط ملف PDF المصدر.
2. قم بإنشاء كائن `Stamp`.
3. قم بربط الختم بملف صورة باستخدام `bindImage`.
4. أضف الختم إلى المستند باستخدام `addStamp`.
5. احفظ الإخراج وأغلق كائن الواجهة.

### مثال جافا

```java
public static void addStampToPdf(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

لا تتضمن فئة `PdfFileStampExamples.java` الحالية نموذج Java منفصلاً لطوابع النص فقط أو التدوير أو تكوين العتامة.
