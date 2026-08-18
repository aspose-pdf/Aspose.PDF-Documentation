---
title: التوقيع على وثائق PDF
linktitle: التوقيع على وثائق PDF
type: docs
weight: 10
url: /java/pdf-signing/
description: تعرف على كيفية توقيع مستندات PDF في Java باستخدام واجهة PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتوقيع مستندات PDF بالتوقيعات الرقمية في Java
Abstract: تعرف على كيفية توقيع مستندات PDF باستخدام Aspose.PDF لـ Java. تغطي مجموعة أمثلة Java التوقيع باستخدام مسار شهادة وكلمة مرور تم تكوينهما، والتوقيع باستخدام كائن توقيع PKCS7 صريح يتضمن بيانات تعريف التوقيع مثل السبب ومعلومات الاتصال والموقع والسلطة.
---
## التوقيع على وثائق PDF

استخدم `PdfFileSignature` عندما تحتاج إلى تطبيق توقيع رقمي مرئي على ملف PDF.

### خطوات

1. قم بإنشاء مثيل `PdfFileSignature` واربط ملف PDF المصدر.
2. قم بتحميل الشهادة إما من خلال `setCertificate` أو عن طريق إنشاء كائن `PKCS7`.
3. اتصل `sign` بالصفحة المستهدفة وإعدادات الرؤية ومستطيل التوقيع وبيانات التوقيع.
4. احفظ ملف PDF الموقع وأغلق كائن الواجهة.

### أمثلة جافا

```java
public static void signPdfWithCertificateObject(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        pdfSignature.sign(1, false, signatureRectangle(), createPkcs7(certificateFile, "Document approval"));
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}

public static void signPdfWithBasicParameters(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        pdfSignature.setCertificate(certificateFile.toString(), CERTIFICATE_PASSWORD);
        pdfSignature.sign(1, "Document approval", "qa@example.com", "New York, USA", false, signatureRectangle());
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
