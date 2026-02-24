---
title: Travailler avec les graphiques vectoriels en Python
linktitle: Travailler avec les graphiques vectoriels
type: docs
weight: 100
url: /fr/python-net/working-with-vector-graphics/
description: Cet article décrit les fonctionnalités de l'outil GraphicsAbsorber avec Python.
lastmod: "2025-05-17"
TechArticle: true
AlternativeHeadline: Utilisez l'outil GraphicsAbsorber dans PDF avec Python
Abstract: La documentation Aspose.PDF pour Python via .NET sur l'article « Travailler avec les graphiques vectoriels » fournit un guide complet pour les développeurs souhaitant manipuler des graphiques vectoriels dans des documents PDF à l'aide de la classe GraphicsAbsorber. Cette classe facilite l'extraction, le déplacement, la suppression et la duplication des éléments graphiques vectoriels à travers les pages PDF.
---

Dans ce chapitre, nous explorerons comment utiliser la puissante classe `GraphicsAbsorber` pour interagir avec les graphiques vectoriels dans les documents PDF. Que vous ayez besoin de déplacer, de supprimer ou d'ajouter des graphiques, ce guide vous montrera comment réaliser ces tâches efficacement.

## Introduction

Les graphiques vectoriels sont un composant essentiel de nombreux documents PDF, utilisés pour représenter des images, des formes et d'autres éléments graphiques. Aspose.PDF fournit la classe `GraphicsAbsorber`, qui permet aux développeurs d'accéder et de manipuler ces graphiques de façon programmée. En utilisant la méthode `Visit` de `GraphicsAbsorber`, vous pouvez extraire les graphiques vectoriels d'une page spécifiée et effectuer diverses opérations, telles que le déplacement, la suppression ou la copie vers d’autres pages.

## Extraction des graphiques

La première étape pour travailler avec les graphiques vectoriels est de les extraire d'un document PDF. Voici comment le faire en utilisant la classe `GraphicsAbsorber` :

