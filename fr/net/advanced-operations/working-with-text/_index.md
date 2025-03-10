---
title: Travailler avec du texte dans un PDF en utilisant C#
linktitle: Travailler avec du texte
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /fr/net/working-with-text/
description: Cette section explique diverses techniques de gestion du texte. Apprenez à ajouter, remplacer, faire pivoter, rechercher du texte en utilisant Aspose.PDF et C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Text in PDF using C#",
    "alternativeHeadline": "Enhanced Text Manipulation Features in PDF with C#",
    "abstract": "Découvrez des capacités puissantes de manipulation de texte dans les PDF en utilisant Aspose.PDF for .NET. Cette fonctionnalité permet aux utilisateurs d'ajouter, de remplacer, de faire pivoter et de formater du texte dans les documents PDF, améliorant ainsi l'interactivité et la personnalisation des documents. Donnez à vos applications des fonctionnalités de recherche efficaces et des techniques de gestion du texte flexibles adaptées aux développeurs C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF manipulation, add text to PDF, rotate text in PDF, search text in PDF, replace text in PDF, text formatting inside PDF, Aspose.PDF for .NET, text handling techniques, PDF document generation, Floating Box tool",
    "wordcount": "371",
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
    "url": "/net/working-with-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-text/"
    },
    "dateModified": "2024-11-26",
    "description": "Cette section explique diverses techniques de gestion du texte. Apprenez à ajouter, remplacer, faire pivoter, rechercher du texte en utilisant Aspose.PDF et C#."
}
</script>

Nous avons tous parfois besoin d'ajouter du texte au fichier PDF. Par exemple, lorsque vous souhaitez ajouter une traduction sous le texte principal, placer une légende à côté d'une image, ou simplement remplir un formulaire de demande. Il est également utile que tous les éléments de texte puissent être formatés dans le style de votre choix. Les manipulations de texte les plus populaires dans votre fichier PDF sont : ajouter du texte au PDF, formater le texte à l'intérieur du fichier PDF, remplacer et faire pivoter le texte dans votre document. **Aspose.PDF for .NET** est la meilleure solution qui a tout ce dont vous avez besoin pour interagir avec le contenu PDF.

Vous pouvez faire ce qui suit :

- [Ajouter du texte au fichier PDF](/pdf/fr/net/add-text-to-pdf-file/) - ajouter du texte à votre PDF, utiliser des polices à partir de flux et de fichiers, ajouter une chaîne HTML, ajouter un lien hypertexte, etc.
- [Info-bulle PDF](/pdf/fr/net/pdf-tooltip/) - vous pouvez ajouter une info-bulle au texte recherché en ajoutant un bouton invisible en utilisant C#.
- [Formatage du texte à l'intérieur du PDF](/pdf/fr/net/text-formatting-inside-pdf/) - De nombreuses fonctionnalités que vous pouvez ajouter à votre document lors du formatage du texte à l'intérieur. Ajouter un retrait de ligne, ajouter une bordure de texte, ajouter du texte souligné, ajouter un saut de ligne avec la bibliothèque Aspose.PDF.
- [Utiliser FloatingBox](/pdf/fr/net/floating-box/) - l'outil Floating Box est un outil spécial pour placer du texte et d'autres contenus sur une page PDF.
- [Remplacer le texte dans le PDF](/pdf/fr/net/replace-text-in-pdf/) - pour remplacer le texte dans toutes les pages d'un document PDF. Vous devez d'abord utiliser TextFragmentAbsorber.
- [Faire pivoter le texte à l'intérieur du PDF](/pdf/fr/net/rotate-text-inside-pdf/) - faire pivoter le texte à l'intérieur du PDF en utilisant la propriété de rotation de la classe TextFragment.
- [Rechercher et obtenir du texte à partir des pages du document PDF](/pdf/fr/net/search-and-get-text-from-pdf/) - vous pouvez utiliser la classe TextFragmentAbsorber pour rechercher et obtenir du texte à partir des pages.
- [Déterminer le saut de ligne](/pdf/fr/net/determine-line-break/) - ce sujet explique comment suivre le saut de ligne des fragments de texte multi-lignes.

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