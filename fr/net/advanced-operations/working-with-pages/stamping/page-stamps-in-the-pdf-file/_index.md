---
title: Ajouter des timbres de page PDF dans un PDF à l'aide de C#
linktitle: Timbres de page dans le fichier PDF
type: docs
weight: 30
url: /fr/net/page-stamps-in-the-pdf-file/
description: Ajouter un timbre de page à un document PDF en utilisant la classe PdfPageStamp avec la bibliothèque Aspose.PDF pour .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter des timbres de page PDF dans un PDF à l'aide de C#",
    "alternativeHeadline": "Ajouter des timbres de page PDF dans un PDF à l'aide de C#",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, génération de documents",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe de documentation Aspose.PDF",
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
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/page-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/page-stamps-in-the-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Ajouter un timbre de page à un document PDF en utilisant la classe PdfPageStamp avec la bibliothèque Aspose.PDF pour .NET."
}
</script>
## Ajouter un cachet de page avec C\#

Un [PdfPageStamp](https://reference.aspose.com/pdf/net/aspose.pdf/PdfPageStamp) peut être utilisé lorsque vous avez besoin d'appliquer un cachet composite contenant des graphiques, du texte, des tableaux. L'exemple suivant montre comment utiliser un cachet pour créer une papeterie comme avec Adobe InDesign, Illustrator, Microsoft Word. Supposons que nous ayons un document d'entrée et que nous voulions appliquer 2 types de bordures de couleur bleue et prune.

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
public static void AddPageStamp()
{
    var inputFileName = "sample-4pages.pdf";
    var outputFileName = "AddPageStamp_out.pdf";
    var pageStampFileName = "PageStamp.pdf";
    var document = new Document(_dataDir + inputFileName);

    var bluePageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 1)
    {
        Height = 800,
        Background = true
    };

    var plumPageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 2)
    {
        Height = 800,
        Background = true
    };

    for (int i = 1; i < 5; i++)
    {
        if (i % 2 == 0)
            document.Pages[i].AddStamp(bluePageStamp);
        else
            document.Pages[i].AddStamp(plumPageStamp);
    }

    document.Save(_dataDir + outputFileName);
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Bibliothèque de manipulation de PDF pour .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

