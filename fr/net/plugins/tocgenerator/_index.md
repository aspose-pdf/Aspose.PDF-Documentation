---
title: ToC Generator
type: docs
weight: 150
url: fr/net/plugins/tocgenerator/
description: Crée une table des matières avec Aspose.PDF ToC Generator pour .NET
lastmod: "2024-01-24"
draft: false
---

Voulez-vous améliorer vos documents PDF en [ajoutant une Table des Matières (TOC)](https://products.aspose.org/pdf/net/toc-generator/) de manière dynamique ? Aspose.PDF pour .NET fournit une puissante classe `TocGenerator` qui vous permet de générer des TOC facilement. Dans ce guide, nous allons parcourir les étapes de base pour créer une TOC dans un document PDF en utilisant Aspose.PDF, en couvrant la création d'un objet `TocGenerator`, l'ajout des chemins d'entrée/sortie, et le processus de génération de la TOC.

## Prérequis

Vous aurez besoin des éléments suivants :

* Visual Studio 2019 ou ultérieur
* Aspose.PDF pour .NET 24.1 ou ultérieur
* Un fichier PDF d'exemple

De plus, familiarisez-vous avec la classe `TocOptions` et ses fonctionnalités. Des informations détaillées peuvent être trouvées dans la [référence API Aspose.PDF](https://reference.aspose.com/pdf/net/aspose.pdf/TocOptions/).

Maintenant, plongeons dans le code et explorons comment générer une Table des Matières pour votre document PDF.
Maintenant, plongeons dans le code et explorons comment générer une Table des Matières pour votre document PDF.

## Exploration du Code

Nous utiliserons la classe `TocGeneratorDemo` avec une méthode `Run` pour démontrer comment créer une ToC. Décortiquons les étapes clés :

```csharp
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation
{
    internal static class TocGeneratorDemo
    {
        private const string PathForSamples = @"C:\Samples\";

        // Exécute la démonstration de génération de la TDM.
        internal static void Run()
        {
            // Crée une nouvelle instance de la classe TocGenerator.
            TocGenerator generator = new();

            // Crée une nouvelle instance de la classe TocOptions.
            TocOptions options = new();
            // Ajoute les chemins d'entrée et de sortie aux TocOptions.
            options.AddInput(new FileDataSource(Path.Combine(PathForSamples, "sample.pdf")));
            options.AddOutput(new FileDataSource(Path.Combine(PathForSamples, "sample_toc.pdf")));

            // Traite la génération de la TDM et obtient le conteneur de résultats.
            var resultContainer = generator.Process(options);

            // Obtient le résultat du conteneur de résultats.
            var result = resultContainer.ResultCollection[0];

            // Imprime le résultat dans la console.
            Console.WriteLine(result);
        }
    }
}
```
### 1. Créer un objet TocGenerator

Le code commence par créer une nouvelle instance de la classe `TocGenerator`. Cette classe fournit des méthodes pour générer des tables des matières pour des documents PDF.

```csharp
TocGenerator generator = new();
```

### 2. Créer TocOptions

Ensuite, une nouvelle instance de la classe `TocOptions` est créée pour configurer le processus de génération de la table des matières. Les chemins des fichiers d'entrée et de sortie sont ajoutés aux options.

```csharp
TocOptions options = new();
options.AddInput(new FileDataSource(Path.Combine(PathForSamples, "sample.pdf")));
options.AddOutput(new FileDataSource(Path.Combine(PathForSamples, "sample_toc.pdf")));
```

### 3. Exécuter le processus de génération de la TOC

La méthode `Process` est ensuite appelée sur l'objet `TocGenerator`, en passant les options configurées. Le conteneur de résultats contient la table des matières générée, et elle est imprimée dans la console.

```csharp
var resultContainer = generator.Process(options);
var result = resultContainer.ResultCollection[0];
Console.WriteLine(result);
```
