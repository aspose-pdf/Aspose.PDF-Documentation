---
title: Convertisseur HTML
type: docs
weight: 70
url: fr/net/plugins/html/
description: Comment convertir des fichiers PDF en fichiers HTML et vice versa en utilisant le plugin Aspose.PDF PdfHtml
lastmod: "2024-01-24"
draft: false
---

Dans cet article, nous vous montrerons comment utiliser le [plugin PdfHtml](https://products.aspose.org/pdf/net/html-converter/), qui peut convertir des fichiers PDF en fichiers HTML et vice versa.

## Prérequis

Vous aurez besoin des éléments suivants :

* Visual Studio 2019 ou ultérieur
* Aspose.PDF pour .NET 21.1 ou ultérieur
* Un fichier PDF exemple et un fichier HTML exemple

Vous pouvez télécharger la bibliothèque Aspose.PDF pour .NET depuis le site officiel ou l'installer en utilisant le gestionnaire de paquets NuGet dans Visual Studio.

## Étapes

Les étapes de base pour convertir des fichiers PDF en fichiers HTML et vice versa en utilisant le plugin PdfHtml sont :

1. Créer un objet de la classe PdfHtml
2. Créer un objet de la classe PdfToHtmlOptions ou HtmlToPdfOptions, selon la direction de la conversion
3. Ajouter les sources de données d'entrée et de sortie à l'objet options
4.
### Étape 1 : Créer un objet de la classe PdfHtml

La classe PdfHtml est la classe principale qui offre la fonctionnalité de conversion des fichiers PDF en fichiers HTML et vice versa. Pour l'utiliser, vous devez créer une instance en utilisant le constructeur par défaut :

```cs
// Créer une instance du plugin PdfHtml
var plugin = new PdfHtml();
```

### Étape 2 : Créer un objet de la classe PdfToHtmlOptions ou HtmlToPdfOptions, en fonction de la direction de la conversion

Les classes PdfToHtmlOptions et HtmlToPdfOptions sont des classes d'aide qui vous permettent de spécifier diverses options et paramètres pour le processus de conversion, tels que le format de sortie, la plage de pages, l'encodage, les polices, etc. Pour utiliser ces classes, vous devez créer une instance de la classe appropriée en utilisant le constructeur par défaut ou en passant certains paramètres. Par exemple, pour convertir un fichier PDF en fichier HTML avec des ressources intégrées, vous pouvez utiliser le code suivant :

```cs
### Étape 1: Créer une nouvelle instance de la classe PdfToHtmlOptions

```cs
// Créer une nouvelle instance de la classe PdfToHtmlOptions
var options = new PdfToHtmlOptions(PdfToHtmlOptions.SaveDataType.FileWithEmbeddedResources);
```

Pour convertir un fichier HTML en fichier PDF avec les paramètres par défaut, vous pouvez utiliser le code suivant :

```cs
// Créer une nouvelle instance de la classe HtmlToPdfOptions
var options = new HtmlToPdfOptions();
```

Vous pouvez également définir d'autres options, telles que le format de sortie, la plage de pages, l'encodage, les polices, etc. en utilisant les propriétés des classes d'options. Par exemple, pour convertir un fichier PDF en fichier HTML avec un encodage UTF-8 et la police Arial, vous pouvez utiliser le code suivant :

```cs
// Créer une nouvelle instance de la classe PdfToHtmlOptions
var options = new PdfToHtmlOptions(PdfToHtmlOptions.SaveDataType.FileWithEmbeddedResources);

// Définir l'encodage en UTF-8
options.Encoding = Encoding.UTF8;

// Définir la police en Arial
options.Font = "Arial";
```

### Étape 3: Ajouter les sources de données d'entrée et de sortie à l'objet options

Les sources de données d'entrée et de sortie sont les fichiers PDF ou HTML que vous souhaitez convertir et enregistrer.
Les sources de données d'entrée et de sortie sont les fichiers PDF ou HTML que vous souhaitez convertir et enregistrer.

```cs
// Spécifiez les chemins des fichiers d'entrée et de sortie
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "sample.html");

// Ajoutez les chemins des fichiers d'entrée et de sortie aux options
options.AddInput(new FileDataSource(inputPath));
options.AddOutput(new FileDataSource(outputPath));
```

### Étape 4 : Exécutez la méthode Process de l'objet PdfHtml

La dernière étape consiste à exécuter la méthode Process de l'objet PdfHtml, en passant l'objet options en paramètre. Cette méthode effectuera la conversion et retournera un objet ResultContainer, qui contient les résultats de la conversion, tels que le statut, les messages, les sources de données de sortie, etc. Vous pouvez accéder aux résultats en utilisant les propriétés et méthodes de la classe ResultContainer. Par exemple, pour obtenir le premier résultat de la collection de résultats et l'imprimer dans la console, vous pouvez utiliser le code suivant :

```cs
// Traitez la conversion et obtenez le conteneur de résultats
var resultContainer = plugin.Process(options);

// Obtenez le premier résultat de la collection de résultats
var result = resultContainer.ResultCollection[0];

// Imprimez le résultat dans la console
Console.WriteLine(result);
```
Le résultat contiendra des informations telles que les chemins des fichiers de sortie.
