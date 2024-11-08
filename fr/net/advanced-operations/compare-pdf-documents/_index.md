---
title: Comparer des documents PDF
linktitle: Comparer des PDF
type: docs
weight: 180
url: /fr/fr/net/compare-pdf-documents/
description: Depuis la version 24.7, il est possible de comparer le contenu des documents PDF avec des marques d'annotation et une sortie côte à côte
lastmod: "2024-08-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Comparaison de documents PDF avec Aspose.PDF pour .NET

Lorsque vous travaillez avec des documents PDF, il arrive des moments où vous devez comparer le contenu de deux documents pour identifier les différences. La bibliothèque Aspose.PDF pour .NET offre un ensemble d'outils puissant à cet effet. Dans cet article, nous explorerons comment comparer des documents PDF en utilisant quelques extraits de code simples.

La fonctionnalité de comparaison dans Aspose.PDF vous permet de comparer deux documents PDF page par page. Vous pouvez choisir de comparer des pages spécifiques ou des documents entiers. Le document de comparaison résultant met en évidence les différences, facilitant ainsi l'identification des changements entre les deux fichiers.

### Comparaison de pages spécifiques

Le premier extrait de code montre comment comparer les premières pages de deux documents PDF.

Le premier extrait de code montre comment comparer les premières pages de deux documents PDF.

Étapes :

1. Initialisation du document.
Le code commence par initialiser deux documents PDF en utilisant leurs chemins de fichiers respectifs (documentPath1 et documentPath2). Les chemins sont spécifiés comme des chaînes vides pour le moment, mais en pratique, vous les remplaceriez par les chemins de fichiers réels.
2. Processus de comparaison.
- Sélection de la page - la comparaison est limitée à la première page de chaque document ('Pages[1]').
- Options de comparaison :

'AdditionalChangeMarks = true' - cette option garantit que des marqueurs de changement supplémentaires sont affichés. Ces marqueurs mettent en évidence les différences qui pourraient être présentes sur d'autres pages, même si elles ne sont pas sur la page actuelle comparée.

'ComparisonMode = ComparisonMode.IgnoreSpaces' - ce mode indique au comparateur d'ignorer les espaces dans le texte, en se concentrant uniquement sur les changements au sein des mots.

3.
```
```cs
    string documentPath1 = "";
    string documentPath2= "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```

### Comparaison de documents entiers

Le deuxième extrait de code étend le champ d'application pour comparer le contenu entier de deux documents PDF.

Étapes :

1. Initialisation du document.
Tout comme dans le premier exemple, deux documents PDF sont initialisés avec leurs chemins de fichier.
2. Processus de comparaison.
- Comparaison de document entier - contrairement au premier extrait, ce code compare le contenu entier des deux documents.
- Options de comparaison - les options sont les mêmes que dans le premier extrait, garantissant que les espaces sont ignorés et que des marqueurs de changement supplémentaires sont affichés.
```cs
    string documentPath1 = "";
    string documentPath2 = "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1, document2, resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```

Les résultats de comparaison générés par ces extraits sont des documents PDF que vous pouvez ouvrir dans un lecteur comme Adobe Acrobat. Si vous utilisez la vue de deux pages dans Adobe Acrobat, vous verrez les changements côte à côte :

- Suppressions - celles-ci sont notées sur la page de gauche.
- Insertions - celles-ci sont notées sur la page de droite.

En définissant 'AdditionalChangeMarks' sur 'true', vous pouvez également voir des marqueurs pour les changements qui peuvent se produire sur d'autres pages, même si ces changements ne sont pas sur la page actuellement visualisée.

**Aspose.PDF pour .NET** fournit des outils robustes pour comparer des documents PDF, que vous ayez besoin de comparer des pages spécifiques ou des documents entiers.
**Aspose.PDF pour .NET** offre des outils robustes pour comparer des documents PDF, que vous ayez besoin de comparer des pages spécifiques ou des documents entiers.
