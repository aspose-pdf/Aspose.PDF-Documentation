---
title: Remplacer l'image dans un fichier PDF existant à l'aide de Python
linktitle: Remplacer l'image
type: docs
weight: 70
url: /fr/python-net/replace-image-in-existing-pdf-file/
description: Apprenez à remplacer les images incorporées dans des fichiers PDF existants en Python.
lastmod: "2026-05-22"
TechArticle: true
AlternativeHeadline: Remplacez les images dans des fichiers PDF existants avec Python
Abstract: Cet article montre comment remplacer les images dans des documents PDF avec Aspose.PDF for Python via .NET. Il couvre le remplacement d'une image par index de ressource et le remplacement d'une image spécifique trouvée avec ImagePlacementAbsorber.
---

## Remplacer une image dans le PDF

Utilisez cette page lorsque vous devez mettre à jour les logos, diagrammes ou autres graphiques incorporés dans un PDF sans reconstruire la mise en page du document.

1. Chargez le PDF source avec `ap.Document(infile)`.
1. Ouvrez l'image de remplacement en tant que flux binaire.
1. Remplacez une ressource d'image par son indice sur une page.
1. Enregistrez le PDF mis à jour.

```python
import aspose.pdf as ap
from io import FileIO


def replace_image(infile, image_file, outfile):
    document = ap.Document(infile)

    with FileIO(image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(outfile)
```

## Remplacer une image spécifique

Cet exemple remplace un emplacement d'image spécifique trouvé par `ImagePlacementAbsorber`.

1. Chargez le PDF source.
1. Créer `ImagePlacementAbsorber` et collecter les placements d'images sur la page.
1. Vérifiez si des placements d'images existent sur la page.
1. Remplacez le placement sélectionné par un nouveau flux d'image.
1. Enregistrez le PDF mis à jour.

```python
import aspose.pdf as ap
from io import FileIO


def replace_image_with_absorber(infile, image_file, outfile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(outfile)
```

## Sujets liés aux images

- [Travailler avec des images dans les PDF en utilisant Python](/pdf/fr/python-net/working-with-images/)
- [Supprimer les images des fichiers PDF](/pdf/fr/python-net/delete-images-from-pdf-file/)
- [Extraire les images des fichiers PDF](/pdf/fr/python-net/extract-images-from-pdf-file/)
- [Ajouter des images aux fichiers PDF existants](/pdf/fr/python-net/add-image-to-existing-pdf-file/)
