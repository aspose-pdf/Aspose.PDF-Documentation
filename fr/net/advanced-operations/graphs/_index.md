---
title: Travailler avec des graphiques dans un fichier PDF
linktitle: Travailler avec des graphiques
type: docs
weight: 70
url: fr/net/graphs/
description: Cet article explique ce qu'est un graphique, comment créer un objet rectangle rempli et autres fonctions
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-graphs/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Travailler avec des graphiques dans un fichier PDF",
    "alternativeHeadline": "Comment créer des graphiques dans un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, graphiques dans pdf",
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
    "url": "/net/graphs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/graphs/"
    },
    "dateModified": "2022-02-04",
    "description": "Cet article explique ce qu'est un graphique, comment créer un objet rectangle rempli et autres fonctions"
}
</script>

## Qu'est-ce qu'un Graphique

L'ajout de graphiques aux documents PDF est une tâche très courante pour les développeurs lorsqu'ils travaillent avec Adobe Acrobat Writer ou d'autres applications de traitement de PDF. Il existe de nombreux types de graphiques qui peuvent être utilisés dans les applications PDF.
[Aspose.PDF pour .NET](/pdf/net/) prend également en charge l'ajout de graphiques aux documents PDF. À cette fin, la classe Graph est fournie. Graph est un élément de niveau paragraphe et peut être ajouté à la collection Paragraphs dans une instance de Page. Une instance de Graph contient une collection de Formes.

Les types de formes suivants sont pris en charge par la classe [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) :

- [Arc](/pdf/net/add-arc/) - parfois appelé aussi un drapeau, est une paire ordonnée de sommets adjacents, mais parfois également appelée une ligne dirigée.
- [Cercle](/pdf/net/add-circle/) - affiche des données en utilisant un cercle divisé en secteurs. Nous utilisons un graphique circulaire (également appelé diagramme circulaire) pour montrer comment les données représentent des parties d'un tout ou d'un groupe.
- [Courbe](/pdf/net/add-curve/) - est une union connectée de lignes projectives, chaque ligne rencontrant trois autres en points doubles ordinaires.
- [Curve](/pdf/net/add-curve/) - est une union connectée de lignes projectives, chaque ligne rencontrant trois autres en points doubles ordinaires.
- [Line](/pdf/net/add-line) - les graphiques linéaires sont utilisés pour afficher des données continues et peuvent être utiles pour prédire des événements futurs lorsqu'ils montrent des tendances dans le temps.
- [Rectangle](/pdf/net/add-rectangle/) - est l'une des nombreuses formes fondamentales que vous verrez dans les graphiques, cela peut être très utile pour vous aider à résoudre un problème.
- [Ellipse](/pdf/net/add-ellipse/) - est un ensemble de points sur un plan, créant une forme ovale et courbée.

Les détails ci-dessus sont également représentés dans les figures ci-dessous :

![Figures in Graphs](graphs.png)

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

