---
title: Control Exception PDF File
type: docs
ai_search_scope: pdfnet
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /net/control-exception/
description: Learn how to handle exceptions in PDF processing and ensure smooth operations while working with PDFs using Aspose.PDF in .NET.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Control Exception PDF File",
    "alternativeHeadline": "Manage PDF Exception Handling with New Security Control",
    "abstract": "The Control Exception feature in the PdfFileSecurity class allows you to manage error handling when decrypting PDF files by toggling the AllowExceptions property. Users can choose between receiving boolean results for decryption success or utilizing try-catch blocks for comprehensive exception management, enhancing flexibility and control over PDF security operations",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "224",
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
    "url": "/net/control-exception/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/control-exception/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

[PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) class allows you to control exceptions. To do this, you need to set [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) property to false or true. If you set the operation to false, the result of [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) will return true or false depending on the correctness of the password. 

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ControlExceptionPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "sample_encrypted.pdf");
        // Disallow exceptions
        fileSecurity.AllowExceptions = false;
        
        // Decrypt PDF document
        if (!fileSecurity.DecryptFile("IncorrectPassword"))
        {
            Console.WriteLine("Something wrong...");
            Console.WriteLine($"Last exception: {fileSecurity.LastException.Message}");
        }
        // Save PDF document
        fileSecurity.Save(dataDir + "SampleDecrtypted_out.pdf");
    }
}
```

If you set [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) property to true, then you can get the result of the operation using the try-catch operator.


```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ControlExceptionPDFFile2()
{   
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "sample_encrypted.pdf");
        // Allow exceptions
        fileSecurity.AllowExceptions = true;
        try
        {
            // Decrypt PDF document
            fileSecurity.DecryptFile("IncorrectPassword");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Something wrong...");
            Console.WriteLine($"Exception: {ex.Message}");
        }
        // Save PDF document
        fileSecurity.Save(dataDir + "SampleDecrtypted_out.pdf");
    }
}
```