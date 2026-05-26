---
title: Ajouter une image au PDF avec Python
linktitle: Ajouter une image
type: docs
weight: 10
url: /fr/python-net/add-image-to-existing-pdf-file/
description: Apprenez comment ajouter des images aux fichiers PDF existants en Python.
lastmod: "2026-05-22"
TechArticle: true
AlternativeHeadline: Ajouter des images aux fichiers PDF existants avec Python
Abstract: Cet article montre comment ajouter des images aux documents PDF avec Aspose.PDF for Python via .NET. Il couvre l'ajout d'une image à des coordonnées fixes, le placement d'images avec des opérateurs de bas niveau, l'attribution d'un texte alternatif pour l'accessibilité et l'intégration d'images avec Flate compression.
---

## Ajouter une image dans un fichier PDF existant

Cet exemple montre comment placer une image à une position fixe sur une page PDF existante en utilisant Aspose.PDF for Python via .NET.

Utilisez ces exemples de cette page lorsque vous devez placer des logos, des photos ou d'autres graphiques à des coordonnées fixes dans une mise en page PDF existante.

1. Chargez un PDF existant avec `ap.Document(infile)`.
1. Sélectionnez la page cible (`document.pages[1]` pour la première page).
1. Appeler `page.add_image()` avec :
    - Le chemin du fichier image.
    - A `Rectangle` définir les coordonnées de placement.
1. Enregistrez le PDF mis à jour.

```python
import aspose.pdf as ap


def add_image(infile, image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))
    document.save(outfile)
```

## Ajouter une image à l'aide d'opérateurs

Cette approche ajoute une image avec des opérateurs PDF de bas niveau au lieu des opérateurs de haut niveau `add_image()` assistant.

1. Créer un nouveau `Document` et ajoutez une page.
1. Ajoutez l'image aux ressources de la page (`page.resources.images`).
1. Créer des opérateurs de transformation (`GSave`, `ConcatenateMatrix`, `Do`, `GRestore`).
1. Ajoutez des opérateurs au contenu de la page.
1. Enregistrez le PDF résultant.

```python
import aspose.pdf as ap
from io import FileIO


def add_image_using_operators(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream)

    rectangle = ap.Rectangle(0, 0, page.media_box.width, page.media_box.height, True)

    operators = [
        ap.operators.GSave(),
        ap.operators.ConcatenateMatrix(
            ap.Matrix(
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            )
        ),
        ap.operators.Do(image_id),
        ap.operators.GRestore(),
    ]

    page.contents.add(operators)
    document.save(outfile)
```

## Ajouter une image avec texte alternatif

Cet exemple ajoute une image et attribue un texte alternatif pour l'accessibilité.

1. Créer un nouveau `Document` et ajoutez une page.
1. Ajouter l'image à la page avec `page.add_image()`.
1. Obtenir des ressources d'image de `page.resources.images`.
1. Définir le texte alternatif en utilisant `try_set_alternative_text()`.
1. Enregistrez le PDF résultant.

```python
import aspose.pdf as ap


def add_image_set_alternative_text(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)

    page.add_image(image_file, ap.Rectangle(0, 0, 842, 595, True))
    resources_images = page.resources.images
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text("Alternative text for image", page)

    if result:
        print("Alternative text has been added successfully")

    document.save(outfile)
```

## Ajouter une image à un PDF avec la compression Flate

Cet exemple intègre une image en utilisant `ImageFilterType.FLATE` compression.

1. Créer un nouveau `Document` et ajoutez une page.
1. Ajouter l'image aux ressources de la page avec la compression Flate.
1. Utiliser les opérateurs de matrice pour placer et dessiner l'image.
1. Enregistrez le document.

```python
import aspose.pdf as ap
from io import FileIO


def add_image_to_pdf_with_flate_compression(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream, ap.ImageFilterType.FLATE)

    rectangle = ap.Rectangle(0, 0, 600, 600, True)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.lly,
    )

    page.contents.add([ap.operators.GSave()])
    page.contents.add([ap.operators.ConcatenateMatrix(matrix)])
    page.contents.add([ap.operators.Do(image_id)])
    page.contents.add([ap.operators.GRestore()])

    document.save(outfile)
```

## Sujets liés aux images

- [Travailler avec des images dans les PDF en utilisant Python](/pdf/fr/python-net/working-with-images/)
- [Remplacer les images dans les fichiers PDF existants](/pdf/fr/python-net/replace-image-in-existing-pdf-file/)
- [Supprimer les images des fichiers PDF](/pdf/fr/python-net/delete-images-from-pdf-file/)
- [Extraire les images des fichiers PDF](/pdf/fr/python-net/extract-images-from-pdf-file/)
