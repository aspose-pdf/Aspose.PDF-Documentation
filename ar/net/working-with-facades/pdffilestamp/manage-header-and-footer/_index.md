---
title: إدارة الرأس والتذييل
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ar/net/manage-header-and-footer/
description: استكشف كيفية التلاعب بالرؤوس والتذييلات في ملفات PDF في .NET باستخدام Aspose.PDF لتحسين هيكلة الوثائق.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manage Header and Footer",
    "alternativeHeadline": "Enhance PDFs with Custom Headers and Footers",
    "abstract": "تتيح ميزات إدارة الرأس والتذييل في Aspose.PDF for .NET للمستخدمين إضافة وتخصيص وتنسيق كل من الرؤوس والتذييلات في مستندات PDF بسهولة باستخدام فئة PdfFileStamp. تدعم هذه الوظيفة تضمين النصوص والصور، مما يوفر مرونة في تقديم الوثائق مع ضمان تنسيق احترافي. يمكن للمستخدمين دمج هذه الميزة بسلاسة في تطبيقاتهم لتعزيز الجاذبية البصرية وتنظيم ملفات PDF",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1007",
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
    "url": "/net/manage-header-and-footer/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manage-header-and-footer/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## إضافة رأس في ملف PDF

تتيح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) إضافة رأس في ملف PDF. لإضافة رأس، تحتاج أولاً إلى إنشاء كائن من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). يمكنك تنسيق نص الرأس باستخدام فئة [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). بمجرد أن تكون جاهزًا لإضافة الرأس في الملف، تحتاج إلى استدعاء طريقة [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). تحتاج أيضًا إلى تحديد على الأقل الهامش العلوي في طريقة [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). يوضح لك المقتطف البرمجي التالي كيفية إضافة رأس في ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeader()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create formatted text for the header
        var formattedText = new Aspose.Pdf.Facades.FormattedText(
            "Aspose - Your File Format Experts!",
            System.Drawing.Color.Yellow,
            System.Drawing.Color.Black,
            Aspose.Pdf.Facades.FontStyle.Courier,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false,
            14);

        // Add header
        fileStamp.AddHeader(formattedText, 10);

        // Save PDF document
        fileStamp.Save(dataDir + "AddHeader_out.pdf");
    }
}
```

## إضافة تذييل في ملف PDF

تتيح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) إضافة تذييل في ملف PDF. لإضافة تذييل، تحتاج أولاً إلى إنشاء كائن من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). يمكنك تنسيق نص التذييل باستخدام فئة [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). بمجرد أن تكون جاهزًا لإضافة التذييل في الملف، تحتاج إلى استدعاء طريقة [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). تحتاج أيضًا إلى تحديد على الأقل الهامش السفلي في طريقة [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). يوضح لك المقتطف البرمجي التالي كيفية إضافة تذييل في ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFooter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create formatted text for the footer
        var formattedText = new Aspose.Pdf.Facades.FormattedText(
            "Aspose - Your File Format Experts!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Courier,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false,
            14);

        // Add footer
        fileStamp.AddFooter(formattedText, 10);

        // Save PDF document
        fileStamp.Save(dataDir + "AddFooter_out.pdf");
    }
}
```

## إضافة صورة في رأس ملف PDF موجود

تتيح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) إضافة صورة في رأس ملف PDF. لإضافة صورة في الرأس، تحتاج أولاً إلى إنشاء كائن من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). بعد ذلك، تحتاج إلى استدعاء طريقة [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). يمكنك تمرير الصورة إلى طريقة [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). يوضح لك المقتطف البرمجي التالي كيفية إضافة صورة في رأس ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageHeader()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Add Header
        using (var fs = new FileStream(dataDir + "ImageHeader.png", FileMode.Open))
        {
            fileStamp.AddHeader(fs, 10);  // Add image header with position offset

            // Save PDF document
            fileStamp.Save(dataDir + "AddImageHeader_out.pdf");
        }
    }
}
```

## إضافة صورة في تذييل ملف PDF موجود

تتيح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) إضافة صورة في تذييل ملف PDF. لإضافة صورة في التذييل، تحتاج أولاً إلى إنشاء كائن من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). بعد ذلك، تحتاج إلى استدعاء طريقة [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). يمكنك تمرير الصورة إلى طريقة [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). يوضح لك المقتطف البرمجي التالي كيفية إضافة صورة في تذييل ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageFooter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Add footer
        using (var fs = new FileStream(dataDir + "ImageFooter.png", FileMode.Open))
        {
            fileStamp.AddFooter(fs, 10);  // Add image footer with position offset

            // Save PDF document
            fileStamp.Save(dataDir + "AddImageFooter_out.pdf");
        }
    }
}
```