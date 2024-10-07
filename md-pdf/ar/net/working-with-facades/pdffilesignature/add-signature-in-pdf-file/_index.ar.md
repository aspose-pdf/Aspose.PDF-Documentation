```
---
title: إضافة توقيع في ملف PDF
type: docs
weight: 10
url: /net/add-signature-in-pdf/
description: يوضح هذا القسم كيفية إضافة توقيع إلى ملف PDF باستخدام فئة PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## إضافة توقيع رقمي في ملف PDF

[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) تتيح لك الفئة إضافة توقيع في ملف PDF.
``` ```
You need to create an object of [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) class using input and output PDF files. You also need to create a [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) object at which you want to add the signature and in order to set appearance you can specify an image using [SignatureAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/signatureappearance) property of the [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) object. Aspose.Pdf.Facades also provides different kinds of signatures like PKCS#1, PKCS#7, and PKCS#7Detached. In order to create a signature of a specific type, you need to create an object of the particular class like **PKCS1** , **PKCS7** or **PKCS7Detached** using the certificate file and the password.

بمجرد إنشاء كائن من نوع توقيع معين، يمكنك استخدام طريقة [Sign](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/sign/index) من فئة [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) لتوقيع ملف PDF وتمرير كائن التوقيع المحدد إلى هذه الفئة.
``` يمكنك أيضًا تحديد سمات أخرى لهذه الطريقة. أخيرًا، تحتاج إلى حفظ ملف PDF الموقع باستخدام [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) طريقة فئة [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). يوضح لك مقتطف الشيفرة التالي كيفية إضافة توقيع في ملف PDF.

```csharp
public static void AddPdfFileSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // إنشاء مستطيل لموقع التوقيع
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
            // تعيين مظهر التوقيع
            pdfSign.SignatureAppearance = _dataDir + "aspose-logo.png";

            // إنشاء أي نوع من أنواع التوقيعات الثلاثة
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, "أنا مؤلف المستند", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect, signature);
            // حفظ ملف PDF الناتج
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```
النموذج التالي من التعليمات البرمجية يظهر لنا القدرة على توقيع مستند بتوقيعين. في مثالنا، نضع التوقيع الأول على الصفحة الأولى، والثاني على الصفحة الثانية. يمكنك تحديد الصفحات التي تحتاجها.

```csharp
 public static void AddTwoSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();

            // Sign with 1st signature

            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Create a rectangle for 1st signature location
            System.Drawing.Rectangle rect1 = new System.Drawing.Rectangle(10, 10, 300, 50);

            // Create 1st signature object
            PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, "أنا مؤلف المستند", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, أستراليا", true, rect1, signature1);
            pdfSign.Save(_dataDir + "DigitallySign.pdf");


            // Sign with 2nd signature

            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            // Create a rectangle for 2nd signature location
            System.Drawing.Rectangle rect2 = new System.Drawing.Rectangle(10, 10, 300, 50);

            // Create 2nd signature object
            PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(2, "أنا مراجع المستند", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, أستراليا", true, rect2, signature2);

            // Save output PDF file
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

For a document with forms or acroforms that needs to be signed, see the following example. تحتاج إلى إنشاء كائن من فئة [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) باستخدام ملفات PDF المدخلة والمخرجة. استخدم [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesignature/bindpdf/methods/1) للربط. قم بإنشاء توقيع مع القدرة على إضافة الخصائص المطلوبة. في مثالنا هم 'Reason' و 'CustomAppearance'.

```csharp
 public static void AddPdfFileSignatureField()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample02.pdf");

            // Create any of the three signature types
            PKCS1 signature = new PKCS1(_dataDir + "test02.pfx", "Aspose2021")
            {
                Reason = "Sign as Author",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6,
                    FontFamilyName = "Calibri"
                }
            }; // PKCS#1
            pdfSign.Sign("Signature1", signature);
            // Save output PDF file
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

إذا كانت مستندنا يحتوي على حقلين، فإن الخوارزمية لتوقيعه تشبه المثال الأول.

```csharp
public static void AddPdfFileSignatureField2()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample03.pdf");

            // إنشاء أي من أنواع التوقيع الثلاثة
            PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021")
            {
                Reason = "التوقيع كمؤلف",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6
                }
            }; // PKCS#1
            pdfSign.Sign("Signature1", signature1);
            // حفظ ملف PDF الناتج
            pdfSign.Save(_dataDir + "DigitallySign.pdf");

            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            // إنشاء أي من أنواع التوقيع الثلاثة
            PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021")
            {
                Reason = "التوقيع كمراجع",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6
                }
            }; // PKCS#1
            pdfSign.Sign("Signature2", signature2);
            // حفظ ملف PDF الناتج
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```