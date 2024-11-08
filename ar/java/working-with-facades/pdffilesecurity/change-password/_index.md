---
title: تغيير كلمة مرور ملف PDF
type: docs
weight: 40
url: /ar/java/change-password/
description: يوضح هذا الموضوع كيفية تغيير كلمة المرور على ملف PDF باستخدام PdfFileSecurity Class.
lastmod: "2021-06-05"
draft: false
---

## تغيير كلمة مرور ملف PDF

لتغيير كلمة مرور ملف PDF، تحتاج إلى إنشاء كائن [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) ثم استدعاء طريقة [ChangePassword](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#changePassword-java.lang.String-java.lang.String-java.lang.String-). تحتاج إلى تمرير كلمة مرور المالك الحالية وكلمات المرور الجديدة للمستخدم والمالك لطريقة [ChangePassword](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#changePassword-java.lang.String-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-).

يظهر مقطع الشيفرة التالي كيفية تغيير كلمات مرور ملف PDF.

```java
    public static void ChangePassword() {
        PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
        // إنشاء كائن PdfFileSecurity
        if (pdfFileInfo.isEncrypted()) {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.changePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", DocumentPrivilege.getPrint(),
                    KeySize.x256);
            fileSecurity.save(_dataDir + "sample_encrtypted1.pdf");
        }
    }
```