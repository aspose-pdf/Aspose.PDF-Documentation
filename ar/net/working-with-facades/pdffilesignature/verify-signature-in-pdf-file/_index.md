---
title: التحقق من التوقيع في ملف PDF
type: docs
weight: 30
url: /ar/net/verify-signature-in-pdf/
description: يوضح هذا القسم كيفية التحقق من التوقيع في ملف PDF باستخدام فئة PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## التحقق مما إذا كان ملف PDF موقعًا باستخدام توقيع

للتحقق مما إذا كان ملف PDF موقعًا باستخدام [توقيع معين](/pdf/ar/net/working-with-signature-in-a-pdf-file/)، استخدم طريقة VerifySigned من فئة [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). تتطلب هذه الطريقة اسم التوقيع وتعيد true إذا كان ملف PDF موقعًا باستخدام اسم التوقيع هذا. من الممكن أيضًا التحقق مما إذا كان [ملف PDF موقعًا](/pdf/ar/net/working-with-signature-in-a-pdf-file/)، دون التحقق من التوقيع الذي تم التوقيع به.

### التحقق من توقيع ملف PDF بتوقيع معين

يوضح لك مقتطف الشفرة التالي كيفية التحقق مما إذا كان ملف PDF موقعًا باستخدام توقيع معين.

```csharp
public static void IsPdfSigned()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.ContainsSignature())
                Console.WriteLine("Document Signed");
            pdfSign.Close();
        }
```


### التحقق من أن ملف PDF موقع

لتحديد ما إذا كان الملف موقعًا، دون توفير اسم التوقيع، استخدم الكود التالي.

```csharp
 public static void IsPdfSignedWithGivenSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.VerifySigned("Signature1"))
            {
                Console.WriteLine("PDF Signed");
            }
            //if (pdfSign.VerifySigned("Signature2"))
            //{
            //    Console.WriteLine("PDF Signed");
            //}
        }
```

## التحقق مما إذا كان التوقيع صالحًا

طريقة [VerifySignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/verifysignature) الخاصة بفئة [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) تتيح لك التحقق من صحة توقيع معين. هذه الطريقة تتطلب اسم التوقيع كمدخل وتعيد true إذا كان التوقيع صالحًا. يوضح لك مقطع الشفرة التالي كيفية التحقق من صحة التوقيع.

```csharp
public static void IsPdfSignatureValid()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.VerifySignature("Signature1"))
            {
                Console.WriteLine("Signature Verified");
            }
        }
```