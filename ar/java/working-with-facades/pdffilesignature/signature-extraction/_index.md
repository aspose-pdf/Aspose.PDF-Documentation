---
title: استخراج التوقيع
linktitle: استخراج التوقيع
type: docs
weight: 50
url: /ar/java/signature-extraction/
description: تعرّف على كيفية استخراج شهادة التوقيع من ملف PDF موقع باستخدام Java و PdfFileSignature.
lastmod: "2026-10-01"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج شهادة التوقيع من PDF باستخدام Java
Abstract: تعرّف على كيفية استخراج الشهادة المرتبطة بتوقيع PDF باستخدام Aspose.PDF for Java. تتضمن مجموعة أمثلة Java الحالية استخراج الشهادة إلى تدفق إخراج، لكنها لا تتضمن عينة لاستخراج صورة التوقيع بشكل منفصل.
---
## استخراج شهادة التوقيع

استخدم هذا Workflow عندما تحتاج إلى حفظ الشهادة المرتبطة بتوقيع موجود.

### الخطوات

1. إنشاء `PdfFileSignature` إنشاء نسخة وربط ملف PDF الموقع.
2. حدد اسم التوقيع للفحص.
3. اتصال `extractCertificate` لفتح تدفق الشهادة.
4. انسخ بايتات الشهادة إلى ملف إخراج.
5. أغلق موارد التدفق وكائن الواجهة.

### مثال Java

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

الحالي `PdfFileSignatureExamples.java` الفئة لا تتضمن عينة Java مخصصة لاستخراج صورة التوقيع المرسومة.
