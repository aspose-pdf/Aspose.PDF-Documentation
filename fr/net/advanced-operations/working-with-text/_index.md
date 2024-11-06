---
title: Travailler avec le texte dans les PDF en utilisant C#
linktitle: Travailler avec le texte
type: docs
weight: 30
url: fr/net/working-with-text/
description: Cette section explique les différentes techniques de manipulation de texte. Apprenez à ajouter, remplacer, faire pivoter, rechercher du texte en utilisant Aspose.PDF et C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Travailler avec le texte dans les PDF en utilisant C#",
    "alternativeHeadline": "Ajouter, faire pivoter, rechercher et supprimer du texte dans un fichier PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, ajouter du texte, rechercher du texte, supprimer du texte, manipuler du texte dans pdf",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe documentaire Aspose.PDF",
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
    "url": "/net/working-with-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-text/"
    },
    "dateModified": "2022-02-04",
    "description": "Cette section explique les différentes techniques de manipulation de texte. Apprenez à ajouter, remplacer, faire pivoter, rechercher du texte en utilisant Aspose.PDF et C#."
}
</script>
Nous avons tous parfois besoin d'ajouter du texte à un fichier PDF. Par exemple, lorsque vous souhaitez ajouter une traduction sous le texte principal, placer une légende à côté d'une image, ou simplement remplir un formulaire de candidature. Il est également utile que tous les éléments textuels puissent être formatés selon le style de votre choix. Les manipulations de texte les plus populaires dans votre fichier PDF sont : ajouter du texte au PDF, formater le texte à l'intérieur du fichier PDF, remplacer et tourner le texte dans votre document. **Aspose.PDF for .NET** est la meilleure solution qui offre tout ce dont vous avez besoin pour interagir avec le contenu PDF.

Vous êtes capable de faire ce qui suit :

- [Ajouter du texte au fichier PDF](/pdf/net/add-text-to-pdf-file/) - ajouter du texte à votre PDF, utiliser des polices à partir de flux et de fichiers, ajouter une chaîne HTML, ajouter un hyperlien, etc.
- [Infobulle PDF](/pdf/net/pdf-tooltip/) - vous pouvez ajouter une infobulle au texte recherché en ajoutant un bouton invisible en utilisant C#.
- [Formatage du texte à l'intérieur du PDF](/pdf/net/text-formatting-inside-pdf/) - De nombreuses fonctionnalités que vous pouvez ajouter à votre document lors du formatage du texte à l'intérieur de celui-ci.
- [Mise en forme du texte dans PDF](/pdf/net/text-formatting-inside-pdf/) - De nombreuses fonctionnalités que vous pouvez ajouter à votre document lors de la mise en forme du texte.
- [Remplacer le texte dans PDF](/pdf/net/replace-text-in-pdf/) - pour remplacer le texte dans toutes les pages d'un document PDF. Vous devez d'abord utiliser TextFragmentAbsorber.
- [Rotation du texte dans PDF](/pdf/net/rotate-text-inside-pdf/) - faire pivoter le texte dans PDF en utilisant la propriété de rotation de la classe TextFragment.
- [Rechercher et obtenir du texte à partir des pages d'un document PDF](/pdf/net/search-and-get-text-from-pdf/) - vous pouvez utiliser la classe TextFragmentAbsorber pour rechercher et obtenir un texte des pages.
- [Déterminer le saut de ligne](/pdf/net/determine-line-break/) - ce sujet explique comment suivre la rupture de ligne des fragments de texte multi-lignes.

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

