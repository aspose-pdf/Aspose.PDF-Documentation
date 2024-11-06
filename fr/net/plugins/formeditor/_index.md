---
title: Éditeur de Formulaire
type: docs
weight: 40
url: fr/net/plugins/formeditor/
description: Comment ajouter, mettre à jour et supprimer des champs de formulaire dans les fichiers PDF en utilisant les plugins Aspose.PDF
lastmod: "2024-01-24"
draft: false
---

Dans cet article, nous allons vous montrer comment utiliser le [plugin Éditeur de Formulaire](https://products.aspose.org/pdf/net/form-editor/), qui peut ajouter, mettre à jour et supprimer des champs de formulaire dans les fichiers PDF.

## Prérequis

Vous aurez besoin des éléments suivants :

* Visual Studio 2019 ou ultérieur
* Aspose.PDF pour .NET 24.1 ou ultérieur
* Un fichier PDF exemple contenant quelques champs de formulaire

Vous pouvez télécharger la bibliothèque Aspose.PDF pour .NET depuis le site officiel ou l'installer à l'aide du gestionnaire de paquets NuGet dans Visual Studio.

## Étapes

Les étapes de base pour ajouter, mettre à jour et supprimer des champs de formulaire dans les fichiers PDF en utilisant le plugin FormEditor sont :

1. Créer un objet de la classe FormEditor
1. Créer un objet de la classe FormEditorAddOptions, FormEditorSetOptions, ou FormRemoveSelectedFieldsOptions, selon l'opération que vous souhaitez effectuer
1.
1.
1. Exécuter la méthode Process de l'objet FormEditor

Voyons comment implémenter ces étapes en code C# pour chaque opération.

### Étape 1 : Créer un objet de la classe FormEditor

La classe FormEditor est la classe principale qui offre la fonctionnalité d'ajouter, de mettre à jour et de supprimer des champs de formulaire dans des fichiers PDF. Pour l'utiliser, vous devez créer une instance de celle-ci en utilisant le constructeur par défaut :

```cs
// Créer une instance du plugin FormEditor
var plugin = new FormEditor();
```

### Étape 2 : Créer un objet de la classe FormEditorAddOptions, FormEditorSetOptions, ou FormRemoveSelectedFieldsOptions, selon l'opération que vous souhaitez effectuer

Les classes `FormEditorAddOptions`, `FormEditorSetOptions` et `FormRemoveSelectedFieldsOptions` sont des classes auxiliaires qui vous permettent de spécifier diverses options et paramètres pour les opérations d'édition de formulaire, telles que les types de champs de formulaire, les valeurs, les propriétés, les prédicats, etc.
Les classes `FormEditorAddOptions`, `FormEditorSetOptions` et `FormRemoveSelectedFieldsOptions` sont des classes d'assistance qui vous permettent de spécifier diverses options et paramètres pour les opérations d'édition de formulaire, telles que les types de champs de formulaire, les valeurs, les propriétés, les prédicats, etc.

```cs
    // Créer des options pour ajouter des champs de formulaire.
    var options = new FormEditorAddOptions(
        [
            // Créer un champ de formulaire case à cocher.
            new FormCheckBoxFieldCreateOptions(1, new Rectangle(110, 700, 125, 715))
            {
                Value = "CheckBoxField 1",
                PartialName = "CheckBoxField_1",
                Color = Color.Blue,
            },
            // Créer un champ de formulaire liste déroulante.
            new FormComboBoxFieldCreateOptions(1, new Rectangle(310, 600, 350, 615))
            {
                Color = Color.Red,
                Editable = true,
                DefaultAppearance = new DefaultAppearance("Arial Bold", 12, System.Drawing.Color.DarkGreen),
                Options = ["option1", "option2", "option3"],
                Selected = 2
            },
            // Créer un champ de formulaire zone de texte.
            new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715))
            {
                MaxLen = 10,
                Value = "Some text",
                Color = Color.Chocolate
            }
        ]);
```
Pour mettre à jour les valeurs des champs de formulaire dont les valeurs sont "a value" ou "an another value" en "new value", vous pouvez utiliser le code suivant :

```cs
    var options = new FormEditorSetOptions(
    (field) => { return field.Value == "a value" || field.Value == "an another value"; },
    new FormFieldSetOptions()
    {
        Value = "new value"
    });
```

Pour supprimer les champs de formulaire dont la coordonnée x du bas gauche est supérieure à 300, vous pouvez utiliser le code suivant :

```cs
// Créer des options pour supprimer les champs de formulaire
var options = new FormRemoveSelectedFieldsOptions((field) => field.Rect.LLX > 300);
```

### Étape 3 : Ajouter les sources de données d'entrée et de sortie à l'objet options

Les sources de données d'entrée et de sortie sont les fichiers PDF que vous souhaitez modifier et enregistrer.
Les sources de données d'entrée et de sortie sont les fichiers PDF que vous souhaitez modifier et enregistrer.

```cs
// Spécifiez les chemins de fichiers d'entrée et de sortie
string inputPath = $@"C:\Samples\Output\sample_forms.pdf";
string outputPath = $@"C:\Samples\Output\sample_forms2.pdf";

// Créez une nouvelle instance de la classe FileDataSource pour les fichiers d'entrée et de sortie
FileDataSource inputData = new(inputPath);
FileDataSource outputData = new(outputPath);

// Ajoutez les sources de données d'entrée et de sortie aux options
options.AddInput(inputData);
options.AddOutput(outputData);
```

### Étape 4 : Exécutez la méthode Process de l'objet FormEditor

La dernière étape consiste à exécuter la méthode Process de l'objet FormEditor, en passant l'objet options en paramètre.
La dernière étape consiste à exécuter la méthode Process de l'objet FormEditor, en passant l'objet options en paramètre.

```cs
// Traiter l'opération d'édition de formulaire en utilisant le plugin et les options
ResultContainer result = plugin.Process(options);

// Obtenir le premier résultat de la collection de résultats
var result = resultContainer.ResultCollection[0];

// Imprimer le résultat
Console.WriteLine(result);
```

Le résultat contiendra des informations telles que les chemins des fichiers de sortie.
