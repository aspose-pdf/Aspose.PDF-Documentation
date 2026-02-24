---
title: Travailler avec les opérateurs en Python
linktitle: Travailler avec les opérateurs
type: docs
weight: 90
url: /fr/python-net/working-with-operators/
description: Ce sujet explique comment utiliser les opérateurs avec Aspose.PDF pour Python via .NET. Les classes d'opérateurs offrent de grandes fonctionnalités pour la manipulation de PDF.
lastmod: "2025-05-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Utilisation des opérateurs dans PDF avec Aspose.PDF pour Python via .NET
Abstract: L'article propose une exploration approfondie des opérateurs PDF et de leurs applications dans la manipulation des flux de contenu PDF. Les opérateurs sont des mots‑clés spécialisés dans le PDF qui déclenchent des actions particulières, comme le rendu d'éléments graphiques sur une page, et ne sont valides que dans les flux de contenu. L'article détaille une méthode permettant d'exercer un contrôle précis sur le placement des images dans les PDF en manipulant directement les flux de contenu à l'aide d'opérateurs graphiques de bas niveau. Cette approche est utile pour les tâches nécessitant un positionnement exact des images, comme l'ajout de filigranes, l'alignement des superpositions et la création de mises en page personnalisées. Des opérateurs spécifiques tels que GSave, ConcatenateMatrix, Do et GRestore sont mis en avant pour leurs rôles dans la gestion des états graphiques et des transformations, garantissant un rendu précis sans affecter le reste du contenu de la page.
---

## Introduction aux opérateurs PDF et à leur utilisation

Un opérateur est un mot‑clé PDF spécifiant une action à exécuter, comme le dessin d'une forme graphique sur la page. Un mot‑clé d'opérateur se distingue d'un objet nommé par l'absence d'un caractère slash initial (2Fh). Les opérateurs n'ont de sens qu'à l'intérieur du flux de contenu.

