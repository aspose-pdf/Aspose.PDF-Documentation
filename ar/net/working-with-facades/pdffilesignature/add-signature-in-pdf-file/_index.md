---
title: إضافة توقيع في ملف PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/add-signature-in-pdf/
description: يشرح هذا القسم كيفية إضافة توقيع إلى ملف PDF باستخدام فئة PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Signature in PDF File",
    "alternativeHeadline": "Add Custom Digital Signatures to PDF Files",
    "abstract": "قم بتحسين مستندات PDF الخاصة بك مع القدرة الجديدة على إضافة توقيعات رقمية باستخدام فئة PdfFileSignature. تتيح هذه الميزة للمستخدمين تطبيق أنواع توقيع مختلفة، بما في ذلك PKCS#1 و PKCS#7 و PKCS#7Detached، مع تخصيص مظهر التوقيع باستخدام الصور وخصائص معينة. قم بتبسيط عملية التحقق من المستندات الخاصة بك من خلال دمج توقيعات متعددة على صفحات مختلفة بسهولة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "838",
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
    "url": "/net/add-signature-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-signature-in-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## إضافة توقيع رقمي في ملف PDF

تتيح لك فئة [PdfFileSignature](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilesignature) إضافة توقيع في ملف PDF. تحتاج إلى إنشاء كائن من فئة [PdfFileSignature](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilesignature) باستخدام ملفات PDF المدخلة والمخرجة. تحتاج أيضًا إلى إنشاء كائن [Rectangle](https://reference.aspose.com/pdf/ar/net/aspose.pdf/rectangle) في المكان الذي تريد إضافة التوقيع فيه، ومن أجل ضبط المظهر يمكنك تحديد صورة باستخدام خاصية [SignatureAppearance](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilesignature/properties/signatureappearance) لكائن [PdfFileSignature](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilesignature). توفر Aspose.Pdf.Facades أيضًا أنواعًا مختلفة من التوقيعات مثل PKCS#1 و PKCS#7 و PKCS#7Detached. لإنشاء توقيع من نوع معين، تحتاج إلى إنشاء كائن من الفئة المحددة مثل **PKCS1** أو **PKCS7** أو **PKCS7Detached** باستخدام ملف الشهادة وكلمة المرور.

بمجرد إنشاء كائن من نوع توقيع معين، يمكنك استخدام طريقة [Sign](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilesignature/methods/sign/index) لفئة [PdfFileSignature](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilesignature) لتوقيع ملف PDF وتمرير كائن التوقيع المحدد إلى هذه الفئة. يمكنك أيضًا تحديد خصائص أخرى لهذه الطريقة. أخيرًا، تحتاج إلى حفظ ملف PDF الموقع باستخدام طريقة [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/save/index) لفئة [PdfFileSignature](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilesignature). يوضح الكود التالي كيفية إضافة توقيع في ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPdfFileSignature()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
    
        // Set signature appearance
        pdFileSignature.SignatureAppearance = dataDir + "aspose-logo.png";

        // Create any of the three signature types
        var signature = new PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdFileSignature.Sign(1, "I'm document author", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect, signature);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

يوضح مثال الكود التالي القدرة على توقيع مستند بتوقيعين. في مثالنا، وضعنا التوقيع الأول على الصفحة الأولى، والثاني على الصفحة الثانية. يمكنك تحديد الصفحات التي تحتاجها.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTwoSignature()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for 1st signature location
        System.Drawing.Rectangle rect1 = new System.Drawing.Rectangle(10, 10, 300, 50);

        // Create 1st signature object
        var signature1 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdFileSignature.Sign(1, "I'm document author", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect1, signature1);
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");

        // Sign with 2nd signature
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "DigitallySign_out.pdf");

        // Create a rectangle for 2nd signature location
        System.Drawing.Rectangle rect2 = new System.Drawing.Rectangle(10, 10, 300, 50);

        // Create 2nd signature object
        var signature2 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdFileSignature.Sign(2, "I'm document reviewer", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect2, signature2);

        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign2_out.pdf");
    }
}
```

للمستندات التي تحتوي على نماذج أو أكروفورمز تحتاج إلى توقيع، انظر المثال التالي. تحتاج إلى إنشاء كائن من فئة [PdfFileSignature](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffilesignature) باستخدام ملفات PDF المدخلة والمخرجة. استخدم [BindPdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdffilesignature/bindpdf/methods/1) للربط. أنشئ توقيعًا مع القدرة على إضافة الخصائص المطلوبة. في مثالنا، هي 'Reason' و 'CustomAppearance'.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPdfFileSignatureField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "input.pdf");

        // Create any of the three signature types
        var signature = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Sign as Author",
            CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
            {
                FontSize = 6,
                FontFamilyName = "Calibri"
            }
        }; // PKCS#1
        
        pdFileSignature.Sign("Signature1", signature);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

إذا كان مستندنا يحتوي على حقلين، فإن خوارزمية توقيعه مشابهة للمثال الأول.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPdfFileSignatureField2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");

        // Create any of the three signature types
        var signature1 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Sign as Author",
            CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
            {
                FontSize = 6
            }
        }; // PKCS#1
        pdFileSignature.Sign("Signature1", signature1);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "DigitallySign_out.pdf");

        // Create any of the three signature types
        var signature2 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Sign as Reviwer",
            CustomAppearance = new SignatureCustomAppearance
            {
                FontSize = 6
            }
        }; // PKCS#1
        
        pdFileSignature.Sign("Signature2", signature2);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign2_out.pdf");
    }
}
```