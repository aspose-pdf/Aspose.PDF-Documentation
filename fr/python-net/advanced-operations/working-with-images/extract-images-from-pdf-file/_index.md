---
title: Extraire des images d'un fichier PDF à l'aide de Python
linktitle: Extraire des images
type: docs
weight: 30
url: /fr/python-net/extract-images-from-pdf-file/
description: Cette section montre comment extraire des images d'un fichier PDF à l'aide d'une bibliothèque Python.
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: Extraire des images du PDF avec Python
Abstract: Cet article explique le processus d'extraction d'images à partir de fichiers PDF à l'aide d'Aspose.PDF pour Python. Il souligne l'utilité de séparer les images à des fins telles que la gestion, l'archivage, l'analyse ou le partage. L'article indique que les images d'un PDF sont stockées dans la collection de ressources de chaque page, en particulier dans la collection XImage. Pour extraire une image, les utilisateurs peuvent accéder à une page particulière et récupérer l'image à l'aide de son indice dans la collection Images. L'objet XImage renvoyé par l'indice fournit une méthode `save()` pour enregistrer l'image extraite. Un extrait de code est fourni pour démontrer les étapes nécessaires pour ouvrir un document PDF, extraire une image spécifique de la deuxième page à l'aide de son indice, et l'enregistrer dans un fichier.
---

Vous devez séparer les images de vos fichiers PDF ? Pour une gestion, un archivage, une analyse ou un partage simplifiés des images de vos documents, utilisez **Aspose.PDF for Python** et extrayez des images de fichiers PDF.

1. Chargez le document PDF avec 'ap.Document()'.
1. Accédez à la page souhaitée du document (document.pages[1]).
1. Sélectionnez l'image parmi les ressources de la page (par exemple, resources.images[1]).
1. Créez un flux de sortie (FileIO) pour le fichier cible.
1. Enregistrez l'image extraite en utilisant 'xImage.save(output_image)'.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    document = ap.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```

## Extraire des images d'une région spécifique dans le PDF

Cet exemple extrait les images situées dans une région rectangulaire spécifiée d'une page PDF et les enregistre en fichiers séparés.

1. Chargez le document PDF en utilisant 'ap.Document'.
1. Créez un 'ImagePlacementAbsorber' pour collecter toutes les images de la première page.
1. Appelez 'document.pages[1].accept(absorber)' pour analyser le placement des images.
1. Parcourez toutes les images dans 'absorber.image_placements' :
- Obtenez la boîte englobante de l'image (llx, lly, urx, ury).
- Vérifiez si les deux coins du rectangle de l'image se trouvent à l'intérieur du rectangle cible (rectangle.contains()).
- Si vrai, enregistrez l'image dans un fichier en utilisant FileIO, en remplaçant 'index' dans le nom de fichier par un numéro séquentiel.
1. Incrémentez l'indice pour chaque image enregistrée.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    rectangle = ap.Rectangle(0, 0, 590, 590, True)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)
    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(
            image_placement.rectangle.llx, image_placement.rectangle.lly
        )
        point2 = ap.Point(
            image_placement.rectangle.urx, image_placement.rectangle.urx
        )
        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(path_outfile.replace("index", str(index)), "w") as output_image:
                image_placement.image.save(output_image)
            index = index + 1
```

## Extraire les informations d'image du PDF

L'exemple ci-dessous montre comment analyser les images intégrées dans une page PDF et calculer leur résolution effective.

1. Ouvrez le PDF avec 'ap.Document'.
1. Suivez l'état graphique lors de la lecture du contenu de la page.
1. Gérez les opérateurs :
- 'GSave'/'GRestore' - empiler/dépiler la matrice.
- 'ConcatenateMatrix' - mettre à jour la transformation.
- 'Do' - si c’est une image, obtenir la taille et appliquer la transformation.
1. Calculez le DPI effectif.
1. Imprimez le nom de l'image, la taille mise à l'échelle et le DPI.

```python

    import aspose.pdf as ap
    from io import FileIO
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
