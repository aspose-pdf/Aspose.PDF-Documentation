---
title: العمل مع العناصر في .NET
linktitle: العمل مع العناصر
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 170
url: /ar/net/artifacts/
description: Aspose.PDF for .NET يتيح لك إضافة صورة خلفية إلى صفحات PDF، والحصول على كل علامة مائية باستخدام فئة Artifact.
lastmod: "2024-01-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Artifacts in .NET",
    "alternativeHeadline": "Add and Manage Artifacts in PDF Documents",
    "abstract": "Aspose.PDF for .NET يقدم فئة Artifact، مما يسمح للمطورين بإدارة العناصر غير المحتوى مثل الصور الخلفية والعلامات المائية بكفاءة داخل مستندات PDF. تعزز هذه الوظيفة هيكل المستند مع تحسين الوصول والأداء، حيث يمكن تجاهل العناصر بواسطة التقنيات المساعدة. مع خيارات قابلة للتخصيص لأنواع وخصائص، يمكن للمستخدمين بسهولة التلاعب بهذه العناصر لإنشاء مستندات PDF جذابة بصريًا.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Artifacts, PDF document generation, Aspose.PDF for .NET, BackgroundArtifact, WatermarkArtifact, Artifact class, PDF artifacts, Artifact types, Accessibility in PDF, PDF watermark handling",
    "wordcount": "779",
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
    "url": "/net/artifacts/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/artifacts/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET يتيح لك إضافة صورة خلفية إلى صفحات PDF، والحصول على كل علامة مائية باستخدام فئة Artifact."
}
</script>

العناصر في PDF هي كائنات رسومية أو عناصر أخرى ليست جزءًا من المحتوى الفعلي للمستند. تُستخدم عادةً لأغراض الزخرفة أو التخطيط أو الخلفية. تشمل أمثلة العناصر رؤوس الصفحات، والتذييلات، والفواصل، أو الصور التي لا تنقل أي معنى.

الغرض من العناصر في PDF هو السماح بالتمييز بين المحتوى والعناصر غير المحتوى. هذا مهم للوصول، حيث يمكن لبرامج قراءة الشاشة وغيرها من التقنيات المساعدة تجاهل العناصر والتركيز على المحتوى ذي الصلة. يمكن أن تحسن العناصر أيضًا من أداء وجودة مستندات PDF، حيث يمكن استبعادها من الطباعة أو البحث أو النسخ.

لإنشاء عنصر كعنصر في PDF، تحتاج إلى استخدام فئة [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact).
تحتوي على الخصائص المفيدة التالية:

- **Artifact.Type** – يحصل على نوع العنصر (يدعم قيم تعداد Artifact.ArtifactType حيث تشمل القيم الخلفية، والتخطيط، والصفحة، والترقيم وغير محدد).
- **Artifact.Subtype** – يحصل على نوع العنصر الفرعي (يدعم قيم تعداد Artifact.ArtifactSubtype حيث تشمل القيم الخلفية، والتذييل، والرأس، وغير محدد، والعلامة المائية).
- **Artifact.Image** – يحصل على صورة العنصر (إذا كانت الصورة موجودة، وإلا null).
- **Artifact.Text** – يحصل على نص العنصر.
- **Artifact.Contents** – يحصل على مجموعة من العمليات الداخلية للعنصر. نوعه المدعوم هو System.Collections.ICollection.
- **Artifact.Form** – يحصل على XForm للعنصر (إذا تم استخدام XForm). تحتوي العناصر مثل العلامات المائية والرأس والتذييل على XForm الذي يظهر جميع محتويات العنصر.
- **Artifact.Rectangle** – يحصل على موضع العنصر على الصفحة.
- **Artifact.Rotation** – يحصل على دوران العنصر (بالدرجات، القيمة الإيجابية تشير إلى دوران عكس عقارب الساعة).
- **Artifact.Opacity** – يحصل على شفافية العنصر. القيم الممكنة تتراوح بين 0...1، حيث 1 تعني غير شفاف تمامًا.

قد تكون الفئات التالية أيضًا مفيدة للعمل مع العناصر:

- [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)
- [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/watermarkartifact/)

## العمل مع العلامات المائية الموجودة

تسمى العلامة المائية التي تم إنشاؤها باستخدام Adobe Acrobat عنصرًا (كما هو موضح في 14.8.2.2 المحتوى الحقيقي والعناصر في مواصفة PDF).

للحصول على جميع العلامات المائية في صفحة معينة، تحتوي فئة [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) على خاصية Artifacts.

تظهر مقتطفات الكود التالية كيفية الحصول على جميع العلامات المائية في الصفحة الأولى من ملف PDF.

_ملاحظة:_ يعمل هذا الكود أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractWatermarkFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample-w.pdf"))
    {
        // Get the watermarks from the first page artifacts
        var watermarks = document.Pages[1].Artifacts
            .Where(artifact =>
                artifact.Type == Aspose.Pdf.Artifact.ArtifactType.Pagination
                && artifact.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Watermark);

        // Iterate through the found watermark artifacts and print details
        foreach (Aspose.Pdf.WatermarkArtifact item in watermarks.Cast<Aspose.Pdf.WatermarkArtifact>())
        {
            Console.WriteLine($"{item.Text} {item.Rectangle}");
        }
    }
}
```

## العمل مع الخلفيات كعناصر

يمكن استخدام الصور الخلفية لإضافة علامة مائية، أو تصميم دقيق آخر، إلى المستندات. في Aspose.PDF for .NET، كل مستند PDF هو مجموعة من الصفحات وكل صفحة تحتوي على مجموعة من العناصر. يمكن استخدام فئة [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) لإضافة صورة خلفية إلى كائن الصفحة.

تظهر مقتطفات الكود التالية كيفية إضافة صورة خلفية إلى صفحات PDF باستخدام كائن BackgroundArtifact.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBackgroundImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Create a new BackgroundArtifact and set the background image
        var background = new Aspose.Pdf.BackgroundArtifact()
        {
            BackgroundImage = File.OpenRead(dataDir + "background.jpg")
        };

        // Add the background image to the first page's artifacts
        document.Pages[1].Artifacts.Add(background);

        // Save PDF document with the added background
        document.Save(dataDir + "SampleArtifactsBackground_out.pdf");
    }
}
```

إذا كنت ترغب، لأي سبب من الأسباب، في استخدام خلفية بلون صلب، يرجى تغيير الكود السابق بالطريقة التالية:

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

 private static void AddBackgroundColorToPDF()
 {
    // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
     {
         // Create a new BackgroundArtifact and set the background color
         var background = new Aspose.Pdf.BackgroundArtifact()
         {
             BackgroundColor = Aspose.Pdf.Color.DarkKhaki
         };

         // Add the background color to the first page's artifacts
         document.Pages[1].Artifacts.Add(background);

         // Save PDF document
         document.Save(dataDir + "SampleArtifactsBackground_out.pdf");
     }
 }
```

## حساب عدد العناصر من نوع معين

لحساب العدد الإجمالي للعناصر من نوع معين (على سبيل المثال، العدد الإجمالي للعلامات المائية)، استخدم الكود التالي:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CountPDFArtifacts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Get pagination artifacts from the first page
        var paginationArtifacts = document.Pages[1].Artifacts
            .Where(artifact => artifact.Type == Aspose.Pdf.Artifact.ArtifactType.Pagination);

        // Count and display the number of each artifact type
        Console.WriteLine("Watermarks: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Watermark));
        Console.WriteLine("Backgrounds: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Background));
        Console.WriteLine("Headers: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Header));
        Console.WriteLine("Footers: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Footer));
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