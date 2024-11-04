---
title: Fusion
type: docs
weight: 100
url: /net/plugins/merger/
description: Comment fusionner plusieurs fichiers PDF en un seul en utilisant le plugin de fusion Aspose.PDF
lastmod: "2024-01-24"
---

Dans cet article, nous vous montrerons comment utiliser le [plugin de fusion](https://products.aspose.org/pdf/net/merger/), qui peut fusionner plusieurs fichiers PDF en un seul et l'enregistrer comme un nouveau fichier.

## Prérequis

Vous aurez besoin des éléments suivants :

* Visual Studio 2019 ou ultérieur
* Aspose.PDF pour .NET 21.1 ou ultérieur
* Trois fichiers PDF d'exemple que vous souhaitez fusionner

Vous pouvez télécharger la bibliothèque Aspose.PDF pour .NET depuis le site officiel ou l'installer à l'aide du Gestionnaire de Paquets NuGet dans Visual Studio.

## Étapes

Les étapes de base pour fusionner plusieurs fichiers PDF en un seul à l'aide du plugin de fusion sont :

1. Créer un objet de la classe Merger
2. Créer un objet de la classe MergeOptions et ajouter les chemins des fichiers d'entrée et de sortie
3. Exécuter la méthode Process de l'objet Merger

Voyons comment implémenter ces étapes en code C#.

### Étape 1 : Créer un objet de la classe Merger
### Étape 1 : Créer un objet de la classe Merger

La classe Merger est la classe principale qui fournit la fonctionnalité de fusionner plusieurs fichiers PDF en un seul. Pour l'utiliser, vous devez créer une instance à l'aide du constructeur par défaut :

```cs
// Créer une nouvelle instance de Merger
var pdfMerger = new Merger();
```

### Étape 2 : Créer un objet de la classe MergeOptions et ajouter les chemins des fichiers d'entrée et de sortie

La classe MergeOptions est une classe d'assistance qui vous permet de spécifier diverses options et paramètres pour le processus de fusion, tels que la plage de pages, l'ordre, la sécurité, etc.
La classe MergeOptions est une classe d'assistance qui vous permet de spécifier diverses options et paramètres pour le processus de fusion, tels que la plage de pages, l'ordre, la sécurité, etc.

```cs
// Spécifier les chemins de fichiers d'entrée et de sortie
string inputFilePath1 = Path.Combine(@"C:\Samples\", "sample1.pdf");
string inputFilePath2 = Path.Combine(@"C:\Samples\", "sample2.pdf");
string inputFilePath3 = Path.Combine(@"C:\Samples\", "sample3.pdf");
var outputFilePath = "TestMerge.pdf";

// Créer une instance de la classe MergeOptions
var mergeOptions = new MergeOptions();

// Ajouter les chemins de fichiers d'entrée et de sortie aux options
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath1));
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath2));
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath3));
mergeOptions.AddOutput(new FileDataSource(outputFilePath));
```

### Étape 3 : Exécuter la méthode Process de l'objet Merger

La dernière étape consiste à exécuter la méthode Process de l'objet Merger, en passant l'objet mergeOptions en paramètre.
L'étape finale consiste à exécuter la méthode Process de l'objet Merger, en passant l'objet mergeOptions en paramètre.

```cs
// Traiter la fusion et sauvegarder le fichier fusionné
pdfMerger.Process(mergeOptions);

// Imprimer un message de confirmation
Console.WriteLine("Les fichiers PDF ont été fusionnés avec succès.");
```
