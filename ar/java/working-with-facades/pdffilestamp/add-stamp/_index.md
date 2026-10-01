---
title: إضافة ختم إلى PDF
linktitle: إضافة ختم إلى PDF
type: docs
weight: 40
url: /ar/java/add-stamp/
description: تعلم كيفية إضافة ختم صورة إلى صفحات PDF في Java باستخدام واجهة PdfFileStamp.
lastmod: "2026-10-01"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة ختماً صورياً إلى PDF في Java
Abstract: تعلم كيفية إضافة محتوى الختم إلى مستندات PDF باستخدام Aspose.PDF for Java عبر واجهة PdfFileStamp. تُظهر مجموعة الأمثلة الحالية للغة Java كيفية إنشاء `Stamp`، ربطه بملف صورة، إضافته إلى المستند، وحفظ PDF الذي تم ختمه.
---
## إضافة ختم إلى PDF

استخدم سير العمل هذا عندما يجب تطبيق ختم قائم على صورة إلى PDF.

### خطوات

1. إنشاء `PdfFileStamp` إنشاء كائن وربط ملف PDF المصدر.
2. إنشاء `Stamp` كائن.
3. ربط الطابع بملف صورة باستخدام `bindImage`.
4. أضف الطابع إلى المستند باستخدام `addStamp`.
5. احفظ الناتج وأغلق كائن الواجهة.

### مثال Java

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

الحالي `PdfFileStampExamples.java` الفئة لا تتضمن عينة Java منفصلة لطوابع النص فقط أو التدوير أو تكوين الشفافية.
