---
title: Working with Artifacts in .NET
linktitle: Working with Artifacts
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 170
url: /net/artifacts/
description: Aspose.PDF for .NET allows you to add a background image to PDF pages, and get each watermark using Artifact class.
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
    "abstract": "Aspose.PDF for .NET introduces the Artifact class, enabling developers to seamlessly manage non-content elements like background images and watermarks in PDF documents. This feature enhances document accessibility and performance by allowing assistive technologies to ignore decorative elements, while providing customizable options for various artifact types and properties",
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
    "description": "Aspose.PDF for .NET allows you to add a background image to PDF pages,  and get each watermark using Artifact class."
}
</script>

Artifacts in PDF are graphics objects or other elements that are not part of the actual content of the document. They are usually used for decoration, layout, or background purposes. Examples of artifacts include page headers, footers, separators, or images that do not convey any meaning.

The purpose of artifacts in PDF is to allow the distinction between content and non-content elements. This is important for accessibility, as screen readers and other assistive technologies can ignore artifacts and focus on the relevant content. Artifacts can also improve the performance and quality of PDF documents, as they can be omitted from printing, searching, or copying.

To create an element as an artifact in PDF, you need to use the [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) class.
It contains following useful properties:

- **Artifact.Type** – gets the artifact type (supports values of the Artifact.ArtifactType enumeration where values include Background, Layout, Page, Pagination and Undefined).
- **Artifact.Subtype** – gets artifact subtype (supports the values of the Artifact.ArtifactSubtype enumeration where values include Background, Footer, Header, Undefined, Watermark).
- **Artifact.Image** – Gets an artifact's image (if an image is presents, else null).
- **Artifact.Text** – Gets an artifact's text.
- **Artifact.Contents** – Gets a collection of artifact internal operators. Its supported type is System.Collections.ICollection.
- **Artifact.Form** – Gets an artifact's XForm (if XForm is used). Watermarks, header, and footer artifacts contains XForm which shows all artifact contents.
- **Artifact.Rectangle** – Gets an position of an artifact on the page.
- **Artifact.Rotation** – Gets an artifact's rotation (in degrees, positive value indicates counter-clockwise rotation).
- **Artifact.Opacity** – Gets an artifact's opacity. Possible values are in the range 0...1, where 1 is completely opaque.

The following classes may also be useful for work with artifacts:

- [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)
- [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/watermarkartifact/)

## Working with Existing Watermarks

A watermark created with Adobe Acrobat is called an artifact (as described in 14.8.2.2 Real Content and Artifacts of the PDF specification). 

In order to get all Watermarks on a particular page, the [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) class has the Artifacts property.

The following code snippet shows how to get all watermarks on the first page of a PDF file.

_Note:_ This code also works with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

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

Background images can be used to add a watermark, or other subtle design, to documents. In Aspose.PDF for .NET, each PDF document is a collection of pages and each page contains a collection of artifacts. The [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) class can be used to add a background image to a page object.

The following code snippet shows how to add a background image to PDF pages using the BackgroundArtifact object.

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

If you want, for some reason, to use a solid color background, please change the previous code in the following manner:

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

To calculate the total count of artifacts of a particular type (for example, the total number of watermarks), use the following code:

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

To add a Bates numbering artifact to a document, call the ```AddBatesNumbering(BatesNArtifact batesNArtifact)``` extension method on the ```PageCollection```, passing the ```BatesNArtifact``` object as a parameter:

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

Or, you can pass a collection of ```PaginationArtifacts```:

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

Alternatively, you can add a Bates numbering artifact using an action delegate:

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

To delete Bates numbering, use the following code:

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
