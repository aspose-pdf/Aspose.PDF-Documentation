---
title: Obtenir et rechercher des images dans le PDF
linktitle: Obtenir et rechercher des images
type: docs
weight: 40
url: /fr/python-net/search-and-get-images-from-pdf-document/
description: Apprenez comment rechercher et inspecter des images dans des documents PDF avec Python.
lastmod: "2026-05-22"
TechArticle: true
AlternativeHeadline: Recherchez et inspectez des images dans des fichiers PDF avec Python.
Abstract: Cet article montre comment rechercher et inspecter les images dans les documents PDF avec Aspose.PDF for Python via .NET. Il couvre l'utilisation de ImagePlacementAbsorber pour analyser le placement, la taille, la résolution et le texte de remplacement des images.
---

## Inspecter les propriétés de placement d'image dans une page PDF

Cet exemple montre comment analyser et afficher les propriétés de toutes les images d'une page PDF spécifique en utilisant Aspose.PDF for Python via .NET.

Utilisez cette page lorsque vous devez auditer le placement des images, inspecter la résolution des images ou identifier les objets image intégrés sur les pages PDF.

1. Créez un 'ImagePlacementAbsorber' pour collecter toutes les images de la page.
1. Appelez 'document.pages[1].accept(absorber)' pour analyser le placement des images sur la première page.
1. Parcourez 'absorber.image_placements' et affichez les propriétés clés de chaque image:
    - Largeur et hauteur (points).
    - Coordonnées X (LLX) et Y (LLY) en bas à gauche.
    - Résolution horizontale (X) et verticale (Y) (DPI).

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_params(infile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))
```

## Extraire et compter les types d'images dans un PDF

Cette fonction analyse toutes les images de la première page d'un PDF et compte combien sont des images en niveaux de gris et RGB.

1. Créez un 'ImagePlacementAbsorber' pour collecter toutes les images de la page.
1. Initialiser les compteurs pour les images en niveaux de gris et RGB.
1. Appelez 'document.pages[1].accept(absorber)' pour analyser le placement des images.
1. Imprimez le nombre total d'images trouvées.
1. Parcourez chaque image dans 'absorber.image_placements' :
    - Obtenez le type de couleur de l'image en utilisant 'image_placement.image.get_color_type()'.
    - Incrémentez le compteur correspondant (grayscaled ou rgb).
    - Affichez un message pour chaque image indiquant si elle est en niveaux de gris ou RGB.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_types_from_pdf(infile):
    """
    Extract and count image types (grayscale/RGB) with resolution analysis.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_image_types_from_pdf("sample_extr.pdf")

    Note:
        Prints total images count, color type for each image, and resolution info.
    """

    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()

    # Counters for grayscale and RGB images
    grayscaled = 0
    rgb = 0

    document.pages[1].accept(absorber)

    print("--------------------------------")
    print("Total Images = " + str(len(absorber.image_placements)))

    image_counter = 1

    for image_placement in absorber.image_placements:
        # Determine the color type of the image
        colorType = image_placement.image.get_color_type()
        if colorType == ap.ColorType.GRAYSCALE:
            grayscaled += 1
            print(f"Image {image_counter} is Grayscale...")
        elif colorType == ap.ColorType.RGB:
            rgb += 1
            print(f"Image {image_counter} is RGB...")
        image_counter += 1

    print("--------------------------------")
    print("Grayscale Images = " + str(grayscaled))
    print("RGB Images = " + str(rgb))
```

## Extraire des informations détaillées sur les images d’un PDF

Cette fonction analyse toutes les images de la première page d’un PDF et calcule leurs dimensions mises à l’échelle ainsi que la résolution effective en fonction des transformations graphiques de la page.

1. Charger le PDF et initialiser les variables
1. Collecter les ressources d’image
1. Traiter les opérateurs de contenu de page :
    - 'GSave' - pousser le CTM actuel sur la pile.
    - 'GRestore' - dépiler le dernier CTM de la pile.
    - 'ConcatenateMatrix' - mettre à jour le CTM actuel en le multipliant par la matrice de l'opérateur.
1. Imprimer le nom de l'image, les dimensions redimensionnées et la résolution calculée.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_information_from_pdf(infile):
    with ap.Document(infile) as document:
        default_resolution = 72
        graphics_state = []

        image_names = list(document.pages[1].resources.images.names)

        graphics_state.append(
            drawing.drawing2d.Matrix(
                float(1), float(0), float(0), float(1), float(0), float(0)
            )
        )

        for op in document.pages[1].contents:
            if is_assignable(op, ap.operators.GSave):
                graphics_state.append(
                    cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone()
                )

            elif is_assignable(op, ap.operators.GRestore):
                graphics_state.pop()

            elif is_assignable(op, ap.operators.ConcatenateMatrix):
                op_cm = cast(ap.operators.ConcatenateMatrix, op)
                cm = drawing.drawing2d.Matrix(
                    float(op_cm.matrix.a),
                    float(op_cm.matrix.b),
                    float(op_cm.matrix.c),
                    float(op_cm.matrix.d),
                    float(op_cm.matrix.e),
                    float(op_cm.matrix.f),
                )

                graphics_state[-1].multiply(cm)
                continue

            elif is_assignable(op, ap.operators.Do):
                op_do = cast(ap.operators.Do, op)
                if op_do.name in image_names:
                    last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                    index = image_names.index(op_do.name) + 1
                    image = document.pages[1].resources.images[index]

                    scaled_width = math.sqrt(
                        last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2
                    )
                    scaled_height = math.sqrt(
                        last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2
                    )

                    original_width = image.width
                    original_height = image.height

                    res_horizontal = (
                        original_width * default_resolution / scaled_width
                    )
                    res_vertical = (
                        original_height * default_resolution / scaled_height
                    )

                    info = (
                        f"{infile} image {op_do.name} "
                        f"({scaled_width:.2f}:{scaled_height:.2f}): "
                        f"res {res_horizontal:.2f} x {res_vertical:.2f}\n"
                    )
                    print(info.rstrip())
```

## Extraire le texte alternatif des images dans un PDF

Cette fonction récupère le texte alternatif (alt text) de toutes les images de la première page d’un PDF, utile pour les vérifications d’accessibilité et de conformité PDF/UA.

1. Chargez le document PDF en utilisant 'ap.Document()'.
1. Créez un 'ImagePlacementAbsorber' pour collecter toutes les images de la page.
1. Acceptez l'absorbeur sur la première page (page.accept(absorber)).
1. Parcourez chaque image dans 'absorber.image_placements' :
    - Imprimez le nom de l'image dans la collection de ressources de la page (get_name_in_collection()).
    - Récupérez le texte alternatif en utilisant 'get_alternative_text(page)'.
    - Imprimez la première ligne du texte alternatif.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_alt_text(infile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: " + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])
```

## Sujets liés aux images

- [Travailler avec des images dans les PDF en utilisant Python](/pdf/fr/python-net/working-with-images/)
- [Extraire les images des fichiers PDF](/pdf/fr/python-net/extract-images-from-pdf-file/)
- [Remplacer les images dans les fichiers PDF existants](/pdf/fr/python-net/replace-image-in-existing-pdf-file/)
- [Ajouter des images aux fichiers PDF existants](/pdf/fr/python-net/add-image-to-existing-pdf-file/)
