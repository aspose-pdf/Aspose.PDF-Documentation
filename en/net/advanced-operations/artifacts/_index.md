---
title: Working with Artifacts in .NET
linktitle: Working with Artifacts
type: docs
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
    "alternativeHeadline": "Add and Manage Artifacts in PDF Documents",
    "abstract": "Aspose.PDF for .NET introduces the Artifact class, allowing developers to efficiently manage non-content elements like background images and watermarks within PDF documents. This functionality enhances document structure while improving accessibility and performance, as artifacts can be ignored by assistive technologies. With customizable options for types and properties, users can easily manipulate these elements to create visually appealing PDFs",
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
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the PDF document
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
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Create a new BackgroundArtifact and set the background image
        var background = new Aspose.Pdf.BackgroundArtifact()
        {
            BackgroundImage = System.IO.File.OpenRead(dataDir + "background.jpg")
        };

        // Add the background image to the first page's artifacts
        document.Pages[1].Artifacts.Add(background);

        // Save the document with the added background
        document.Save(dataDir + "sample_artifacts_background.pdf");
    }
}
```

If you want, for some reason, to use a solid color background, please change the previous code in the following manner:

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddBackgroundColorToPDF()
 {
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Load the PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
     {
         // Create a new BackgroundArtifact and set the background color
         var background = new Aspose.Pdf.BackgroundArtifact()
         {
             BackgroundColor = Aspose.Pdf.Color.DarkKhaki
         };

         // Add the background color to the first page's artifacts
         document.Pages[1].Artifacts.Add(background);

         // Save the document with the applied background color
         document.Save(dataDir + "sample_artifacts_background.pdf");
     }
 }
```

## Counting Artifacts of a Particular Type

To calculate the total count of artifacts of a particular type (for example, the total number of watermarks), use the following code:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CountPDFArtifacts()
{
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the PDF document
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
