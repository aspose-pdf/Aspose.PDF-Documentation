---
title: Convertisseur JPEG
type: docs
weight: 90
url: /net/plugins/jpeg/
description: Comment convertir des pages PDF en images JPEG à l'aide du convertisseur JPEG Aspose.PDF
lastmod: "2024-01-24"
draft: false
---

Dans cet article, nous allons vous montrer comment utiliser le [convertisseur JPEG](https://products.aspose.org/pdf/net/jpeg-converter/), qui peut convertir des pages PDF en images JPEG et les enregistrer en tant que fichiers séparés.

## Prérequis

Vous aurez besoin de ce qui suit :

* Visual Studio 2019 ou ultérieur
* Aspose.PDF pour .NET 24.1 ou ultérieur
* Un fichier PDF exemple contenant quelques pages

Vous pouvez télécharger la bibliothèque Aspose.PDF pour .NET depuis le site officiel ou l'installer en utilisant le gestionnaire de paquets NuGet dans Visual Studio.

## Étapes

Les étapes de base pour convertir des pages PDF en images JPEG à l'aide du convertisseur JPEG sont :

1. Créer un objet de la classe Jpeg
1. Créer un objet de la classe JpegOptions et ajouter les chemins des fichiers d'entrée et de sortie
1. Exécuter la méthode Process de l'objet Jpeg et obtenir le conteneur de résultat
1.
1.

Voyons comment implémenter ces étapes en code C#.

### Étape 1 : Créer un objet de la classe Jpeg

La classe Jpeg est la classe principale qui fournit la fonctionnalité de conversion des pages PDF en images JPEG. Pour l'utiliser, vous devez créer une instance à l'aide du constructeur par défaut :

```cs
// Créer une nouvelle instance de Jpeg
var converter = new Jpeg();
```

### Étape 2 : Créer un objet de la classe JpegOptions et ajouter les chemins des fichiers d'entrée et de sortie

La classe JpegOptions est une classe d'assistance qui vous permet de spécifier diverses options et paramètres pour le processus de conversion, tels que la résolution de sortie, la plage de pages, la qualité de l'image, etc.
La classe JpegOptions est une classe d'assistance qui vous permet de spécifier diverses options et paramètres pour le processus de conversion, tels que la résolution de sortie, la plage de pages, la qualité de l'image, etc.

```cs
// Spécifier les chemins de fichier d'entrée et de sortie
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "images");

// Créer une instance de la classe JpegOptions
var converterOptions = new JpegOptions();

// Ajouter les chemins de fichier d'entrée et de sortie aux options
converterOptions.AddInput(new FileDataSource(inputPath));
converterOptions.AddOutput(new FileDataSource(outputPath));
```

Vous pouvez également définir d'autres options, telles que la résolution de sortie, la plage de pages, la qualité de l'image, etc. en utilisant les propriétés de la classe JpegOptions. Par exemple, pour convertir uniquement la première page du fichier PDF en une image JPEG avec une résolution de 300 dpi, vous pouvez utiliser le code suivant :

```cs
// Définir la résolution de sortie à 300 dpi
converterOptions.OutputResolution = 300;

// Définir la plage de pages à la première page
converterOptions.PageRange = new PageRange(1);
```
### Étape 3 : Exécuter la méthode Process de l'objet Jpeg et obtenir le conteneur de résultat

La dernière étape consiste à exécuter la méthode Process de l'objet Jpeg, en passant l'objet converterOptions en paramètre. Cette méthode effectuera la conversion et retournera un objet ResultContainer, qui contient les résultats de la conversion, tels que le statut, les messages, les chemins des fichiers de sortie, etc. Vous pouvez accéder aux résultats en utilisant les propriétés et méthodes de la classe ResultContainer. Par exemple, pour obtenir le conteneur de résultat et imprimer le statut de la conversion, vous pouvez utiliser le code suivant :

```cs
// Traitement de la conversion et obtention du conteneur de résultat
ResultContainer resultContainer = converter.Process(converterOptions);

// Imprimer le statut de la conversion
Console.WriteLine(resultContainer.Status);
```

Le statut de la conversion peut être soit Succès soit Échec, selon que la conversion a été réalisée avec succès ou non.

### Étape 4 : Imprimer les chemins des images JPEG converties

Le conteneur de résultat contient une collection de résultats, un pour chaque chemin de fichier de sortie.
Le conteneur de résultats contient une collection de résultats, un pour chaque chemin de fichier de sortie.

```cs
// Imprimer les chemins des images JPEG converties
foreach (FileResult operationResult in resultContainer.ResultCollection.Cast<FileResult>())
{
  Console.WriteLine(operationResult.Data.ToString());
}
```

Les chemins de fichiers de sortie auront le format de {outputPath}{pageNumber}.jpg, où {outputPath} est le répertoire de sortie et {pageNumber} est le numéro de page du fichier PDF. Par exemple, si le répertoire de sortie est C:\Samples\images et que le fichier PDF a trois pages, les chemins de fichiers de sortie seront :

```text
C:\Samples\images\1.jpg
C:\Samples\images\2.jpg
C:\Samples\images\3.jpg
```
