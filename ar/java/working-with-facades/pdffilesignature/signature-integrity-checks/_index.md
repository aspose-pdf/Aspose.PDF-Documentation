---
title: فحوصات سلامة التوقيع
linktitle: فحوصات سلامة التوقيع
type: docs
weight: 70
url: /ar/java/signature-integrity-checks/
description: تعلم كيفية التحقق من تغطية التوقيع وسلامته في Java باستخدام واجهة PdfFileSignature.
lastmod: "2026-10-01"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحقق من تغطية توقيع PDF وسلامته في Java
Abstract: تعلم كيفية فحص سلامة التوقيع باستخدام Aspose.PDF for Java. مجموعة الأمثلة الحالية في Java تستخدم `verifySignature` للتحقق من التوقيع المحدد و `coversWholeDocument` لتحديد ما إذا كان التوقيع يحمي المستند PDF بالكامل.
---
## تحقق من سلامة التوقيع

هذه المقالة ترتبط بنفس سير التحقق المعروض من قبل `PdfFileSignatureExamples.java`.

### خطوات

1. اربط ملف PDF الموقع بـ `PdfFileSignature`.
2. حدد اسم التوقيع من المستند.
3. مكالمة `verifySignature` للتحقق من محتويات التوقيع.
4. مكالمة `coversWholeDocument` لتأكيد التغطية على مستوى المستند.
5. إغلاق كائن الواجهة.

### مثال Java

```java
public static void verifyPdfSignature(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature '" + signatureName + "' is valid: " + pdfSignature.verifySignature(signatureName));
        System.out.println("Signature covers whole document: " + pdfSignature.coversWholeDocument(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```
