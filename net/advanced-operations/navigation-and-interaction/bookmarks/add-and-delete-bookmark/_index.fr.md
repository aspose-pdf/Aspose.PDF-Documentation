---
title: Ajouter et supprimer un signet
linktitle: Ajouter et supprimer un signet
type: docs
weight: 10
url: /net/add-and-delete-bookmark/
description: Vous pouvez ajouter un signet à un document PDF avec C#. Il est possible de supprimer tous les signets ou des signets particuliers d'un document PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/add-and-delete-a-bookmark/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter et supprimer un signet",
    "alternativeHeadline": "Comment ajouter et supprimer un signet d'un PDF",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "génération de document PDF",
    "keywords": "pdf, c#, supprimer un signet, ajouter un signet",
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
    "url": "/net/add-and-delete-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-and-delete-bookmark/"
    },
    "dateModified": "2022-02-04",
    "description": "Vous pouvez ajouter un signet à un document PDF avec C#. Il est possible de supprimer tous les signets ou des signets particuliers d'un document PDF."
}
</script>
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Ajouter un Signet à un Document PDF

Les signets sont conservés dans la collection [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) de l'objet Document, elle-même dans la collection [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).

Pour ajouter un signet à un PDF :

1. Ouvrir un document PDF en utilisant l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Créer un signet et définir ses propriétés.
1. Ajouter la collection [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) à la collection des contours.

Le code suivant vous montre comment ajouter un signet dans un document PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "AddBookmark.pdf");

// Créer un objet signet
OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfOutline.Title = "Test Outline";
pdfOutline.Italic = true;
pdfOutline.Bold = true;
// Définir le numéro de la page de destination
pdfOutline.Action = new GoToAction(pdfDocument.Pages[1]);
// Ajouter le signet dans la collection de contours du document.
pdfDocument.Outlines.Add(pdfOutline);

dataDir = dataDir + "AddBookmark_out.pdf";
// Sauvegarder le résultat
pdfDocument.Save(dataDir);
```
## Ajouter un signet enfant au document PDF

Les signets peuvent être imbriqués, indiquant une relation hiérarchique avec des signets parent et enfant. Cet article explique comment ajouter un signet enfant, c'est-à-dire un signet de deuxième niveau, à un PDF.

Pour ajouter un signet enfant à un fichier PDF, commencez d'abord par ajouter un signet parent :

1. Ouvrir un document.
1. Ajouter un signet à la collection [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection), en définissant ses propriétés.
1. Ajouter la OutlineItemCollection à la collection [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) de l'objet Document.

Le signet enfant est créé de la même manière que le signet parent, expliqué ci-dessus, mais est ajouté à la collection Outlines du signet parent.

Les extraits de code suivants montrent comment ajouter un signet enfant à un document PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "AddChildBookmark.pdf");

// Créer un objet signet parent
OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfOutline.Title = "Parent Outline";
pdfOutline.Italic = true;
pdfOutline.Bold = true;

// Créer un objet signet enfant
OutlineItemCollection pdfChildOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfChildOutline.Title = "Child Outline";
pdfChildOutline.Italic = true;
pdfChildOutline.Bold = true;

// Ajouter un signet enfant dans la collection du signet parent
pdfOutline.Add(pdfChildOutline);
// Ajouter un signet parent dans la collection de contours du document.
pdfDocument.Outlines.Add(pdfOutline);

dataDir = dataDir + "AddChildBookmark_out.pdf";
// Sauvegarder la sortie
pdfDocument.Save(dataDir);
```
## Supprimer tous les signets d'un document PDF

Tous les signets dans un PDF sont contenus dans la collection [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). Cet article explique comment supprimer tous les signets d'un fichier PDF.

Pour supprimer tous les signets d'un fichier PDF :

1. Appelez la méthode Delete de la collection [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).
1. Enregistrez le fichier modifié en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) de l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Les extraits de code suivants montrent comment supprimer tous les signets d'un document PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "DeleteAllBookmarks.pdf");

// Supprimer tous les signets
pdfDocument.Outlines.Delete();

dataDir = dataDir + "DeleteAllBookmarks_out.pdf";
// Enregistrer le fichier mis à jour
pdfDocument.Save(dataDir);
```
## Supprimer un signet particulier d'un document PDF

Pour supprimer un signet particulier d'un fichier PDF :

1. Passez le titre du signet en paramètre à la méthode Delete de la collection [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).
1. Ensuite, enregistrez le fichier mis à jour avec la méthode Save de l'objet Document.

La classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) fournit la collection [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). La méthode [Delete](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection/methods/delete) supprime tout signet dont le titre est passé à la méthode.

Les extraits de code suivants montrent comment supprimer un signet particulier du document PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "DeleteParticularBookmark.pdf");

// Supprimer un contour particulier par Titre
pdfDocument.Outlines.Delete("Child Outline");

// Enregistrer le fichier mis à jour
pdfDocument.Save(dataDir + "DeleteParticularBookmark_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour .NET Library",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Bibliothèque de manipulation de PDF pour .NET",
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
```

