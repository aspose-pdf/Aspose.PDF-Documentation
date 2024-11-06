---
title: Travailler avec les AcroForms
linktitle: AcroForms
type: docs
weight: 10
url: fr/net/acroforms/
description: Avec Aspose.PDF pour .NET, vous pouvez créer un formulaire à partir de zéro, remplir le champ de formulaire dans un document PDF, extraire les données du formulaire, etc.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Travailler avec les AcroForms",
    "alternativeHeadline": "Options pour travailler avec les AcroForms dans PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, acroforms dans pdf",
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
    "dateModified": "2022-02-04",
    "description": "Avec Aspose.PDF pour .NET, vous pouvez créer un formulaire à partir de zéro, remplir le champ de formulaire dans un document PDF, extraire les données du formulaire, etc."
}
</script>
## Fondamentaux des AcroForms

**AcroForms** sont la technologie originale des formulaires PDF. Les AcroForms sont des formulaires orientés page. Ils ont été introduits pour la première fois en 1998. Ils acceptent les entrées au format de données de formulaire ou FDF et le format de données de formulaire XML ou xFDF. Les fournisseurs tiers prennent en charge les AcroForms. Lorsque Adobe a introduit les AcroForms, ils les ont décrits comme « un formulaire PDF créé avec Adobe Acrobat Pro/Standard et qui n'est pas un type spécial de formulaire XFA statique ou dynamique. Les Acroforms sont portables et fonctionnent sur toutes les plateformes.

Vous pouvez utiliser les AcroForms pour ajouter des pages supplémentaires au document de formulaire PDF. Grâce au concept de modèles, vous pouvez utiliser les AcroForms pour remplir le formulaire avec plusieurs enregistrements de base de données.

Le PDF 1.7 prend en charge deux méthodes différentes pour intégrer des données et des formulaires PDF.

*AcroForms (également connus sous le nom de formulaires Acrobat)*, introduits et inclus dans la spécification de format PDF 1.2.

*Adobe XML Forms Architecture (XFA) formulaires*, introduits dans la spécification de format PDF 1.5 comme une fonctionnalité optionnelle (La spécification XFA n'est pas incluse dans la spécification PDF, elle est seulement référencée.
*Les formulaires Adobe XML Forms Architecture (XFA)*, introduits dans la spécification du format PDF 1.5 comme une fonctionnalité optionnelle (La spécification XFA n'est pas incluse dans la spécification PDF, elle est uniquement référencée.

Pour comprendre les **Acroforms** par rapport aux formulaires **XFA**, nous devons d'abord comprendre les bases. Pour commencer, les deux sont des formulaires PDF que vous pouvez utiliser. Acroforms est le plus ancien, créé en 1998, et il est toujours considéré comme le formulaire PDF classique. Les formulaires XFA sont des pages web que vous pouvez enregistrer en tant que PDF, et sont apparus en 2003. Il a fallu un certain temps avant que le PDF commence à accepter les formulaires XFA.

Les AcroForms possèdent des capacités que l'on ne trouve pas dans les XFA et inversement, les XFA ont des capacités que l'on ne trouve pas dans les AcroForms. Par exemple :

- Les AcroForms prennent en charge le concept de "Modèles", permettant d'ajouter des pages supplémentaires au document de formulaire PDF pour prendre en charge le remplissage du formulaire avec plusieurs enregistrements de base de données.
- Les XFA prennent en charge le concept de reflow de document permettant à un champ de redimensionner si nécessaire pour accueillir des données.

Pour en savoir plus sur les capacités de la bibliothèque Java, consultez les articles suivants :
Pour un apprentissage plus détaillé des capacités de la bibliothèque Java, consultez les articles suivants :

- [Créer AcroForm](/pdf/net/create-form) - créer un formulaire à partir de zéro avec C#.
- [Remplir AcroForm](/pdf/net/fill-form) - remplir le champ du formulaire dans votre document PDF.
- [Extraire AcroForm](/pdf/net/extract-form) - obtenir la valeur de tous ou d'un champ individuel du document PDF.
- [Modifier AcroForm](/pdf/net/modifing-form) - obtenir ou définir FieldLimit, définir la police du champ du formulaire et etc.
- [Poster les données AcroForm](/pdf/net/posting-acroform-data/) - importer et exporter les données du formulaire vers et depuis un fichier XML.
- [Importer et exporter des données](/pdf/net/import-and-export-data/) - importer et exporter des données en utilisant la classe Form.

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


