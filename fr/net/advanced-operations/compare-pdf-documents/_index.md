---
title: Comparer des documents PDF
linktitle: Comparer PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 130
url: /fr/net/compare-pdf-documents/
description: Depuis la version 24.7, il est possible de comparer le contenu des documents PDF avec des marques d'annotation et une sortie côte à côte
lastmod: "2024-08-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Compare PDF documents",
    "alternativeHeadline": "Enhanced PDF Document Comparison with Visual Highlights",
    "abstract": "La nouvelle fonctionnalité de comparaison PDF dans Aspose.PDF for .NET permet aux utilisateurs d'identifier efficacement les différences entre deux documents PDF, soit par pages spécifiques, soit par l'ensemble du contenu. Avec des sorties côte à côte et des options personnalisables telles que des marqueurs de changement supplémentaires et divers modes de comparaison, cet outil puissant améliore la collaboration en facilitant le suivi et la révision des révisions.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Compare PDF documents, PDF comparison, Aspose.PDF for .NET, comparing specific pages, comparing entire documents, graphical PDF comparer, side-by-side comparison, change markers, document accuracy, ImagesDifference",
    "wordcount": "1367",
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
    "url": "/net/compare-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/compare-pdf-documents/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

Veuillez noter que tous les outils de comparaison sont disponibles dans la bibliothèque [Aspose.PDF.Drawing](https://docs.aspose.com/pdf/net/drawing/).

## Façons de comparer des documents PDF

Lorsque vous travaillez avec des documents PDF, il y a des moments où vous devez comparer le contenu de deux documents pour identifier les différences. La bibliothèque Aspose.PDF for .NET fournit un ensemble d'outils puissant à cet effet. Dans cet article, nous allons explorer comment comparer des documents PDF en utilisant quelques extraits de code simples.

La fonctionnalité de comparaison dans Aspose.PDF vous permet de comparer deux documents PDF page par page. Vous pouvez choisir de comparer soit des pages spécifiques, soit des documents entiers. Le document de comparaison résultant met en évidence les différences, ce qui facilite l'identification des changements entre les deux fichiers.

Voici une liste des façons possibles de comparer des documents PDF en utilisant Aspose.PDF pour la bibliothèque .NET :

1. **Comparer des pages spécifiques** - Comparez les premières pages de deux documents PDF.

1. **Comparer des documents entiers** - Comparez l'ensemble du contenu de deux documents PDF.

1. **Comparer des documents PDF graphiquement** :

- Comparez PDF avec la méthode GetDifference - images individuelles où les changements sont marqués.

- Comparez PDF avec la méthode CompareDocumentsToPdf - document PDF avec des images où les changements sont marqués.

## Comparer des pages spécifiques

Le premier extrait de code démontre comment comparer les premières pages de deux documents PDF.

1. Initialisation du document.
Le code commence par initialiser deux documents PDF en utilisant leurs chemins de fichiers respectifs (documentPath1 et documentPath2). Les chemins sont spécifiés comme des chaînes vides pour l'instant, mais en pratique, vous les remplaceriez par les chemins de fichiers réels.

2. Processus de comparaison.

- Sélection de la page - la comparaison est limitée à la première page de chaque document ('Pages[1]').
- Options de comparaison :

'AdditionalChangeMarks = true' - cette option garantit que des marqueurs de changement supplémentaires sont affichés. Ces marqueurs mettent en évidence les différences qui pourraient être présentes sur d'autres pages, même si elles ne se trouvent pas sur la page actuelle en cours de comparaison.

'ComparisonMode = ComparisonMode.IgnoreSpaces' - ce mode indique au comparateur d'ignorer les espaces dans le texte, se concentrant uniquement sur les changements au sein des mots.

3. Le document de comparaison résultant, qui met en évidence les différences entre les deux pages, est enregistré dans le chemin de fichier spécifié dans 'resultPdfPath'.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparingSpecificPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], dataDir + "ComparingSpecificPages_out.pdf", new Aspose.Pdf.Comparison.SideBySideComparisonOptions
            {
                AdditionalChangeMarks = true,
                ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
            });
        }
    }
}
```

## Comparer des documents entiers

Le deuxième extrait de code élargit le champ d'application pour comparer l'ensemble du contenu de deux documents PDF.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparingEntireDocuments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(
                document1,
                document2,
                dataDir + "ComparingEntireDocuments_out.pdf",
                new Aspose.Pdf.Comparison.SideBySideComparisonOptions
                {
                    AdditionalChangeMarks = true,
                    ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
                });
        }
    }
}
```

Les résultats de comparaison générés par ces extraits sont des documents PDF que vous pouvez ouvrir dans un visualiseur comme Adobe Acrobat. Si vous utilisez la vue à deux pages dans Adobe Acrobat, vous verrez les changements côte à côte :

