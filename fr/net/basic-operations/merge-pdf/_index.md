---
title: Comment fusionner des PDF en utilisant C#
linktitle: Fusionner des fichiers PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /fr/net/merge-pdf-documents/
description: Cette page explique comment fusionner des documents PDF en un seul fichier PDF avec C# ou VB.NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Merge PDF using C#",
    "alternativeHeadline": "Combine PDF Effortlessly Using C#",
    "abstract": "Découvrez la puissante capacité de fusionner sans effort plusieurs documents PDF en un seul fichier en utilisant C# avec la bibliothèque Aspose.PDF. Cette fonctionnalité permet aux développeurs de rationaliser leurs flux de travail en combinant efficacement des PDF, tout en préservant la qualité et la structure tout au long du processus. Parfait pour l'intégration logicielle, cette fonctionnalité améliore la productivité en simplifiant les tâches de gestion de documents.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "411",
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
    "url": "/net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/merge-pdf-documents/"
    },
    "dateModified": "2024-11-26",
    "description": "Cette page explique comment fusionner des documents PDF en un seul fichier PDF avec C# ou VB.NET."
}
</script>

## Fusionner ou combiner plusieurs PDF en un seul PDF en C#

Fusionner des PDF en C# n'est pas une tâche simple sans utiliser une bibliothèque tierce.
Cet article montre comment fusionner plusieurs fichiers PDF en un seul document PDF en utilisant Aspose.PDF for .NET. L'exemple est écrit en C# mais l'API peut également être utilisée dans d'autres langages de programmation .NET tels que VB.NET. Les fichiers PDF sont fusionnés de sorte que le premier soit joint à la fin de l'autre document.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Fusionner des fichiers PDF

Pour concaténer deux fichiers PDF :

1. Créez deux objets [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document), chacun contenant l'un des fichiers PDF d'entrée.
1. Ensuite, appelez la méthode Add de la collection [PageCollection](https://reference.aspose.com/pdf/fr/net/aspose.pdf/pagecollection) pour l'objet Document auquel vous souhaitez ajouter l'autre fichier PDF.
1. Passez la collection PageCollection de l'objet Document second à la méthode Add de la première collection PageCollection.
1. Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Save](https://reference.aspose.com/pdf/fr/net/aspose.pdf.document/save/methods/4).

Le code suivant montre comment concaténer des fichiers PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeDocuments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "Concat1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "Concat2.pdf"))
        {
            // Add pages of second document to the first
            document1.Pages.Add(document2.Pages);

            // Save PDF document
            document1.Save(dataDir + "MergeDocuments_out.pdf");
        }
    }
}
```

## Exemple en direct

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) est une application web gratuite en ligne qui vous permet d'explorer comment fonctionne la fonctionnalité de fusion de présentations.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

## Voir aussi

- [Diviser un PDF en utilisant DOM](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [Concaténer des documents PDF en utilisant des façades](https://docs.aspose.com/pdf/net/concatenate-pdf-documents/)
- [Diviser un PDF en utilisant des façades](https://docs.aspose.com/pdf/net/split-pdf-pages/)

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