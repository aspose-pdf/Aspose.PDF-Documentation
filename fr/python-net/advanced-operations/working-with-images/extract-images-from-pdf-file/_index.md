---
title: Extraire des images d'un fichier PDF à l'aide de Python
linktitle: Extraire des images
type: docs
weight: 30
url: /fr/python-net/extract-images-from-pdf-file/
description: Apprenez comment extraire des images incorporées à partir de fichiers PDF en Python.
lastmod: "2026-05-22"
TechArticle: true
AlternativeHeadline: Extraire des images de fichiers PDF avec Python
Abstract: Cet article montre comment extraire des images de documents PDF avec Aspose.PDF for Python via .NET. Il couvre l'extraction d'une seule image incorporée et l'exportation des images trouvées dans une région rectangulaire spécifique sur une page.
---

Utilisez cette page lorsque vous devez réutiliser des graphiques incorporés, archiver des ressources d'images, ou traiter le contenu d'images en dehors du PDF.

1. Chargez le PDF source avec `ap.Document(infile)`.
1. Sélectionnez la page cible et l'index de la ressource d'image.
1. Enregistrez l'objet image dans un flux de sortie.

```python
import aspose.pdf as ap
from io import FileIO


def extract_image(infile, outfile):
    document = ap.Document(infile)
    x_image = document.pages[1].resources.images[1]
    with FileIO(outfile, "wb") as output_image:
        x_image.save(output_image)
```

## Extraire des images d'une région spécifique du PDF

Cet exemple extrait les images situées dans une région rectangulaire spécifiée sur une page PDF et les enregistre en fichiers séparés.

1. Chargez le PDF source.
1. Créer `ImagePlacementAbsorber` et l'accepter sur la page cible.
1. Définissez le rectangle cible.
1. Itérez à travers les placements d’images et vérifiez si les limites de chaque image s’insèrent dans la région.
1. Enregistrez les images correspondantes dans les fichiers de sortie.

```python
import aspose.pdf as ap
from io import FileIO


def extract_image_from_specific_region(infile, outfile):
    document = ap.Document(infile)
    rectangle = ap.Rectangle(0, 0, 590, 590, True)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(image_placement.rectangle.llx, image_placement.rectangle.lly)
        point2 = ap.Point(image_placement.rectangle.urx, image_placement.rectangle.ury)

        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(outfile.replace("index", str(index)), "wb") as output_image:
                image_placement.image.save(output_image)
            index += 1
```

## Sujets liés aux images

- [Travailler avec des images dans les PDF en utilisant Python](/pdf/fr/python-net/working-with-images/)
- [Remplacer les images dans les fichiers PDF existants](/pdf/fr/python-net/replace-image-in-existing-pdf-file/)
- [Supprimer les images des fichiers PDF](/pdf/fr/python-net/delete-images-from-pdf-file/)
- [Ajouter des images aux fichiers PDF existants](/pdf/fr/python-net/add-image-to-existing-pdf-file/)
