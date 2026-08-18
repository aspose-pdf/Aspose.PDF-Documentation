---
title: التحقق من سلامة التوقيع
linktitle: التحقق من سلامة التوقيع
type: docs
weight: 70
url: /java/signature-integrity-checks/
description: تعرف على كيفية التحقق من صحة تغطية التوقيع وتكامله في Java باستخدام واجهة PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: التحقق من صحة تغطية توقيع PDF وتكامله في Java
Abstract: تعرف على كيفية فحص سلامة التوقيع باستخدام Aspose.PDF لـ Java. تستخدم مجموعة أمثلة Java الحالية `verifySignature` للتحقق من صحة التوقيع المحدد و`coversWholeDocument` لتحديد ما إذا كان التوقيع يحمي ملف PDF بأكمله.
---
## التحقق من سلامة التوقيع

تعين هذه المقالة نفس سير عمل التحقق الذي تم الكشف عنه بواسطة `PdfFileSignatureExamples.java`.

### خطوات

1. قم بربط ملف PDF الموقع بـ `PdfFileSignature`.
2. حدد اسم التوقيع من المستند.
3. اتصل بـ `verifySignature` للتحقق من صحة محتويات التوقيع.
4. اتصل بـ `coversWholeDocument` لتأكيد التغطية على مستوى المستند.
5. أغلق كائن الواجهة.

### مثال جافا

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
