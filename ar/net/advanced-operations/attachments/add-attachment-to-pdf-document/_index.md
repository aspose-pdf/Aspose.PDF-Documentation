---
title: إضافة مرفق إلى مستند PDF
linktitle: إضافة مرفق إلى مستند PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/add-attachment-to-pdf-document/
description: تصف هذه الصفحة كيفية إضافة مرفق إلى ملف PDF باستخدام مكتبة Aspose.PDF لـ .NET
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Attachment to a PDF document",
    "alternativeHeadline": "Easily Attach Files to Your PDF Documents",
    "abstract": "Aspose.PDF for .NET الآن يقدم طريقة فعالة لتعزيز مستندات PDF الخاصة بك من خلال السماح للمستخدمين بإضافة مرفقات متنوعة بسلاسة، بما في ذلك ملفات نصية وصور. تبسط هذه الوظيفة عملية تضمين معلومات إضافية داخل PDF، مما يضمن أن البيانات الأساسية متاحة بسهولة داخل مستنداتك. قم بتحسين إدارة مستنداتك مع هذه الميزة القوية وتحسين تجربة المستخدم من خلال الاحتفاظ بجميع الموارد ذات الصلة معًا",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Adding attachments to PDF, PDF file types, Aspose.PDF for .NET, FileSpecification object, Document object, EmbeddedFiles collection, PDF document manipulation, C# PDF library, PDF attachment functionality, Aspose.Drawing integration",
    "wordcount": "309",
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
    "url": "/net/add-attachment-to-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-attachment-to-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "تصف هذه الصفحة كيفية إضافة مرفق إلى ملف PDF باستخدام مكتبة Aspose.PDF لـ .NET"
}
</script>

يمكن أن تحتوي المرفقات على مجموعة واسعة من المعلومات ويمكن أن تكون من أنواع ملفات متنوعة. تشرح هذه المقالة كيفية إضافة مرفق إلى ملف PDF.

يعمل مقتطف الكود التالي أيضًا مع مكتبة [Aspose.Drawing](/pdf/net/drawing/).

1. أنشئ مشروع C# جديد.
1. أضف مرجعًا إلى DLL Aspose.PDF.
1. أنشئ كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. أنشئ كائن [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) مع الملف الذي تضيفه، ووصف الملف.
1. أضف كائن [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) إلى مجموعة [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) لكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) باستخدام طريقة Add الخاصة بالمجموعة.

تحتوي مجموعة [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) على جميع المرفقات في ملف PDF. يوضح لك مقتطف الكود التالي كيفية إضافة مرفق في مستند PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddEmbeddedFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf"))
    {
        // Setup new file to be added as attachment
        Aspose.Pdf.FileSpecification fileSpecification = new Aspose.Pdf.FileSpecification(dataDir + "test.txt", "Sample text file");

        // Add attachment to document's attachment collection
        document.EmbeddedFiles.Add(fileSpecification);

        // Save PDF document
        document.Save(dataDir + "AddAnnotations_out.pdf");
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