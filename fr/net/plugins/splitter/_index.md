---
title: Splitter
type: docs
weight: 120
url: fr/net/plugins/splitter/
description: Divise un document PDF en pages séparées
lastmod: "2024-01-24"
draft: false
---

Avez-vous un grand document PDF que vous souhaitez diviser en fichiers plus petits et plus gérables? Avec [Aspose.PDF Splitter pour .NET](https://products.aspose.org/pdf/net/splitter/), vous pouvez facilement accomplir cette tâche. Dans cet article, nous allons explorer le processus de division d'un document PDF en plusieurs fichiers à l'aide du plugin Aspose.PDF. Plongeons dans le code et parcourons les étapes.

## Prérequis

Vous aurez besoin de ce qui suit :

* Visual Studio 2019 ou ultérieur
* Aspose.PDF pour .NET 24.1 ou ultérieur
* Un fichier PDF exemple

De plus, familiarisez-vous avec la classe `SplitOptions` et ses propriétés. Vous pouvez trouver des informations détaillées sur cette classe dans la [Référence API](https://reference.aspose.com/pdf/net/aspose.pdf/SplitOptions/). Notez que chaque `FileDataSource` de sortie représente une page unique dans les fichiers PDF divisés.

Maintenant, explorons le code fourni et comprenons comment diviser un document PDF.
Maintenant, explorons le code fourni et comprenons comment diviser un document PDF.

## Explication du code

Le code ci-dessous montre une démonstration de division de PDF en utilisant Aspose.PDF.Plugins :

```csharp
using Aspose.Pdf.Plugins;
// ...........

// Définissez le chemin d'entrée du document PDF à diviser.
using var inputStream = File.OpenRead(Path.Combine(@"C:\Samples\", "sample.pdf"));

// Créez une nouvelle instance de Splitter.
var splitter = new Splitter();

// Créez des options pour diviser le document.
var options = new SplitOptions();

// Ajoutez des sources de données d'entrée et de sortie aux options.
options.AddInput(new StreamDataSource(inputStream));

var document = new Aspose.Pdf.Document(inputStream);

for (int i = 1; i <= document.Pages.Count; i++)
{
   var pageNum = string.Format("{0,3}", i.ToString("D3"));
   options.AddOutput(new FileDataSource(Path.Combine(@"C:\Samples\", $"splitter_{pageNum}.pdf")));
}

// Traitez les options pour diviser le document.
var result = splitter.Process(options);
Console.WriteLine(result);
```

Décomposons les étapes clés :
Décortiquons les étapes clés :

1. **Définir le PDF d'entrée**

   Le code commence par spécifier le chemin du document PDF d'entrée à diviser. Ceci est réalisé en utilisant la méthode `File.OpenRead`.

2. **Créer un Objet (Diviseur et Options de Division)**

   Le code crée une instance de la classe `Splitter` pour gérer le processus de division. De plus, une instance de la classe `SplitOptions` est créée pour configurer l'opération de division.

3. **Ajouter une Source de Données (Entrée et Sortie)**

   Le document PDF d'entrée est ajouté aux `SplitOptions` comme une source de données d'entrée en utilisant la méthode `AddInput`. Pour chaque page du document, un chemin de fichier de sortie est ajouté comme une source de données de sortie en utilisant la méthode `AddOutput`.

4. **Exécuter la Méthode Process**

   Le processus de division est initié en appelant la méthode `Process` sur la classe `Splitter`, en passant les `SplitOptions` configurés. Le résultat de l'opération est stocké dans la variable `result`.

5. **Gérer le Résultat**

   Le code imprime le résultat dans la console, fournissant des informations sur le processus de division.
Le code affiche le résultat dans la console, fournissant des informations sur le processus de division.
