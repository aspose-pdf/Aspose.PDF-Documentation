---
title: فك تشفير ملف PDF
type: docs
weight: 20
url: /net/decrypt-pdf-file/
description: يشرح هذا الموضوع كيفية فك تشفير ملف PDF باستخدام فئة PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

يجب فتح مستند PDF مشفر بكلمة مرور أو شهادة قبل أن يمكن تنفيذ عملية أخرى عليه. إذا حاولت العمل على مستند PDF مشفر، فسوف ترمي استثناء. بعد فتح ملف PDF مشفر، يمكنك تنفيذ عملية واحدة أو أكثر عليه.

## فك تشفير ملف PDF باستخدام كلمة مرور المالك

{{% alert color="primary" %}}
جرب عبر الإنترنت <br>
يمكنك محاولة فتح المستند باستخدام Aspose.PDF والحصول على النتائج عبر الإنترنت في هذا الرابط:
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

لفك تشفير ملف PDF، تحتاج إلى إنشاء كائن [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) ثم استدعاء طريقة [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile). ```
أنت بحاجة أيضًا إلى تمرير كلمة مرور المالك إلى [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) الطريقة. يوضح لك مقتطف الشفرة التالي كيفية فك تشفير ملف PDF.

```csharp
    public static void DecryptPDFFile()
        {
            PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
            // Create PdfFileSecurity object
            if (pdfFileInfo.IsEncrypted)
            {
                PdfFileSecurity fileSecurity = new PdfFileSecurity();
                fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
                // Decrypt PDF document
                fileSecurity.DecryptFile("P@ssw0rd");
                fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
            }
        }
```
```