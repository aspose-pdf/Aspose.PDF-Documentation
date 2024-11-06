---
title: Form Exporter
type: docs
weight: 50
url: fr/net/plugins/formexpoter/
description: Comment exporter les valeurs des champs de formulaire vers des fichiers CSV en utilisant le plugin Aspose.PDF Form Exporter
lastmod: "2024-01-24"
draft: false
---

Dans cet article, nous allons vous montrer comment utiliser le [plugin Form Exporter](https://products.aspose.org/pdf/net/form-exporter/), qui peut exporter les valeurs des champs de formulaire des fichiers PDF vers des fichiers CSV.

## Prérequis

Vous aurez besoin de ce qui suit :

* Visual Studio 2019 ou ultérieur
* Aspose.PDF pour .NET 21.1 ou ultérieur
* Un fichier PDF exemple contenant quelques champs de formulaire

Vous pouvez télécharger la bibliothèque Aspose.PDF pour .NET depuis le site officiel ou l'installer en utilisant le Gestionnaire de Paquets NuGet dans Visual Studio.

## Étapes

Les étapes de base pour exporter les valeurs des champs de formulaire vers des fichiers CSV en utilisant le plugin FormExporter sont :

1. Créer un objet de la classe `FormExporter`
2. Créer un objet de la classe `FormExporterValuesToCsvOptions` et spécifier le prédicat et le délimiteur
3.
1.
1. Exécutez la méthode `Process` de l'objet `FormExporter`

Voyons comment implémenter ces étapes en code C#.

### Étape 1 : Créer un objet de la classe FormExporter

La classe FormExporter est la classe principale qui fournit la fonctionnalité d'exportation des valeurs des champs de formulaire vers des fichiers CSV. Pour l'utiliser, vous devez créer une instance en utilisant le constructeur par défaut :

```cs
// Créez une instance du plugin FormExporter
var plugin = new FormExporter();
```

### Étape 2 : Créer un objet de la classe FormExporterValuesToCsvOptions et spécifier le prédicat et le délimiteur

La classe FormExporterValuesToCsvOptions est une classe d'assistance qui vous permet de spécifier diverses options et paramètres pour le processus d'exportation, tels que le prédicat et le délimiteur.
La classe FormExporterValuesToCsvOptions est une classe d'assistance qui vous permet de spécifier diverses options et paramètres pour le processus d'exportation, tels que le prédicat et le délimiteur.

```cs
// Créer des options pour exporter les valeurs des champs de formulaire en CSV
var options = new FormExporterValuesToCsvOptions(
(field) => { return field is TextBoxField && field.PageIndex == 2; }, ';');
```

### Étape 3 : Ajouter les sources de données d'entrée et de sortie à l'objet options

Les sources de données d'entrée et de sortie sont les fichiers PDF que vous souhaitez exporter et le fichier CSV que vous souhaitez enregistrer.
Les sources de données d'entrée et de sortie sont les fichiers PDF que vous souhaitez exporter et le fichier CSV que vous souhaitez enregistrer.

```cs
// Ajouter les fichiers d'entrée et de sortie aux options
options.AddInput(new FileDataSource("inputFileNameWithFields-1.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-2.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-3.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-4.pdf"));
options.AddOutput(new FileDataSource("outputFileName.csv"));

```

### Étape 4 : Exécuter la méthode Process de l'objet FormExporter

La dernière étape consiste à exécuter la méthode Process de l'objet FormExporter, en passant l'objet options en paramètre.
L'étape finale consiste à exécuter la méthode Process de l'objet FormExporter, en passant l'objet options en paramètre.

```cs
// Traiter les valeurs des champs de formulaire en utilisant le plugin
var resultContainer = plugin.Process(options);
var result = resultContainer.ResultCollection[0];
Console.WriteLine(result);

```

Le résultat contiendra des informations telles que les chemins des fichiers d'entrée et de sortie.
