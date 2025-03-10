---
title: استخراج الصور من ملف PDF
linktitle: استخراج الصور
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ar/net/extract-images-from-pdf-file/
description: يوضح هذا القسم كيفية استخراج الصور من ملف PDF باستخدام مكتبة C#.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images from PDF File",
    "alternativeHeadline": "Effortlessly Extract Images from PDF Files",
    "abstract": "تتيح الميزة الجديدة لاستخراج الصور من ملفات PDF باستخدام مكتبة C# للمطورين استرجاع الصور وحفظها بسهولة من المستندات PDF. من خلال الاستفادة من مكتبة Aspose.PDF، يمكن للمستخدمين الوصول إلى صور معينة من أي صفحة وتصديرها بتنسيقات مختلفة، مما يسهل سير العمل الخاص بهم في إدارة محتوى PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Extract images, PDF file, C# library, images collection, extract images from PDF, XImage object, save extracted image, PDF manipulation, Aspose.PDF for .NET, document resources",
    "wordcount": "227",
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
    "url": "/net/extract-images-from-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-images-from-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "يظهر هذا القسم كيفية استخراج الصور من ملف PDF باستخدام مكتبة C#."
}
</script>

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/) .

تحتوي الصور على مجموعة [Resources](https://reference.aspose.com/pdf/net/aspose.pdf/resources) الخاصة بكل صفحة في مجموعة [Images](https://reference.aspose.com/pdf/net/aspose.pdf/resources/properties/images) . لاستخراج صفحة معينة، ثم الحصول على الصورة من مجموعة الصور باستخدام الفهرس المحدد للصورة.

يعيد فهرس الصورة كائن [XImage](https://reference.aspose.com/pdf/net/aspose.pdf/ximage) . يوفر هذا الكائن طريقة Save يمكن استخدامها لحفظ الصورة المستخرجة. يوضح مقتطف الشيفرة التالي كيفية استخراج الصور من ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractImages.pdf"))
    {
        // Extract a particular image
        var xImage = document.Pages[1].Resources.Images[1];
        using (var outputImage = new FileStream(dataDir + "ExtractedImage.jpg", FileMode.Create))
        {
            // Save PDF document image
            xImage.Save(outputImage, System.Drawing.Imaging.ImageFormat.Jpeg);
        }

        // Save PDF document
        document.Save(dataDir + "ExtractImages_out.pdf");
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