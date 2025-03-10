---
title: Travailler avec des pages PDF en C#
linktitle: Travailler avec des pages
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/working-with-pages/
description: Comment ajouter des pages, ajouter des en-têtes et des pieds de page, ajouter des filigranes, vous pouvez le savoir dans cette section. Aspose.PDF for .NET vous explique tous les détails sur ce sujet.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with PDF Pages in C#",
    "alternativeHeadline": "Enhance PDF Management with C# Page Features",
    "abstract": "Découvrez les capacités avancées de Aspose.PDF for .NET pour gérer les pages PDF, y compris l'ajout, le déplacement et la suppression de pages avec précision. Cette fonctionnalité permet aux utilisateurs d'améliorer leurs documents PDF en incorporant des en-têtes, des pieds de page, des filigranes et des tailles de page personnalisées, le tout à travers un code C# intuitif. Optimisez vos flux de travail documentaires avec des fonctionnalités de manipulation et de personnalisation PDF sans faille.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "450",
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
    "url": "/net/working-with-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "Comment ajouter des pages, ajouter des en-têtes et des pieds de page, ajouter des filigranes, vous pouvez le savoir dans cette section. Aspose.PDF for .NET vous explique tous les détails sur ce sujet."
}
</script>

**Aspose.PDF for .NET** vous permet d'insérer une page dans un document PDF à n'importe quel endroit du fichier ainsi qu'ajouter des pages à la fin d'un fichier PDF. Cette section montre comment ajouter des pages à un PDF sans Acrobat Reader.
Vous pouvez ajouter du texte ou des images dans les en-têtes et les pieds de page de votre fichier PDF, et choisir différents en-têtes dans votre document avec la bibliothèque C# d'Aspose.
Essayez également de rogner des pages dans un document PDF par programmation en utilisant C#.

Cette section vous apprend comment ajouter des filigranes dans votre fichier PDF en utilisant la classe Artifact. Vous vérifierez l'exemple de programmation pour cette tâche.
Ajoutez le numéro de page en utilisant la classe PageNumberStamp. Pour ajouter un tampon dans votre document, utilisez les classes ImageStamp et TextStamp. Utilisez l'ajout d'un filigrane pour créer des images de fond dans votre fichier PDF avec **Aspose.PDF for .NET**.

Vous êtes capable de faire ce qui suit :

- [Ajouter des pages](/pdf/net/add-pages/) - ajouter des pages à l'emplacement souhaité ou à la fin d'un fichier PDF et supprimer une page de votre document.
- [Déplacer des pages](/pdf/net/move-pages/) - déplacer des pages d'un document à un autre.
- [Supprimer des pages](/pdf/net/delete-pages/) - supprimer une page de votre fichier PDF en utilisant la collection PageCollection.
- [Changer la taille de la page](/pdf/net/change-page-size/) - vous pouvez changer la taille de la page PDF avec un extrait de code en utilisant la bibliothèque Aspose.PDF.
- [Faire pivoter des pages](/pdf/net/rotate-pages/) - vous pouvez changer l'orientation des pages dans un fichier PDF existant.
- [Diviser des pages](/pdf/net/split-document/) - vous pouvez diviser des fichiers PDF en un ou plusieurs PDF.
- [Ajouter des en-têtes et/ou des pieds de page](/pdf/net/add-headers-and-footers-of-pdf-file/) - ajouter du texte ou des images dans les en-têtes et les pieds de page de votre fichier PDF.
- [Rogner des pages](/pdf/net/crop-pages/) - vous pouvez rogner des pages dans un document PDF par programmation avec différentes propriétés de page.
- [Ajouter des filigranes](/pdf/net/add-watermarks/) - ajouter des filigranes dans votre fichier PDF avec la classe Artifact.
- [Ajouter la numérotation des pages dans le fichier PDF](/pdf/net/add-page-number/) - la classe PageNumberStamp vous aidera à ajouter un numéro de page dans votre fichier PDF.
- [Ajouter des arrière-plans](/pdf/net/add-backgrounds/) - des images de fond peuvent être utilisées pour ajouter un filigrane.
- [Tamponnage](/pdf/net/stamping/) - vous pouvez utiliser la classe ImageStamp pour ajouter un tampon d'image à un fichier PDF et la classe TextStamp pour ajouter un texte.

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