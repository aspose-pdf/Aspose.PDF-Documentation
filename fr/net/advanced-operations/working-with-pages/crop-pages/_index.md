---
title: Rogner les pages PDF par programmation C#
linktitle: Rogner les pages
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /fr/net/crop-pages/
description: Vous pouvez obtenir les propriétés des pages, telles que la largeur, la hauteur, le fond perdu, la zone de rognage et la zone de coupe en utilisant Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Crop PDF Pages programmatically C#",
    "alternativeHeadline": "Crop PDF Pages Easily with Aspose.PDF for .NET",
    "abstract": "Aspose.PDF for .NET introduit une nouvelle fonctionnalité puissante qui permet aux développeurs d'accéder et de manipuler par programmation diverses propriétés des pages d'un PDF, y compris la boîte média, la boîte de fond perdu, la boîte de coupe, la boîte d'art et la boîte de rognage. Cette fonctionnalité simplifie le processus de personnalisation des mises en page PDF, garantissant la précision dans la présentation des documents et améliorant la qualité d'impression tout en minimisant les bords blancs. Avec des extraits de code faciles à utiliser, les utilisateurs peuvent intégrer ces capacités dans leurs applications, améliorant ainsi la gestion et la manipulation des PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "494",
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
    "url": "/net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/crop-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "Vous pouvez obtenir les propriétés des pages, telles que la largeur, la hauteur, le fond perdu, la zone de rognage et la zone de coupe en utilisant Aspose.PDF for .NET."
}
</script>

## Obtenir les propriétés des pages

Chaque page d'un fichier PDF possède un certain nombre de propriétés, telles que la largeur, la hauteur, le fond perdu, la zone de rognage et la zone de coupe. Aspose.PDF vous permet d'accéder à ces propriétés.

- **Boîte média** : La boîte média est la plus grande boîte de page. Elle correspond à la taille de la page (par exemple A4, A5, US Letter, etc.) sélectionnée lors de l'impression du document au format PostScript ou PDF. En d'autres termes, la boîte média détermine la taille physique du support sur lequel le document PDF est affiché ou imprimé.
- **Boîte de fond perdu** : Si le document a un fond perdu, le PDF aura également une boîte de fond perdu. Le fond perdu est la quantité de couleur (ou d'œuvre) qui s'étend au-delà du bord d'une page. Il est utilisé pour s'assurer que lorsque le document est imprimé et découpé à la taille ("rogné"), l'encre ira jusqu'au bord de la page. Même si la page est mal rognée - coupée légèrement en dehors des marques de coupe - aucun bord blanc n'apparaîtra sur la page.
- **Boîte de coupe** : La boîte de coupe indique la taille finale d'un document après impression et rognage.
- **Boîte d'art** : La boîte d'art est la boîte dessinée autour des contenus réels des pages de vos documents. Cette boîte de page est utilisée lors de l'importation de documents PDF dans d'autres applications.
- **Boîte de rognage** : La boîte de rognage est la taille de la "page" à laquelle votre document PDF est affiché dans Adobe Acrobat. En vue normale, seuls les contenus de la boîte de rognage sont affichés dans Adobe Acrobat. Pour des descriptions détaillées de ces propriétés, lisez la spécification Adobe.Pdf, en particulier 10.10.1 Limites de page.
- **Page.Rect** : l'intersection (rectangle communément visible) de la MediaBox et de la DropBox. L'image ci-dessous illustre ces propriétés.
Pour plus de détails, veuillez visiter [cette page](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

L'extrait de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

L'extrait ci-dessous montre comment rogner la page :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CropPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CropPageInput.pdf"))
    {
        Console.WriteLine(document.Pages[1].CropBox);
        Console.WriteLine(document.Pages[1].TrimBox);
        Console.WriteLine(document.Pages[1].ArtBox);
        Console.WriteLine(document.Pages[1].BleedBox);
        Console.WriteLine(document.Pages[1].MediaBox);
        // Create new Box rectangle
        var newBox = new Rectangle(200, 220, 2170, 1520);
        document.Pages[1].CropBox = newBox;
        document.Pages[1].TrimBox = newBox;
        document.Pages[1].ArtBox = newBox;
        document.Pages[1].BleedBox = newBox;
        // Save PDF document
        document.Save(dataDir + "CropPage_out.pdf");  
    }
}
```

Dans cet exemple, nous avons utilisé un fichier d'exemple [ici](crop_page.pdf). Au départ, notre page ressemble à celle montrée sur la Figure 1.

Après le changement, la page ressemblera à la Figure 2.

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