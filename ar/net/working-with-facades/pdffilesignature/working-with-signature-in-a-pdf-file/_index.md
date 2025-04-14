---
title: العمل مع التوقيع في ملف PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ar/net/working-with-signature-in-a-pdf-file/
description: يشرح هذا القسم كيفية استخراج معلومات التوقيع، استخراج الصورة من التوقيع، تغيير اللغة، وما إلى ذلك باستخدام فئة PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Signature in PDF File",
    "alternativeHeadline": "Extract Signature Details and Images from PDFs",
    "abstract": "تعمل الوظيفة الجديدة في Aspose.PDF for .NET على تعزيز أمان مستندات PDF من خلال السماح للمستخدمين باستخراج معلومات التوقيع والصور باستخدام فئة PdfFileSignature. تتضمن هذه الميزة أيضًا القدرة على تخصيص التوقيعات الرقمية، وإخفاء معلومات معينة مثل الموقع والسبب، وتغيير إعدادات اللغة لنص التوقيع، مما يوفر مجموعة أدوات شاملة لإدارة توقيعات PDF بكفاءة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "878",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/working-with-signature-in-a-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-signature-in-a-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## كيفية استخراج معلومات التوقيع

يدعم Aspose.PDF for .NET ميزة التوقيع الرقمي لملفات PDF باستخدام فئة PdfFileSignature. حاليًا، من الممكن أيضًا تحديد صلاحية الشهادة ولكن لا يمكننا استخراج الشهادة بالكامل. المعلومات التي يمكن استخراجها هي المفتاح العام، بصمة الإصبع، والجهة المصدرة، وما إلى ذلك.

لاستخراج معلومات التوقيع، قمنا بإدخال طريقة ExtractCertificate(..) إلى فئة PdfFileSignature. يرجى إلقاء نظرة على مقتطف الكود التالي الذي يوضح الخطوات لاستخراج الشهادة من كائن PdfFileSignature:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSignatureInfo()
{ 
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        // Get list of signature names
        var sigNames = pdfFileSignature.GetSignatureNames();
        if (sigNames.Count > 0)
        {
            SignatureName sigName = sigNames[0];            
            // Extract signature certificate
            Stream cerStream = pdfFileSignature.ExtractCertificate(sigName);
            if (cerStream != null)
            {
                using (cerStream)
                {
                    using (FileStream fs = new FileStream(dataDir + "extracted_cert.pfx", FileMode.CreateNew))
                    {
                        cerStream.CopyTo(fs);
                    }
                }
            }
            
        }
    }
}
```

## استخراج الصورة من حقل التوقيع (PdfFileSignature)

يدعم Aspose.PDF for .NET ميزة التوقيع الرقمي لملفات PDF باستخدام فئة PdfFileSignature وأثناء توقيع المستند، يمكنك أيضًا تعيين صورة لمظهر التوقيع. الآن توفر هذه الواجهة البرمجية أيضًا القدرة على استخراج معلومات التوقيع بالإضافة إلى الصورة المرتبطة بحقل التوقيع.

لاستخراج معلومات التوقيع، قمنا بإدخال طريقة ExtractImage(..) إلى فئة PdfFileSignature. يرجى إلقاء نظرة على مقتطف الكود التالي الذي يوضح الخطوات لاستخراج الصورة من كائن PdfFileSignature:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSignatureImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var signature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        signature.BindPdf(dataDir + "ExtractingImage.pdf");

        if (signature.ContainsSignature())
        {
            // Get list of signature names
            foreach (string sigName in signature.GetSignatureNames())
            {                
                // Extract signature image
                using (Stream imageStream = signature.ExtractImage(sigName))
                {
                    if (imageStream != null)
                    {
                        imageStream.Position = 0;
                        using (FileStream fs = new FileStream(dataDir + "ExtractImages_out.jpg", FileMode.OpenOrCreate))
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

## إخفاء الموقع والسبب

تسمح وظيفة Aspose.PDF بتكوين مرن لنسخة التوقيع الرقمية. توفر فئة [PdfFileSignature](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilesignature) القدرة على توقيع ملف PDF. يسمح تنفيذ طريقة التوقيع بتوقيع PDF وتمرير كائن التوقيع المحدد إلى هذه الفئة. تحتوي طريقة التوقيع على مجموعة من الخصائص لتخصيص التوقيع الرقمي الناتج. في حالة الحاجة إلى إخفاء بعض الخصائص النصية من نتيجة التوقيع، يمكنك تركها فارغة. يوضح مقتطف الكود التالي كيفية إخفاء موقع وسبب السطرين من كتلة التوقيع:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SupressLocationReason()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
        // Set signature appearance
        pdfFileSignature.SignatureAppearance = dataDir + "aspose-logo.png";

        // Create any of the three signature types
        var signature = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdfFileSignature.Sign(1, string.Empty, "test01@aspose-pdf-demo.local", string.Empty, true, rect, signature);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

## ميزات التخصيص للتوقيع الرقمي

يتيح Aspose.PDF for .NET ميزات التخصيص لتوقيع رقمي. تحتوي طريقة التوقيع في فئة [SignatureCustomAppearance](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/signaturecustomappearance) على 6 تحميلات مفرطة لراحتك. على سبيل المثال، يمكنك تكوين التوقيع الناتج فقط من خلال مثيل فئة SignatureCustomAppearance وقيم خصائصها. يوضح مقتطف الكود التالي كيفية إخفاء عنوان "تم التوقيع رقميًا بواسطة" من التوقيع الرقمي الناتج لملف PDF الخاص بك.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomizationFeaturesForDigitalSign()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);

        // Create any of the three signature types
        var signature = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1
        // Create signature appearance
        var signatureCustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
        {
            FontSize = 6,
            FontFamilyName = "Times New Roman",
            DigitalSignedLabel = "Signed by:"
        };
        // Set signature appearance
        signature.CustomAppearance = signatureCustomAppearance;

        pdfFileSignature.Sign(1, true, rect, signature);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

## تغيير اللغة في نص التوقيع الرقمي

باستخدام واجهة برمجة التطبيقات Aspose.PDF for .NET، يمكنك توقيع ملف PDF باستخدام أي من الأنواع الثلاثة التالية من التوقيعات:

- PKCS#1.
- PKCS#7.
- PKCS#12.

تحتوي كل من التوقيعات المقدمة على مجموعة من خصائص التكوين المطبقة لراحتك (التعريب، تنسيق التاريخ والوقت، عائلة الخط، إلخ). توفر فئة [SignatureCustomAppearance](https://reference.aspose.com/pdf/ar/net/aspose.pdf.forms/signaturecustomappearance) الوظيفة المقابلة. يوضح مقتطف الكود التالي كيفية تغيير اللغة في نص التوقيع الرقمي: 

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangeLanguageInDigitalSignText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();   
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");
        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);

        // Create any of the three signature types
        var pkcs = new Aspose.Pdf.Forms.PKCS7(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Pruebas Firma",
            ContactInfo = "Contacto Pruebas",
            Location = "Población (Provincia)",
            Date = DateTime.Now
        };
        
        var signatureCustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
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
        // Set signature appearance
        pkcs.CustomAppearance = signatureCustomAppearance;
        // Sign the PDF file
        pdfFileSignature.Sign(1, true, rect, pkcs);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```