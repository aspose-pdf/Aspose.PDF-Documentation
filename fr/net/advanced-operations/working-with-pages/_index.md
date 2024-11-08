---
title: Travailler avec les pages PDF en C#
linktitle: Travailler avec les pages
type: docs
weight: 20
url: /fr/net/working-with-pages/
description: Comment ajouter des pages, ajouter des en-têtes et des pieds de page, ajouter des filigranes, vous pouvez le savoir dans cette section. Aspose.PDF pour .NET vous explique tous les détails sur ce sujet.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-stamps-and-watermarks/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Travailler avec les pages PDF en C#",
    "alternativeHeadline": "Comment travailler avec les pages PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de document pdf",
    "keywords": "pdf, c#, page pdf, ajouter une page pdf, ajouter un numéro de page, tourner une page, supprimer une page",
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
    "url": "/net/working-with-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Comment ajouter des pages, ajouter des en-têtes et des pieds de page, ajouter des filigranes, vous pouvez le savoir dans cette section. Aspose.PDF pour .NET vous explique tous les détails sur ce sujet."
}
</script>
**Aspose.PDF pour .NET** vous permet d'insérer une page dans un document PDF à n'importe quel endroit du fichier ainsi que d'ajouter des pages à la fin d'un fichier PDF. Cette section montre comment ajouter des pages à un PDF sans Acrobat Reader.
Vous pouvez ajouter du texte ou des images dans les en-têtes et pieds de page de votre fichier PDF, et choisir différents en-têtes dans votre document avec la bibliothèque C# par Aspose.
Essayez également de rogner les pages dans un document PDF de manière programmatique en utilisant C#.

Cette section vous apprend comment ajouter des filigranes dans votre fichier PDF en utilisant la classe Artifact. Vous vérifierez l'exemple de programmation pour cette tâche.
Ajoutez un numéro de page en utilisant la classe PageNumberStamp. Pour ajouter un tampon dans votre document, utilisez les classes ImageStamp et TextStamp. Utilisez l'ajout d'un filigrane pour créer des images de fond dans votre fichier PDF avec **Aspose.PDF pour .NET**.

Vous êtes capable de faire ce qui suit :

- [Ajouter des Pages](/pdf/fr/net/add-pages/) - ajouter des pages à l'emplacement souhaité ou à la fin d'un fichier PDF et supprimer une page de votre document.
- [Déplacer des Pages](/pdf/fr/net/move-pages/) - déplacer des pages d'un document à un autre.
- [Déplacer des Pages](/pdf/fr/net/move-pages/) - déplacer des pages d'un document à un autre.
- [Supprimer des Pages](/pdf/fr/net/delete-pages/) - supprimer une page de votre fichier PDF en utilisant la collection PageCollection.
- [Modifier la Taille de la Page](/pdf/fr/net/change-page-size/) - vous pouvez modifier la taille de la page PDF avec un extrait de code utilisant la bibliothèque Aspose.PDF.
- [Pivoter des Pages](/pdf/fr/net/rotate-pages/) - vous pouvez changer l'orientation des pages dans un fichier PDF existant.
- [Diviser des Pages](/pdf/fr/net/split-document/) - vous pouvez diviser des fichiers PDF en un ou plusieurs PDF.
- [Ajouter des En-têtes et/ou des Pieds de page](/pdf/fr/net/add-headers-and-footers-of-pdf-file/) - ajouter du texte ou des images dans les en-têtes et les pieds de page de votre fichier PDF.
- [Rogner des Pages](/pdf/fr/net/crop-pages/) - vous pouvez rogner des pages dans un document PDF de manière programmatique avec différentes propriétés de page.
- [Ajouter des Filigranes](/pdf/fr/net/add-watermarks/) - ajouter des filigranes dans votre fichier PDF avec la classe Artifact.
- [Ajouter une Numérotation des Pages dans le Fichier PDF](/pdf/fr/net/add-page-number/) - la classe PageNumberStamp vous aidera à ajouter un Numéro de Page dans votre fichier PDF.
- [Ajouter la numérotation des pages dans un fichier PDF](/pdf/fr/net/add-page-number/) - La classe PageNumberStamp vous aidera à ajouter un numéro de page dans votre fichier PDF.
- [Ajouter des arrière-plans](/pdf/fr/net/add-backgrounds/) - les images d'arrière-plan peuvent être utilisées pour ajouter un filigrane.
- [Estampillage](/pdf/fr/net/stamping/) - vous pouvez utiliser la classe ImageStamp pour ajouter un timbre d'image à un fichier PDF et la classe TextStamp pour ajouter un texte.

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


