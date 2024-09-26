---
title: Convertisseur PNG
type: docs
weight: 110
url: /net/plugins/png/
description: Convertir des documents PDF en images PNG avec le plugin Aspose.PDF PNG
lastmod: "2024-01-24"
---

Si vous cherchez à [convertir des documents PDF en images PNG](https://products.aspose.org/pdf/net/png-converter/) en utilisant .NET, Aspose.PDF pour .NET offre une solution robuste. Dans cet article, nous allons parcourir les étapes essentielles pour créer un objet, ajouter une source de données et exécuter la méthode de traitement en utilisant la bibliothèque Aspose.PDF.

## Prérequis

Vous aurez besoin des éléments suivants :

* Visual Studio 2019 ou ultérieur
* Aspose.PDF pour .NET 24.1 ou ultérieur
* Un fichier PDF d'exemple

## Code Walkthrough

Le code ci-dessous montre une démo de conversion PNG utilisant le plugin Aspose.PDF PNG :

```csharp
using Aspose.Pdf.Plugins;

//....

// Créer une nouvelle instance de la classe PngOptions.
var convertorOptions = new PngOptions();

// Ajouter les chemins d'entrée et de sortie aux PngOptions.
convertorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));
convertorOptions.AddOutput(new FileDataSource(Path.Combine(@"C:\Samples\", "images")));

// Définir la résolution de sortie à 300 DPI.
convertorOptions.OutputResolution = 300;

// Créer une nouvelle instance de la classe Png.
Png converter = new ();

// Traiter la conversion PNG et obtenir le conteneur de résultats.
ResultContainer resultContainer = converter.Process(convertorOptions);

// Imprimer le résultat dans la console.
foreach (FileResult operationResult in resultContainer.ResultCollection.Cast<FileResult>())
{
      Console.WriteLine(operationResult.Data.ToString());
}
```
Décortiquons les étapes clés :

1. **Créer un Objet (PngOptions et Png)**

   Le code commence par créer une instance de la classe `PngOptions` pour configurer la conversion en PNG. De plus, une instance de la classe `Png` est créée pour un traitement ultérieur.

2. **Ajouter une Source de Données**

   Le chemin du fichier PDF d'entrée est ajouté à `PngOptions` en utilisant la méthode `AddInput`. De même, le chemin de sortie pour les images PNG est ajouté en utilisant la méthode `AddOutput`.

3. **Définir la Résolution de Sortie**

   Le code définit la résolution de sortie à 300 DPI en utilisant la propriété `OutputResolution` de la classe `PngOptions`.

4. **Exécuter la Méthode Process**

   La conversion en PNG est initiée en appelant la méthode `Process` sur la classe `Png`, en passant les `PngOptions` configurés. Le résultat est stocké dans le `resultContainer`.

5. **Gérer le Résultat**

   Le code imprime le résultat dans la console, montrant le ou les chemins des fichiers convertis.
