---
title: استخراج الصور من PDF C#
linktitle: استخراج الصور من PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/extract-images-from-the-pdf-file/
description: كيفية استخراج جزء من الصورة من PDF باستخدام Aspose.PDF for .NET في C#
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images from PDF C#",
    "alternativeHeadline": "Effortlessly Extract Images from PDF Files in C#",
    "abstract": "افتح قوة Aspose.PDF for .NET مع الوظيفة الجديدة لاستخراج الصور من ملفات PDF مباشرة في C#. تتيح هذه الميزة للمستخدمين استرجاع وحفظ الصور من صفحات معينة بسهولة، مما يسهل إدارة الصور ومعالجتها في تطبيقات .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "240",
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
    "url": "/net/extract-images-from-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-images-from-the-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

تحتوي الصور على كل مجموعة [الموارد](https://reference.aspose.com/pdf/net/aspose.pdf/resources) في كل صفحة في مجموعة [الصور](https://reference.aspose.com/pdf/net/aspose.pdf/resources/properties/images). لاستخراج صفحة معينة، ثم احصل على الصورة من مجموعة الصور باستخدام الفهرس المحدد للصورة.

يعيد فهرس الصورة كائن [XImage](https://reference.aspose.com/pdf/net/aspose.pdf/ximage). يوفر هذا الكائن طريقة Save التي يمكن استخدامها لحفظ الصورة المستخرجة. يوضح مقتطف الكود التالي كيفية استخراج الصور من ملف PDF.

يعمل مقتطف الكود التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractImages.pdf"))
    {
        // Extract a particular image
        var xImage = document.Pages[1].Resources.Images[1];

        using (var outputImage = new FileStream(dataDir + "outputImage.jpg", FileMode.Create))
        {
            // Save the output image
            xImage.Save(outputImage, ImageFormat.Jpeg);
        }

        // Save PDF document
        document.Save(dataDir + "ExtractImages_out.pdf");
    }
}
```