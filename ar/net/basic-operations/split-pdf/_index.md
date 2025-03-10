---
title: تقسيم PDF برمجياً
linktitle: تقسيم ملفات PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ar/net/split-pdf-document/
description: يوضح هذا الموضوع كيفية تقسيم صفحات PDF إلى ملفات PDF فردية في تطبيقات .NET الخاصة بك باستخدام C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Split PDF programmatically",
    "alternativeHeadline": "Effortlessly split PDF into individual files with C#",
    "abstract": "يتيح للمطورين تقسيم مستندات PDF برمجياً إلى ملفات فردية باستخدام C#. تسهل هذه الميزة إدارة محتوى PDF من خلال تمكين استخراج صفحات متميزة إلى ملفات PDF منفصلة داخل تطبيقات .NET، مما يعزز كفاءة سير العمل وقدرات التعامل مع الوثائق.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "326",
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
    "url": "/net/split-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/split-pdf-document/"
    },
    "dateModified": "2024-11-26",
    "description": "يظهر هذا الموضوع كيفية تقسيم صفحات PDF إلى ملفات PDF فردية في تطبيقات .NET الخاصة بك باستخدام C#."
}
</script>

## مثال حي

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) هو تطبيق ويب مجاني عبر الإنترنت يتيح لك استكشاف كيفية عمل وظيفة تقسيم العرض.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

يظهر هذا الموضوع كيفية تقسيم صفحات PDF إلى ملفات PDF فردية في تطبيقات .NET الخاصة بك. لتقسيم صفحات PDF إلى ملفات PDF صفحة واحدة باستخدام C#، يمكن اتباع الخطوات التالية:

1. قم بالتكرار عبر صفحات مستند PDF من خلال مجموعة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) الخاصة بكائن [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. في كل تكرار، قم بإنشاء كائن Document جديد وأضف كائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) الفردي إلى المستند الفارغ.
1. احفظ PDF الجديد باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## تقسيم PDF إلى ملفات متعددة أو PDFs منفصلة

تظهر مقتطفات كود C# التالية كيفية تقسيم صفحات PDF إلى ملفات PDF فردية.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document1 = new Aspose.Pdf.Document(dataDir + "SplitToPages.pdf"))
    {
        int pageCount = 1;

        // Loop through all the pages
        foreach (var page in document1.Pages)
        {
            // Create PDF document
            using (var document2 = new Aspose.Pdf.Document())
            {
                document2.Pages.Add(page);
                // Save PDF document
                document2.Save(dataDir + "Page_" + pageCount + "_out.pdf");
                pageCount++;
            }
        }
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