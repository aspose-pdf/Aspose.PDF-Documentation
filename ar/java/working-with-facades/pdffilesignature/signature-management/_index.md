---
title: إدارة التوقيع
linktitle: إدارة التوقيع
type: docs
weight: 80
url: /ar/java/signature-management/
description: تعلم كيفية إزالة توقيع PDF موجود في Java باستخدام واجهة PdfFileSignature.
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إزالة توقيعات PDF في Java
Abstract: تعلم كيفية إزالة توقيع من ملف PDF موقع باستخدام Aspose.PDF for Java. تغطي مجموعة أمثلة Java الحالية إزالة توقيع موجود بالاسم وحفظ المستند المحدث. لا تتضمن عينة منفصلة لتنظيف حقل التوقيع المرتبط.
---
## إزالة توقيع

استخدم هذا Workflow عندما يجب إزالة توقيع رقمي موجود من المستند.

### خطوات

1. أنشئ `PdfFileSignature` إنشاء كائن وربط ملف PDF الموقع.
2. اقرأ مجموعة التوقيعات واختيار اسم توقيع.
3. استدعِ `removeSignature` بهذا الاسم.
4. احفظ الملف المحدث وأغلق كائن الواجهة.

### مثال Java

```java
public static void removeSignature(Path inputFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        pdfSignature.removeSignature(signatureName);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```

مجموعة عينات Java الحالية لا تتضمن طريقة منفصلة لإزالة حقل التوقيع المرتبط بعد حذف التوقيع.
