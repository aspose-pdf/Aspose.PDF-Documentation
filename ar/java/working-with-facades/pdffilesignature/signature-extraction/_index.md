---
title: استخراج التوقيع
linktitle: استخراج التوقيع
type: docs
weight: 50
url: /java/signature-extraction/
description: تعرف على كيفية استخراج شهادة التوقيع من ملف PDF موقع في Java باستخدام PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج شهادة التوقيع من PDF في جافا
Abstract: تعرف على كيفية استخراج الشهادة المرتبطة بتوقيع PDF باستخدام Aspose.PDF لـ Java. تتضمن مجموعة أمثلة Java الحالية استخراج الشهادات إلى دفق الإخراج، ولكنها لا تتضمن عينة منفصلة لاستخراج صورة التوقيع.
---
## استخراج شهادة التوقيع

استخدم سير العمل هذا عندما تحتاج إلى حفظ الشهادة المرتبطة بتوقيع موجود.

### خطوات

1. قم بإنشاء مثيل `PdfFileSignature` واربط ملف PDF الموقع.
2. حدد اسم التوقيع للفحص.
3. اتصل بـ `extractCertificate` لفتح دفق الشهادات.
4. انسخ بايت الشهادة إلى ملف الإخراج.
5. أغلق موارد الدفق وكائن الواجهة.

### مثال جافا

```java
public static void extractSignatureCertificate(Path inputFile, Path outputFile) throws Exception {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        try (InputStream inputStream = pdfSignature.extractCertificate(signatureName);
             OutputStream outputStream = Files.newOutputStream(outputFile)) {
            inputStream.transferTo(outputStream);
        }
    } finally {
        pdfSignature.close();
    }
}
```

لا تتضمن فئة `PdfFileSignatureExamples.java` الحالية نموذج Java مخصصًا لاستخراج صورة التوقيع المقدمة.
