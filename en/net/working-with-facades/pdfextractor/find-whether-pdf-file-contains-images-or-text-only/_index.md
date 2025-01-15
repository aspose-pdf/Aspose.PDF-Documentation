---
title: Find whether PDF contains images or text
linktitle: Check presence text and images
type: docs
weight: 40
url: /net/find-whether-pdf-file-contains-images-or-text-only/
description: This topic explain how to find whether PDF file contains images or text only with PdfExtractor Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Find whether PDF contains images or text",
    "alternativeHeadline": "Determine PDF Content: Text, Images, or Both",
    "abstract": "Discover the functionality that allows users to efficiently determine whether a PDF file contains text, images, or both, using the PdfExtractor Class. This feature simplifies the process of analyzing PDF content, providing clear output on the presence of text and images within the file. With just a few lines of code, users can effectively classify their PDF documents based on content type",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "265",
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
    "url": "/net/find-whether-pdf-file-contains-images-or-text-only/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/find-whether-pdf-file-contains-images-or-text-only/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Background

A PDF file can contain both text and images. Sometimes, a user might need to find out whether a PDF file contains only text, or it contains only images. We can also find whether it contain both or none.

{{% alert color="primary" %}}

Following code snippet shows you how to fulfill this requirement.

{{% /alert %}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckIfPdfContainsTextOrImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Instantiate a memoryStream object to hold the extracted text from Document
    MemoryStream ms = new MemoryStream();
    // Create the PdfExtractor
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind the input PDF document to extractor
        extractor.BindPdf(dataDir + "FilledForm.pdf");
        // Extract text from the input PDF document
        extractor.ExtractText();
        // Save the extracted text to a text file
        extractor.GetText(ms);
        // Check if the MemoryStream length is greater than or equal to 1

        bool containsText = ms.Length >= 1;

        // Extract images from the input PDF document
        extractor.ExtractImage();

        // Calling HasNextImage method in while loop. When images will finish, loop will exit
        bool containsImage = extractor.HasNextImage();

        // Now find out whether this PDF is text only or image only

        if (containsText && !containsImage)
        {
            Console.WriteLine("PDF contains text only");
        }
        else if (!containsText && containsImage)
        {
            Console.WriteLine("PDF contains image only");
        }
        else if (containsText && containsImage)
        {
            Console.WriteLine("PDF contains both text and image");
        }
        else if (!containsText && !containsImage)
        {
            Console.WriteLine("PDF contains neither text or nor image");
        }
    }
}
```