- Suppressions - celles-ci sont notées sur la page de gauche.
- Insertion - celles-ci sont notées sur la page de droite.

En définissant 'AdditionalChangeMarks' sur 'true', vous pouvez également voir des marqueurs pour les changements qui peuvent se produire sur d'autres pages, même si ces changements ne sont pas sur la page actuelle affichée.

**Aspose.PDF for .NET** fournit des outils robustes pour comparer des documents PDF, que vous ayez besoin de comparer des pages spécifiques ou des documents entiers. En utilisant des options comme 'AdditionalChangeMarks' et différents paramètres 'ComparisonMode', vous pouvez adapter le processus de comparaison à vos besoins spécifiques. Le document résultant fournit une vue claire, côte à côte des changements, facilitant le suivi des révisions et garantissant l'exactitude des documents.

## Comparer des documents PDF en utilisant GraphicalPdfComparer

Lors de la collaboration sur des documents, en particulier dans des environnements professionnels, vous vous retrouvez souvent avec plusieurs versions du même fichier.

Vous pouvez utiliser la classe [GraphicalPdfComparer](https://reference.aspose.com/pdf/fr/net/aspose.pdf.comparison.graphicalcomparison/graphicalpdfcomparer/) pour comparer des documents et des pages PDF. La classe est adaptée pour comparer les changements dans le contenu graphique d'une page.

Avec Aspose.PDF for .NET, il est possible de comparer des documents et des pages et de produire le résultat de la comparaison dans un document PDF ou un fichier image.

Vous pouvez définir les propriétés de classe suivantes :

- Résolution - résolution en unités DPI pour les images de sortie, ainsi que pour les images générées lors de la comparaison.
- Couleur - la couleur des marques de changement.
- Seuil - seuil de changement en pourcentage. La valeur par défaut est zéro. Définir une valeur autre que zéro vous permet d'ignorer les changements graphiques qui sont insignifiants pour vous.

La classe a une méthode qui vous permet d'obtenir les différences d'image de page sous une forme adaptée à un traitement ultérieur : **ImagesDifference GetDifference(Page page1, Page page2)**.

Cette méthode retourne un objet de la classe [ImagesDifference](https://reference.aspose.com/pdf/fr/net/aspose.pdf.comparison.graphicalcomparison/imagesdifference/) qui contient une image de la première page comparée et un tableau de différences. Le tableau de différences et l'image originale ont le format de pixel **RGB24bpp**.

ImagesDifference vous permet de générer une image différente et d'obtenir une image de la deuxième page comparée en ajoutant un tableau de différences à l'image originale. Pour ce faire, utilisez les méthodes **ImagesDifference.GetDestinationImage et ImagesDifference.DifferenceToImage**.

### Comparer PDF avec la méthode GetDifference

Le code fourni définit une méthode [GetDifference](https://reference.aspose.com/pdf/fr/net/aspose.pdf.comparison.graphicalcomparison/imagesdifference/#methods) qui compare deux documents PDF et génère des représentations visuelles des différences entre eux.

Cette méthode compare les premières pages de deux fichiers PDF et génère deux images PNG :

- Une image (diffPngFilePath) met en évidence les différences entre les pages en rouge.
- L'autre image (destPngFilePath) est une représentation visuelle de la page PDF de destination (deuxième).

Ce processus peut être utile pour comparer visuellement les changements ou les différences entre deux versions d'un document.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparePDFWithGetDifferenceMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithGetDifferenceMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithGetDifferenceMethod2.pdf"))
        {
            // Create comparer 
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer();
            // Compare
            using (var imagesDifference = comparer.GetDifference(document1.Pages[1], document2.Pages[1]))
            {
                using (var diffImg = imagesDifference.DifferenceToImage(Aspose.Pdf.Color.Red, Aspose.Pdf.Color.White))
                {
                    diffImg.Save(dataDir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png");
                }
                using (var destImg = imagesDifference.GetDestinationImage())
                {
                    destImg.Save(dataDir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png");
                }
            }
        }
    }
}
```

### Comparer PDF avec la méthode CompareDocumentsToPdf

L'extrait de code fourni utilise la méthode [CompareDocumentsToPdf](https://reference.aspose.com/pdf/fr/net/aspose.pdf.comparison.graphicalcomparison/graphicalpdfcomparer/comparedocumentstopdf/) qui compare deux documents et génère un rapport PDF des résultats de la comparaison.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparePDFWithCompareDocumentsToPdfMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf"))
        {
            // Create comparer
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer()
            {
                Threshold = 3.0,
                Color = Aspose.Pdf.Color.Blue,
                Resolution = new Aspose.Pdf.Devices.Resolution(300)
            };
            // Compare
            comparer.CompareDocumentsToPdf(document1, document2, dataDir + "compareDocumentsToPdf_out.pdf");
        }
    }
}
```