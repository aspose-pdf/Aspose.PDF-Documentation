---
title: Extract Text From Stamps using C#
type: docs
weight: 60
url: /net/extract-text-from-stamps/
description: Learn how to use special feature of Aspose.PDF for .NET - text exstraction from stamp annotations
lastmod: "2021-01-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text From Stamps using C#",
    "alternativeHeadline": "Extract Text from PDF Stamp Annotations with Ease",
    "abstract": "Discover the powerful text extraction capabilities of Aspose.PDF for .NET, designed specifically for retrieving text from stamp annotations in PDF documents. This new feature streamlines the process, enabling developers to easily access and manipulate text within stamp annotations using concise code snippets, enhancing productivity and efficiency in PDF management tasks",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "168",
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
    "url": "/net/extract-text-from-stamps/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text-from-stamps/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Extract Text from Stamp Annotations

Aspose.PDF for NET lets you extract text from stamp annotations. In order to extract text from Stamp Annotations in a PDF, the following steps can be used.

1. Create a `Document` class object.
1. Get the desired `Annotation` from list of annotations of a page.
1. Define a new object of `TextAbsorber` class.
1. Use the TextAbsorber's visit method to get the Text.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractText()
{
    // The path to the documents directory.
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractStampText.pdf"))
    {
        Aspose.Pdf.Annotations.Annotation item = document.Pages[1].Annotations[1];
        if (item is Aspose.Pdf.Annotations.StampAnnotation annot)
        {
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            Aspose.Pdf.XForm appearance = annot.Appearance["N"];
            absorber.Visit(appearance);
            Console.WriteLine(absorber.Text);
        }
    }
}
```
