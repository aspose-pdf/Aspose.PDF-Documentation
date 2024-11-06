---
title: Diviser un PDF de manière programmatique
linktitle: Diviser des fichiers PDF
type: docs
weight: 60
url: fr/net/split-pdf-document/
keywords: diviser pdf en plusieurs fichiers, diviser pdf en pdf séparés, diviser pdf c#
description: Ce sujet montre comment diviser les pages PDF en fichiers PDF individuels dans vos applications .NET avec C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/split-document/
    - /net/split-pdf-pages/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Diviser un PDF de manière programmatique",
    "alternativeHeadline": "Comment diviser un PDF avec .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, diviser pdf",
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
    "url": "/net/split-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/split-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Ce sujet montre comment diviser les pages PDF en fichiers PDF individuels dans vos applications .NET avec C#."
}
</script>

## Exemple en direct

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) est une application web gratuite en ligne qui vous permet de découvrir comment fonctionne la fonctionnalité de division de présentations.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Ce sujet montre comment diviser les pages PDF en fichiers PDF individuels dans vos applications .NET. Pour diviser les pages PDF en fichiers PDF d'une seule page en utilisant C#, les étapes suivantes peuvent être suivies :

1. Parcourir les pages du document PDF via la collection [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) de l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. À chaque itération, créer un nouvel objet Document et ajouter l'objet [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) individuel dans le document vide
1. Enregistrer le nouveau PDF en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Diviser un PDF en plusieurs fichiers ou pdf séparés en C#

Le code C# suivant vous montre comment diviser les pages PDF en fichiers PDF individuels.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "SplitToPages.pdf");

int pageCount = 1;

// Boucler sur toutes les pages
foreach (Page pdfPage in pdfDocument.Pages)
{
    Document newDocument = new Document();
    newDocument.Pages.Add(pdfPage);
    newDocument.Save(dataDir + "page_" + pageCount + "_out" + ".pdf");
    pageCount++;
}
```

