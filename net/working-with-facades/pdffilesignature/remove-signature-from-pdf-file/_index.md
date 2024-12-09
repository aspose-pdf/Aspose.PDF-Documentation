---
title: Remove Signature from PDF File
type: docs
weight: 20
url: /net/remove-signature-from-pdf/
description: This section explains how to remove signature from PDF File using PdfFileSignature class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Remove Signature from PDF File",
    "alternativeHeadline": "Effortlessly Remove Signatures from PDF Files",
    "abstract": "The functionality allows users to efficiently remove digital signatures from PDF files using the PdfFileSignature class. This feature provides flexibility, enabling the removal of specific signatures while optionally retaining the signature fields for future use, enhancing document management capabilities",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "434",
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
    "url": "/net/remove-signature-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-signature-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Remove Digital Signature from the PDF File

When a signature has been added to a PDF files, it is possible to remove it. You can remove either a particular signature, or all signatures in a file. The fastest method for removing the signature also removes the signature field, but it is possible to just remove the signature, keeping the signature field so the file can be signed again.

The [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) class RemoveSignature method allows you to remove a signature from a PDF file. This method takes the signature name as an input. Either specify the signature name directly, to remove all signatures, get the signature names using the [GetSignNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/getsignername) method. 

The following code snippet shows how to remove digital signature from the PDF file.

```csharp
public static void RemoveSignature()
{
    // Create PdfFileSignature object
    PdfFileSignature pdfSign = new PdfFileSignature();
    // Open PDF document
    pdfSign.BindPdf(dataDir + "DigitallySign.pdf");
    // Get list of signature names
    var sigNames = pdfSign.GetSignNames();
    // Remove all the signatures from the PDF file
    for (int index = 0; index < sigNames.Count; index++)
    {
        Console.WriteLine($"Removed {sigNames[index]}");
        pdfSign.RemoveSignature(sigNames[index]);
    }
    // Save updated PDF file
    pdfSign.Save(dataDir + "RemoveSignature_out.pdf");
}
```

### Remove Signature but Keep the Signature field

As shown above, the [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) class [RemoveSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/removesignature) method lets you remove signature fields from PDF files. When using this method with versions prior to 9.3.0, both the signature and signature field are removed. Some develoeprs want to remove only the signature and keep the signature field so that it can be used to resign the document. To keep the signature field and only remove the signature, please use the following code snippet.

```csharp
public static void RemoveSignatureButKeepField()
{
    // Create PdfFileSignature object
    PdfFileSignature pdfSign = new PdfFileSignature();

    // Open PDF document
    pdfSign.BindPdf(dataDir + "DigitallySign.pdf");

    pdfSign.RemoveSignature("Signature1", false);

    // Save updated PDF file
    pdfSign.Save(dataDir + "RemoveSignature_out.pdf");
}
```

The following example shows how to remove all signatures from fields.

```csharp
public static void RemoveSignatureButKeepField2()
{
    // Create PdfFileSignature object
    PdfFileSignature pdfSign = new PdfFileSignature();

    // Open PDF document
    pdfSign.BindPdf(dataDir + "DigitallySign.pdf");

    var sigNames = pdfSign.GetSignNames();
    foreach (var sigName in sigNames)
    {
        pdfSign.RemoveSignature(sigName, false);
    }

    // Save updated PDF file
    pdfSign.Save(dataDir + "RemoveSignature_out.pdf");
}
```
