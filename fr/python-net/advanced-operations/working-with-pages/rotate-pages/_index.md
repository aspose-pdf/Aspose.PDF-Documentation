---
title: Faire pivoter les pages PDF en Python
linktitle: Faire pivoter les pages PDF
type: docs
weight: 110
url: /fr/python-net/rotate-pages/
description: Apprenez comment faire pivoter les pages PDF et changer l’orientation des pages en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment faire pivoter les pages dans un PDF avec Python
Abstract: Cet article propose un guide sur la façon de mettre à jour ou de modifier l’orientation des pages d’un fichier PDF existant de manière programmatique avec Python. En utilisant Aspose.PDF for Python via .NET, les utilisateurs peuvent facilement basculer entre les orientations paysage et portrait en ajustant les propriétés MediaBox de la page. L’article comprend un extrait de code Python montrant comment parcourir les pages d’un document PDF, modifier leurs dimensions et positions MediaBox, et ajuster le CropBox si nécessaire. De plus, il explique comment définir l’angle de rotation des pages à l’aide de la méthode ‘rotate’ pour obtenir l’orientation souhaitée. Le processus se termine par l’enregistrement du fichier PDF mis à jour.
---

Ce sujet décrit comment mettre à jour ou modifier l’orientation des pages d’un fichier PDF existant de manière programmatique avec Python.

Utilisez cette page lorsque vous devez basculer les pages entre l'orientation portrait et paysage ou appliquer des angles de rotation au contenu PDF existant.

## Modifier l'orientation de la page

Cette fonction fait pivoter chaque page d'un PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) de 90 degrés dans le sens des aiguilles d'une montre en utilisant Aspose.PDF for Python.
Il est utile pour corriger les problèmes d'orientation des pages, comme les documents numérisés qui sont de travers. Le PDF original reste inchangé, et la version pivotée est enregistrée comme un nouveau fichier.

```python
import sys
import aspose.pdf as ap
from os import path

def rotate_page(infile, outfile):
    document = ap.Document(infile)
    for page in document.pages:
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```

## Sujets de page associés

- [Travailler avec les pages PDF en Python](/pdf/fr/python-net/working-with-pages/)
- [Modifier la taille des pages PDF en Python](/pdf/fr/python-net/change-page-size/)
- [Recadrer les pages PDF en Python](/pdf/fr/python-net/crop-pages/)
- [Obtenir et définir les propriétés de page PDF en Python](/pdf/fr/python-net/get-and-set-page-properties/)