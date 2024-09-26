---
title: DOC Converter
type: docs
weight: 10
url: /net/plugins/doc/
description: Convertir un PDF en Word simplifié avec le plugin PdfDoc
lastmod: "2024-01-24"
---

Cet article vous guide dans l'utilisation du [Convertisseur DOC Aspose.Pdf pour .NET](https://products.aspose.org/pdf/net/doc-converter/) pour convertir un document PDF au format Microsoft Word (.doc / .docx).

## Prérequis

Vous aurez besoin des éléments suivants :

* Visual Studio 2019 ou ultérieur
* Aspose.PDF pour .NET 24.1 ou ultérieur
* Un fichier PDF exemple contenant quelques champs de formulaire

Vous pouvez télécharger la bibliothèque Aspose.PDF pour .NET depuis le site officiel ou l'installer en utilisant le Gestionnaire de Paquets NuGet dans Visual Studio.

## Étapes

### 1. Configuration de votre conversion (capture d'écran de la classe FileDataSource)

Le processus de conversion implique trois étapes principales : définir les fichiers d'entrée et de sortie, créer un objet `PdfDoc`, et spécifier les options de conversion.

#### 1.1. Définition des sources de données

* **Fichier d'entrée :** Nous utiliserons la classe `FileDataSource` pour spécifier l'emplacement du fichier PDF que vous souhaitez convertir.
* **Fichier d'entrée :** Nous utiliserons la classe `FileDataSource` pour spécifier l'emplacement du fichier PDF que vous souhaitez convertir.

```csharp
  FileDataSource inputDataSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));
```

  * Remplacez `"C:\Samples\sample.pdf"` par le chemin réel de votre fichier PDF.

* **Fichier de sortie :** De manière similaire, utilisez un autre objet `FileDataSource` pour définir l'emplacement et le nom du fichier du document Word résultant.

```csharp
  FileDataSource outputDataSource = new(Path.Combine(@"C:\Samples\", "sample.docx"));
```

* Remplacez `"C:\Samples\sample.docx"` par le chemin et le nom de fichier de sortie souhaités.

### 2. Création de l'objet Plugin PdfDoc (capture d'écran de la classe PdfDoc)

Ensuite, nous créons une instance de la classe `PdfDoc` pour effectuer la conversion.

```csharp
  var plugin = new PdfDoc();
```

Cet objet sert de moteur pour le processus de conversion.

### 3. Configuration des options de conversion

La classe `PdfToDocOptions` vous permet d'affiner le processus de conversion.
La classe `PdfToDocOptions` vous permet de personnaliser le processus de conversion.

* **Format de Sauvegarde :** Spécifiez le format de sortie désiré pour le document Word. Dans ce cas, nous utilisons `SaveFormat.DocX` pour générer un document compatible Microsoft Word 2007 ou ultérieur (.docx).

* **Mode de Conversion :** Définissez comment le plugin interprète la structure du PDF lors de la conversion. Nous utiliserons `ConversionMode.EnhancedFlow` pour optimiser le document Word résultant en termes de mise en page et de formatage.

Voici le code pour configurer les options :

```csharp
  PdfToDocOptions options = new()
  {
      SaveFormat = SaveFormat.DocX,
      ConversionMode = ConversionMode.EnhancedFlow
  };
```

**Ajout de l'Entrée et de la Sortie :**

Finalement, nous associons les sources de données précédemment définies avec les options de conversion en utilisant les méthodes `AddInput` et `AddOutput` :

```csharp
  options.AddInput(inputDataSource);
  options.AddOutput(outputDataSource);
```

Cela connecte le PDF d'entrée et le document Word de sortie souhaité au processus de conversion.

### 4.
### 4.

Avec tout configuré, lançons la conversion en appelant la méthode `Process` du plugin `PdfDoc` et en passant les options configurées :

```csharp
  var resultContainer = plugin.Process(options);
```

Cette méthode exécute la conversion et retourne un objet `ResultContainer` contenant les détails sur le processus.

**Récupération des résultats :**

Bien que cela ne soit pas essentiel pour une conversion de base, vous pouvez accéder aux résultats via la propriété `ResultCollection` de l'objet `ResultContainer`. Cela peut être utile pour le débogage ou le suivi de détails spécifiques de conversion.

```csharp
  var result = resultContainer.ResultCollection[0];

  // Imprimer le résultat (facultatif à des fins de démonstration)
  Console.WriteLine(result);
```

Avec cette dernière étape, votre document PDF sera converti au format Word spécifié et sauvegardé à l'emplacement de sortie défini.
