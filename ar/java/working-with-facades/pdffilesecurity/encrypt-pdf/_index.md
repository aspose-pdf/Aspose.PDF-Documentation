---
title: تشفير ملف PDF
type: docs
weight: 10
url: ar/java/encrypt-pdf-file/
description: يشرح هذا الموضوع كيفية تشفير ملف PDF باستخدام فئة PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## تشفير ملف PDF باستخدام أنواع وخوارزميات تشفير مختلفة

من أجل تشفير ملف PDF، تحتاج إلى إنشاء كائن [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) ثم استدعاء طريقة [EncryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#encryptFile-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-). يمكنك تمرير كلمة مرور المستخدم، وكلمة مرور المالك والامتيازات إلى طريقة [EncryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#encryptFile-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-). تحتاج أيضًا إلى تمرير قيم KeySize وAlgorithm لهذه الطريقة.

يوضح لك مقتطف الشيفرة التالي كيفية تشفير ملف PDF.

```java
    public static void EncryptPDFFile() {
        // إنشاء كائن PdfFileSecurity
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        // تشفير الملف باستخدام تشفير 256 بت
        fileSecurity.encryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", DocumentPrivilege.getPrint(), KeySize.x256,
                Algorithm.AES);
        fileSecurity.save(_dataDir + "sample_encrypted.pdf");
    }
```