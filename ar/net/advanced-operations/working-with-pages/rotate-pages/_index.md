---
title: تدوير صفحات PDF باستخدام C#
linktitle: تدوير صفحات PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ar/net/rotate-pages/
description: يصف هذا الموضوع كيفية تدوير اتجاه الصفحة في ملف PDF موجود برمجياً باستخدام C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Rotate PDF Pages Using C#",
    "alternativeHeadline": "Effortlessly Rotate PDF Pages with C#",
    "abstract": "تتيح الميزة الجديدة في Aspose.PDF for .NET للمطورين تغيير اتجاه الصفحات في ملفات PDF الموجودة برمجياً. يمكن للمستخدمين التبديل بسهولة بين وضعي العرض والعمودي، مما يضمن تناسب المحتوى بشكل صحيح ضمن التخطيط الجديد، مما يعزز قابلية استخدام الوثيقة وعرضها.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "236",
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
    "url": "/net/rotate-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/rotate-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "يصف هذا الموضوع كيفية تدوير اتجاه الصفحة في ملف PDF موجود برمجياً باستخدام C#."
}
</script>

يصف هذا الموضوع كيفية تحديث أو تغيير اتجاه الصفحة للصفحات في ملف PDF موجود برمجياً باستخدام C#.

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## تغيير اتجاه الصفحة

من إصدار Aspose.PDF for .NET 9.6.0، أضفنا ميزات جديدة رائعة مثل تغيير اتجاه الصفحة من العرض إلى العمودي والعكس. لتغيير اتجاه الصفحة، قم بتعيين MediaBox للصفحة باستخدام مقتطف الشيفرة التالي. يمكنك أيضًا تغيير اتجاه الصفحة عن طريق تعيين زاوية الدوران باستخدام طريقة Rotate().

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePageOrientation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RotatePagesInput.pdf"))
    {
        foreach (Page page in document.Pages)
        {
            Aspose.Pdf.Rectangle r = page.MediaBox;
            double newHeight = r.Width;
            double newWidth = r.Height;
            double newLLX = r.LLX;
            //  We must to move page upper in order to compensate changing page size
            // (lower edge of the page is 0,0 and information is usually placed from the
            //  Top of the page. That's why we move lover edge upper on difference between
            //  Old and new height.
            double newLLY = r.LLY + (r.Height - newHeight);
            page.MediaBox = new Aspose.Pdf.Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight);
            // Sometimes we also need to set CropBox (if it was set in original file)
            page.CropBox = new Aspose.Pdf.Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight);
            // Setting Rotation angle of page
            page.Rotate = Rotation.on90;
        }
        // Save PDF document
        document.Save(dataDir + "ChangeOrientation_out.pdf");
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