1. Ouvrez le document PDF.
1. Initialisez le GraphicsAbsorber.
1. Sélectionnez la page cible.
1. Extrayez les graphiques de la page.
1. Parcourez et affichez les éléments extraits.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Select the first page of the document
            page = document.pages[1]
            # Use the `Visit` method to extract graphics from the page
            graphics_absorber.visit(page)
            # Display information about the extracted elements
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")
```

La classe GraphicsAbsorber fait partie de l'espace de noms aspose.pdf.vector et est spécialement conçue pour interagir avec les graphiques vectoriels dans les documents PDF.

## Déplacement de graphiques

Une fois que vous avez extrait les graphiques, vous pouvez les déplacer vers une position différente sur la même page. Voici comment y parvenir :

1. Ouvrez le document PDF.
1. Initialisez le GraphicsAbsorber.
1. Sélectionnez la page cible.
1. Extraction des éléments graphiques.
1. Suspension des mises à jour pour les performances.
1. Modification des positions des éléments graphiques.
1. Reprise des mises à jour et application des modifications.
1. Enregistrement du document mis à jour.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create a GraphicsAbsorber instance
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Select the first page of the document
            page = document.pages[1]
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Temporarily suspend updates to improve performance
            graphics_absorber.suppress_update()
            # Loop through each extracted graphic element and shift its position
            for element in graphics_absorber.elements:
                position = element.position
                # Move graphics by shifting its X and Y coordinates
                element.position = ap.Point(position.x + 150, position.y - 10)
            # Resume updates and apply changes
            graphics_absorber.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

## Suppression de graphiques

Il existe des scénarios où vous pourriez vouloir supprimer des graphiques spécifiques d'une page. Aspose.PDF pour Python propose deux méthodes pour y parvenir :

### Méthode 1 : Utilisation de la frontière rectangulaire

L'exemple suivant montre comment supprimer des éléments graphiques vectoriels situés dans une zone rectangulaire spécifique de la première page d'un document PDF à l'aide de la bibliothèque Aspose.PDF pour Python via .NET. Ce processus consiste à identifier les éléments graphiques à l'intérieur du rectangle défini et à les supprimer afin de nettoyer ou modifier le contenu du PDF.

1. Ouvrez le document PDF.
1. Initialisez le GraphicsAbsorber.
1. Sélectionnez la page cible.
1. Extraction des éléments graphiques.
1. Définition du rectangle cible.
1. Suspension des mises à jour pour les performances.
1. Suppression des éléments graphiques à l'intérieur du rectangle.
1. Reprise des mises à jour et application des modifications.
1. Enregistrement du document mis à jour.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first page of the document
            page = document.pages[1]
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Define the rectangle where graphics will be removed
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            # Temporarily suspend updates for better performance
            graphics_absorber.suppress_update()
            # Iterate through the extracted graphic elements and remove elements inside the rectangle
            for element in graphics_absorber.elements:
                # Check if the graphic's position falls within the rectangle
                if rectangle.contains(element.position, False):
                    # Remove the graphic element
                    element.remove()
            # Resume updates and apply changes
            graphics_absorber.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

### Méthode 2 : Utilisation d’une collection d’éléments supprimés

L'exemple suivant montre comment supprimer des éléments graphiques vectoriels situés dans une zone rectangulaire spécifique de la première page d'un document PDF à l'aide de la bibliothèque Aspose.PDF pour Python via .NET. Ce processus consiste à identifier les éléments graphiques à l'intérieur du rectangle défini et à les supprimer afin de nettoyer ou modifier le contenu du PDF.

1. Ouvrez le document PDF.
1. Initialisez le GraphicsAbsorber.
1. Sélectionnez la page cible.
1. Définition du rectangle cible.
1. Extraction des éléments graphiques.
1. Création d’une collection pour la suppression.
1. Identification des éléments à l’intérieur du rectangle.
1. Suspension des mises à jour pour améliorer les performances.
1. Suppression des éléments graphiques.
1. Reprise des mises à jour et application des modifications.
1. Enregistrement du document mis à jour.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first page of the document
            page = document.pages[1]
            # Define the rectangle where graphics will be removed
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Create a collection for the removed elements
            removed_elements_collection = ap.vector.GraphicElementCollection()
            # Add elements within the rectangle to the collection
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position,False):
                    removed_elements_collection.add(item)
            # Temporarily suppress updates for better performance
            page.contents.suppress_update()
            # Delete the selected graphic elements
            page.delete_graphics(removed_elements_collection)
            # Resume updates and apply changes
            page.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

## Ajouter des graphiques à une autre page

Les graphiques absorbés d’une page peuvent être ajoutés à une autre page du même document.
Voici deux méthodes pour y parvenir :

### Méthode 1 : Ajout de graphiques individuellement

L’exemple suivant montre comment copier des éléments graphiques vectoriels de la première page d’un document PDF et les coller sur la deuxième page. Cette opération est facilitée par la classe GraphicsAbsorber, qui permet l’extraction et la manipulation de graphiques vectoriels dans les documents PDF.

1. Ouvrir le document PDF.
1. Initialiser le GraphicsAbsorber.
1. Sélectionner la page cible.
1. Extraction des éléments graphiques de la première page.
1. Suspension des mises à jour sur la deuxième page pour améliorer les performances.
1. Ajout des éléments graphiques extraits à la deuxième page.
1. Reprise des mises à jour et application des modifications.
1. Enregistrement du document mis à jour.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first and second pages
            page_1 = document.pages[1]
            page_2 = document.pages[2]
            # Extract graphic elements from the first page
            graphics_absorber.visit(page_1)
            # Temporarily suppress updates for better performance
            page_2.contents.suppress_update()
            # Add each graphic element from the first page to the second page
            for element in graphics_absorber.elements:
                element.add_on_page(page_2) # Add each graphic element to the second page.
            # Resume updates and apply changes
            page_2.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

### Méthode 2 : Ajout de graphiques sous forme de collection

L’exemple suivant montre comment dupliquer des éléments graphiques vectoriels de la première page d’un document PDF et les placer dans la deuxième page. Cela est réalisé grâce à la classe GraphicsAbsorber, qui facilite l’extraction et la manipulation de graphiques vectoriels dans les documents PDF.

1. Ouvrir le document PDF.
1. Initialiser le GraphicsAbsorber.
1. Sélectionner la page cible.
1. Extraction des éléments graphiques de la première page.
1. Suspension des mises à jour sur la deuxième page pour améliorer les performances.
1. Ajout des éléments graphiques extraits à la deuxième page.
1. Reprise des mises à jour et application des modifications.
1. Enregistrement du document mis à jour.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first and second pages
            page_1 = document.pages[1]
            page_2 = document.pages[2]
            # Extract graphic elements from the first page
            graphics_absorber.visit(page_1)
            # Temporarily suppress updates for better performance
            page_2.contents.suppress_update()
            # Add all graphics at once from the first page to the second page
            page_2.add_graphics(graphics_absorber.elements, None)
            # Resume updates and apply changes
            page_2.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```
