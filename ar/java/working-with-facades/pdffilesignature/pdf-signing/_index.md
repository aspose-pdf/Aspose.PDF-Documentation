---
title: توقيع مستندات PDF
linktitle: توقيع مستندات PDF
type: docs
weight: 10
url: /ar/java/pdf-signing/
description: تعرف على كيفية توقيع مستندات PDF في Java باستخدام واجهة PdfFileSignature.
lastmod: "2026-10-01"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: توقيع مستندات PDF باستخدام التوقيعات الرقمية في Java
Abstract: تعرف على كيفية توقيع مستندات PDF باستخدام Aspose.PDF for Java. تغطي مجموعة الأمثلة في Java التوقيع باستخدام مسار شهادة وكلمة مرور مُكوَّنة، والتوقيع باستخدام كائن توقيع PKCS7 صريح يتضمن بيانات تعريف التوقيع مثل السبب ومعلومات الاتصال والموقع والسلطة.
---
## توقيع مستندات PDF

استخدام `PdfFileSignature` عندما تحتاج إلى تطبيق توقيع رقمي مرئي على ملف PDF.

### خطوات

1. إنشاء `PdfFileSignature` مثيل وربط ملف PDF المصدر.
2. تحميل الشهادة إما عبر `setCertificate` أو عن طريق إنشاء `PKCS7` كائن.
3. اتصال `sign` مع صفحة الهدف، وإعدادات الرؤية، ومستطيل التوقيع، وبيانات التوقيع.
4. حفظ ملف PDF الموقع وإغلاق كائن الواجهة.

### أمثلة Java

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
