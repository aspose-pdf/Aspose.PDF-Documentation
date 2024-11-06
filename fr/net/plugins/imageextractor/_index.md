---
title: Extracteur d'images
type: docs
weight: 80
url: fr/net/plugins/imageextractor/
description: Extraction facile d'images depuis des PDFs avec le plugin ImageExtractor
lastmod: "2024-01-24"
draft: false
---

Si vous avez déjà eu besoin d'extraire des images d'un fichier PDF en utilisant .NET, Aspose.PDF pour .NET offre une solution puissante et simple. Dans ce guide, nous allons parcourir les étapes de base pour créer un objet, ajouter une source de données et exécuter la méthode processus en utilisant l'[Extracteur d'images Aspose.PDF](https://products.aspose.org/pdf/net/image-extractor/).

## Prérequis

Vous aurez besoin de ce qui suit :

* Visual Studio 2019 ou ultérieur
* Aspose.PDF pour .NET 21.1 ou ultérieur
* Un fichier PDF exemple

Vous pouvez télécharger la bibliothèque Aspose.PDF pour .NET depuis le site officiel ou l'installer en utilisant le Gestionnaire de Paquets NuGet dans Visual Studio.
Maintenant, plongeons dans le code et apprenons à utiliser le plugin ImageExtractor.

## Étapes

Le code fourni démontre l'utilisation du plugin `ImageExtractor` pour extraire des images d'un fichier PDF.
Le code fourni démontre l'utilisation du plugin `ImageExtractor` pour extraire des images d'un fichier PDF.

### 1. Créer un Objet (ImageExtractor)

La première étape consiste à créer une instance du plugin `ImageExtractor`. Ceci est réalisé en utilisant le code suivant :

```csharp
using var plugin = new ImageExtractor();
```

Ici, l'instruction `using` assure l'élimination appropriée des ressources lorsque l'opération est terminée.

### 2. Ajouter une Source de Données

Ensuite, une instance de la classe `ImageExtractorOptions` est créée pour configurer le processus d'extraction d'images. Le chemin du fichier d'entrée est ajouté aux options en utilisant la méthode `AddInput` :

```csharp
var imageExtractorOptions = new ImageExtractorOptions();
imageExtractorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));
```

Assurez-vous de remplacer `"C:\Samples\"` et `"sample.pdf"` par le chemin et le nom de fichier appropriés de votre fichier PDF.

### 3. Exécuter la Méthode Process

La dernière étape consiste à traiter l'extraction d'image en utilisant le plugin et les options :

```csharp

```csharp
var resultContainer = plugin.Process(imageExtractorOptions);
```

Le résultat est stocké dans le `resultContainer`, qui contient les images extraites.

### 4. Gérer les images extraites

Après avoir exécuté le processus, vous pouvez récupérer les images extraites du conteneur de résultats. Le code ci-dessous montre comment sauvegarder la première image extraite dans un emplacement temporaire :

```csharp
var imageExtracted = resultContainer.ResultCollection[0].ToStream();
var someTemporaryPlace = File.OpenWrite("C:\\tmp\\tmp.jpg");
imageExtracted.CopyTo(someTemporaryPlace);
```

Assurez-vous de personnaliser le chemin de destination et le nom de fichier selon vos préférences.

Vous pouvez copier l'exemple complet ci-dessous :

```cs
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation;

internal static class ImageExtractorDemo
{
    // <summary>
    // Démontre l'utilisation du plugin ImageExtractor pour extraire des images d'un fichier PDF.
    // </summary>
    internal static void Run()
    {
        // Créez une instance du plugin ImageExtractor.
        using var plugin = new ImageExtractor();

        // Créez une instance de la classe ImageExtractorOptions.
        var imageExtractorOptions = new ImageExtractorOptions();

        // Ajoutez le chemin du fichier d'entrée aux options.
        imageExtractorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));

        // Traitez l'extraction d'image en utilisant le plugin et les options.
        var resultContainer = plugin.Process(imageExtractorOptions);

        // Obtenez l'image extraite du conteneur de résultats.
        var imageExtracted = resultContainer.ResultCollection[0].ToStream();
        var someTemporaryPlace = File.OpenWrite(Path.Combine(@"C:\Samples\","tmp.jpg"));
        imageExtracted.CopyTo(someTemporaryPlace);
    }
}
```

