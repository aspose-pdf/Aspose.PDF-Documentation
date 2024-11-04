---
title: التحكم في استثناء ملف PDF
type: docs
weight: 30
url: /net/control-exception/
description: يشرح هذا الموضوع كيفية التحكم في الاستثناء على ملف PDF باستخدام فئة PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

تسمح لك فئة [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) بالتحكم في الاستثناءات. للقيام بذلك، تحتاج إلى تعيين خاصية [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) إلى false أو true. إذا قمت بتعيين العملية على false، فإن نتيجة [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) ستعيد true أو false اعتمادًا على صحة كلمة المرور.

```csharp
   public static void ControlExceptionPDFFile()
        {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.AllowExceptions = false;
            // فك تشفير مستند PDF
            if (!fileSecurity.DecryptFile("IncorrectPassword"))
            {
                Console.WriteLine("هناك خطأ ما...");
                Console.WriteLine($"آخر استثناء: {fileSecurity.LastException.Message}");
            }
            fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
        }
```

إذا قمت بتعيين خاصية [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) إلى true، فيمكنك الحصول على نتيجة العملية باستخدام مشغل try-catch.

```csharp
public static void ControlExceptionPDFFile2()
        {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.AllowExceptions = true;
            try
            {
                // فك تشفير مستند PDF
                fileSecurity.DecryptFile("IncorrectPassword");
            }
            catch (Exception ex)
            {
                Console.WriteLine("هناك خطأ ما...");
                Console.WriteLine($"استثناء: {ex.Message}");
            }
            fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
        }
```