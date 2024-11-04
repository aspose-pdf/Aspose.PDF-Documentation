---
title: Faire pivoter les pages PDF en utilisant C#
linktitle: Faire pivoter les pages PDF
type: docs
weight: 50
url: /net/rotate-pages/
description: Ce sujet décrit comment faire pivoter l'orientation des pages dans un fichier PDF existant de manière programmatique avec C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Faire pivoter les pages PDF en utilisant C#",
    "alternativeHeadline": "Comment faire pivoter les pages PDF avec .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, faire pivoter la page pdf",
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
    "url": "/net/rotate-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/rotate-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Ce sujet décrit comment faire pivoter l'orientation des pages dans un fichier PDF existant de manière programmatique avec C#."
}
</script>
Ce sujet décrit comment mettre à jour ou changer l'orientation des pages d'un fichier PDF existant de manière programmatique avec C#.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Changer l'Orientation de la Page

Depuis la version 9.6.0 d'Aspose.PDF pour .NET, nous avons ajouté de nouvelles fonctionnalités intéressantes comme le changement de l'orientation de la page de paysage à portrait et vice versa. Pour changer l'orientation de la page, définissez la MediaBox de la page en utilisant le code suivant. Vous pouvez également changer l'orientation de la page en définissant l'angle de rotation avec la méthode Rotate().

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-ChangeOrientation-ChangeOrientation.cs" >}}

## Adapter le Contenu de la Page à la Nouvelle Orientation de la Page

Veuillez noter que lorsque vous utilisez le code ci-dessus, certains contenus du document pourraient être coupés car la hauteur de la page est diminuée. Pour éviter cela, augmentez la largeur proportionnellement et laissez la hauteur intacte. Exemple de calculs :

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-FitPageContents-FitPageContents.cs" >}}
En plus de l'approche ci-dessus, envisagez d'utiliser la façade PdfPageEditor qui peut appliquer un zoom sur le contenu de la page.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-ZoomToPageContents-ZoomToPageContents.cs" >}}

