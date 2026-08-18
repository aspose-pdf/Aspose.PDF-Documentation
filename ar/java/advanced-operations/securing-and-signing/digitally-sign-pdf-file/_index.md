---
title: أضف توقيعًا رقميًا أو قم بتوقيع PDF رقميًا في Java
linktitle: التوقيع رقميا على PDF
type: docs
weight: 10
url: /java/digitally-sign-pdf-file/
description: تعرف على كيفية التوقيع والتصديق على مستندات PDF رقميًا في Java باستخدام Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتوقيع ملفات PDF رقميًا باستخدام Java
Abstract: يشرح هذا الدليل كيفية التوقيع رقميًا على مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي التوقيع باستخدام كائن شهادة، والتوقيع باستخدام معلمات الشهادة الأساسية، والتصديق على مستند بتوقيع DocMDP للتحكم في التغييرات المسموح بها بعد التوقيع.
---
يدعم Aspose.PDF for Java تدفقات التوقيع المتعددة من خلال `PdfFileSignature`.

## قم بتوقيع ملف PDF باستخدام كائن الشهادة

1. قم بإنشاء واجهة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) وربط مستند PDF المصدر.
1. قم بإنشاء كائن التوقيع [PKCS7](https://reference.aspose.com/pdf/java/com.aspose.pdf/pkcs7/) وقم بتكوين خيارات التوقيع.
1. قم بتطبيق التوقيع على مستند PDF من خلال [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
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

ينشئ هذا الأسلوب كائن التوقيع `PKCS7` أولاً ثم يطبقه على الصفحة 1.

## قم بتوقيع ملف PDF بمعلمات الشهادة الأساسية

1. قم بإنشاء واجهة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) وربط مستند PDF المصدر.
1. قم بتكوين معلمات الشهادة المطلوبة بواسطة مثال التوقيع.
1. قم بتطبيق التوقيع على مستند PDF من خلال [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
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

## التصديق على ملف PDF مع DocMDP

استخدم كشف تعديل المستند وتوقيع المنع عندما تحتاج إلى قيود على مستوى الشهادة:

1. قم بإنشاء واجهة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) وربط مستند PDF المصدر.
1. قم بإنشاء كائن [DocMDPSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpsignature/) وقم بتكوين خيارات التوقيع [DocMDPAccessPermissions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpaccesspermissions/).
1. قم بتطبيق توقيع الشهادة واحفظ مستند PDF المحدث.

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
