---
title: Add Image stamps in PDF using C#
linktitle: Image stamps in PDF File
type: docs
weight: 10
url: /net/image-stamps-in-pdf-page/
description: Add the Image Stamp in your PDF document using ImageStamp class with the Aspose.PDF library.
lastmod: "2024-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Image stamps in PDF using C#",
    "alternativeHeadline": "Add Custom Image Stamps to PDF Documents",
    "abstract": "The new feature in the Aspose.PDF library allows users to seamlessly add image stamps to PDF documents using C#. With the ImageStamp class, developers can customize attributes such as size, opacity, and quality, significantly enhancing document presentation and accessibility. This functionality also includes the ability to add alternative text, promoting better usability for screen readers",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "646",
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
    "url": "/net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2024-11-26",
    "description": "Add the Image Stamp in your PDF document using ImageStamp class with the Aspose.PDF library."
}
</script>


## Add Image Stamp in PDF File

You can use the ImageStamp class to add an image stamp to a PDF file. The ImageStamp class provides the properties necessary for creating an image-based stamp, such as height, width, opacity and so on.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

To add an image stamp:

1. Create a Document object and an ImageStamp object using required properties.
1. Call the Page class’ AddStamp method to add the stamp to the PDF.

The following code snippet shows how to add image stamp in the PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampInPdfFile()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    // Open document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create image stamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg");
        imageStamp.Background = true;
        imageStamp.XIndent = 100;
        imageStamp.YIndent = 100;
        imageStamp.Height = 300;
        imageStamp.Width = 300;
        imageStamp.Rotate = Rotation.on270;
        imageStamp.Opacity = 0.5;
        // Add stamp to particular page
        document.Pages[1].AddStamp(imageStamp);
        // Save document
        document.Save(dataDir + "AddImageStamp_out.pdf");
    }
}
```

## Control Image Quality when Adding Stamp

When adding an image as a stamp object, you can control the quality of the image. The Quality property of the ImageStamp class is used for this purpose. It indicates the quality of image in percents (valid values are 0..100).

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ControlImageQualityWhenAddingStamp()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    // Open document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create image stamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg");
        imageStamp.Quality = 10;
        document.Pages[1].AddStamp(imageStamp);
        document.Save(dataDir + "ControlImageQuality_out.pdf");
    }
}
```

## Image Stamp as Background in Floating Box

Aspose.PDF API lets you add image stamp as background in a floating box. The BackgroundImage property of FloatingBox class can be used to set the background image stamp for a floating box as shown in following code sample.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImageStampAsBackgroundInFloatingBox()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    // Instantiate Document object
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to PDF document
        Page page = document.Pages.Add();
        // Create FloatingBox object
        var aBox = new Aspose.Pdf.FloatingBox(200, 100);
        // Set left position for FloatingBox
        aBox.Left = 40;
        // Set Top position for FloatingBox
        aBox.Top = 80;
        // Set the Horizontal alignment for FloatingBox
        aBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        // Add text fragment to paragraphs collection of FloatingBox
        aBox.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("main text"));
        // Set border for FloatingBox
        aBox.Border = new Aspose.Pdf.BorderInfo(BorderSide.All, Aspose.Pdf.Color.Red);
        // Add background image
        aBox.BackgroundImage = new Aspose.Pdf.Image
        {
            File = dataDir + "aspose-logo.jpg"
        };
        // Set background color for FloatingBox
        aBox.BackgroundColor = Aspose.Pdf.Color.Yellow;
        // Add FloatingBox to paragraphs collection of page object
        page.Paragraphs.Add(aBox);
        // Save document
        document.Save(dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
    }
}
```

## Add alternative text to the image stamp

Since version 24.6, it is possible to add alternative text to the image stamp.

This code opens a PDF file, adds an image as a stamp at a specific position, and includes alternative text for accessibility. The updated PDF is then saved with a new filename.

```cs
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAlternativeTextToTheImageStamp()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    // Open document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create image stamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "yourImage.jpg")
        {
            XIndent = 100,
            YIndent = 700,
            Quality = 100,
            AlternativeText = "Your alt text"  // This property added.
        };
        // Add stamp
        document.Pages[1].AddStamp(imageStamp);
        // Save document
        document.Save(dataDir + "docWithImageStamp_out.pdf");
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
