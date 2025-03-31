---
title: العمل مع العناصر في .NET
linktitle: العمل مع العناصر
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 170
url: /ar/net/artifacts/
description: يسمح Aspose.PDF لـ .NET بإضافة صورة خلفية إلى صفحات PDF، والحصول على كل علامة مائية باستخدام فئة Artifact.
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
    "alternativeHeadline": "Enhance PDF Documents with Artifacts Management",
    "abstract": "تقدم Aspose.PDF لـ .NET فئة Artifact، مما يمكّن المطورين من إدارة العناصر غير المحتوى مثل الصور الخلفية وعلامات الماء بسلاسة في مستندات PDF. تعزز هذه الميزة إمكانية الوصول إلى المستندات والأداء من خلال السماح للتقنيات المساعدة بتجاهل العناصر الزخرفية، مع توفير خيارات قابلة للتخصيص لمختلف أنواع وخصائص العناصر.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2501",
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
    "dateModified": "2025-03-12",
    "description": "يسمح Aspose.PDF لـ .NET بإضافة صورة خلفية إلى صفحات PDF، والحصول على كل علامة مائية باستخدام فئة Artifact."
}
</script>

Artifacts in PDF هي كائنات رسومية أو عناصر أخرى ليست جزءًا من المحتوى الفعلي للمستند. عادةً ما تُستخدم لأغراض الزينة أو التخطيط أو كخلفية. تشمل أمثلة Artifacts رؤوس الصفحات، وتذييلها، والفواصل، أو الصور التي لا تنقل أي معنى.

الغرض من Artifacts في PDF هو التمييز بين عناصر المحتوى وغير المحتوى. وهذا مهم لإمكانية الوصول، حيث يمكن لبرامج قارئات الشاشة والتقنيات المساعدة تجاهل Artifacts والتركيز على المحتوى ذي الصلة. كما يمكن أن تحسن Artifacts من أداء وجودة مستندات PDF، إذ يمكن حذفها عند الطباعة أو البحث أو النسخ.

