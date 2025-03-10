---
title: Travailler avec des annotations
linktitle: Annotations dans PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 160
url: /fr/net/annotations/
description: Apprenez à travailler avec des annotations dans des fichiers PDF en utilisant Aspose.PDF dans .NET, y compris l'ajout de commentaires, de surlignages et d'autres annotations.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/working-with-annotations/
    - /net/annotation/
    - /net/working-with-annotations-facades/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Annotations",
    "alternativeHeadline": "Enhance PDFs with Comprehensive Annotation Capabilities",
    "abstract": "Améliorez vos documents PDF avec les puissantes capacités d'annotation de la bibliothèque Aspose.PDF. Cette fonctionnalité permet aux utilisateurs d'ajouter, de modifier et de supprimer facilement divers types d'annotations, y compris des surlignages, des notes et des formes, tout en maintenant une compatibilité totale avec les visionneuses PDF. Découvrez comment gérer sans effort les annotations et importer/exporter des données au format XFDF et FDF pour une manipulation efficace des documents PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF Annotations, Aspose.PDF, annotations, XFDF format, FDF format, edit annotations, add annotations, delete annotations, PDF manipulation, interactive features",
    "wordcount": "294",
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
    "url": "/net/annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

Le contenu à l'intérieur d'une page PDF est difficile à modifier, mais la spécification PDF définit un ensemble complet d'objets qui peuvent être ajoutés aux pages PDF sans changer le contenu de la page.

Ces objets sont appelés annotations, et leur but va de la mise en forme du contenu de la page à la mise en œuvre de fonctionnalités interactives telles que des formulaires.

Les visionneuses PDF permettent généralement la création et la modification de divers types d'annotations, par exemple des surlignages de texte, des notes, des lignes ou des formes. Quel que soit le type d'annotation pouvant être créé, les visionneuses PDF conformes à la spécification PDF devraient également prendre en charge le rendu de tous les types d'annotations.

L'annotation est une partie importante du fichier PDF. En utilisant Aspose.PDF for .NET, vous pouvez ajouter une nouvelle annotation, modifier une annotation existante et supprimer des annotations, etc. Cette section couvre le sujet suivant :

Vous êtes en mesure de faire ce qui suit :

- [Aperçu des annotations](/pdf/net/overview-of-annotations/) - apprenez quels types d'annotations sont définis par la spécification PDF et ce que prend en charge Aspose.PDF.
- [Ajouter, supprimer et obtenir une annotation](/pdf/net/add-delete-and-get-annotation/) - cette section explique comment travailler avec tous les types d'annotations autorisées.
- [Importer et exporter des annotations avec le format XFDF](/pdf/net/import-export-xfdf/) - la bibliothèque Aspose.PDF fournit des méthodes pour importer et exporter des données d'annotations vers des fichiers XFDF.
- [Importer des annotations au format FDF dans PDF](/pdf/net/import-fdf/) - la bibliothèque Aspose.PDF fournit une méthode pour importer des annotations au format FDF dans des fichiers PDF.

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