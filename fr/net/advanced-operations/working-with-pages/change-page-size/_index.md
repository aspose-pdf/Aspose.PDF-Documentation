---
title: Changer la taille de page PDF avec C#
linktitle: Changer la taille de page PDF
type: docs
weight: 40
url: /fr/net/change-page-size/
description: Changer la taille de page de votre document PDF en utilisant la bibliothèque Aspose.PDF pour .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Changer la taille de page PDF avec C#",
    "alternativeHeadline": "Redimensionner la page PDF avec .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, changer la taille du pdf, redimensionner le pdf",
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
    "url": "/net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-page-size/"
    },
    "dateModified": "2022-02-04",
    "description": "Changer la taille de page de votre document PDF en utilisant la bibliothèque Aspose.PDF pour .NET."
}
</script>
## Changer la taille de la page PDF

Aspose.PDF pour .NET vous permet de changer la taille de page d'un PDF avec quelques lignes de code dans vos applications .NET. Ce sujet explique comment mettre à jour/changer les dimensions de la page (taille) d'un fichier PDF existant.

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

La classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) contient la méthode SetPageSize(...) qui vous permet de définir la taille de la page. Le fragment de code ci-dessous met à jour les dimensions de la page en quelques étapes faciles :

1. Charger le fichier PDF source.
1. Obtenir les pages dans l'objet [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. Obtenir une page donnée.
1. Appeler la méthode SetPageSize(..) pour mettre à jour ses dimensions.
1. Appeler la méthode Save(..) de la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) pour générer le fichier PDF avec les dimensions de page mises à jour.

{{% alert color="primary" %}}

Veuillez noter que les propriétés de hauteur et de largeur utilisent les points comme unité de base, où 1 pouce = 72 points et 1 cm = 1/2.54 pouce = 0.3937 pouce = 28.3 points.
Veuillez noter que les propriétés de hauteur et de largeur utilisent les points comme unité de base, où 1 pouce = 72 points et 1 cm = 1/2,54 pouce = 0,3937 pouce = 28,3 points.

{{% /alert %}}

Le code suivant montre comment changer les dimensions de la page PDF en format A4.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-UpdateDimensions-UpdateDimensions.cs" >}}

## Obtenir la taille de page PDF

Vous pouvez lire la taille de page d'un fichier PDF existant en utilisant Aspose.PDF pour .NET. L'exemple de code suivant montre comment lire les dimensions de la page PDF en utilisant C#.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetDimensions-GetDimensions.cs" >}}

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


