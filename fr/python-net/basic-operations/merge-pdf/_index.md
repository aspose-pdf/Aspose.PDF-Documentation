---
title: Fusionner des fichiers PDF en Python
linktitle: Fusionner des fichiers PDF
type: docs
weight: 50
url: /fr/python-net/merge-pdf/
description: Apprenez comment fusionner plusieurs fichiers PDF en un seul document en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combiner des pages PDF à l'aide de Python
Abstract: Cet article traite du besoin commun de fusionner plusieurs fichiers PDF en un seul document, un processus précieux pour organiser et optimiser le stockage et le partage de contenu PDF. Il explore l'utilisation d'Aspose.PDF for Python via .NET pour combiner efficacement des fichiers PDF, en reconnaissant que la fusion de PDF en Python peut être difficile sans bibliothèques tierces. L'article fournit un guide étape par étape pour concaténer des fichiers PDF – créer un nouveau document, fusionner les fichiers et enregistrer le document fusionné. Un extrait de code montre l'implémentation à l'aide d'Aspose.PDF, mettant en évidence la capacité de la bibliothèque à rationaliser le processus de fusion. De plus, il présente l'Aspose.PDF Merger, un outil en ligne pour fusionner des PDF, permettant aux utilisateurs d'explorer la fonctionnalité dans un environnement web.
---

## Fusionner des fichiers PDF en utilisant Python et DOM

Concaténer deux fichiers PDF :

1. Créer un Nouveau Document.
1. Fusionner les fichiers PDF
1. Enregistrer le Document fusionné

Combiner plusieurs documents PDF en un seul fichier :

```python
import sys
import aspose.pdf as ap
from os import path

def merge_two_documents(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    document1.pages.add(document2.pages)
    document1.save(outfile)
```

## Exemple en direct

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) est une application web gratuite en ligne qui vous permet d'examiner comment fonctionne la fonctionnalité de fusion de présentations.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

