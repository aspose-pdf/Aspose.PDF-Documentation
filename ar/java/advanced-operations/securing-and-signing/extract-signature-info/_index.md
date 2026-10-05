---
title: استخراج معلومات التوقيع من PDF باستخدام Java
linktitle: استخراج تفاصيل من التوقيع
type: docs
weight: 20
url: /ar/java/extract-image-and-signature-information/
description: تعلم كيفية استخراج تفاصيل الشهادة والتوقيع الرقمي من ملفات PDF باستخدام Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج تفاصيل التوقيع وبيانات الشهادة من ملفات PDF الموقعة باستخدام Java
Abstract: تشرح هذه المقالة كيفية فحص التواقيع الرقمية في مستندات PDF باستخدام Aspose.PDF for Java. تعرف على كيفية قراءة تفاصيل المُوقّع، والتحقق من التوقيع، والتحقق مما إذا كان التوقيع يغطي المستند بأكمله، واستخراج شهادة التوقيع المضمنة، وإزالة توقيع موجود.
---
استخدام `PdfFileSignature` لفحص وإدارة التوقيعات الموجودة بالفعل في مستند PDF.

## قراءة معلومات التوقيع

1. أنشئ واجهة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) وربط مستند PDF المصدر.
1. انتقل إلى اسم توقيع المستند واضبط تدفق فحص التوقيع المطلوب وفقًا للمثال.
1. اقرأ والتحقق من معلومات التوقيع من واجهة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. اقرأ القيم المرجعة أو واصل إلى خطوة المعالجة التالية.

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

## تحقق من التوقيع

1. أنشئ واجهة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) وربط مستند PDF المصدر.
1. انتقل إلى اسم توقيع المستند واضبط تدفق التحقق المطلوب من قبل المثال.
1. اقرأ والتحقق من معلومات التوقيع من واجهة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).

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

1. أنشئ واجهة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) وربط مستند PDF المصدر.
1. انتقل إلى اسم توقيع المستند المطلوب لاستخراج الشهادة.
1. اكتب المخرجات المستخرجة أو افحص القيم المرجعة من واجهة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).

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
