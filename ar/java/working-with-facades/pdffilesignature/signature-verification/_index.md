---
title: التحقق من التوقيع
linktitle: التحقق من التوقيع
type: docs
weight: 90
url: /java/signature-verification/
description: تعرف على كيفية التحقق من توقيعات PDF في Java باستخدام واجهة PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: التحقق من توقيعات PDF في Java
Abstract: تعرف على كيفية التحقق من توقيع PDF باستخدام Aspose.PDF لـ Java. يحدد مثال Java أول توقيع متاح، ويتحقق من صحة التوقيع، ويتحقق مما إذا كان يغطي المستند بأكمله.
---
## التحقق من توقيع PDF

استخدم سير العمل هذا عندما تحتاج إلى تمرير سريع للتحقق من صحة ملف PDF الموقع الموجود.

### خطوات

1. قم بإنشاء مثيل `PdfFileSignature` واربط ملف PDF الموقع.
2. حدد اسم التوقيع الذي تريد فحصه.
3. اتصل بـ `verifySignature` للتحقق من صحة التوقيع.
4. اتصل بـ `coversWholeDocument` للتحقق من التغطية.
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
