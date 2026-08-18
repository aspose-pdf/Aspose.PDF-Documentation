---
title: استخراج معلومات التوقيع من PDF في جافا
linktitle: استخراج التفاصيل من التوقيع
type: docs
weight: 20
url: /java/extract-image-and-signature-information/
description: تعرف على كيفية استخراج تفاصيل الشهادة والتوقيع الرقمي من ملفات PDF في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج تفاصيل التوقيع وبيانات الشهادة من ملفات PDF الموقعة في Java
Abstract: تشرح هذه المقالة كيفية فحص التوقيعات الرقمية في مستندات PDF باستخدام Aspose.PDF لـ Java. تعرف على كيفية قراءة تفاصيل الموقّع، والتحقق من التوقيع، والتحقق مما إذا كان التوقيع يغطي المستند بأكمله، واستخراج شهادة التوقيع المضمنة، وإزالة التوقيع الحالي.
---
استخدم `PdfFileSignature` لفحص وإدارة التوقيعات الموجودة بالفعل في مستند PDF.

## قراءة معلومات التوقيع

1. قم بإنشاء واجهة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) وربط مستند PDF المصدر.
1. قم بالوصول إلى اسم توقيع المستند وقم بتكوين تدفق فحص التوقيع الذي يتطلبه المثال.
1. اقرأ معلومات التوقيع من الواجهة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) وتحقق منها.
1. اقرأ القيم التي تم إرجاعها أو تابع خطوة المعالجة التالية.

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

## التحقق من التوقيع

1. قم بإنشاء واجهة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) وربط مستند PDF المصدر.
1. قم بالوصول إلى اسم توقيع المستند وقم بتكوين تدفق التحقق الذي يتطلبه المثال.
1. اقرأ معلومات التوقيع من الواجهة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) وتحقق منها.

```java
public static void verifyPdfSignature(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature '" + signatureName + "' is valid: "
                + pdfSignature.verifySignature(signatureName));
        System.out.println("Signature covers whole document: "
                + pdfSignature.coversWholeDocument(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```

## استخراج شهادة التوقيع

1. قم بإنشاء واجهة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) وربط مستند PDF المصدر.
1. الوصول إلى اسم توقيع المستند المطلوب لاستخراج الشهادة.
1. اكتب المخرجات المستخرجة أو افحص القيم التي تم إرجاعها من الواجهة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).

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
