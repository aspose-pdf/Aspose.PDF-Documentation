---
title: فك تشفير ملف PDF
type: docs
weight: 20
url: ar/java/decrypt-pdf-file/
description: يشرح هذا الموضوع كيفية فك تشفير ملف PDF باستخدام فئة PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## فك تشفير ملف PDF باستخدام كلمة مرور المالك

{{% alert color="primary" %}}
جرب عبر الإنترنت <br>
يمكنك محاولة فتح الوثيقة باستخدام Aspose.PDF والحصول على النتائج عبر الإنترنت من خلال هذا الرابط:
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

لفك تشفير ملف PDF، تحتاج إلى إنشاء كائن [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) ثم استدعاء طريقة [DecryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-). تحتاج أيضًا إلى تمرير كلمة مرور المالك إلى طريقة [DecryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-). يوضح لك مقطع الشيفرة التالي كيفية فك تشفير ملف PDF.

```java
    public static void DecryptPDFFile() {
        PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
        // إنشاء كائن PdfFileSecurity
        if (pdfFileInfo.isEncrypted()) {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
            // فك تشفير مستند PDF
            fileSecurity.decryptFile("User_P@ssw0rd");
            fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
        }
    }
```