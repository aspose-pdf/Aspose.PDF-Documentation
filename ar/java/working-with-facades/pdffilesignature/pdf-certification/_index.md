---
title: تصديق PDF
linktitle: تصديق PDF
type: docs
weight: 30
url: /ar/java/pdf-certification/
description: تعرف على كيفية تصديق مستندات PDF في Java باستخدام PdfFileSignature و DocMDPSignature.
lastmod: "2026-10-01"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: صادق مستندات PDF باستخدام أذونات DocMDP في Java
Abstract: تعرف على كيفية تصديق مستندات PDF باستخدام Aspose.PDF for Java. يستخدم مثال Java‏‏ ‏PdfFileSignature مع DocMDPSignature و DocMDPAccessPermissions لتصديق مستند للملء عبر النماذج والتوقيع مع تقييد الأنواع الأخرى من التعديل.
---
## صادق مستندات PDF

استخدم التصديق عندما يجب أن يبقى المستند موثوقًا لكنه يسمح بفئة محددة من التغييرات بعد التوقيع.

### خطوات

1. إنشاء `PdfFileSignature` إنشاء نسخة وربط ملف PDF المصدر.
2. إنشاء `PKCS7` كائن التوقيع مع الشهادة وكلمة مرور الشهادة.
3. غلف تلك التوقيع بـ `DocMDPSignature` مع المطلوب `DocMDPAccessPermissions` القيمة.
4. اتصال `certify` مع صفحة الهدف، بيانات تعريف التوقيع، المستطيل الظاهر، وتوقيع MDP.
5. حفظ ملف PDF المصدق وإغلاق كائن الواجهة.

### مثال Java

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
