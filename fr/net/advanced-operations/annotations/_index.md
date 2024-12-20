---
title: Travailler avec les annotations
linktitle: Annotations dans PDF
type: docs
weight: 100
url: /fr/net/annotations/
description: Cette section montre comment utiliser toutes sortes d'annotations sur votre fichier PDF avec la bibliothèque Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Annotations PDF",
    "alternativeHeadline": "Travailler avec des annotations dans des PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, annotations",
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
    "url": "/net/annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/annotations/"
    },
    "dateModified": "2022-02-04",
    "description": "Cette section montre comment utiliser toutes sortes d'annotations sur votre fichier PDF avec la bibliothèque Aspose.PDF."
}
</script>

Le contenu à l'intérieur d'une page PDF est difficile à éditer, mais la spécification PDF définit un ensemble complet d'objets qui peuvent être ajoutés aux pages PDF sans modifier le contenu de la page.

Ces objets sont appelés des annotations, et leur but varie du marquage du contenu de la page à la mise en œuvre de fonctionnalités interactives telles que des formulaires.

Les visionneuses PDF permettent généralement la création et l'édition de divers types d'annotations, par exemple des surlignages de texte, des notes, des lignes ou des formes. Indépendamment des types d'annotations qui peuvent être créés, les visionneuses PDF conformes à la spécification PDF doivent également prendre en charge le rendu pour tous les types d'annotations.

L'annotation est une partie importante du fichier PDF. En utilisant Aspose.PDF pour .NET, vous pouvez ajouter une nouvelle annotation, modifier une annotation existante, supprimer des annotations, etc. Cette section couvre le sujet suivant :

Vous êtes capable de faire ce qui suit :

- [Aperçu des Annotations](/pdf/fr/net/overview-of-annotations/) - apprenez quels types d'annotations sont définis par la spécification PDF, et ce que Aspose.PDF prend en charge.
- [Ajouter, Supprimer et Obtenir une Annotation](/pdf/fr/net/add-delete-and-get-annotation/) - cette section explique comment travailler avec tous les types d'annotations autorisés.
- [Ajouter, Supprimer et Obtenir une Annotation](/pdf/fr/net/add-delete-and-get-annotation/) - cette section explique comment travailler avec tous les types d'annotations autorisées.
- [Importer et exporter une annotation au format XFDF](/pdf/fr/net/import-export-xfdf/) - La bibliothèque Aspose.PDF fournit des méthodes pour importer et exporter des données d'annotations vers des fichiers XFDF.

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


