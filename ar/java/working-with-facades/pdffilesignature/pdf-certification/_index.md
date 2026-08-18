---
title: شهادة قوات الدفاع الشعبي
linktitle: شهادة قوات الدفاع الشعبي
type: docs
weight: 30
url: /java/pdf-certification/
description: تعرف على كيفية التصديق على مستندات PDF في Java باستخدام PdfFileSignature وDocMDPSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: اعتماد مستندات PDF بأذونات DocMDP في Java
Abstract: تعرف على كيفية التصديق على مستندات PDF باستخدام Aspose.PDF لـ Java. يستخدم مثال Java PdfFileSignature مع DocMDPSignature وDocMDPAccessPermissions لاعتماد مستند لملء النموذج وتوقيعه مع تقييد أنواع التعديل الأخرى.
---
## التصديق على وثائق PDF

استخدم الشهادة عندما يجب أن تظل الوثيقة موثوقة ولكن مع السماح بفئة محددة من التغييرات بعد التوقيع.

### خطوات

1. قم بإنشاء مثيل `PdfFileSignature` واربط ملف PDF المصدر.
2. أنشئ كائن توقيع `PKCS7` باستخدام الشهادة وكلمة مرور الشهادة.
3. قم بلف هذا التوقيع في `DocMDPSignature` بالقيمة `DocMDPAccessPermissions` المطلوبة.
4. اتصل `certify` بالصفحة المستهدفة وبيانات تعريف التوقيع والمستطيل المرئي وتوقيع MDP.
5. احفظ ملف PDF المعتمد وأغلق كائن الواجهة.

### مثال جافا

```java
public static void certifyPdfWithMdpSignature(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        DocMDPSignature signature = new DocMDPSignature(
                createPkcs7(certificateFile, "Certified for form filling and signing"),
                DocMDPAccessPermissions.FillingInForms);
        pdfSignature.certify(1, "Certified for form filling and signing", "security@example.com", "New York, USA", true, signatureRectangle(), signature);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
