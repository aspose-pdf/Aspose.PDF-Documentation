---
title: Set PDF File Information
type: docs
weight: 40
url: /net/set-pdf-file-information/
description: This section explains how to set PDF File Information with Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set PDF File Information",
    "alternativeHeadline": "Set Custom Metadata for PDF Files Effortlessly",
    "abstract": "Enhance your PDF file management with the new functionality in Aspose.PDF for .NET that allows you to easily set and update file-specific information such as Author, Title, and Keywords. Utilize the PdfFileInfo class to efficiently modify your PDFs, adding valuable metadata to improve organization and searchability. Streamline your workflow by saving these updates seamlessly with the SaveNewInfo method",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "251",
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
    "url": "/net/set-pdf-file-information/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-pdf-file-information/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

[PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) class allows you to set file specific information of a PDF file. You need to create an object of [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) class and then set different file specific properties like Author, Title, Keyword, and Creator etc. Finally, save the updated PDF file using [SaveNewInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileinfo/savenewinfo/methods/1) method of the [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) object.

The following code snippet shows you how to set PDF file information.

```csharp
private static void SetPdfInfo()
{
    // Define the directory for input and output files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PdfFileInfo object to work with PDF metadata
    var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample.pdf")
    {
        // Set PDF information
        Author = "Aspose",
        Title = "Hello World!",
        Keywords = "Peace and Development",
        Creator = "Aspose"
    };

    // Save the PDF with updated information
    fileInfo.SaveNewInfo(dataDir + "SetFileInfo_out.pdf");
}
```

## Set Meta Info

[SetMetaInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/methods/setmetainfo) method allows you to add any information. In our example, we added a field. Check next code snippet:

```csharp
private static void SetMetaInfo()
{
    // Define the directory for input and output files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of the PdfFileInfo object
    var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample.pdf");

    // Set a new custom attribute as meta info
    fileInfo.SetMetaInfo("Reviewer", "Aspose.PDF user");

    // Save the updated file
    fileInfo.SaveNewInfo(dataDir + "SetMetaInfo_out.pdf");
}
```