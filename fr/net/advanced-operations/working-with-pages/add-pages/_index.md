---
title: Ajouter des pages à un document PDF
linktitle: Ajouter des pages
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/add-pages/
description: Explorez comment ajouter des pages à un PDF existant en .NET avec Aspose.PDF pour améliorer et étendre vos documents.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Pages to PDF Document",
    "alternativeHeadline": "Insert and Manage Pages in PDF Easily with C#",
    "abstract": "La fonctionnalité dans Aspose.PDF for .NET permet aux utilisateurs d'insérer facilement des pages dans un document PDF à tout emplacement spécifié, améliorant la flexibilité et l'organisation du document. Cette fonctionnalité prend non seulement en charge l'ajout de pages, mais inclut également des options pour déplacer ou supprimer des pages existantes à l'aide de C#. Rationalisez votre gestion de PDF avec cet ajout intuitif à votre boîte à outils de développement.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Pages to PDF, insert PDF page, empty page PDF, C# PDF manipulation, PDF document generation, PageCollection, Aspose.PDF for .NET, move PDF pages, remove PDF pages, add pages to PDF",
    "wordcount": "651",
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
    "url": "/net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "Cet article explique comment insérer (ajouter) une page à l'emplacement souhaité dans un fichier PDF. Apprenez à déplacer, supprimer (effacer) des pages d'un fichier PDF à l'aide de C#."
}
</script>

Aspose.PDF for .NET API offre une flexibilité totale pour travailler avec les pages d'un document PDF en utilisant C# ou tout autre langage .NET. Il maintient toutes les pages d'un document PDF dans [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) qui peut être utilisée pour travailler avec des pages PDF.
Aspose.PDF for .NET vous permet d'insérer une page dans un document PDF à tout emplacement dans le fichier ainsi qu'ajouter des pages à la fin d'un fichier PDF.
Cette section montre comment ajouter des pages à un PDF en utilisant C#.

## Ajouter ou insérer une page dans un fichier PDF

Aspose.PDF for .NET vous permet d'insérer une page dans un document PDF à tout emplacement dans le fichier ainsi qu'ajouter des pages à la fin d'un fichier PDF.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

### Insérer une page vide dans un fichier PDF à l'emplacement souhaité

Pour insérer une page vide dans un fichier PDF :

1. Créez un objet de classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) avec le fichier PDF d'entrée.
1. Appelez la méthode [Insert](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection/methods/insert) de la collection [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) avec l'index spécifié.
1. Enregistrez le PDF de sortie en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Le code suivant vous montre comment insérer une page dans un fichier PDF.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "InsertEmptyPage.pdf"))
    {
       // Insert an empty page in a PDF
       document.Pages.Insert(2);
        // Save PDF document
       document.Save(dataDir + "InsertEmptyPage_out.pdf");
    }
}
```

Dans l'exemple ci-dessus, nous avons ajouté une page vide avec des paramètres par défaut. Si vous devez faire en sorte que la taille de la page soit la même que celle d'une autre page dans le document, vous devez ajouter quelques lignes de code :

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPageWithParameters()
{
    var page = document.Pages.Insert(2);
    //copy page parameters from page 1
    page.ArtBox = document.Pages[1].ArtBox;
    page.BleedBox = document.Pages[1].BleedBox;
    page.CropBox = document.Pages[1].CropBox;
    page.MediaBox = document.Pages[1].MediaBox;
    page.TrimBox = document.Pages[1].TrimBox;
}
```

### Ajouter une page vide à la fin d'un fichier PDF

Parfois, vous souhaitez vous assurer qu'un document se termine sur une page vide. Ce sujet explique comment insérer une page vide à la fin du document PDF.

Pour insérer une page vide à la fin d'un fichier PDF :

1. Créez un objet de classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) avec le fichier PDF d'entrée.
1. Appelez la méthode [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) de la collection [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection), sans aucun paramètre.
1. Enregistrez le PDF de sortie en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Le code suivant vous montre comment insérer une page vide à la fin d'un fichier PDF.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPageAtTheEnd()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "InsertEmptyPageAtEnd.pdf"))
    {
        // Insert an empty page at the end of a PDF file
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "InsertEmptyPageAtEnd_out.pdf");
    }
}
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