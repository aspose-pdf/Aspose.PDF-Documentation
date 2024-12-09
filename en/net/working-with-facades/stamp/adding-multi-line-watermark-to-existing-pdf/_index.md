---
title: Adding multi line watermark 
type: docs
weight: 10
url: /net/adding-multi-line-watermark-to-existing-pdf/
description: This section explains how to add multi line watermark to existing PDF using FormattedText Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding multi line watermark",
    "alternativeHeadline": "Enhance PDFs with Multi-Line Watermarks Easily",
    "abstract": "Introducing the ability to add multi-line watermarks to existing PDFs using the Aspose.Pdf.Facades namespace. This new functionality simplifies the process, allowing users to easily incorporate multiple lines of text into their documents with the newly implemented AddNewLineText() method in the FormattedText class. Enhance your PDF presentations with customized multi-line watermarks effortlessly",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "188",
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
    "url": "/net/adding-multi-line-watermark-to-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-multi-line-watermark-to-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

{{% alert color="primary" %}}

A lot of users want to stamp their PDF documents with multi-line text. They usually try to use `\n` and `<br>` but these types of characters are not supported by Aspose.Pdf.Facades namespace. So, to make it possible, we have added another method named [AddNewLineText()](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext/methods/addnewlinetext/index) in [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) class of Aspose.Pdf.Facades namespace.

{{% /alert %}}

## Implementation details

Please refer to the following code chunk to add multi-line watermark in existing PDF.

```csharp
// Instantiate a stamp object
Stamp logoStamp = new Stamp();

// Instantiate an object of FormattedText class
FormattedText formatText = new FormattedText("Hello World!",
System.Drawing.Color.FromArgb(180, 0, 0), FontStyle.TimesItalic, EncodingType.Winansi, false, 50);

// Add another line for Stamp
formatText.AddNewLineText("Good Luck");
// BindLogo to PDF
logoStamp.BindLogo(formatText);
```