لإنشاء عنصر كـ Artifact في PDF، تحتاج إلى استخدام فئة [Artifact](https://reference.aspose.com/pdf/ar/net/aspose.pdf/artifact).
تحتوي على الخصائص المفيدة التالية:

- **Artifact.Type** – يحصل على نوع Artifact (يدعم القيم من تعداد Artifact.ArtifactType حيث تشمل القيم Background، Layout، Page، Pagination و Undefined).
- **Artifact.Subtype** – يحصل على النوع الفرعي لـ Artifact (يدعم القيم من تعداد Artifact.ArtifactSubtype حيث تشمل القيم Background، Footer، Header، Undefined، Watermark).
- **Artifact.Image** – يحصل على صورة Artifact (إذا كانت الصورة موجودة، وإلا null).
- **Artifact.Text** – يحصل على نص Artifact.
- **Artifact.Contents** – يحصل على مجموعة من العمليات الداخلية لـ Artifact. النوع المدعوم هو System.Collections.ICollection.
- **Artifact.Form** – يحصل على XForm لـ Artifact (إذا تم استخدام XForm). تحتوي Artifacts الخاصة بـ Watermarks و header و footer على XForm تُظهر جميع محتويات Artifact.
- **Artifact.Rectangle** – يحصل على موضع Artifact في الصفحة.
- **Artifact.Rotation** – يحصل على دوران Artifact (بالدرجات؛ حيث تشير القيمة الموجبة إلى دوران عكس اتجاه عقارب الساعة).
- **Artifact.Opacity** – يحصل على شفافية Artifact. القيم الممكنة تتراوح من 0 إلى 1، حيث يعني 1 شفافية كاملة.

الفئات التالية قد تكون مفيدة أيضًا للعمل مع Artifacts:

- [ArtifactCollection](https://reference.aspose.com/pdf/ar/net/aspose.pdf/artifactcollection)
- [BackgroundArtifact](https://reference.aspose.com/pdf/ar/net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/ar/net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/ar/net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/ar/net/aspose.pdf/watermarkartifact/)

## Working with Existing Watermarks

العلامة المائية المُنشأة باستخدام Adobe Acrobat تُسمى Artifact (كما هو موضح في 14.8.2.2 Real Content and Artifacts من مواصفات PDF).

للحصول على جميع العلامات المائية على صفحة معينة، تحتوي فئة [Page](https://reference.aspose.com/pdf/ar/net/aspose.pdf/page) على خاصية Artifacts.

تُظهر الشيفرة التالية كيفية الحصول على جميع العلامات المائية في الصفحة الأولى من ملف PDF.

_Note:_ تعمل هذه الشيفرة أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/) library.

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

## Working with Backgrounds as Artifacts

يمكن استخدام الصور الخلفية لإضافة علامة مائية أو تصميم دقيق إلى المستندات. في Aspose.PDF for .NET، كل مستند PDF عبارة عن مجموعة من الصفحات، وتحتوي كل صفحة على مجموعة من Artifacts. يمكن استخدام فئة [BackgroundArtifact](https://reference.aspose.com/pdf/ar/net/aspose.pdf/backgroundartifact) لإضافة صورة خلفية إلى كائن الصفحة.

تُظهر الشيفرة التالية كيفية إضافة صورة خلفية إلى صفحات PDF باستخدام كائن BackgroundArtifact.

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

إذا كنت ترغب، لأي سبب من الأسباب، في استخدام خلفية بلون ثابت، يرجى تغيير الشيفرة السابقة على النحو التالي:

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

## Counting Artifacts of a Particular Type

لحساب العدد الإجمالي لـ Artifacts من نوع معين (على سبيل المثال، العدد الإجمالي للعلامات المائية)، استخدم الشيفرة التالية:

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

## Adding Bates Numbering Artifact

لإضافة Bates numbering artifact إلى المستند، استدعِ طريقة التمديد ```AddBatesNumbering(BatesNArtifact batesNArtifact)``` على ```PageCollection```، مع تمرير كائن ```BatesNArtifact``` كمعامل:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBatesNArtifact()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create or open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add 10 pages
        for (int i = 0; i < 10; i++)
        {
            document.Pages.Add();
        }

        // Add Bates numbering to all pages
        document.Pages.AddBatesNumbering(new BatesNArtifact
        {
            // These properties are set to their default values, as if they were not specified
            StartPage = 1,
            EndPage = 0,
            Subset = Subset.All,
            NumberOfDigits = 6,
            StartNumber = 1,
            Prefix = "",
            Suffix = "",
            ArtifactVerticalAlignment = VerticalAlignment.Bottom,
            ArtifactHorizontalAlignment = HorizontalAlignment.Right,
            RightMargin = 72,
            LeftMargin = 72,
            TopMargin = 36,
            BottomMargin = 36
        });

        // Save PDF document
        document.Save(dataDir + "SampleBatesNArtifact_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// The path to the documents directory
var dataDir = RunExamples.GetDataDir_AsposePdf();

// Create or open PDF document
using var document = new Aspose.Pdf.Document();

// Add 10 pages
for (int i = 0; i < 10; i++)
{
    document.Pages.Add();
}

// Add Bates numbering to all pages
document.Pages.AddBatesNumbering(new BatesNArtifact
{
    // These properties are set to their default values, as if they were not specified
    StartPage = 1,
    EndPage = 0,
    Subset = Subset.All,
    NumberOfDigits = 6,
    StartNumber = 1,
    Prefix = "",
    Suffix = "",
    ArtifactVerticalAlignment = VerticalAlignment.Bottom,
    ArtifactHorizontalAlignment = HorizontalAlignment.Right,
    RightMargin = 72,
    LeftMargin = 72,
    TopMargin = 36,
    BottomMargin = 36
});

// Save PDF document
document.Save(dataDir + "SampleBatesNArtifact_out.pdf");
```
{{< /tab >}}
{{< /tabs >}}

أو، يمكنك تمرير مجموعة من ```PaginationArtifacts```:

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBatesNArtifact()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create or open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add 10 pages
        for (int i = 0; i < 10; i++)
        {
            document.Pages.Add();
        }

        // Add Bates numbering to all pages
        document.Pages.AddPagination(new List<Aspose.Pdf.PaginationArtifact>
        {
            new Aspose.Pdf.BatesNArtifact
            {
                // These properties are set to their default values, as if they were not specified
                StartPage = 1,
                EndPage = 0,
                Subset = Subset.All,
                NumberOfDigits = 6,
                StartNumber = 1,
                Prefix = "",
                Suffix = "",
                ArtifactVerticalAlignment = VerticalAlignment.Bottom,
                ArtifactHorizontalAlignment = HorizontalAlignment.Right,
                RightMargin = 72,
                LeftMargin = 72,
                TopMargin = 36,
                BottomMargin = 36
            }
        });

        // Save PDF document
        document.Save(dataDir + "SampleBatesNArtifact_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBatesNArtifact()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create or open PDF document
    using var document = new Aspose.Pdf.Document();

    // Add 10 pages
    for (int i = 0; i < 10; i++)
    {
        document.Pages.Add();
    }

    // Add Bates numbering to all pages
    document.Pages.AddPagination(new List<Aspose.Pdf.PaginationArtifact>
    {
        new Aspose.Pdf.BatesNArtifact
        {
            // These properties are set to their default values, as if they were not specified
            StartPage = 1,
            EndPage = 0,
            Subset = Subset.All,
            NumberOfDigits = 6,
            StartNumber = 1,
            Prefix = "",
            Suffix = "",
            ArtifactVerticalAlignment = VerticalAlignment.Bottom,
            ArtifactHorizontalAlignment = HorizontalAlignment.Right,
            RightMargin = 72,
            LeftMargin = 72,
            TopMargin = 36,
            BottomMargin = 36
        }
    });

    // Save PDF document
    document.Save(dataDir + "SampleBatesNArtifact_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

بدلاً من ذلك، يمكنك إضافة Bates numbering artifact باستخدام مُفوَّض فعل:

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBatesNArtifact()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create or open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add 10 pages
        for (int i = 0; i < 10; i++)
        {
            document.Pages.Add();
        }

        // Add Bates numbering to all pages
        document.Pages.AddBatesNumbering(batesN =>
        {
            // These properties are set to their default values, as if they were not specified
            batesN.StartPage = 1;
            batesN.EndPage = 0;
            batesN.Subset = Subset.All;
            batesN.NumberOfDigits = 6;
            batesN.StartNumber = 1;
            batesN.Prefix = "";
            batesN.Suffix = "";
            batesN.ArtifactVerticalAlignment = VerticalAlignment.Bottom;
            batesN.ArtifactHorizontalAlignment = HorizontalAlignment.Right;
            batesN.ArtifactVerticalAlignment = VerticalAlignment.Bottom;
            batesN.RightMargin = 72;
            batesN.LeftMargin = 72;
            batesN.TopMargin = 36;
            batesN.BottomMargin = 36;
            batesN.TextState.FontSize = 10;
        });

        // Save PDF document
        document.Save(dataDir + "SampleBatesNArtifact_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBatesNArtifact()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create or open PDF document
    using var document = new Aspose.Pdf.Document();

    // Add 10 pages
    for (int i = 0; i < 10; i++)
    {
        document.Pages.Add();
    }

    // Add Bates numbering to all pages
    document.Pages.AddBatesNumbering(batesN =>
    {
        // These properties are set to their default values, as if they were not specified
        batesN.StartPage = 1;
        batesN.EndPage = 0;
        batesN.Subset = Subset.All;
        batesN.NumberOfDigits = 6;
        batesN.StartNumber = 1;
        batesN.Prefix = "";
        batesN.Suffix = "";
        batesN.ArtifactVerticalAlignment = VerticalAlignment.Bottom;
        batesN.ArtifactHorizontalAlignment = HorizontalAlignment.Right;
        batesN.ArtifactVerticalAlignment = VerticalAlignment.Bottom;
        batesN.RightMargin = 72;
        batesN.LeftMargin = 72;
        batesN.TopMargin = 36;
        batesN.BottomMargin = 36;
        batesN.TextState.FontSize = 10;
    });

    // Save PDF document
    document.Save(dataDir + "SampleBatesNArtifact_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

لحذف Bates numbering، استخدم الشيفرة التالية:

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteBatesNArtifacts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SampleBatesNArtifact_out.pdf"))
    {
        // Delete Bates numbering from all pages
        document.Pages.DeleteBatesNumbering();

        //Save PDF document
        document.Save(dataDir + "DeleteBatesNArtifacts_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteBatesNArtifacts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "SampleBatesNArtifact_out.pdf");

    // Delete Bates numbering from all pages
    document.Pages.DeleteBatesNumbering();

    //Save PDF document
    document.Save(dataDir + "DeleteBatesNArtifacts_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

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