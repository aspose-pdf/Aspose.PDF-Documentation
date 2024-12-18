---
title: Create Links in PDF file with C#
linktitle: Create Links
type: docs
weight: 10
url: /net/create-links/
description: This section explains how to create links in your PDF document with C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create Links in PDF file with C#",
    "alternativeHeadline": "Create Interactive Links in PDFs Using C#",
    "abstract": "The new feature allows developers to seamlessly create interactive links within PDF documents using C#. This functionality enhances user engagement by linking to external applications or other PDF files, enabling a more dynamic and feature-rich document experience. Ideal for tutorials and guiding users, this integration empowers users to connect content effectively",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Create Links, PDF document, C#, LinkAnnotation, LaunchAction, GoToRemoteAction, Aspose.PDF, Document object, PDF manipulation, External link",
    "wordcount": "690",
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
    "url": "/net/create-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-links/"
    },
    "dateModified": "2024-11-25",
    "description": "This section explains how to create links in your PDF document with C#."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Create Links

By adding a link to an application into a document, it is possible to link to applications from a document. This is useful when you want readers to take a certain action at a specific point in a tutorial, for example, or to create a feature-rich document. To create an application link:

1. [Create a Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object.
1. Get the [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) you want to add link to.
1. Create a [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) object using the Page and [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) objects.
1. Set the link attributes using the [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) object.
1. Also, set the to [LaunchAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/launchaction) object's Action property.
1. When creating the [LaunchAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/launchaction) object, specify the application you want to launch.
1. Add the link to the Page object's [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/annotations) property.
1. Finally, save the updated PDF using the Document object's [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method.

The following code snippet shows how to create a link to an application in a PDF file.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void CreateLinkAnnotation()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open document
    using (var document = new Aspose.Pdf.Document(dataDir + "CreateApplicationLink.pdf"))
    {
        // Create link
        Aspose.Pdf.Page page = document.Pages[1];
        Aspose.Pdf.Annotations.LinkAnnotation link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
        link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
        link.Action = new Aspose.Pdf.Annotations.LaunchAction(document, dataDir + "CreateApplicationLink.pdf");
        page.Annotations.Add(link);

        // Save updated document
        document.Save(dataDir + "CreateApplicationLink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void CreateLinkAnnotation()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open document
    using var document = new Aspose.Pdf.Document(dataDir + "CreateApplicationLink.pdf");

    // Create link
    var page = document.Pages[1];
    Aspose.Pdf.Annotations.LinkAnnotation link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
    link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
    link.Action = new Aspose.Pdf.Annotations.LaunchAction(document, dataDir + "CreateApplicationLink.pdf");
    page.Annotations.Add(link);

    // Save updated document
    document.Save(dataDir + "CreateApplicationLink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### Create PDF Document Link in a PDF File

Aspose.PDF for .NET allows you to add a link to an external PDF file so that you can link several documents together. To create a PDF document link:

1. First, create a [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object.
1. Then, get the particular [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) you want to add the link to.
1. Create a [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) object using the Page and [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) objects.
1. Set the link attributes using the [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) object.
1. Set the Action property to the [GoToRemoteAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoremoteaction) object.
1. While creating the GoToRemoteAction object, specify the PDF file that should launch, as well as the page number it should open on.
1. Add the link to the Page object's Annotations collection.
1. Save the updated PDF using the Document object's [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method.

The following code snippet shows how to create PDF document link in a PDF file.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void CreateLinkAnnotation()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open document
    using (var document = new Aspose.Pdf.Document(dataDir + "CreateDocumentLink.pdf"))
    {
        // Create link
        var page = document.Pages[1];
        var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
        link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
        link.Action = new Aspose.Pdf.Annotations.GoToRemoteAction(dataDir + "RemoveOpenAction.pdf", 1);
        page.Annotations.Add(link);

        // Save updated document
        document.Save(dataDir + "CreateDocumentLink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void CreateLinkAnnotation()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open document
    using var document = new Aspose.Pdf.Document(dataDir + "CreateDocumentLink.pdf");

    // Create link
    var page = document.Pages[1];
    var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
    link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
    link.Action = new Aspose.Pdf.Annotations.GoToRemoteAction(dataDir + "RemoveOpenAction.pdf", 1);
    page.Annotations.Add(link);

    // Save updated document
    document.Save(dataDir + "CreateDocumentLink_out.pdf");
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
