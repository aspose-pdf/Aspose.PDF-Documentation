---
title: Rotate PDF Pages Using C#
linktitle: Rotate PDF Pages
type: docs
weight: 50
url: /net/rotate-pages/
description: This topic describes how to rotate the page orientation in an existing PDF file programmatically with C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Rotate PDF Pages Using C#",
    "alternativeHeadline": "Effortlessly Rotate PDF Pages with C#",
    "abstract": "The new feature in Aspose.PDF for .NET allows developers to programmatically change the orientation of pages in existing PDF files. Users can effortlessly switch between landscape and portrait modes, ensuring that content fits properly within the new layout, enhancing document usability and presentation",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "236",
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
    "url": "/net/rotate-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/rotate-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "This topic describes how to rotate the page orientation in an existing PDF file programmatically with C#."
}
</script>

This topic describes how to update or change the page orientation of pages in an existing PDF file programmatically with C#.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Change Page Orientation

From Aspose.PDF for .NET 9.6.0 release, we have added great new features like changing the page orientation from landscape to portrait and vice versa. To change the page orientation, set the page's MediaBox using the following code snippet. You can also change page orientation by setting rotation angle using Rotate() method.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePageOrientation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    //Open document
    using (var document = new Aspose.Pdf.Document(dataDir + "RotatePagesInput.pdf"))
    {
        foreach (Page page in document.Pages)
        {
            Aspose.Pdf.Rectangle r = page.MediaBox;
            double newHeight = r.Width;
            double newWidth = r.Height;
            double newLLX = r.LLX;
            //  We must to move page upper in order to compensate changing page size
            // (lower edge of the page is 0,0 and information is usually placed from the
            //  Top of the page. That's why we move lover edge upper on difference between
            //  Old and new height.
            double newLLY = r.LLY + (r.Height - newHeight);
            page.MediaBox = new Aspose.Pdf.Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight);
            // Sometimes we also need to set CropBox (if it was set in original file)
            page.CropBox = new Aspose.Pdf.Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight);
            // Setting Rotation angle of page
            page.Rotate = Rotation.on90;
        }
        // Save output file
        document.Save(dataDir + "ChangeOrientation_out.pdf");
    }
}
```

## Fitting the Page Content to the New Page Orientation

Please note that when using the above code snippet, some of the document's content might be cut because the page height is decreased. To avoid this, increase width proportionally and leave the height intact. Example of calculations:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FittingThePageContentToTheNewPageOrientation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    //Open document
    using (var document = new Aspose.Pdf.Document(dataDir + "RotatePagesInput.pdf"))
    {
        foreach (Page page in document.Pages)
        {
            Aspose.Pdf.Rectangle r = page.MediaBox;
            // New height the same
            double newHeight = r.Height;
            // New width is expanded proportionally to make orientation landscape
            // (we assume that previous orientation is portrait)
            double newWidth = r.Height * r.Height / r.Width;
        }
    }
}
```

Besides the above approach, consider using the PdfPageEditor facade which can apply zoom to the page contents).

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ZoomToPageContents()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    //Open document
    using (var document = new Aspose.Pdf.Document(dataDir + "RotatePagesInput.pdf"))
    {
        // Get rectangular region of first page of PDF
        Aspose.Pdf.Rectangle rect = document.Pages[1].Rect;
        // Instantiate PdfPageEditor instance
        var pdfPageEditor = new Aspose.Pdf.Facades.PdfPageEditor();
        // Bind source PDF
        pdfPageEditor.BindPdf(dataDir + "RotatePagesInput.pdf");
        // Set zoom coefficient
        pdfPageEditor.Zoom = (float)(rect.Width / rect.Height);
        // Update page size
        pdfPageEditor.PageSize = new Aspose.Pdf.PageSize((float)rect.Height, (float)rect.Width);
        // Save output file
        document.Save(dataDir + "ZoomToPageContents_out.pdf");
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
