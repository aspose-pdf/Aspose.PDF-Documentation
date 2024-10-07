---
title: العمل مع التوقيع في ملف PDF
type: docs
weight: 40
url: /net/working-with-signature-in-a-pdf-file/
description: يشرح هذا القسم كيفية استخراج معلومات التوقيع، استخراج الصورة من التوقيع، تغيير اللغة، وغيرها باستخدام فئة PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## كيفية استخراج معلومات التوقيع

تدعم Aspose.PDF لـ .NET ميزة توقيع ملفات PDF رقميًا باستخدام فئة PdfFileSignature. حاليًا، من الممكن أيضًا تحديد صلاحية الشهادة ولكن لا يمكننا استخراج الشهادة بالكامل. المعلومات التي يمكن استخراجها هي المفتاح العام، البصمة، والجهة المصدرة، إلخ.

لاستخراج معلومات التوقيع، قمنا بإدخال الطريقة ExtractCertificate(..) إلى فئة PdfFileSignature. يرجى إلقاء نظرة على مقتطف الكود التالي الذي يوضح الخطوات لاستخراج الشهادة من كائن PdfFileSignature:

```csharp
public static void ExtractSignatureInfo()
        {
            string input = _dataDir + "DigitallySign.pdf";
            string certificateFileName = "extracted_cert.pfx";
            using (PdfFileSignature pdfFileSignature = new PdfFileSignature())
            {
                pdfFileSignature.BindPdf(input);
                var sigNames = pdfFileSignature.GetSignNames();
                if (sigNames.Count > 0)
                {
                    string sigName = sigNames[0];
                    if (!string.IsNullOrEmpty(sigName))
                    {
                        Stream cerStream = pdfFileSignature.ExtractCertificate(sigName);
                        if (cerStream != null)
                        {
                            using (cerStream)
                            {
                                using (FileStream fs = new FileStream(_dataDir + certificateFileName, FileMode.CreateNew))
                                {
                                    cerStream.CopyTo(fs);
                                }
                            }
                        }
                    }
                }
            }
        }
```
```

## استخراج الصورة من حقل التوقيع (PdfFileSignature)

تدعم Aspose.PDF لـ .NET ميزة التوقيع الرقمي لملفات PDF باستخدام فئة PdfFileSignature وأثناء توقيع المستند، يمكنك أيضًا تعيين صورة لمظهر التوقيع. الآن يوفر هذا API أيضًا القدرة على استخراج معلومات التوقيع بالإضافة إلى الصورة المرتبطة بحقل التوقيع.

من أجل استخراج معلومات التوقيع، قمنا بإدخال طريقة ExtractImage(..) إلى فئة PdfFileSignature. يرجى إلقاء نظرة على مقتطف الكود التالي الذي يوضح الخطوات لاستخراج الصورة من كائن PdfFileSignature:

```csharp
public static void ExtractSignatureImage()
        {
            using (PdfFileSignature signature = new PdfFileSignature())
            {
                signature.BindPdf(_dataDir + "DigitallySign.pdf");

                if (signature.ContainsSignature())
                {
                    foreach (string sigName in signature.GetSignNames())
                    {
                        string outFile = _dataDir + "ExtractImages_out.jpg";
                        using (Stream imageStream = signature.ExtractImage(sigName))
                        {
                            if (imageStream != null)
                            {
                                imageStream.Position = 0;
                                using (FileStream fs = new FileStream(outFile, FileMode.OpenOrCreate))
                                {
                                    imageStream.CopyTo(fs);
                                }
                            }
                        }
                    }
                }
            }
        }
