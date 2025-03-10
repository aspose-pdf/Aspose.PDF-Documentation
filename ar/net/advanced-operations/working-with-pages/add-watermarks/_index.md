---
title: إضافة علامة مائية إلى PDF باستخدام C#
linktitle: إضافة علامة مائية
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /ar/net/add-watermarks/
description: تشرح هذه المقالة ميزات العمل مع العناصر والحصول على العلامات المائية في ملفات PDF باستخدام C# برمجيًا.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add watermark to PDF using C#",
    "alternativeHeadline": "Add Custom Watermarks to PDF with C#",
    "abstract": "تتيح الميزة الجديدة في Aspose.PDF for .NET للمطورين إضافة علامات مائية قابلة للتخصيص إلى مستندات PDF برمجيًا باستخدام وظيفة Artifact. تعزز هذه الميزة إدارة المستندات من خلال دعم خصائص العناصر المختلفة، بما في ذلك النوع، والشفافية، والدوران، وتخصيص النص، مما يمكّن المستخدمين من إنشاء ملفات PDF احترافية وقابلة للتعرف عليها بسهولة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "462",
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
    "url": "/net/add-watermarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-watermarks/"
    },
    "dateModified": "2024-11-26",
    "description": "تشرح هذه المقالة ميزات العمل مع العناصر والحصول على العلامات المائية في ملفات PDF باستخدام C# برمجيًا."
}
</script>

**Aspose.PDF for .NET** يسمح بإضافة علامات مائية إلى مستند PDF الخاص بك باستخدام العناصر. يرجى مراجعة هذه المقالة لحل مهمتك.

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

تسمى العلامة المائية التي تم إنشاؤها باستخدام Adobe Acrobat عنصرًا (كما هو موضح في 14.8.2.2 المحتوى الحقيقي والعناصر في مواصفات PDF). للعمل مع العناصر، تحتوي Aspose.PDF على فئتين: [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) و [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection).

للحصول على جميع العناصر في صفحة معينة، تحتوي فئة [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) على خاصية Artifacts. تشرح هذه الموضوع كيفية العمل مع العناصر في ملفات PDF.

## العمل مع العناصر

تحتوي فئة [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) على الخصائص التالية:

- **Artifact.Type**: يحصل على نوع العنصر (يدعم قيم تعداد Artifact.ArtifactType حيث تشمل القيم الخلفية، والتخطيط، والصفحة، والترقيم وغير محدد).
- **Artifact.Subtype**: يحصل على نوع العنصر الفرعي (يدعم قيم تعداد Artifact.ArtifactSubtype حيث تشمل القيم الخلفية، والتذييل، والرأس، وغير محدد، والعلامة المائية).

{{% alert color="primary" %}}

يرجى ملاحظة أن العلامات المائية التي تم إنشاؤها باستخدام Adobe Acrobat لها النوع ترقيم والنوع الفرعي علامة مائية.

{{% /alert %}}

- **Artifact.Contents**: يحصل على مجموعة من العمليات الداخلية للعنصر. نوعه المدعوم هو System.Collections.ICollection.
- **Artifact.Form**: يحصل على XForm للعنصر (إذا تم استخدام XForm). تحتوي العلامات المائية والرؤوس والتذييلات على XForm الذي يظهر جميع محتويات العنصر.
- **Artifact.Image**: يحصل على صورة العنصر (إذا كانت الصورة موجودة، وإلا null).
- **Artifact.Text**: يحصل على نص العنصر.
- **Artifact.Rectangle**: يحصل على موضع العنصر على الصفحة.
- **Artifact.Rotation**: يحصل على دوران العنصر (بالدرجات، القيمة الإيجابية تشير إلى دوران عكس عقارب الساعة).
- **Artifact.Opacity**: يحصل على شفافية العنصر. القيم الممكنة تتراوح بين 0…1، حيث 1 تعني غير شفاف تمامًا.

## كيفية إضافة علامة مائية على ملفات PDF

تظهر مقتطفات الشيفرة التالية كيفية الحصول على كل علامة مائية في الصفحة الأولى من ملف PDF باستخدام C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddWatermarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddWatermarksInput.pdf"))
    {
        // Create a new watermark artifact
        var artifact = new Aspose.Pdf.WatermarkArtifact();
        artifact.SetTextAndState(
            "WATERMARK",
            new Aspose.Pdf.Text.TextState()
            {
                FontSize = 72,
                ForegroundColor = Aspose.Pdf.Color.Blue,
                Font = Aspose.Pdf.Text.FontRepository.FindFont("Courier")
            });
        // Set watermark properties
        artifact.ArtifactHorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        artifact.ArtifactVerticalAlignment = Aspose.Pdf.VerticalAlignment.Center;
        artifact.Rotation = 45;
        artifact.Opacity = 0.5;
        artifact.IsBackground = true;
        // Add watermark artifact to the first page
        document.Pages[1].Artifacts.Add(artifact);
        // Save PDF document
        document.Save(dataDir + "AddWatermarks_out.pdf");
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