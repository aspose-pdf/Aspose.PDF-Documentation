---
title: التحقق من التوقيع في ملف PDF
type: docs
weight: 30
url: ar/java/verify-signature-in-pdf/
description: يشرح هذا القسم كيفية العمل مع التوقيع في ملف PDF باستخدام فئة PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## التحقق مما إذا كان ملف PDF موقعًا باستخدام توقيع

للتحقق مما إذا كان ملف PDF موقعًا باستخدام طريقة VerifySigned من فئة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature). تتطلب هذه الطريقة اسم التوقيع وتعيد true إذا كان ملف PDF موقعًا باستخدام ذلك الاسم. من الممكن أيضًا التحقق من أن [ملف PDF موقع](/pdf/java/working-with-signature-in-a-pdf-file/)، دون التحقق من التوقيع الذي تم التوقيع به.

### التحقق من أن ملف PDF موقع بتوقيع معين

يوضح مقتطف الشيفرة التالي كيفية التحقق مما إذا كان ملف PDF موقعًا باستخدام توقيع معين.

```java
    public static void IsPdfSigned() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.containsSignature())
            System.out.println("Document Signed");

        pdfSign.close();
    }
```


### التحقق من أن ملف PDF موقّع

لتحديد ما إذا كان الملف موقّعًا، دون توفير اسم التوقيع، استخدم الكود التالي.

```java
    public static void IsPdfSignedWithGivenSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.verifySigned("Signature1")) {
            System.out.println("PDF Signed");
        }
    }
```

## التحقق مما إذا كان التوقيع صالحًا

طريقة [VerifySignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#verifySignature-java.lang.String-) من فئة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) تسمح لك بالتحقق من صحة توقيع معين. تتطلب هذه الطريقة اسم التوقيع كمدخل وتعيد true إذا كان التوقيع صالحًا. يوضح لك جزء الكود التالي كيفية التحقق من صحة توقيع.

```java
    public static void IsPdfSignatureValid() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.verifySignature("Signature1")) {
            System.out.println("Signature Verified");
        }
    }
```