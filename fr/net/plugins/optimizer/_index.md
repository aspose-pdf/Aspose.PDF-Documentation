---
title: Optimizer
type: docs
weight: 80
url: /fr/net/plugins/optimizer/
description: Comment optimiser et manipuler des fichiers PDF avec Aspose.PDF Optimizer
lastmod: "2024-01-24"
---

Dans ce chapitre, nous explorerons comment utiliser l'[Aspose.PDF Optimizer](https://products.aspose.org/pdf/net/optimizer/) pour optimiser, redimensionner et faire pivoter des fichiers PDF dans vos applications C#. 
Plongeons et apprenons comment effectuer ces tâches étape par étape.

## Prérequis

Vous aurez besoin de ce qui suit :

* Visual Studio 2019 ou ultérieur
* Aspose.PDF pour .NET 24.1 ou ultérieur
* Un fichier PDF d'exemple contenant quelques champs de formulaire

## Optimisation de fichiers PDF

Optimiser un fichier PDF implique de réduire sa taille et d'améliorer sa performance. Les extraits suivants montrent comment accomplir cette tâche. Voici comment vous pouvez optimiser un fichier PDF :

* Créez une nouvelle source de données de fichier pour le fichier PDF d'entrée.
* Créez une nouvelle source de données de fichier pour le fichier PDF optimisé de sortie.
* Créez une instance de `OptimizeOptions`.
* Ajoutez les sources de données d'entrée et de sortie aux options d'optimisation.
* Ajoutez les sources de données d'entrée et de sortie aux options d'optimisation.
* Créez une instance de `Optimizer` et traitez l'optimisation en utilisant les options d'optimisation.

```cs
// Créez une nouvelle source de données de fichier pour le fichier PDF d'entrée.
var inputDataSource = new FileDataSource(inputPath);

// Créez une nouvelle source de données de fichier pour le fichier PDF optimisé en sortie.
var outputDataSource = new FileDataSource("sample_optimized.pdf");

// Créez une nouvelle instance de OptimizeOptions.
var options = new OptimizeOptions();

// Ajoutez les sources de données d'entrée et de sortie aux options d'optimisation.
options.AddInput(inputDataSource);
options.AddOutput(outputDataSource);

// Créez une nouvelle instance de Optimizer.
var optimizer = new Optimizer();

// Traitez l'optimisation en utilisant les options d'optimisation.
optimizer.Process(options);
```

## Redimensionnement des fichiers PDF

Le redimensionnement d'un fichier PDF implique de changer sa taille de page. Le code suivant montre comment accomplir cette tâche. Suivez ces étapes pour redimensionner un fichier PDF :

* Créez une nouvelle source de données de fichier pour le fichier PDF d'entrée.
* Créer une nouvelle source de données de fichier pour le fichier PDF d'entrée.
* Créer une nouvelle source de données de fichier pour le fichier PDF redimensionné en sortie.
* Créer une instance de `ResizeOptions` et définir la taille de page souhaitée.
* Ajouter les sources de données d'entrée et de sortie aux options de redimensionnement.
* Créer une instance de `Optimizer` et traiter le redimensionnement en utilisant les options de redimensionnement.

```cs
// Créer une nouvelle source de données de fichier pour le fichier PDF d'entrée.
var inputDataSource = new FileDataSource("sample.pdf");

// Créer une nouvelle source de données de fichier pour le fichier PDF redimensionné en sortie.
var outputDataSource = new FileDataSource("sample_resized.pdf");

// Créer une nouvelle instance de ResizeOptions et définir la taille de page souhaitée.
var opt = new ResizeOptions
{
    PageSize = PageSize.PageLetter
};

// Ajouter les sources de données d'entrée et de sortie aux options de redimensionnement.
opt.AddInput(inputDataSource);
opt.AddOutput(outputDataSource);

// Créer une nouvelle instance de Optimizer.
var optimizer = new Optimizer();

// Traiter le redimensionnement en utilisant les options de redimensionnement.
optimizer.Process(opt);
```

## Rotation des pages PDF
## Rotation des pages PDF

La rotation des pages PDF vous permet de changer l'orientation des pages au sein d'un document PDF. Voici comment vous pouvez effectuer la rotation des pages PDF :

* Créer une nouvelle source de données de fichier pour le fichier PDF d'entrée.
* Créer une nouvelle source de données de fichier pour le fichier PDF de sortie.
* Créer une instance de `RotateOptions` et définir la valeur de rotation.
* Ajouter les sources de données d'entrée et de sortie aux options de rotation.
* Créer une instance de `Optimizer` et traiter la rotation en utilisant les options de rotation.

```cs
// Créer une nouvelle source de données de fichier pour le fichier PDF d'entrée.
var inputDataSource = new FileDataSource(inputPath);

// Créer une nouvelle source de données de fichier pour le fichier PDF optimisé de sortie.
var outputDataSource = new FileDataSource("sample_optimized.pdf");

// Créer une nouvelle instance de RotateOptions.
var opt = new RotateOptions();

// Ajouter les sources de données d'entrée et de sortie aux options de rotation.
opt.AddInput(inputDataSource);
opt.AddOutput(outputDataSource);

// Définir la valeur de rotation
opt.Rotation = Rotation.on180;

// Créer une nouvelle instance de Optimizer.
var optimizer = new Optimizer();

// Traiter l'optimisation en utilisant les options de rotation.
optimizer.Process(opt)
```
## Conclusion

Vous avez appris à optimiser, redimensionner et faire pivoter des fichiers PDF en utilisant le plugin Aspose.PDF Optimizer en C#. Intégrez ces techniques dans vos applications pour manipuler efficacement les documents PDF selon vos besoins.
