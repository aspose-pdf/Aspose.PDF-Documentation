---
title: Get PDF file information
type: docs
weight: 50
url: /net/get-pdf-file-information/
description: This section explains how to get PDF File Information with Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get PDF file information",
    "alternativeHeadline": "Retrieve Detailed Information from PDF Files",
    "abstract": "Unlock essential PDF metadata with the new feature that utilizes the PdfFileInfo class from Aspose.PDF for .NET Facades. This functionality allows developers to easily access and retrieve important file-specific details such as Subject, Title, Keywords, and Creator, enhancing document management and analysis processes. Streamline your PDF interactions by leveraging this powerful tool for comprehensive file information retrieval",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "285",
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
    "url": "/net/get-pdf-file-information/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-pdf-file-information/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

In order to get file specific information of a PDF file, you need to create an object of [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) class. After that, you can get values of the individual properties like Subject, Title, Keywords and Creator etc.

The following code snippet shows you how to get PDF file information.

```csharp
public static void GetPdfInfo()
{
    // Open document
    PdfFileInfo fileInfo = new PdfFileInfo(dataDir + "sample.pdf");
    // Get PDF information
    Console.WriteLine("Subject: {0}", fileInfo.Subject);
    Console.WriteLine("Title: {0}", fileInfo.Title);
    Console.WriteLine("Keywords: {0}", fileInfo.Keywords);
    Console.WriteLine("Creator: {0}", fileInfo.Creator);
    Console.WriteLine("Creation Date: {0}", fileInfo.CreationDate);
    Console.WriteLine("Modification Date: {0}", fileInfo.ModDate);
    // Find whether is it valid PDF and it is encrypted as well
    Console.WriteLine("Is Valid PDF: {0}", fileInfo.IsPdfFile);
    Console.WriteLine("Is Encrypted: {0}", fileInfo.IsEncrypted);

    Console.WriteLine("Page width:{0}", fileInfo.GetPageWidth(1));
    Console.WriteLine("Page height:{0}", fileInfo.GetPageHeight(1));
}
```

## Get Meta Info

In order to get information, we use the [Header](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/header) property. With 'Hashtable'  we get all the possible values.

```csharp
public static void GetMetaInfo()
{
    // Create instance of PdfFileInfo object
    Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "SetMetaInfo_out.pdf");
    // Retrieve all existing custom attributes
    Hashtable hTable = new Hashtable(fInfo.Header);

    IDictionaryEnumerator enumerator = hTable.GetEnumerator();
    while (enumerator.MoveNext())
    {
        string output = enumerator.Key.ToString() + " " + enumerator.Value;
        Console.WriteLine(output);
    }

    // Retrieve one custom attributes
    Console.WriteLine(fInfo.GetMetaInfo("Reviewer"));
}
```