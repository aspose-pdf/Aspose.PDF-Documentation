---
title: Obtenir et rechercher des images dans un PDF
linktitle: Obtenir et rechercher des images
type: docs
weight: 40
url: /fr/python-net/search-and-get-images-from-pdf-document/
description: Apprenez à rechercher et obtenir des images d'un document PDF en Python avec Aspose.PDF.
lastmod: "2025-09-17"
TechArticle: true
AlternativeHeadline: Recherche et extraction d'images d'un PDF
Abstract: La bibliothèque Aspose.PDF pour Python via .NET offre des capacités robustes pour rechercher et extraire des images de documents PDF. En utilisant la classe 'ImagePlacementAbsorber', les développeurs peuvent localiser et accéder efficacement aux images intégrées sur toutes les pages d'un PDF.
---

## Inspecter les propriétés de placement d'image dans une page PDF

Cet exemple montre comment analyser et afficher les propriétés de toutes les images d'une page PDF spécifique en utilisant Aspose.PDF pour Python via .NET.

1. Créez un 'ImagePlacementAbsorber' pour collecter toutes les images de la page.
1. Appelez 'document.pages[1].accept(absorber)' pour analyser le placement des images sur la première page.
1. Parcourez 'absorber.image_placements' et affichez les propriétés clés de chaque image :
- Largeur et hauteur (points).
- Coordonnées X (LLX) et Y (LLY) du coin inférieur gauche.
- Résolution horizontale (X) et verticale (Y) (DPI).

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        # Display image placement properties for all placements
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))
```

## Extraire et compter les types d'images dans un PDF

Cette fonction analyse toutes les images de la première page d'un PDF et compte combien sont en niveaux de gris et en couleur RVB.

1. Créez un 'ImagePlacementAbsorber' pour collecter toutes les images de la page.
1. Initialisez les compteurs pour les images en niveaux de gris et RVB.
1. Appelez 'document.pages[1].accept(absorber)' pour analyser le placement des images.
1. Affichez le nombre total d'images trouvées.
1. Parcourez chaque image dans 'absorber.image_placements' :
- Obtenez le type de couleur de l'image avec 'image_placement.image.get_color_type()'.
- Incrémentez le compteur correspondant (niveaux de gris ou RVB).
- Affichez un message pour chaque image indiquant si elle est en niveaux de gris ou en RVB.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
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
```

## Extraire des informations détaillées sur les images d'un PDF

Cette fonction analyse toutes les images de la première page d'un PDF et calcule leurs dimensions redimensionnées ainsi que la résolution effective en fonction des transformations graphiques de la page.

1. Chargez le PDF et initialisez les variables
1. Collectez les ressources d'images
1. Traitez les opérateurs de contenu de la page :
- 'GSave' - empile le CTM actuel.
- 'GRestore' - dépile le dernier CTM de la pile.
- 'ConcatenateMatrix' - met à jour le CTM actuel en le multipliant par la matrice de l'opérateur.
1. Affichez le nom de l'image, ses dimensions redimensionnées et la résolution calculée.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)

    default_resolution = 72
    graphics_state = []

    image_names = list(document.pages[1].resources.images.names)

    graphics_state.append(drawing.drawing2d.Matrix(float(1), float(0), float(0), float(1), float(0), float(0)))

    for op in document.pages[1].contents:
        if is_assignable(op, ap.operators.GSave):
            graphics_state.append(cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone())

        elif is_assignable(op, ap.operators.GRestore):
            graphics_state.pop()

        elif is_assignable(op, ap.operators.ConcatenateMatrix):
            opCM = cast(ap.operators.ConcatenateMatrix, op)
            cm = drawing.drawing2d.Matrix(
                float(opCM.matrix.a),
                float(opCM.matrix.b),
                float(opCM.matrix.c),
                float(opCM.matrix.d),
                float(opCM.matrix.e),
                float(opCM.matrix.f),
            )

            graphics_state[-1].multiply(cm)
            continue

        elif is_assignable(op, ap.operators.Do):
            opDo = cast(ap.operators.Do, op)
            if opDo.name in image_names:
                last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                index = image_names.index(opDo.name) + 1
                image = document.pages[1].resources.images[index]

                scaled_width = math.sqrt(last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2)
                scaled_height = math.sqrt(last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2)

                original_width = image.width
                original_height = image.height

                res_horizontal = original_width * default_resolution / scaled_width
                res_vertical = original_height * default_resolution / scaled_height

                print(
                    f"{self.data_dir}image {opDo.name} "
                    f"({scaled_width:.2f}:{scaled_height:.2f}): "
                    f"res {res_horizontal:.2f} x {res_vertical:.2f}"
                )
```

## Extraire le texte alternatif des images dans un PDF

Cette fonction récupère le texte alternatif (alt text) de toutes les images de la première page d'un PDF, utile pour l'accessibilité et les vérifications de conformité PDF/UA.

1. Chargez le document PDF en utilisant 'ap.Document()'.
1. Créez un 'ImagePlacementAbsorber' pour collecter toutes les images de la page.
1. Appliquez l'absorbeur à la première page (page.accept(absorber)).
1. Parcourez chaque image dans 'absorber.image_placements' :
- Affichez le nom de l'image dans la collection de ressources de la page (get_name_in_collection()).
- Récupérez le texte alternatif avec 'get_alternative_text(page)'.
- Affichez la première ligne du texte alternatif.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: "
            + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])
```
