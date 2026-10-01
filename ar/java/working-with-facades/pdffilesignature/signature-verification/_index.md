---
title: التحقق من التوقيع
linktitle: التحقق من التوقيع
type: docs
weight: 90
url: /ar/java/signature-verification/
description: تعرف على كيفية التحقق من توقيعات PDF في Java باستخدام واجهة PdfFileSignature.
lastmod: "2026-10-01"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحقق من توقيعات PDF في Java
Abstract: تعرف على كيفية التحقق من توقيع PDF باستخدام Aspose.PDF for Java. يختار مثال Java التوقيع الأول المتاح، يتحقق من صحة التوقيع، ويتأكد مما إذا كان يغطي المستند بالكامل.
---
## تحقق من توقيع PDF

استخدم هذه العملية عندما تحتاج إلى تمرير تحقق سريع على PDF موقّع موجود.

### الخطوات

1. إنشاء `PdfFileSignature` مثيل وربط ملف PDF الموقّع.
2. اختر اسم التوقيع الذي تريد فحصه.
3. اتصال `verifySignature` للتحقق من صحة التوقيع.
4. اتصال `coversWholeDocument` للتحقق من التغطية.
5. اغلق كائن الواجهة.

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
