---
title: معلومات التوقيع
linktitle: معلومات التوقيع
type: docs
weight: 60
url: /java/signature-information/
description: تعرف على كيفية قراءة أسماء التوقيع وتفاصيل المُوقع من ملفات PDF الموقعة في Java باستخدام PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قراءة تفاصيل التوقيع من مستندات PDF في Java
Abstract: تعرف على كيفية فحص البيانات التعريفية للتوقيع باستخدام Aspose.PDF لـ Java. يقرأ مثال Java اسم التوقيع الأول المتاح ثم يسترد الموقع والتاريخ والسبب والموقع من ملف PDF الموقع.
---
## الحصول على معلومات التوقيع

استخدم سير العمل هذا عندما تحتاج إلى فحص من قام بالتوقيع على ملف PDF وما هي بيانات تعريف التوقيع التي تم تخزينها.

### خطوات

1. قم بإنشاء مثيل `PdfFileSignature` واربط ملف PDF الموقع.
2. اقرأ مجموعة التوقيع وحدد اسم التوقيع.
3. اتصل بأدوات الوصول إلى معلومات التوقيع للحصول على اسم المُوقع والتاريخ والسبب والموقع.
4. أغلق كائن الواجهة عند الانتهاء.

### مثال جافا

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
