---
title: Comment fusionner des PDF en utilisant C#
linktitle: Fusionner des fichiers PDF
type: docs
weight: 50
url: fr/net/merge-pdf-documents/
keywords: "fusionner plusieurs pdf en un seul pdf c#, combiner plusieurs pdf en un seul c#, fusionner plusieurs pdf en un seul c#"
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
    "headline": "Comment fusionner des PDF en utilisant C#",
    "alternativeHeadline": "Combiner des documents PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "manipulation de documents PDF",
    "keywords": "pdf, c#, fusionner pdf, concaténer, combiner pdf",
    "wordcount": "212",
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
    "url": "https://docs.aspose.com/pdf/net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://docs.aspose.com/pdf/net/merge-pdf-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "Cette page explique comment fusionner des documents PDF en un seul fichier PDF avec C# ou VB.NET."
}
</script>
## Fusionner ou combiner plusieurs PDF en un seul PDF en C#

Fusionner des PDF en C# n'est pas une tâche simple sans utiliser de bibliothèque tierce.
Cet article montre comment fusionner plusieurs fichiers PDF en un seul document PDF en utilisant Aspose.PDF pour .NET. L'exemple est écrit en C#, mais l'API peut également être utilisée dans d'autres langages de programmation .NET tels que VB.NET. Les fichiers PDF sont fusionnés de sorte que le premier soit joint à la fin de l'autre document.

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Fusionner des fichiers PDF en utilisant C# et DOM

Pour concaténer deux fichiers PDF :

1. Créez deux objets [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), chacun contenant l'un des fichiers PDF d'entrée.
1. Puis appelez la méthode Add de la collection [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) pour l'objet Document auquel vous souhaitez ajouter l'autre fichier PDF.
1.
1. Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Le code suivant montre comment concaténer des fichiers PDF.

```csharp
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Ouvrir le premier document
Document pdfDocument1 = new Document(dataDir + "Concat1.pdf");
// Ouvrir le second document
Document pdfDocument2 = new Document(dataDir + "Concat2.pdf");

// Ajouter les pages du second document au premier
pdfDocument1.Pages.Add(pdfDocument2.Pages);

dataDir = dataDir + "ConcatenatePdfFiles_out.pdf";
// Enregistrer le fichier de sortie concaténé
pdfDocument1.Save(dataDir);
```

## Exemple en direct

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) est une application web gratuite en ligne qui vous permet de découvrir comment fonctionne la fusion de présentations.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

## Voir aussi

- [Diviser PDF en utilisant DOM](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [Diviser un PDF en utilisant DOM](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [Concaténer des documents PDF en utilisant Facades](https://docs.aspose.com/pdf/net/concatenate-pdf-documents/)
- [Diviser un PDF en utilisant Facades](https://docs.aspose.com/pdf/net/split-pdf-pages/)

