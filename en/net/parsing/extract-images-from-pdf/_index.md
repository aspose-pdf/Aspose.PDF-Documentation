---
title: Extract Images from PDF C#
linktitle: Extract Images from PDF
type: docs
weight: 20
url: /net/extract-images-from-the-pdf-file/
description: How to extract a part of the image from PDF using Aspose.PDF for .NET in C#
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images from PDF C#",
    "alternativeHeadline": "Effortlessly Extract Images from PDF Files in C#",
    "abstract": "Unlock the power of Aspose.PDF for .NET with the new functionality to extract images from PDF files directly in C#. This feature allows users to easily retrieve and save images from specific pages, facilitating efficient image management and processing in .NET applications",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "240",
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
    "url": "/net/extract-images-from-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-images-from-the-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

Images are held in each page's [Resources](https://reference.aspose.com/pdf/net/aspose.pdf/resources) collection's [Images](https://reference.aspose.com/pdf/net/aspose.pdf/resources/properties/images) collection. To extract a particular page, then get the image from the Images collection using the particular index of the image.

The image's index returns an [XImage](https://reference.aspose.com/pdf/net/aspose.pdf/ximage) object. This object provides a Save method which can be used to save the extracted image. The following code snippet shows how to extract images from a PDF file.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ExtractImagesFromPDF()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open the document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractImages.pdf"))
    {
        // Extract a particular image
        var xImage = document.Pages[1].Resources.Images[1];

        using (var outputImage = new FileStream(dataDir + "outputImage.jpg", FileMode.Create))
        {
            // Save the output image
            xImage.Save(outputImage, ImageFormat.Jpeg);
        }

        // Save the document
        document.Save(dataDir + "ExtractImages_out.pdf");
    }
}
```
