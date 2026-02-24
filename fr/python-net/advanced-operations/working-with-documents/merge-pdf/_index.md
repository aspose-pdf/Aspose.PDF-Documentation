---
title: Comment fusionner des PDF avec Python
linktitle: Fusionner des fichiers PDF
type: docs
weight: 50
url: /fr/python-net/merge-pdf-documents/
description: Cette page explique comment fusionner des documents PDF en un seul fichier PDF avec Python.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combiner les pages PDF avec Python
Abstract: Cet article répond au besoin fréquent de fusionner plusieurs fichiers PDF en un seul document, un processus utile pour organiser, optimiser le stockage et le partage de contenu PDF. Il explore l'utilisation d'Aspose.PDF pour Python via .NET afin de combiner efficacement les fichiers PDF, en reconnaissant que la fusion de PDF avec Python peut être difficile sans bibliothèques tierces. L'article propose un guide étape par étape pour concaténer les fichiers PDF – créer un nouveau document, fusionner les fichiers et enregistrer le document fusionné. Un extrait de code montre la mise en œuvre avec Aspose.PDF, soulignant la capacité de la bibliothèque à simplifier le processus de fusion. De plus, il présente Aspose.PDF Merger, un outil en ligne de fusion de PDF, permettant aux utilisateurs d'explorer la fonctionnalité dans un environnement web.
---

## Fusionner ou combiner plusieurs PDF en un seul PDF avec Python

Combiner des fichiers PDF est une requête très populaire parmi les utilisateurs. Cela peut être utile lorsque vous avez plusieurs fichiers PDF que vous souhaitez partager ou stocker ensemble en un seul document.

Fusionner des fichiers PDF peut vous aider à organiser vos documents, libérer de l'espace de stockage sur votre PC et partager plusieurs fichiers PDF avec d'autres en les combinant en un seul document.

Fusionner des PDF en Python via .NET n'est pas une tâche simple sans l'utilisation d'une bibliothèque tierce.
Cet article montre comment fusionner plusieurs fichiers PDF en un seul document PDF en utilisant Aspose.PDF pour Python via .NET.

## Fusionner des fichiers PDF avec Python et DOM

Pour concaténer deux fichiers PDF :

1. Créez un nouveau document.
1. Fusionnez les fichiers PDF
1. Enregistrez le document fusionné

Combiner plusieurs documents PDF en un seul fichier :

```python

    import aspose.pdf as apdf
    import aspose.pydrawing as asdrw
    from io import FileIO
    from os import path

    path_infile1 = path.join(self.dataDir, infile1)
    path_infile2 = path.join(self.dataDir, infile2)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document()
    document.merge(files=[path_infile1, path_infile2])
    document.save(path_outfile)
```

## Exemple en direct

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) est une application web gratuite en ligne qui vous permet d'examiner le fonctionnement de la fonctionnalité de fusion de présentations.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)