Vous trouverez plus de détails sur les opérateurs PDF dans la [spécification PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### Détails de mise en œuvre

Cette méthode offre un contrôle fin du placement des images dans un PDF en manipulant directement le flux de contenu avec des opérateurs graphiques de bas niveau. Elle est particulièrement utile lorsque le positionnement et la transformation précis des images sont requis, tels que :

- ajouter des filigranes ou des logos à des emplacements spécifiques.

- superposer des images sur le contenu existant avec un alignement précis.

- implémenter des mises en page personnalisées qui ne sont pas réalisables avec des abstractions de haut niveau.

En utilisant des opérateurs comme GSave, ConcatenateMatrix, Do et GRestore, les développeurs peuvent garantir que les images sont rendues avec précision et sans effets secondaires indésirables sur le reste du contenu de la page.

- L'opérateur [GSave](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/gsave/) enregistre l'état graphique actuel du PDF.
- L'opérateur [ConcatenateMatrix](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/concatenatematrix/) (concaténation de matrice) est utilisé pour définir comment une image doit être placée sur la page PDF.
- L'opérateur [Do](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/do/) dessine l'image sur la page.
- L'opérateur [GRestore](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/grestore/) restaure l'état graphique.

Pour ajouter une image dans un fichier PDF :

1. Ouvrir le document PDF
1. Définir les coordonnées de placement de l'image
1. Accéder à la page cible
1. Charger l'image dans un flux
1. Enregistrer l'état graphique actuel
1. Créer un rectangle et une matrice de transformation
1. Appliquer la matrice de transformation
1. Dessiner l'image
1. Restaurer l'état graphique précédent
1. Enregistrer le document PDF modifié

Le fragment de code suivant montre comment utiliser les opérateurs PDF :

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Set coordinates for the image placement
        lower_left_x = 100
        lower_left_y = 100
        upper_right_x = 200
        upper_right_y = 200

        # Get the page where the image needs to be added
        page = document.pages[1]

        # Load the image into a file stream
        with open(path_imagefile, "rb") as image_stream:
            # Add the image to the page's Resources collection
            page.resources.images.add(image_stream)

        # Save the current graphics state using the GSave operator
        page.contents.add(ap.operators.GSave())

        # Create a rectangle and matrix for positioning the image
        rectangle = ap.Rectangle(lower_left_x, lower_left_y, upper_right_x, upper_right_y)
        matrix = ap.Matrix([
            rectangle.urx - rectangle.llx, 0,
            0, rectangle.ury - rectangle.lly,
            rectangle.llx, rectangle.lly
        ])

        # Define how the image must be placed using the ConcatenateMatrix operator
        page.contents.add(ap.operators.ConcatenateMatrix(matrix))

        # Get the image from the Resources collection
        x_image = page.resources.images[page.resources.images.count]

        # Draw the image using the Do operator
        page.contents.add(ap.operators.Do(x_image.name))

        # Restore the graphics state using the GRestore operator
        page.contents.add(ap.operators.GRestore())

        # Save PDF document
        document.save(path_outfile)
```

## Dessiner un XForm sur la page en utilisant des opérateurs

Cet exemple a exploité la puissance des XForms et des opérateurs graphiques pour réutiliser efficacement le contenu graphique au sein d'un PDF. En encapsulant l'image dans un XForm, il est possible de la dessiner plusieurs fois sans dupliquer les données de l'image, ce qui réduit la taille du fichier et améliore les performances. Cette approche est particulièrement bénéfique lorsque :

- la même image ou le même graphique doit apparaître plusieurs fois dans un document.

- un contrôle précis du placement et de la transformation des graphiques est requis.

- optimiser le PDF pour la performance et la taille est une priorité.

En gérant l'état graphique avec GSave et GRestore, et en utilisant des matrices de transformation avec ConcatenateMatrix, cette technique garantit que chaque graphique est rendu correctement et de manière indépendante.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        page_contents = document.pages[1].contents

        # Wrap existing contents with GSave/GRestore operators to preserve graphics state
        page_contents.insert(1, ap.operators.GSave())
        page_contents.add(ap.operators.GRestore())

        # Add GSave operator to start new graphics state
        page_contents.add(ap.operators.GSave())

        # Create an XForm
        form = ap.XForm.create_new_form(document.pages[1], document)
        document.pages[1].resources.forms.add(form)

        form.contents.add(ap.operators.GSave())
        # Define image width and height
        form.contents.add(ap.operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0))

        # Load image into stream
        with open(path_imagefile, 'rb') as image_stream:
            # Add the image to the XForm's resources
            form.resources.images.add(image_stream)

        x_image = form.resources.images[form.resources.images.count]
        # Draw the image on the XForm
        form.contents.add(ap.operators.Do(x_image.name))
        form.contents.add(ap.operators.GRestore())

        # Place and draw the XForm at two different coordinates

        # Draw the XForm at (100, 500)
        page_contents.add(ap.operators.GSave())
        page_contents.add(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500))
        page_contents.add(ap.operators.Do(form.name))
        page_contents.add(ap.operators.GRestore())

        # Draw the XForm at (100, 300)
        page_contents.add(ap.operators.GSave())
        page_contents.add(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300))
        page_contents.add(ap.operators.Do(form.name))
        page_contents.add(ap.operators.GRestore())

        # Restore graphics state
        page_contents.add(ap.operators.GRestore())

        # Save PDF document
        document.save(path_outfile)
```

## Supprimer des objets graphiques à l'aide des classes d'opérateurs

Le fragment de code suivant montre comment supprimer des graphiques. Veuillez noter que si le fichier PDF contient des libellés texte pour les graphiques, ils peuvent persister dans le PDF en utilisant cette approche. Il faut donc rechercher les opérateurs graphiques pour une méthode alternative afin de supprimer ces images.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Get the specific page (page 2 in this case)
        page = document.pages[2]

        # Get the operator collection from the page contents
        operator_collection = page.contents

        # Define the path-painting operators to be removed
        operators_to_remove = [
            ap.operators.Stroke(),
            ap.operators.ClosePathStroke(),
            ap.operators.Fill()
        ]

        # Delete the specified operators from the page contents
        operator_collection.delete(operators_to_remove)

        # Save PDF document
        document.save(path_outfile)
```


