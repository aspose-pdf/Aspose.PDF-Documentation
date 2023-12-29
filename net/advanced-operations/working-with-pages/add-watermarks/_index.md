---
title: Add watermark to PDF using C#
linktitle: Add watermark
type: docs
weight: 90
url: /net/add-watermarks/
description: This article explains the features of working with artifacts and getting watermarks in PDFs using  programmatically the C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/working-with-existing-watermarks/
    - /net/adding-multi-line-watermark-to-existing-pdf/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add watermark to PDF using C#",
    "alternativeHeadline": "How to add watermark to PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, add watermark",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "dateModified": "2022-02-04",
    "description": "This article explains the features of working with artifacts and getting watermarks in PDFs using  programmatically the C#."
}
</script>

**Aspose.PDF for .NET** allows adding watermarks to your PDF document using Artifacts. Please check this article to resolve your task.

The next code snippets also work with a new graphical [Aspose.Drawing](/pdf/net/drawing/) interface.

A watermark created with Adobe Acrobat is called an artifact (as described in 14.8.2.2 Real Content and Artifacts of the PDF specification). In order to work with artifacts, Aspose.PDF has two classes: [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) and [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection).

In order to get all artifacts on a particular page, the [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) class has the Artifacts property. This topic explains how to work with artifact in PDF files.

## Working with Artifacts

The [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) class contains following properties:

**Artifact.Type** – gets the artifact type (supports values of the Artifact.ArtifactType enumeration where values include Background, Layout, Page, Pagination and Undefined).
**Artifact.Subtype** – gets artifact subtype (supports the values of the Artifact.ArtifactSubtype enumeration where values include Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Please note that watermarks created with Adobe Acrobat have the type Pagination and subtype Watermark.

{{% /alert %}}

**Artifact.Contents** – Gets a collection of artifact internal operators. Its supported type is System.Collections.ICollection.
**Artifact.Form** – Gets an artifact’s XForm (if XForm is used). Watermarks, header, and footer artifacts contains XForm which shows all artifact contents.
**Artifact.Image** – Gets an artifact’s image (if an image is presents, else null).
**Artifact.Text** – Gets an artifact’s text.
**Artifact.Rectangle** – Gets an position of an artifact on the page.
**Artifact.Rotation** – Gets an artifact’s rotation (in degrees, positive value indicates counter-clockwise rotation).
**Artifact.Opacity** – Gets an artifact’s opacity. Possible values are in the range 0…1, where 1 is completely opaque.

## Programming Samples: How To Add Watermark On PDF Files

The following code snippet shows how to get each watermark on the first page of a PDF file with C#.

```csharp
public static void AddWatermarks()
{
    Document document = new Document(_dataDir + "text.pdf");
    WatermarkArtifact artifact = new WatermarkArtifact();
    artifact.SetTextAndState(
        "WATERMARK",
        new TextState()
        {
            FontSize = 72,
            ForegroundColor = Color.Blue,
            Font = FontRepository.FindFont("Courier")
        });
    artifact.ArtifactHorizontalAlignment = HorizontalAlignment.Center;
    artifact.ArtifactVerticalAlignment = VerticalAlignment.Center;
    artifact.Rotation = 45;
    artifact.Opacity = 0.5;
    artifact.IsBackground = true;
    document.Pages[1].Artifacts.Add(artifact);
    document.Save(_dataDir + "watermark.pdf");
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
