---
title: Travailler avec AcroForms
linktitle: AcroForms
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/acroforms/
description: Avec Aspose.PDF for .NET, vous pouvez créer un formulaire à partir de zéro, remplir le champ du formulaire dans un document PDF, extraire des données du formulaire, etc.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with AcroForms",
    "alternativeHeadline": "Enhance PDF forms with flexible AcroForms functionality",
    "abstract": "Aspose.PDF for .NET introduit des capacités améliorées pour travailler avec les AcroForms, permettant aux utilisateurs de créer efficacement des formulaires à partir de zéro, de remplir des champs PDF et d'extraire des données sans effort. Cette fonctionnalité puissante prend en charge l'intégration de plusieurs enregistrements de base de données, permettant une gestion dynamique des formulaires et une expérience utilisateur rationalisée.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "AcroForms, PDF forms technology, create a form, fill form fields, extract data, database records, Templates, modify AcroForms, posting AcroForm data, import and export data",
    "wordcount": "484",
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
    "url": "/net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/acroforms/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Fondamentaux des AcroForms

**AcroForms** sont la technologie originale des formulaires PDF. AcroForms est un formulaire orienté page. Ils ont été introduits pour la première fois en 1998. Ils acceptent les entrées au format Forms Data Format ou FDF et XML Forms Data Format ou xFDF. Des fournisseurs tiers prennent en charge les AcroForms. Lorsque Adobe a introduit les AcroForms, ils les ont qualifiés de « formulaire PDF créé avec Adobe Acrobat Pro/Standard et qui n'est pas un type spécial de formulaire XFA statique ou dynamique. Les AcroForms sont portables et fonctionnent sur toutes les plateformes.

Vous pouvez utiliser les AcroForms pour ajouter des pages supplémentaires au document de formulaire PDF. Grâce au concept de Modèles, vous pouvez utiliser les AcroForms pour prendre en charge le remplissage du formulaire avec plusieurs enregistrements de base de données.

Le PDF 1.7 prend en charge deux méthodes différentes pour intégrer des données et des formulaires PDF.

*AcroForms (également connus sous le nom de formulaires Acrobat)*, introduits et inclus dans la spécification du format PDF 1.2.

*Adobe XML Forms Architecture (XFA) forms*, introduits dans la spécification du format PDF 1.5 en tant que fonctionnalité optionnelle (La spécification XFA n'est pas incluse dans la spécification PDF, elle est seulement référencée).

Pour comprendre **Acroforms** vs **XFA** forms, nous devons d'abord comprendre les bases. Pour commencer, les deux sont des formulaires PDF que vous pouvez utiliser. Les Acroforms sont les plus anciens, créés en 1998, et ils sont toujours considérés comme le formulaire PDF classique. Les formulaires XFA sont des pages web que vous pouvez enregistrer en tant que PDF, et sont apparus en 2003. Il a fallu un certain temps avant que le PDF commence à accepter les formulaires XFA.

Les AcroForms ont des capacités qui ne se trouvent pas dans XFA et inversement, XFA a certaines capacités qui ne se trouvent pas dans les AcroForms. Par exemple :

- Les AcroForms prennent en charge le concept de « Modèles », permettant d'ajouter des pages supplémentaires au document de formulaire PDF pour prendre en charge le remplissage du formulaire avec plusieurs enregistrements de base de données.
- XFA prend en charge le concept de réajustement de document permettant à un champ de redimensionner si nécessaire pour accueillir des données.

Pour un apprentissage plus détaillé des capacités de la bibliothèque Java, consultez les articles suivants :

- [Créer AcroForm](/pdf/net/create-form) - créer un formulaire à partir de zéro avec C#.
- [Remplir AcroForm](/pdf/net/fill-form) - remplir le champ de formulaire dans votre document PDF.
- [Extraire AcroForm](/pdf/net/extract-form) - obtenir la valeur de tous ou d'un champ individuel du document PDF.
- [Modifier AcroForm](/pdf/net/modifing-form) - obtenir ou définir FieldLimit, définir la police du champ de formulaire, etc.
- [Publier des données AcroForm](/pdf/net/posting-acroform-data/) - importer et exporter des données de formulaire vers un fichier XML.
- [Importer et exporter des données](/pdf/net/import-and-export-data/) - importer et exporter des données en utilisant la classe Form.
- [Supprimer des formulaires du PDF](/pdf/net/remove-form/) - supprimer du texte basé sur le sous-type/formulaire, supprimer tous les formulaires.
- [Importer et exporter des données en JSON](/pdf/net/import-export-json/) - importer et exporter des données avec JSON

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