---
title: Form Exporter
type: docs
weight: 60
url: /net/plugins/formflattener/
description: Comment aplatir les champs de formulaire dans les fichiers PDF en utilisant le plugin Aspose.PDF FormFlattener
lastmod: "2024-01-24"
---

Dans cet article, nous allons vous montrer comment utiliser le [plugin FormFlattener](https://products.aspose.org/pdf/net/form-flattener/), qui peut aplatir les champs de formulaire dans les fichiers PDF.

## Prérequis

Vous aurez besoin de ce qui suit :

* Visual Studio 2019 ou ultérieur
* Aspose.PDF pour .NET 21.1 ou ultérieur
* Un fichier PDF exemple contenant quelques champs de formulaire

Vous pouvez télécharger la bibliothèque Aspose.PDF pour .NET depuis le site officiel ou l'installer en utilisant le Gestionnaire de Paquets NuGet dans Visual Studio.

## Étapes

Les étapes de base pour aplatir les champs de formulaire dans les fichiers PDF en utilisant le plugin FormFlattener sont :

1. Créer un objet de la classe FormFlattener
1. Créer un objet de la classe FormFlattenAllFieldsOptions ou FormFlattenSelectedFieldsOptions, selon que vous voulez aplatir tous les champs ou certains champs
1. Exécutez la méthode Process de l'objet FormFlattener

Voyons comment implémenter ces étapes en code C#.

### Étape 1 : Créer un objet de la classe FormFlattener

La classe FormFlattener est la classe principale qui fournit la fonctionnalité de l'aplatissement des champs de formulaire dans les fichiers PDF. Pour l'utiliser, vous devez créer une instance à l'aide du constructeur par défaut :

```cs
// Créez une instance du plugin FormFlattener
var plugin = new FormFlattener();
```

### Étape 2 : Créer un objet de la classe FormFlattenAllFieldsOptions ou FormFlattenSelectedFieldsOptions, selon que vous souhaitez aplatir tous les champs ou certains champs

Les classes FormFlattenAllFieldsOptions et FormFlattenSelectedFieldsOptions sont des classes d'assistance qui vous permettent de spécifier diverses options et paramètres pour le processus d'aplatissement.
Les classes FormFlattenAllFieldsOptions et FormFlattenSelectedFieldsOptions sont des classes d'assistance qui vous permettent de spécifier diverses options et paramètres pour le processus d'aplatissement.

```cs
// Créer des options pour aplatir tous les champs
var options = new FormFlattenAllFieldsOptions();
```

Pour aplatir uniquement les champs de formulaire dont la coordonnée x du coin inférieur gauche est supérieure à 300, vous pouvez utiliser le code suivant :

```cs
// Créer des options pour aplatir les champs sélectionnés
var options = new FormFlattenSelectedFieldsOptions((field) => field.Rect.LLX > 300);
```

### Étape 3 : Ajouter les sources de données d'entrée et de sortie à l'objet options

Les sources de données d'entrée et de sortie sont les fichiers PDF que vous souhaitez aplatir et enregistrer.
Les sources de données d'entrée et de sortie sont les fichiers PDF que vous souhaitez aplatir et enregistrer.

```cs
// Ajouter les sources de données d'entrée et de sortie aux options
options.Inputs.Add(new FileDataSource("sample.pdf"));
options.Outputs.Add(new FileDataSource("sample-flat.pdf"));
```

### Étape 4 : Exécuter la méthode Process de l'objet FormFlattener

L'étape finale consiste à exécuter la méthode Process de l'objet FormFlattener, en passant l'objet options en paramètre. Cette méthode effectuera le processus d'aplatissement et retournera un objet ResultContainer, qui contient les résultats du processus, tels que le statut, les messages, les sources de données de sortie, etc. Vous pouvez accéder aux résultats en utilisant les propriétés et méthodes de la classe ResultContainer. Par exemple, pour obtenir le premier résultat de la collection de résultats et l'imprimer dans la console, vous pouvez utiliser le code suivant :

```cs
// Traiter les options et obtenir le conteneur de résultats
var resultContainer = plugin.Process(options);

// Obtenir le premier résultat du conteneur de résultats
var result = resultContainer.ResultCollection[0];

// Imprimer le résultat
Console.WriteLine(result);
```
Le résultat contiendra des informations telles que les chemins des fichiers de sortie.
