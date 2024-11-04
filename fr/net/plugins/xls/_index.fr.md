---
title: Convertisseur XLS
type: docs
weight: 20
url: /net/plugins/xls/
description: Comment convertir des fichiers PDF en feuilles de calcul Excel en utilisant les plugins Aspose.Pdf
lastmod: "2024-01-24"
---

{{% alert color="primary" %}}

Dans cet article, nous vous montrerons comment utiliser le [plugin PdfXls](https://products.aspose.org/pdf/net/xls-converter/), qui peut convertir des fichiers PDF en format Excel avec une grande fidélité et précision.

{{% /alert %}}

## Prérequis

Vous aurez besoin des éléments suivants :

* Visual Studio 2019 ou ultérieur
* Aspose.PDF pour .NET 24.1 ou ultérieur
* Un fichier PDF exemple que vous souhaitez convertir au format Excel

Vous pouvez télécharger la bibliothèque Aspose.PDF pour .NET depuis le site officiel ou l'installer en utilisant le Gestionnaire de Packages NuGet dans Visual Studio.

## Étapes

Les étapes de base pour convertir un fichier PDF au format Excel en utilisant le plugin PdfXls sont :

1. Créer un objet de la classe PdfXls
1. Ajouter les sources de données d'entrée et de sortie à l'objet PdfToXlsOptions
1. Exécuter la méthode Process de l'objet PdfXls

Voyons comment implémenter ces étapes en code C#.
Voyons comment implémenter ces étapes en code C#.

### Étape 1 : Créer un objet de la classe PdfXls

La classe PdfXls est la classe principale qui fournit la fonctionnalité de conversion de PDF en Excel. Pour l'utiliser, vous devez créer une instance à l'aide du constructeur par défaut :

```csharp
// Créer une instance du plugin PdfXls
var plugin = new PdfXls();
```

### Étape 2 : Ajouter les sources de données d'entrée et de sortie à l'objet PdfToXlsOptions

La classe PdfToXlsOptions est une classe d'aide qui vous permet de spécifier diverses options et paramètres pour le processus de conversion. Pour l'utiliser, vous devez créer une instance et ajouter les sources de données d'entrée et de sortie en utilisant les méthodes `AddInput` et `AddOutput`. Les sources de données peuvent être soit des chemins de fichiers, soit des flux. Par exemple, pour convertir un fichier PDF nommé `sample.pdf` dans le dossier `C:\Samples` en un fichier Excel nommé `sample.xlsx` dans le même dossier, vous pouvez utiliser le code suivant :

```csharp
// Spécifier les chemins de fichiers d'entrée et de sortie
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "sample.xlsx");

// Créer une instance de la classe PdfToXlsOptions
var options = new PdfToXlsOptions();

// Ajouter les chemins de fichiers d'entrée et de sortie aux options
options.AddInput(new FileDataSource(inputPath));
options.AddOutput(new FileDataSource(outputPath));
```
Vous pouvez également définir d'autres options, telles que le format de sortie, la plage de pages, le nom de la feuille de calcul, etc. en utilisant les propriétés de la classe PdfToXlsOptions. Par exemple, pour convertir le fichier PDF au format XLSX, insérer une colonne vide en première position et nommer la feuille de calcul "MySheet", vous pouvez utiliser le code suivant :

```csharp
// Définir le format de sortie en XLSX
options.Format = PdfToXlsOptions.ExcelFormat.XLSX;

// Insérer une colonne vide en première position
options.InsertBlankColumnAtFirst = true;
```

### Étape 3 : Exécuter la méthode Process de l'objet PdfXls

La dernière étape consiste à exécuter la méthode Process de l'objet PdfXls, en passant l'objet PdfToXlsOptions en paramètre.
La dernière étape consiste à exécuter la méthode Process de l'objet PdfXls, en passant l'objet PdfToXlsOptions en paramètre.

```csharp
// Traiter la conversion du PDF en Excel en utilisant le plugin et les options
var resultContainer = plugin.Process(options);

// Obtenir le premier résultat de la collection de résultats
var result = resultContainer.ResultCollection[0];

// Imprimer le résultat
Console.WriteLine(result);
```

Le résultat contiendra des informations telles que les chemins des fichiers de sortie.