```

## قمع الموقع والسبب

تتيح وظيفة Aspose.PDF تكوينًا مرنًا لتوقيع النسخة الرقمية. توفر فئة [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) القدرة على توقيع ملف PDF. يتيح تنفيذ طريقة التوقيع توقيع ملف PDF وتمرير كائن التوقيع المحدد إلى هذه الفئة. تحتوي طريقة التوقيع على مجموعة من السمات لتخصيص توقيع النسخة الرقمية النهائية. في حالة الحاجة إلى قمع بعض السمات النصية من توقيع النسخة النهائية، يمكنك تركها فارغة. يوضح مقتطف الشيفرة التالي كيفية قمع سطرين "الموقع" و"السبب" من كتلة التوقيع:

```csharp
public static void SupressLocationReason()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Create a rectangle for signature location
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
            // Set signature appearance
            pdfSign.SignatureAppearance = _dataDir + "aspose-logo.png";

            // Create any of the three signature types
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, string.Empty, "test01@aspose-pdf-demo.local", string.Empty, true, rect, signature);
            // Save output PDF file
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

## ميزات التخصيص للتوقيع الرقمي

Aspose.PDF لـ .NET يسمح بميزات التخصيص للتوقيع الرقمي. تقوم طريقة Sign التابعة لفئة [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) بالتنفيذ مع 6 تحميلات زائدة لاستخدامك المريح. على سبيل المثال، يمكنك تكوين التوقيع الناتج فقط بواسطة مثيل فئة SignatureCustomAppearance وقيم خصائصها. يوضح مقطع الشيفرة التالي كيفية إخفاء التسمية "موقعة رقميًا بواسطة" من توقيعك الرقمي الناتج لملف PDF الخاص بك.

```csharp
  public static void CustomizationFeaturesForDigitalSign()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Create a rectangle for signature location
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);

            // Create any of the three signature types
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance
            {
                FontSize = 6,
                FontFamilyName = "Times New Roman",
                DigitalSignedLabel = "Signed by:"
            };
            signature.CustomAppearance = signatureCustomAppearance;

            pdfSign.Sign(1, true, rect, signature);
            // Save output PDF file
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```


## تغيير اللغة في نص التوقيع الرقمي

باستخدام Aspose.PDF لواجهة برمجة التطبيقات .NET، يمكنك توقيع ملف PDF باستخدام أي من أنواع التوقيعات الثلاثة التالية:

- PKCS#1
- PKCS#7
- PKCS#7

كل من التوقيعات المقدمة يحتوي على مجموعة من خصائص التكوين التي تم تنفيذها لراحتك (التوطين، تنسيق التاريخ والوقت، عائلة الخطوط إلخ). توفر فئة [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) الوظائف المقابلة. يوضح المقتطف البرمجي التالي كيفية تغيير اللغة في نص التوقيع الرقمي:

```csharp
     public static void ChangeLanguageInDigitalSignText()
        {
            string inFile = _dataDir + "sample01.pdf";
            string outFile = _dataDir + "DigitallySign.pdf";

            using (Aspose.Pdf.Facades.PdfFileSignature pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
            {
                pdfSign.BindPdf(inFile);
                //create a rectangle for signature location
                System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);

                //create any of the three signature types
                PKCS7 pkcs = new PKCS7(_dataDir + "test01.pfx", "Aspose2021")
                {
                    Reason = "Pruebas Firma",
                    ContactInfo = "Contacto Pruebas",
                    Location = "Población (Provincia)",
                    Date = DateTime.Now
                };
                SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance
                {
                    DateSignedAtLabel = "Fecha",
                    DigitalSignedLabel = "Digitalmente firmado por",
                    ReasonLabel = "Razón",
                    LocationLabel = "Localización",
                    FontFamilyName = "Arial",
                    FontSize = 10d,
                    Culture = System.Globalization.CultureInfo.InvariantCulture,
                    DateTimeFormat = "yyyy.MM.dd HH:mm:ss"
                };
                pkcs.CustomAppearance = signatureCustomAppearance;
                // sign the PDF file
                pdfSign.Sign(1, true, rect, pkcs);
                //save output PDF file
                pdfSign.Save(outFile);
            }
        }
```
```