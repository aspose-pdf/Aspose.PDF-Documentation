---
title: Extract Attachments from PDF File
type: docs
weight: 10
url: /net/extract-attachments/
description: Discover how to extract and manage attachments in PDF documents in .NET using Aspose.PDF for better document handling.
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Attachments from PDF File",
    "alternativeHeadline": "Effortlessly Extract and Manage PDF Attachments",
    "abstract": "The new attachment extraction functionality in Aspose.PDF for .NET allows developers to easily retrieve and manage file attachments within PDF documents. By utilizing the PdfExtractor class, users can extract attachments and obtain essential information, such as attachment names and details, enhancing document processing capabilities",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "208",
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
    "url": "/net/extract-attachments/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-attachments/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

One of the main category under the extraction capabilities of [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) is the attachment extraction. This category provides a set of methods, which not only help extract the attachments but also provides the methods which can give you the attachment related information i.e. [GetAttachmentInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachmentinfo) and [GetAttachName](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachnames) methods provide attachment information and attachment name respectively. In order to extract and then get attachments we use [ExtractAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractattachment) and [GetAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachment) methods.

The following code snippet shows you how to use PdfExtractor methods:

```csharp
private static void ExtractAttachments(string inputFilePath, string outputDirectory)
{
	// Create extractor
	using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
	{
		pdfExtractor.BindPdf(inputFilePath);

		// Extract attachments
		pdfExtractor.ExtractAttachment();

		// Get attachment names
		if (pdfExtractor.GetAttachNames().Count > 0)
		{
			Console.WriteLine("Extracting and storing...");

			// Get extracted attachments
			pdfExtractor.GetAttachment(outputDirectory);
		}
	}
}
```
