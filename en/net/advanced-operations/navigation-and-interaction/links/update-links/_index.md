---
title: Update Links in PDF
linktitle: Update Links
type: docs
weight: 20
url: /net/update-links/
description: Update links in PDF programmatically. This guide is about how to update links in PDF in C# language.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Update Links in PDF",
    "alternativeHeadline": "Programmatically Modify PDF Links Using C#",
    "abstract": "The new Update Links in PDF feature allows users to programmatically modify hyperlinks within PDF documents using C#. This functionality enables users to direct links to specific pages, external web addresses, or even other PDF files, enhancing the interactivity and usability of digital documents. By simplifying the link management process, this feature is ideal for developers looking to optimize their PDF applications",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Update links in PDF, C#, LinkAnnotation, GoToAction, XYZExplicitDestination, GoToURIAction, update hyperlink, PDF manipulation",
    "wordcount": "797",
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
    "url": "/net/update-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/update-links/"
    },
    "dateModified": "2024-11-25",
    "description": "Update links in PDF programmatically. This guide is about how to update links in PDF in C# language."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Update Links in PDF File

As discussed in Add Hyperlink in a PDF File, the [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) class makes it possible to add links in a PDF file. There's also a similar class used to get existing links from inside PDF files. Use this if you need to update an existing link. To update an existing link:

1. Load a PDF file.
1. Go to a specific page in the PDF file.
1. Specify the link destination using the [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) object's Destination property.
1. The destination page is specified using the [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) constructor.

### Set Link Target to a Page in the Same Document

The following code snippet shows you how to update a link in a PDF file and set its target to the second page of the document.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Load the PDF file
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf"))
    {
        // Get the first link annotation from first page of document
        var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];

        // Modification link: change link destination
        var goToAction = (Aspose.Pdf.Annotations.GoToAction)linkAnnot.Action;

        // Specify the destination for link object
        // The first parameter is document object, second is destination page number.
        // The 5ht argument is zoom factor when displaying the respective page. When using 2, the page will be displayed in 200% zoom
        goToAction.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 1, 2, 2);

        // Save the document with updated link
        document.Save(dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Load the PDF file
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf");

    // Get the first link annotation from first page of document
    var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];

    // Modification link: change link destination
    var goToAction = (Aspose.Pdf.Annotations.GoToAction)linkAnnot.Action;

    // Specify the destination for link object
    // The first parameter is document object, second is destination page number.
    // The 5ht argument is zoom factor when displaying the respective page. When using 2, the page will be displayed in 200% zoom
    goToAction.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 1, 2, 2);

    // Save the document with updated link
    document.Save(dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### Set Link Destination to a Web Address

To update the hyperlink so that it points to a web address, instantiate the [GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) object and pass it to the LinkAnnotation's Action property. The following code snippet shows how to update a link in a PDF file and set its target to a web address.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Load the PDF file
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf"))
    {
        // Get the first link annotation from first page of document
        var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];

        // Modification link: change link action and set target as web address
        linkAnnot.Action = new Aspose.Pdf.Annotations.GoToURIAction("www.aspose.com");

        // Save the document with updated link
        document.Save(dataDir + "SetDestinationLink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Load the PDF file
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf");

    // Get the first link annotation from first page of document
    var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];

    // Modification link: change link action and set target as web address
    linkAnnot.Action = new Aspose.Pdf.Annotations.GoToURIAction("www.aspose.com");

    // Save the document with updated link
    document.Save(dataDir + "SetDestinationLink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### Set Link Target to Another PDF File

The following code snippet shows how to update a link in a PDF file and set its target to another PDF file.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Load the PDF file
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf"))
    {
        var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];
        var goToR = (Aspose.Pdf.Annotations.GoToRemoteAction)linkAnnot.Action;

        // Next line update destination, do not update file
        goToR.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(2, 0, 0, 1.5);

        // Next line update file
        goToR.File = new Aspose.Pdf.FileSpecification(dataDir + "input.pdf");

        // Save the document with updated link
        document.Save(dataDir + "SetTargetLink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Load the PDF file
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf");

    var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];
    var goToR = (Aspose.Pdf.Annotations.GoToRemoteAction)linkAnnot.Action;

    // Next line update destination, do not update file
    goToR.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(2, 0, 0, 1.5);

    // Next line update file
    goToR.File = new Aspose.Pdf.FileSpecification(dataDir + "input.pdf");

    // Save the document with updated link
    document.Save(dataDir + "SetTargetLink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### Update LinkAnnotation Text Color

The link annotation does not contain text. Instead, the text is placed in the contents of the page under the annotation. Therefore, to change the color of the text, replace the color of the page text instead of trying change color of the annotation. The following code snippet shows how to update the color of link annotation in a PDF file.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Load the PDF file
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf"))
    {
        foreach (var annotation in document.Pages[1].Annotations)
        {
            if (annotation is Aspose.Pdf.Annotations.LinkAnnotation)
            {
                // Search the text under the annotation
                var ta = new Aspose.Pdf.Text.TextFragmentAbsorber();
                var rect = annotation.Rect;
                rect.LLX -= 10;
                rect.LLY -= 10;
                rect.URX += 10;
                rect.URY += 10;
                ta.TextSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(rect);
                ta.Visit(document.Pages[1]);

                // Change color of the text.
                foreach (var textFragment in ta.TextFragments)
                {
                    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
                }
            }
        }

        // Save the document with updated link
        document.Save(dataDir + "UpdateLinkTextColor_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Load the PDF file
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf");

    foreach (var annotation in document.Pages[1].Annotations)
    {
        if (annotation is Aspose.Pdf.Annotations.LinkAnnotation)
        {
            // Search the text under the annotation
            var ta = new Aspose.Pdf.Text.TextFragmentAbsorber();
            var rect = annotation.Rect;
            rect.LLX -= 10;
            rect.LLY -= 10;
            rect.URX += 10;
            rect.URY += 10;
            ta.TextSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(rect);
            ta.Visit(document.Pages[1]);

            // Change color of the text.
            foreach (var textFragment in ta.TextFragments)
            {
                textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
            }
        }
    }

    // Save the document with updated link
    document.Save(dataDir + "UpdateLinkTextColor_out.pdf");
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
