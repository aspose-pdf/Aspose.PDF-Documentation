---
title: Travailler avec des Graphiques dans un fichier PDF
linktitle: Travailler avec des Graphiques
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /fr/net/working-with-graphs/
description: Cet article explique ce qu'est un Graphique, comment créer un objet rectangle rempli, et d'autres fonctions
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
    "headline": "Working with Graphs in PDF file",
    "alternativeHeadline": "Create and Manipulate Graphs in PDF Files",
    "abstract": "Découvrez la nouvelle fonctionnalité puissante pour générer et manipuler des graphiques dans des documents PDF en utilisant Aspose.PDF for .NET. Cette fonctionnalité permet aux développeurs de créer une variété de formes de graphiques, y compris des arcs, des cercles, des lignes et des rectangles, améliorant la présentation visuelle des données dans leurs applications. Optimisez votre processus de génération de PDF et fournissez des visualisations de données dynamiques avec facilité.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Graph, PDF documents, Aspose.PDF for .NET, Graph class, Shapes, Arc, Circle, Line graph, Rectangle, PDF manipulation",
    "wordcount": "329",
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
    "url": "/net/graphs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/graphs/"
    },
    "dateModified": "2024-11-25",
    "description": "Cet article explique ce qu'est un Graphique, comment créer un objet rectangle rempli, et d'autres fonctions"
}
</script>

## Qu'est-ce qu'un Graphique

Ajouter des graphiques aux documents PDF est une tâche très courante pour les développeurs travaillant avec Adobe Acrobat Writer ou d'autres applications de traitement de PDF. Il existe de nombreux types de graphiques qui peuvent être utilisés dans les applications PDF.
[Aspose.PDF for .NET](/pdf/net/) prend également en charge l'ajout de graphiques aux documents PDF. À cet effet, la classe Graphique est fournie. Un Graphique est un élément de niveau paragraphe et peut être ajouté à la collection de Paragraphes dans une instance de Page. Une instance de Graphique contient une collection de Formes.

Les types de formes suivants sont pris en charge par la classe [Graphique](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) :

- [Arc](/pdf/net/add-arc/) - parfois aussi appelé un drapeau, est une paire ordonnée de sommets adjacents, mais parfois aussi appelé une ligne dirigée.
- [Cercle](/pdf/net/add-circle/) - affiche des données à l'aide d'un cercle divisé en secteurs. Nous utilisons un graphique circulaire (également appelé un diagramme circulaire) pour montrer comment les données représentent des portions d'un tout ou d'un groupe.
- [Courbe](/pdf/net/add-curve/) - est une union connectée de lignes projectives, chaque ligne rencontrant trois autres en points doubles ordinaires.
- [Ligne](/pdf/net/add-line) - les graphiques linéaires sont utilisés pour afficher des données continues et peuvent être utiles pour prédire des événements futurs lorsqu'ils montrent des tendances au fil du temps.
- [Rectangle](/pdf/net/add-rectangle/) - est l'une des nombreuses formes fondamentales que vous verrez dans les graphiques, elle peut être très utile pour vous aider à résoudre un problème.
- [Ellipse](/pdf/net/add-ellipse/) - est un ensemble de points sur un plan, créant une forme ovale et courbée.

Les opérations suivantes sont prises en charge pour les types de formes :
- [Vérifier les limites](/pdf/net/aspose-pdf-drawing-graph-shapes-bounds-check/) - vérifier les limites de la forme dans la collection de Formes.

Les détails ci-dessus sont également représentés dans les figures ci-dessous :

![Figures dans les Graphiques](graphs.png)

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