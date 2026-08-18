---
title: إدارة التوقيع
linktitle: إدارة التوقيع
type: docs
weight: 80
url: /java/signature-management/
description: تعرف على كيفية إزالة توقيع PDF موجود في Java باستخدام واجهة PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إزالة توقيعات PDF في Java
Abstract: تعرف على كيفية إزالة التوقيع من ملف PDF موقع باستخدام Aspose.PDF لـ Java. تغطي مجموعة أمثلة Java الحالية إزالة التوقيع الموجود بالاسم وحفظ المستند المحدث. ولا يتضمن نموذجًا منفصلاً لتنظيف حقل التوقيع المرتبط.
---
## إزالة التوقيع

استخدم سير العمل هذا عندما يجب إزالة التوقيع الرقمي الموجود من المستند.

### خطوات

1. قم بإنشاء مثيل `PdfFileSignature` واربط ملف PDF الموقع.
2. اقرأ مجموعة التوقيع وحدد اسم التوقيع.
3. اتصل `removeSignature` بهذا الاسم.
4. احفظ الملف المحدث وأغلق كائن الواجهة.

### مثال جافا

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

لا تتضمن مجموعة نماذج Java الحالية طريقة منفصلة لإزالة حقل التوقيع المرتبط بعد حذف التوقيع.
