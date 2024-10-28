---
title: Aspose PDF License
linktitle: Licensing and limitations
type: docs
weight: 90
url: /cpp/licensing/
description: Aspose. PDF pour C++ invite ses clients à obtenir une licence Classique et une Licence Mesurée. Ainsi qu'à utiliser une licence limitée pour mieux explorer le produit.
lastmod: "2021-11-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Limitations de la Version d'Évaluation

Nous souhaitons que nos clients testent nos composants de manière approfondie avant d'acheter, donc la version d'évaluation vous permet de l'utiliser normalement. Cependant, il y aurait les limitations suivantes lors de l'utilisation d'une version d'évaluation de l'API :

**PDF créé avec un filigrane d'évaluation**  
La version d'évaluation d'Aspose.PDF pour C++ fournit toutes les fonctionnalités du produit, mais toutes les pages des documents PDF générés comportent un filigrane avec "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2017 Aspose Pty Ltd" en haut.

**Limite du nombre d'éléments de collection pouvant être traités**

Dans la version d'évaluation, seuls quatre éléments peuvent être traités à partir de n'importe quelle collection (par exemple, seulement quatre pages, quatre champs de formulaire, etc.).

## Appliquer une licence à l'aide d'un fichier ou d'un objet flux

La licence peut être chargée à partir d'un fichier ou d'un objet flux. Aspose.PDF pour C++ essaiera de trouver la licence dans les emplacements suivants :

1. Chemin explicite.
1. Le dossier contenant Aspose.PDF.dll.
1. Le dossier contenant l'assembly qui a appelé Aspose.PDF.dll.
1. Le dossier contenant l'assembly d'entrée (votre .exe).
1. Une ressource intégrée dans l'assembly qui a appelé Aspose.PDF.dll.

La manière la plus simple de définir une licence est de placer le fichier de licence dans le même dossier que le fichier Aspose.PDF.dll et de spécifier le nom du fichier, sans chemin d'accès, comme indiqué dans l'exemple ci-dessous.

### Chargement d'une licence à partir d'un fichier

La manière la plus simple d'appliquer une licence est de placer le fichier de licence dans le même dossier que le fichier Aspose.PDF.dll et de spécifier uniquement le nom du fichier sans chemin d'accès.

{{% alert color="primary" %}}

Lorsque vous appelez la méthode SetLicense, le nom de la licence que vous passez doit être celui du fichier de licence. For example, if you change the license file name to "Aspose.PDF.lic.xml" pass that file name to the Pdf->SetLicense(…) method.

{{% /alert %}}

```cpp
auto lic = MakeObject<Aspose::Pdf::License>();
lic->SetLicense(L"Aspose.PDF.Cpp.lic");
```

### Chargement d'une Licence à partir d'un Objet Stream

L'exemple suivant montre comment charger une licence à partir d'un flux.

```cpp
intrusive_ptr<License>license = new License();
intrusive_ptr<FileStream> myStream = new FileStream(new String("Aspose.PDF.Cpp.lic"), FileMode_Open);

license->SetLicense(myStream);
```

## Licence Mesurée

Aspose.PDF permet aux développeurs d'appliquer une clé mesurée. C'est un nouveau mécanisme de licence. Le nouveau mécanisme de licence sera utilisé en parallèle avec la méthode de licence existante. Les clients qui souhaitent être facturés en fonction de l'utilisation des fonctionnalités de l'API peuvent utiliser la licence mesurée. Pour plus de détails, veuillez vous référer à la section FAQ sur la Licence Mesurée.

Une nouvelle classe Metered a été introduite pour appliquer la clé mesurée. Voici le code d'exemple démontrant comment définir des clés publiques et privées mesurées.

Pour plus de détails, veuillez vous référer à la section [FAQ sur la Licence Mesurée](https://purchase.aspose.com/faqs/licensing/metered).