---
title: Remplacer une image dans un fichier PDF existant avec Python
linktitle: Remplacer l'image
type: docs
weight: 70
url: /fr/python-net/replace-image-in-existing-pdf-file/
description: Cette section décrit le remplacement d'image dans un fichier PDF existant à l'aide d'une bibliothèque Python.
lastmod: "2025-09-17"
TechArticle: true
AlternativeHeadline: Remplacer une image dans un PDF
Abstract: La documentation Aspose.PDF pour Python via .NET fournit un guide complet sur le remplacement des images dans les fichiers PDF existants. Cette fonctionnalité est essentielle pour des tâches telles que la mise à jour des logos, graphiques ou autres éléments visuels d'un document PDF sans modifier son contenu texte.
---

## Remplacer une image dans un PDF

Comment remplacer une image existante sur une page PDF par une nouvelle image ? Implémentez cela avec Aspose.PDF pour Python via .NET.

1. Importer les modules nécessaires (aspose.pdf, os.path, FileIO).
1. Définir les chemins pour :
- PDF d'entrée (infile)
- Nouveau fichier image (image_file)
- PDF de sortie (outfile)
1. Charger le document PDF en utilisant 'apdf.Document(path_infile)'.
1. Ouvrir le nouveau fichier image en mode lecture binaire.
1. Remplacer la première image de la première page :
- 'document.pages[1].resources.images.replace(1, image_stream)'
1. Enregistrer le PDF mis à jour vers 'path_outfile'.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, outfile)

    document = apdf.Document(path_infile)

    with FileIO(path_image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(path_outfile)
```

## Remplacer une image spécifique

Cet exemple montre comment remplacer une image spécifique sur une page PDF en la localisant grâce à la détection du placement d'image.

1. Charger le PDF en utilisant 'apdf.Document()'.
1. Créer un 'ImagePlacementAbsorber' pour collecter tous les placements d'images sur la page.
1. Appliquer l'absorbeur sur la première page ('document.pages[1].accept(absorber)').
1. Vérifier si des placements d'images existent sur la page.
1. Sélectionner le premier placement d'image (absorber.image_placements[1]) et le remplacer.
1. Enregistrer le PDF modifié vers 'path_outfile'.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, outfile)

    document = apdf.Document(path_infile)

    # Create ImagePlacementAbsorber to find image placements
    absorber = apdf.ImagePlacementAbsorber()

    # Accept the absorber for the first page
    document.pages[1].accept(absorber)

    # Replace the first image placement found
    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(path_image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(path_outfile)
```
