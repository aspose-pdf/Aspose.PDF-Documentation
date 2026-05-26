---
title: Supprimer les images d'un fichier PDF à l'aide de Python
linktitle: Supprimer les images
type: docs
weight: 20
url: /fr/python-net/delete-images-from-pdf-file/
description: Apprenez comment supprimer des images spécifiques ou toutes les images des fichiers PDF en Python.
lastmod: "2026-05-22"
TechArticle: true
AlternativeHeadline: Supprimer les images des fichiers PDF avec Python
Abstract: Cet article montre comment supprimer des images des documents PDF avec Aspose.PDF for Python via .NET. Il couvre la suppression d'une ressource d'image spécifique et la suppression de toutes les images d'une page sélectionnée.
---

Utilisez cette page lorsque vous devez supprimer des graphiques inutiles, réduire la taille du PDF ou nettoyer le contenu visuel sensible d'un document.

## Supprimer les images du fichier PDF

Utilisez les étapes suivantes pour supprimer une image d’une page :

1. Chargez le PDF source avec `ap.Document(infile)`.
1. Sélectionnez la page et l’index de la ressource d’image.
1. Supprimer l'image avec `resources.images.delete(index)`.
1. Enregistrez le PDF mis à jour.

```python
import aspose.pdf as ap


def delete_image(infile, outfile):
    document = ap.Document(infile)
    document.pages[1].resources.images.delete(1)
    document.save(outfile)
```

## Supprimer toutes les images d'une page

Utilisez cet exemple pour supprimer chaque image d'une page spécifique.

```python
import aspose.pdf as ap


def delete_all_images_from_page(infile, outfile, page_number):
    document = ap.Document(infile)
    page = document.pages[page_number]

    while len(page.resources.images) != 0:
        page.resources.images.delete(1)

    document.save(outfile)
```

## Sujets liés aux images

- [Travailler avec des images dans les PDF en utilisant Python](/pdf/fr/python-net/working-with-images/)
- [Remplacer les images dans les fichiers PDF existants](/pdf/fr/python-net/replace-image-in-existing-pdf-file/)
- [Extraire les images des fichiers PDF](/pdf/fr/python-net/extract-images-from-pdf-file/)
- [Ajouter des images aux fichiers PDF existants](/pdf/fr/python-net/add-image-to-existing-pdf-file/)