---
title: معلومات التوقيع
linktitle: معلومات التوقيع
type: docs
weight: 60
url: /ar/java/signature-information/
description: تعرف على كيفية قراءة أسماء التوقيعات وتفاصيل الموقع من ملفات PDF الموقعة في Java باستخدام PdfFileSignature.
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قراءة تفاصيل التوقيع من مستندات PDF في Java
Abstract: تعرف على كيفية فحص البيانات الوصفية للتوقيع باستخدام Aspose.PDF for Java. يقرأ مثال Java اسم التوقيع الأول المتاح ثم يستخرج الموقّع، التاريخ، السبب، والموقع من ملف PDF الموقّع.
---
## الحصول على معلومات التوقيع

استخدم هذا سير العمل عندما تحتاج إلى فحص من وقع ملف PDF وما هي البيانات الوصفية للتوقيع المخزنة.

### خطوات

1. أنشئ مثيلًا `PdfFileSignature` وربط ملف PDF الموقّع.
2. اقرأ مجموعة التوقيعات واختيار اسم توقيع.
3. استدعِ وصول معلومات التوقيع للحصول على اسم الموقع، التاريخ، السبب، والموقع.
4. أغلق كائن الواجهة عند الانتهاء.

### مثال Java

```java
public static void getSignatureInformation(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature Names: " + pdfSignature.getSignNames());
        System.out.println("Signer: " + pdfSignature.getSignerName(signatureName));
        System.out.println("Date: " + pdfSignature.getDateTime(signatureName));
        System.out.println("Reason: " + pdfSignature.getReason(signatureName));
        System.out.println("Location: " + pdfSignature.getLocation(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```
