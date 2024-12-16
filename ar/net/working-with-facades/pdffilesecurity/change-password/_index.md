---
title: تغيير كلمة مرور ملف PDF
type: docs
weight: 40
url: /ar/net/change-password/
description: يوضح هذا الموضوع كيفية تغيير كلمة المرور على ملف PDF باستخدام فئة PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## تغيير كلمة مرور ملف PDF

لتغيير كلمة مرور ملف PDF، تحتاج إلى إنشاء كائن [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) ثم استدعاء طريقة [ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2). يجب عليك تمرير كلمة مرور المالك الحالية وكلمات مرور المستخدم والمالك الجديدة إلى طريقة [ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2).

{{% alert color="primary" %}}

- **كلمة مرور المستخدم**، إذا تم تعيينها، هي ما تحتاج إلى تقديمه لفتح PDF. سيقوم Acrobat/Reader بطلب من المستخدم إدخال كلمة المرور. إذا لم تكن صحيحة، لن يفتح المستند.
- **كلمة مرور المالك**، إذا تم تعيينها، تتحكم في الأذونات، مثل الطباعة، التحرير، الاستخراج، التعليق، إلخ. Acrobat/Reader سيمنع هذه الأشياء بناءً على إعدادات الإذن. سيتطلب Acrobat هذه الكلمة السرية إذا كنت تريد تعيين/تغيير الأذونات.

{{% /alert %}}

يظهر لك مقطع الشيفرة التالي كيفية تغيير كلمات السر لملف PDF.

```csharp
public static void ChangePassword()
        {
            PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
            // Create PdfFileSecurity object
            if (pdfFileInfo.IsEncrypted)
            {
                PdfFileSecurity fileSecurity = new PdfFileSecurity();
                fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
                fileSecurity.ChangePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", DocumentPrivilege.Print, KeySize.x256);
                fileSecurity.Save(_dataDir + "sample_encrtypted1.pdf");
            }
        }
```