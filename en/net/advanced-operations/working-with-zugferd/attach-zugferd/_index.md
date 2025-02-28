---
title: Creating PDF/3-A compliant PDF and attaching ZUGFeRD invoice in C#
linktitle: Attach ZUGFeRD to PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /net/attach-zugferd/
description: Learn how to generate a PDF document with ZUGFeRD in Aspose.PDF for .NET
lastmod: "2023-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating PDF/3-A compliant PDF and attaching ZUGFeRD invoice in C#",
    "alternativeHeadline": "Attach ZUGFeRD Invoices to PDF in C#",
    "abstract": "Discover the new functionality that allows developers to generate PDF documents compliant with PDF/A-3B and seamlessly attach ZUGFeRD invoices using C#. This feature simplifies the process of embedding invoice metadata in PDF files, ensuring long-term document preservation and compliance with electronic invoicing standards",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "429",
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
    "url": "/net/attach-zugferd/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/attach-zugferd/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Attach ZUGFeRD to PDF

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

We recommend following steps to attach ZUGFeRD to PDF:

* Define a path variable that points to a folder where the input and output PDF files are located.
* Create a document object by loading an existing PDF file (e.g. "ZUGFeRD-test.pdf") from the path.
* Create a [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification/) object by providing the path and description of another file named "factur-x.xml", which contains invoice metadata conforming to the ZUGFeRD standard.
* Add properties to the file specification object, such as the description, MIME type, and AF relationship. The AF relationship indicates how the embedded file is related to the PDF document. In this case, it is set to "Alternative", meaning the embedded file is an alternative representation of the PDF content.
* Add the file specification object to the document's embedded files collection. File name should be specified to ZUGFeRD standard, e.g. "factur-x.xml".
* Convert the document to PDF/A-3B format, a subset of PDF that ensures the long-term preservation of electronic documents. PDF/A-3B allows embedding files of any format in PDF documents.
* Save the converted document as a new PDF file (e.g. "ZUGFeRD-res.pdf").

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AttachZUGFeRD()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ZUGFeRD-testInput.pdf"))
    {
        // Setup new file to be added as attachment
        var description = "Invoice metadata conforming to ZUGFeRD standard";
        var fileSpecification = new Aspose.Pdf.FileSpecification(dataDir + "ZUGFeRD-testXmlInput.xml", description)
        {
            Description = "Zugferd",
            MIMEType = "text/xml",
            Name = "factur-x.xml"
        };
        // Add attachment to document's attachment collection
        document.EmbeddedFiles.Add(fileSpecification);
        document.Convert(new MemoryStream(), Aspose.Pdf.PdfFormat.ZUGFeRD, Aspose.Pdf.ConvertErrorAction.Delete);
        // Save PDF document
        document.Save(dataDir + "AttachZUGFeRD_out.pdf");
    }
}
```

The convert method takes a stream, a PDF format, and a convert error action as parameters. The stream parameter can be used to save the conversion log. The convert error action parameter specifies what to do if any errors occur during the conversion. In this case, it is set to "Delete", which means that any elements that are not compliant with the PDF/A-3B format will be deleted from the document.
