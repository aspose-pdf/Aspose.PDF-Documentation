---
title: Converting an FDF to XML format
type: docs
weight: 10
url: /net/converting-an-fdf-to-xml-format/
description: This section explains how you can convert an FDF to XML format with FormDataConverter Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting an FDF to XML format",
    "alternativeHeadline": "Convert FDF Files to XML Easily",
    "abstract": "Discover how to efficiently convert FDF files to XML format using the FormDataConverter class in Aspose.PDF for .NET. This functionality streamlines data handling by transforming key/value pairs from FDF into an easily readable XML structure, enhancing interoperability and data management in your applications",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "288",
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
    "url": "/net/converting-an-fdf-to-xml-format/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-an-fdf-to-xml-format/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

{{% alert color="primary" %}}

The [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) namespace in [Aspose.PDF for .NET](/pdf/net/) supports AcroForms very well. It also supports importing and exporting form data to different file formats like FDF, XFDF, and XML. However, sometimes developers might need to convert one format into another one. This article looks at the feature that converts FDF into XML.

{{% /alert %}}

## Implementation details

FDF stands for Forms Data Format, and an FDF file contains the form values in a key/value pair. We also know that XML file contains the values as tags. Where, mostly the key is represented as the tag name and value is represented as the value within that tag. Now, [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) provides us the flexibility to convert an FDF file format into an XML format.

We can use [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter) class for this purpose. This class provides us different method to convert one data format into another format. In this article, we will just use one method named [ConvertFdfToXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter/methods/convertfdftoxml). This method takes FDF file as an input or source stream and saves it into XML format.

The following code snippet shows you how to convert an FDF file into an XML file:


{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConvertPdfToXML-ConvertPdfToXML.cs" >}}
