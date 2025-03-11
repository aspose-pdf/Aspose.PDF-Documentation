---
title: Déplacer des pages PDF par programmation C#
linktitle: Déplacer des pages PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/move-pages/
description: Essayez de déplacer des pages à l'emplacement souhaité ou à la fin d'un fichier PDF en utilisant Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Move PDF Pages programmatically C#",
    "alternativeHeadline": "Programmatically Rearrange PDF Pages with .NET",
    "abstract": "Aspose.PDF for .NET introduit une nouvelle fonctionnalité puissante qui permet aux utilisateurs de déplacer par programmation des pages PDF entre des documents ou de les réorganiser au sein du même document. Cette fonctionnalité améliore les capacités de manipulation des PDF en permettant aux développeurs d'insérer des pages à des emplacements désignés et de gérer facilement l'organisation des pages tout en maintenant l'intégrité du document.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "668",
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
    "url": "/net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "Essayez de déplacer des pages à l'emplacement souhaité ou à la fin d'un fichier PDF en utilisant Aspose.PDF for .NET."
}
</script>

## Déplacer une page d'un document PDF à un autre

Ce sujet explique comment déplacer une page d'un document PDF à la fin d'un autre document en utilisant C#.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Pour déplacer une page, nous devrions :

1. Créer un objet de classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) avec le fichier PDF source.
1. Créer un objet de classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) avec le fichier PDF de destination.
1. Obtenir la page de la collection [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [Ajouter](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) la page au document de destination.
1. Enregistrer le PDF de sortie en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [Supprimer](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) la page dans le document source.
1. Enregistrer le PDF source en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Le code suivant vous montre comment déplacer une page.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingAPageFromOnePdfDocumentToAnother()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var srcDocument = new Aspose.Pdf.Document(dataDir + "MovingPageInput.pdf"))
    {
        using (var dstDocument = new Aspose.Pdf.Document())
        {
            var page = srcDocument.Pages[2];
            dstDocument.Pages.Add(page);
            // Save PDF document
            dstDocument.Save(dataDir + "MovingPage_out.pdf");
            srcDocument.Pages.Delete(2);
            // Save PDF document
            srcDocument.Save(dataDir + "MovingPageInput_out.pdf");
        }
    }
}
```

## Déplacer un ensemble de pages d'un document PDF à un autre

1. Créer un objet de classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) avec le fichier PDF source.
1. Créer un objet de classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) avec le fichier PDF de destination.
1. Définir un tableau avec les numéros de pages à déplacer.
1. Exécuter une boucle à travers le tableau :
    1. Obtenir la page de la collection [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
    1. [Ajouter](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) la page au document de destination.
1. Enregistrer le PDF de sortie en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [Supprimer](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/2) la page dans le document source en utilisant le tableau.
1. Enregistrer le PDF source en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Le code suivant vous montre comment déplacer un ensemble de pages d'un document PDF à un autre.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingBunchOfPagesFromOnePdfDocumentToAnother()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var srcDocument = new Aspose.Pdf.Document(dataDir + "MovingBunchOfPagesInput.pdf"))
    {
        using (var dstDocument = new Aspose.Pdf.Document())
        {
            var pages = new[] { 1, 3 };
            foreach (int pageIndex in pages)
            {
                var page = srcDocument.Pages[pageIndex];
                dstDocument.Pages.Add(page);
            }
            // Save PDF document
            dstDocument.Save(dataDir + "MovingBunchOfPages_out.pdf");
            srcDocument.Pages.Delete(pages);
            // Save PDF document
            srcDocument.Save(dataDir + "MovingBunchOfPagesInput_out.pdf";
        }
    }
}
```

## Déplacer une page à un nouvel emplacement dans le document PDF actuel

1. Créer un objet de classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) avec le fichier PDF source.
1. Obtenir la page de la collection [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [Ajouter](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) la page à la nouvelle position (par exemple à la fin).
1. [Supprimer](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) la page à l'emplacement précédent.
1. Enregistrer le PDF de sortie en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingAPageInNewLocationInTheCurrentPdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "MovingAPageInNewLocationInTheCurrentPdfDocumentInput.pdf"))
    {
        var page = document.Pages[2];
        document.Pages.Add(page);
        document.Pages.Delete(2);
        // Save PDF document
        document.Save(dataDir + "MovingAPageInNewLocationInTheCurrentPdfDocument_out.pdf");
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