---
title: إضافة توقيع رقمي أو توقيع PDF رقمياً في Java
linktitle: توقيع PDF رقمياً
type: docs
weight: 10
url: /ar/java/digitally-sign-pdf-file/
description: تعرف على كيفية توقيع وثائق PDF رقمياً وتصديقها في Java باستخدام Aspose.PDF.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: توقيع ملفات PDF رقمياً باستخدام Java
Abstract: يوضح هذا الدليل كيفية توقيع مستندات PDF رقمياً باستخدام Aspose.PDF for Java. يغطي التوقيع باستخدام كائن شهادة، والتوقيع باستخدام معلمات الشهادة الأساسية، وتوثيق المستند بتوقيع DocMDP للتحكم في التغييرات المسموح بها بعد التوقيع.
---
يدعم Aspose.PDF for Java تدفقات توقيع متعددة عبر `PdfFileSignature`.

## توقيع PDF باستخدام كائن شهادة

1. أنشئ كائنًا من الفئة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) الواجهة وربط مستند PDF المصدر.
1. أنشئ كائنًا من الفئة [PKCS7](https://reference.aspose.com/pdf/java/com.aspose.pdf/pkcs7/) التوقيع واضبط خيارات التوقيع.
1. طبّق التوقيع على مستند PDF من خلال [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. احفظ مستند PDF المحدث.

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
```

هذا النهج يبني كائن `PKCS7` التوقيع أولاً ثم يطبقه على الصفحة 1.

## توقيع ملف PDF باستخدام معلمات الشهادة الأساسية

1. أنشئ كائنًا من الفئة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) الواجهة وربط مستند PDF المصدر.
1. هيّئ معلمات الشهادة المطلوبة بواسطة مثال التوقيع.
1. طبّق التوقيع على مستند PDF من خلال [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. احفظ مستند PDF المحدث.

```java
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

## تصديق ملف PDF باستخدام DocMDP

استخدم توقيع اكتشاف وتمنع تعديل المستند عندما تحتاج إلى قيود على مستوى الشهادة:

1. أنشئ كائنًا من الفئة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) الواجهة وربط مستند PDF المصدر.
1. أنشئ الكائن [DocMDPSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpsignature/) واضبط [DocMDPAccessPermissions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpaccesspermissions/) خيارات التوقيع.
1. طبّق توقيع الشهادة واحفظ مستند PDF المحدث.

```java
public static void certifyPdfWithMdpSignature(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        DocMDPSignature signature = new DocMDPSignature(
                createPkcs7(certificateFile, "Certified for form filling and signing"),
                DocMDPAccessPermissions.FillingInForms);
        pdfSignature.certify(1, "Certified for form filling and signing", "security@example.com",
                "New York, USA", true, signatureRectangle(), signature);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
