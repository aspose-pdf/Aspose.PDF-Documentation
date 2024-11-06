---
title: Extracteur de texte
type: docs
weight: 140
url: fr/net/plugins/textextractor/
description: Extrait le contenu texte du document PDF.
lastmod: "2024-01-24"
---

Avez-vous un document PDF dont vous devez [extraire le texte de manière programmatique](https://products.aspose.org/pdf/net/text-extractor/)? Avec Aspose.PDF pour .NET, vous pouvez facilement accomplir cette tâche en utilisant la classe TextExtractor. Dans cet article, nous allons parcourir les étapes de base pour créer une application d'extraction de texte en .NET, couvrant la création d'un objet TextExtractor, l'ajout d'une source de données, et l'exécution du processus d'extraction de texte.

## Prérequis

Vous aurez besoin des éléments suivants :

* Visual Studio 2019 ou ultérieur
* Aspose.PDF pour .NET 24.1 ou ultérieur
* Un fichier PDF d'exemple

De plus, familiarisez-vous avec la classe `TextExtractorOptions` et ses fonctionnalités. Des informations détaillées peuvent être trouvées dans la [référence API Aspose.PDF](https://reference.aspose.com/pdf/net/aspose.pdf/TextExtractorOptions/).

Maintenant, plongeons dans le code et explorons comment extraire du texte d'un document PDF.
Maintenant, plongeons dans le code et explorons comment extraire du texte d'un document PDF.

## Exploration du Code

Le code suivant démontre les capacités d'extraction de texte. Décortiquons les étapes clés :

### 1. Créer un Objet TextExtractor

Le code commence par créer une nouvelle instance de la classe `TextExtractor`. Cette classe fournit des méthodes pour extraire du texte des documents PDF.

```csharp
using TextExtractor extractor = new();
```

### 2. Ajouter une Source de Données

Ensuite, un `FileDataSource` est créé pour le fichier PDF d'entrée. C'est le fichier à partir duquel le texte sera extrait.

```csharp
FileDataSource fileSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));
```

### 3. Créer TextExtractorOptions

Un objet `TextExtractorOptions` est créé pour configurer le processus d'extraction de texte. La source de fichier d'entrée est ajoutée aux options.

```csharp
TextExtractorOptions textExtractorOptions = new();
textExtractorOptions.AddInput(fileSource);
```

### 4. Exécuter le Processus d'Extraction de Texte

La méthode `Process` est ensuite appelée sur l'objet `TextExtractor`, en passant les options configurées.
La méthode `Process` est ensuite appelée sur l'objet `TextExtractor`, en passant les options configurées.

```csharp
var resultContainer = extractor.Process(textExtractorOptions);
var results = resultContainer.ResultCollection;
Console.WriteLine(results[0]);
```

Vous pouvez voir le code complet ci-dessous :

``````cs
using Aspose.Pdf.Plugins;
// ...

// Créez une nouvelle instance de TextExtractor.
using TextExtractor extractor = new();

// Créez un FileDataSource pour le fichier PDF d'entrée.
FileDataSource fileSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));

// Créez TextExtractorOptions.
TextExtractorOptions textExtractorOptions = new();
textExtractorOptions.AddInput(fileSource);

// Traitez l'extraction de texte.
var resultContainer = extractor.Process(textExtractorOptions);
var results = resultContainer.ResultCollection;

// Imprimez le texte extrait.
Console.WriteLine(results[0]);

```

