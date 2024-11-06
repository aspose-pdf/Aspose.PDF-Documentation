---
title: Déplacer des pages PDF de manière programmée en C#
linktitle: Déplacer des pages PDF
type: docs
weight: 20
url: fr/net/move-pages/
description: Essayez de déplacer des pages à l'emplacement souhaité ou à la fin d'un fichier PDF en utilisant Aspose.PDF pour .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Déplacer des pages PDF de manière programmée en C#",
    "alternativeHeadline": "Comment déplacer des pages PDF avec .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, déplacer page pdf",
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
    "url": "/net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Essayez de déplacer des pages à l'emplacement souhaité ou à la fin d'un fichier PDF en utilisant Aspose.PDF pour .NET."
}
</script>

## Déplacer une page d'un document PDF à un autre

Ce sujet explique comment déplacer une page d'un document PDF à la fin d'un autre document en utilisant C#.

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

Pour déplacer une page, nous devons :

1. Créer un objet de classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) avec le fichier PDF source.
1. Créer un objet de classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) avec le fichier PDF de destination.
1. Obtenir la page de la collection [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [Ajouter](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) la page au document de destination.
1. Sauvegarder le PDF de sortie en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [Supprimer](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) la page dans le document source.
1.

Le code suivant vous montre comment déplacer une page.

```csharp
var srcFileName = "<entrez le nom du fichier>";
var dstFileName = "<entrez le nom du fichier>";
var srcDocument = new Document(srcFileName);
var dstDocument = new Document();
var page = srcDocument.Pages[2];
dstDocument.Pages.Add(page);
// Sauvegarder le fichier de sortie
dstDocument.Save(srcFileName);
srcDocument.Pages.Delete(2);
srcDocument.Save(dstFileName);
```

## Déplacement d'un groupe de pages d'un document PDF à un autre

1. Créez un objet de classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) avec le fichier PDF source.
1. Créez un objet de classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) avec le fichier PDF de destination.
1. Définissez un tableau avec les numéros de pages à déplacer.
1. Exécutez une boucle à travers le tableau :
    1. Obtenez la page de la collection [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. Enregistrez le PDF de sortie en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [Supprimez](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/2) la page dans le document source en utilisant un tableau.
1. Enregistrez le PDF source en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Le code suivant montre comment déplacer un ensemble de pages d'un document PDF à un autre.

```csharp
var srcFileName = "<entrez le nom du fichier>";
var dstFileName = "<entrez le nom du fichier>";
var srcDocument = new Aspose.Pdf.Document(srcFileName);
var dstDocument = new Aspose.Pdf.Document();
var pages = new []{ 1, 3 };
foreach (var pageIndex in pages)
{
    var page = srcDocument.Pages[pageIndex];
    dstDocument.Pages.Add(page);
}                       
// Enregistrez les fichiers de sortie
dstDocument.Save(dstFileName);
srcDocument.Pages.Delete(pages);
srcDocument.Save(srcFileName);
```

## Déplacer une page à un nouvel emplacement dans le document PDF actuel

1.
1. Obtenir la page de la collection [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [Ajouter](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) une page à un nouvel emplacement (par exemple à la fin).
1. [Supprimer](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) la page de l'emplacement précédent.
1. Enregistrer le PDF de sortie en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

```csharp
var srcFileName = "<entrez le nom du fichier>";
var dstFileName = "<entrez le nom du fichier>";
var srcDocument = new Aspose.Pdf.Document(srcFileName);

var page = srcDocument.Pages[2];
srcDocument.Pages.Add(page);
srcDocument.Pages.Delete(2);          

// Enregistrer le fichier de sortie
srcDocument.Save(dstFileName);
```

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


