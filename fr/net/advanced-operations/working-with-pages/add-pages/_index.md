---
title: Ajouter des pages à un document PDF
linktitle: Ajouter des pages
type: docs
weight: 10
url: /fr/net/add-pages/
description: Cet article explique comment insérer (ajouter) une page à l'emplacement souhaité dans un fichier PDF. Apprenez à déplacer, supprimer (effacer) des pages d'un fichier PDF en utilisant C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter des pages dans un PDF avec C#",
    "alternativeHeadline": "Comment ajouter des pages dans un document PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de document PDF",
    "keywords": "pdf, c#, ajouter page pdf, insérer page pdf",
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
    "url": "/net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Cet article explique comment insérer (ajouter) une page à l'emplacement souhaité dans un fichier PDF. Apprenez à déplacer, supprimer (effacer) des pages d'un fichier PDF en utilisant C#."
}
</script>
Aspose.PDF pour .NET offre une flexibilité totale pour travailler avec les pages d'un document PDF en utilisant C# ou tout autre langage .NET. Il maintient toutes les pages d'un document PDF dans [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) qui peut être utilisé pour travailler avec les pages PDF.
Aspose.PDF pour .NET vous permet d'insérer une page dans un document PDF à n'importe quel endroit du fichier ainsi que d'ajouter des pages à la fin d'un fichier PDF.
Cette section montre comment ajouter des pages à un PDF en utilisant C#.

## Ajouter ou Insérer une Page dans un Fichier PDF

Aspose.PDF pour .NET vous permet d'insérer une page dans un document PDF à n'importe quel endroit du fichier ainsi que d'ajouter des pages à la fin d'un fichier PDF.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

### Insérer une Page Vide dans un Fichier PDF à l'Emplacement Souhaité

Pour insérer une page vide dans un fichier PDF :

1. Créez un objet de classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) avec le fichier PDF d'entrée.
1.
1.
1. Enregistrez le PDF de sortie en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Le code suivant montre comment insérer une page dans un fichier PDF.

```cs
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "InsertEmptyPage.pdf");

// Insérer une page vide dans un PDF
pdfDocument.Pages.Insert(2);
// Sauvegarder le fichier de sortie
pdfDocument.Save(dataDir + "InsertEmptyPage_out.pdf");
```

Dans l'exemple ci-dessus, nous avons ajouté une page vide avec les paramètres par défaut. Si vous devez ajuster la taille de la page pour qu'elle soit identique à une autre page du document, vous devez ajouter quelques lignes de code :

```cs
var page = pdfDocument.Pages.Insert(2);
// copier les paramètres de la page depuis la page 1
page.ArtBox = pdfDocument.Pages[1].ArtBox;
page.BleedBox = pdfDocument.Pages[1].BleedBox;
page.CropBox = pdfDocument.Pages[1].CropBox;
page.MediaBox = pdfDocument.Pages[1].MediaBox;
page.TrimBox = pdfDocument.Pages[1].TrimBox;
```
### Ajouter une page vide à la fin d'un fichier PDF

Parfois, vous souhaitez vous assurer qu'un document se termine sur une page vide. Ce sujet explique comment insérer une page vide à la fin du document PDF.

Pour insérer une page vide à la fin d'un fichier PDF :

1. Créez un objet de classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) avec le fichier PDF d'entrée.
1. Appelez la méthode [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) de la collection [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection), sans aucun paramètre.
1. Enregistrez le PDF de sortie en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Le code suivant montre comment insérer une page vide à la fin d'un fichier PDF.

```cs
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "InsertEmptyPageAtEnd.pdf");

// Insérer une page vide à la fin d'un fichier PDF
pdfDocument.Pages.Add();

// Enregistrer le fichier de sortie
pdfDocument.Save(dataDir + "InsertEmptyPageAtEnd_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Bibliothèque Aspose.PDF pour .NET",
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

