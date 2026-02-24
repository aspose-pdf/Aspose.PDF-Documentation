---
title: Ajouter une image à un PDF avec Python
linktitle: Ajouter une image
type: docs
weight: 10
url: /fr/python-net/add-image-to-existing-pdf-file/
description: Cette section décrit comment ajouter une image à un fichier PDF existant en utilisant une bibliothèque Python.
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: Comment ajouter des images dans un PDF avec Python
Abstract: Cet article fournit des conseils sur l'ajout d'images à des fichiers PDF existants en utilisant Python avec la bibliothèque Aspose.PDF. Deux méthodes sont présentées pour y parvenir. La première méthode utilise la classe `Document` d'Aspose.PDF, où l'utilisateur charge le PDF, spécifie le numéro de page et utilise la méthode `add_image` de la classe `Page` pour positionner l'image. Le document est ensuite enregistré avec la méthode `save()`. La deuxième méthode utilise la classe `PdfFileMend` du namespace Aspose.PDF.Facades, qui offre une interface plus simple. Ici, la méthode `add_image()` est invoquée pour ajouter l'image à la page et aux coordonnées spécifiées, suivie de l'enregistrement du PDF mis à jour et de la fermeture de l'objet `PdfFileMend`. Des extraits de code sont fournis pour les deux méthodes afin de démontrer le processus.
---

## Ajouter une image dans un fichier PDF existant

Cet exemple montre comment insérer une image à une position spécifique sur une page PDF en utilisant Aspose.PDF pour Python via .NET.

1. Chargez le document PDF avec 'ap.Document'.
1. Sélectionnez la page cible '(document.pages[1]' - la première page.
1. Utilisez 'page.add_image()' pour placer l'image :
- Chemin du fichier de l'image.
- Un objet 'Rectangle' définissant les coordonnées de l'image (left=20, bottom=730, right=120, top=830).
1. Enregistrez le PDF mis à jour.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    page = document.pages[1]
    page.add_image(
        path.join(self.data_dir, image_file),
        ap.Rectangle(20, 730, 120, 830, True),
    )
    document.save(path_outfile)
```

## Ajouter une image en utilisant des opérateurs

Le morceau de code suivant montre une approche bas niveau pour ajouter une image à une page PDF en manipulant manuellement les opérateurs PDF plutôt qu'en utilisant des méthodes d'aide de haut niveau.

Étapes :

1. Créez un nouveau 'Document' vierge.
1. Ajoutez une page et définissez sa taille (842 × 595 - A4 paysage).
1. Accédez aux ressources d'images de la page (page.resources.images).
1. Chargez le fichier image dans un flux et ajoutez-le aux ressources.
- La méthode renvoie un 'image_id'.
- L'objet image nouvellement ajouté est récupéré à partir des ressources.
1. Définissez un rectangle qui maintient le ratio d'aspect de l'image :
1. Construisez une séquence d'opérateurs :
- 'GSave()' - Enregistre l'état graphique actuel.
- 'ConcatenateMatrix(matrix)' - Applique une transformation (mise à l'échelle et centrage vertical de l'image sur la page).
- 'Do(image_id)' - Rend l'image.
- 'GRestore()' - Restaure l'état graphique.
1. Ajoutez la séquence d'opérateurs à 'page.contents'.
1. Enregistrez le PDF résultant.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842,595)

    # Get page resources
    resources_images = page.resources.images

    # Add image to resources
    image_stream = FileIO(path.join(self.data_dir, path_infile), "rb")
    image_id = resources_images.add(image_stream)

    x_image = list(resources_images)[-1]

    rectangle = ap.Rectangle(
        0,
        0,
        page.media_box.width,
        (page.media_box.width * x_image.height) / x_image.width,
        True,
    )

    # Create operator sequence for adding image
    operators = []

    # Save graphics state
    operators.append(ap.operators.GSave())

    # Set transformation matrix (position and size)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.llx + (page.media_box.height - rectangle.height) / 2,
    )
    operators.append(ap.operators.ConcatenateMatrix(matrix))

    # Draw the image
    operators.append(ap.operators.Do(image_id))

    # Restore graphics state
    operators.append(ap.operators.GRestore())

    # Add operators to page contents
    page.contents.add(operators)

    document.save(path_outfile)
```

## Ajouter une image avec texte alternatif

Cet exemple montre comment ajouter une image à une page PDF et assigner un texte alternatif (alt text) pour la conformité d'accessibilité (comme PDF/UA).

1. Créez un nouveau 'Document' et ajoutez une page (842 × 595, A4 paysage).
1. Placez l'image sur la page en utilisant 'page.add_image()' avec un rectangle qui couvre toute la page.
1. Accédez aux ressources d'images de la page ('page.resources.images').
1. Définissez une chaîne de texte alternatif (par ex., 'Texte alternatif pour l'image').
1. Récupérez le premier objet image des ressources ('x_image = resources_images[1]').
1. Utilisez 'try_set_alternative_text(alt_text, page)' pour assigner le texte alternatif à l'image.
1. Enregistrez le PDF résultant.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842,595)

    page.add_image(
        path_image_file,
        ap.Rectangle(0, 0, 842, 595, True),
    )

    resources_images = page.resources.images
    alt_text = "Alternative text for image"
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text(alt_text, page)

    # If set is successful, then get the alternative text for the image
    if (result):
        print ("Text has been added successfuly")
    document.save(path_outfile)
```
