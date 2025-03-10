---
title: إضافة رقم الصفحة إلى PDF
linktitle: إضافة رقم الصفحة
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 100
url: /ar/net/add-page-number/
description: Aspose.PDF for .NET يتيح لك إضافة ختم رقم الصفحة إلى ملف PDF الخاص بك باستخدام فئة PageNumber Stamp.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Page Number to PDF",
    "alternativeHeadline": "Add Dynamic Page Numbering to PDF",
    "abstract": "Aspose.PDF for .NET يقدم ميزة قوية لختم رقم الصفحة، مما يتيح دمج أرقام الصفحات بسلاسة في مستندات PDF. تعزز هذه الوظيفة من تنقل المستند وتنظيمه من خلال السماح للمستخدمين بتخصيص التنسيق والمحاذاة والتصميم لتحسين قابلية القراءة والعرض الاحترافي.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Page Number, PDF Stamp, Aspose.PDF for .NET, PageNumberStamp class, Document object, PageNumberStamp properties, Bates numbering, PDF document generation, Page number stamp, C# PDF manipulation",
    "wordcount": "559",
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
    "url": "/net/add-page-number/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-page-number/"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NET يتيح لك إضافة ختم رقم الصفحة إلى ملف PDF الخاص بك باستخدام فئة PageNumber Stamp."
}
</script>

يجب أن تحتوي جميع المستندات على أرقام صفحات. رقم الصفحة يسهل على القارئ تحديد أجزاء مختلفة من المستند.
**Aspose.PDF for .NET** يتيح لك إضافة أرقام الصفحات باستخدام PageNumberStamp.

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

يمكنك استخدام فئة [PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) لإضافة ختم رقم الصفحة في ملف PDF. توفر فئة [PageNumber Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) الخصائص اللازمة لإنشاء ختم يعتمد على رقم الصفحة مثل التنسيق، الهوامش، المحاذاة، الرقم الابتدائي، إلخ. لإضافة ختم رقم الصفحة، تحتاج إلى إنشاء كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) وكائن [PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) من [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) لإضافة الختم في PDF. يمكنك أيضًا تعيين سمات الخط لختم رقم الصفحة. يوضح لك مقتطف الشيفرة التالي كيفية إضافة أرقام الصفحات في ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageNumberToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PageNumberStamp.pdf"))
    {
        // Create page number stamp
        var pageNumberStamp = new Aspose.Pdf.PageNumberStamp();
        // Whether the stamp is background
        pageNumberStamp.Background = false;
        pageNumberStamp.Format = "Page # of " + document.Pages.Count;
        pageNumberStamp.BottomMargin = 10;
        pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
        pageNumberStamp.StartingNumber = 1;
        // Set text properties
        pageNumberStamp.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        pageNumberStamp.TextState.FontSize = 14.0F;
        pageNumberStamp.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        pageNumberStamp.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
        pageNumberStamp.TextState.ForegroundColor = Color.Aqua;
        // Add stamp to particular page
        document.Pages[1].AddStamp(pageNumberStamp);
        // Save PDF document
        document.Save(dataDir + "PageNumberStamp_out.pdf");  
    }
}
```

## مثال حي

[إضافة أرقام صفحات PDF](https://products.aspose.app/pdf/page-number) هو تطبيق ويب مجاني عبر الإنترنت يتيح لك استكشاف كيفية عمل وظيفة إضافة أرقام الصفحات.

[![كيفية إضافة رقم الصفحة في PDF باستخدام C#](page_number.png)](https://products.aspose.app/pdf/page-number)

## إضافة/إزالة ترقيم بايتس

**ترقيم بايتس** (المعروف أيضًا بختم بايتس) يُستخدم في المجالات القانونية والطبية والتجارية لوضع أرقام تعريفية و/أو علامات تاريخ/وقت على الصور والمستندات أثناء مسحها أو معالجتها، على سبيل المثال، خلال مرحلة الاكتشاف من التحضيرات للمحاكمة أو تحديد إيصالات الأعمال. توفر هذه العملية التعريف والحماية والترقيم التلقائي المتسلسل للصور أو المستندات.

تدعم Aspose.PDF حاليًا ترقيم بايتس بشكل محدود. سيتم تحديث هذه الوظيفة وفقًا لطلبات العملاء.

### كيفية إزالة ترقيم بايتس

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveBatesNumbering()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveBatesNumberingInput.pdf"))
    {
        foreach (var page in document.Pages)
        {
            // Remove bates numbering
            var artifacts = page.Artifacts.Where(ar => ar.CustomSubtype == "BatesN");
            foreach (var artifact in artifacts)
            {
                page.Artifacts.Delete(artifact);   
            }
        }
        // Save PDF document
        document.Save(dataDir + "RemoveBatesNumbering_out.pdf");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>