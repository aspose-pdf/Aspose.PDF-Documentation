---
title: Faire pivoter les pages PDF en utilisant C#
linktitle: Faire pivoter les pages PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /fr/net/rotate-pages/
description: Ce sujet décrit comment faire pivoter l'orientation des pages dans un fichier PDF existant par programmation avec C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Rotate PDF Pages Using C#",
    "alternativeHeadline": "Effortlessly Rotate PDF Pages with C#",
    "abstract": "La nouvelle fonctionnalité dans Aspose.PDF for .NET permet aux développeurs de changer par programmation l'orientation des pages dans des fichiers PDF existants. Les utilisateurs peuvent passer facilement entre les modes paysage et portrait, garantissant que le contenu s'adapte correctement dans la nouvelle mise en page, améliorant l'utilisabilité et la présentation du document.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "236",
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
    "url": "/net/rotate-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/rotate-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "Ce sujet décrit comment faire pivoter l'orientation des pages dans un fichier PDF existant par programmation avec C#."
}
</script>

Ce sujet décrit comment mettre à jour ou changer l'orientation des pages dans un fichier PDF existant par programmation avec C#.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Changer l'orientation de la page

Depuis la version Aspose.PDF for .NET 9.6.0, nous avons ajouté de nouvelles fonctionnalités intéressantes comme le changement de l'orientation de la page du paysage au portrait et vice versa. Pour changer l'orientation de la page, définissez le MediaBox de la page en utilisant le code suivant. Vous pouvez également changer l'orientation de la page en définissant l'angle de rotation en utilisant la méthode Rotate().

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePageOrientation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RotatePagesInput.pdf"))
    {
        foreach (Page page in document.Pages)
        {
            Aspose.Pdf.Rectangle r = page.MediaBox;
            double newHeight = r.Width;
            double newWidth = r.Height;
            double newLLX = r.LLX;
            //  We must to move page upper in order to compensate changing page size
            // (lower edge of the page is 0,0 and information is usually placed from the
            //  Top of the page. That's why we move lover edge upper on difference between
            //  Old and new height.
            double newLLY = r.LLY + (r.Height - newHeight);
            page.MediaBox = new Aspose.Pdf.Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight);
            // Sometimes we also need to set CropBox (if it was set in original file)
            page.CropBox = new Aspose.Pdf.Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight);
            // Setting Rotation angle of page
            page.Rotate = Rotation.on90;
        }
        // Save PDF document
        document.Save(dataDir + "ChangeOrientation_out.pdf");
    }
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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