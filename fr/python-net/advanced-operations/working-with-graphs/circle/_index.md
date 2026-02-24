---
title: Ajouter un objet cercle au fichier PDF
linktitle: Ajouter un cercle
type: docs
weight: 20
url: /fr/python-net/add-circle/
description: Cet article explique comment créer un objet cercle dans votre PDF à l'aide d'Aspose.PDF pour Python via .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajout d'un objet cercle au PDF avec Python
Abstract: L'article fournit un guide sur l'utilisation d'Aspose.PDF pour Python via .NET afin de créer des objets cercle dans les documents PDF. Il explique le processus d'ajout de graphiques de cercle à la fois contournés et remplis, soulignant comment les graphiques circulaires peuvent être un outil utile pour afficher des données à travers plusieurs catégories lorsque les données représentent un tout complet. L'article inclut des instructions étape par étape pour créer une instance de `Document`, configurer un objet `Drawing` avec des dimensions spécifiques, appliquer une bordure et ajouter un objet `Graph` à une page PDF. Les exemples de code démontrent le dessin d'un cercle simple et d'un cercle rempli, avec des instructions détaillées sur la définition des couleurs et l'ajout de texte au cercle. Les résultats visuels de ces opérations sont également présentés, mettant en avant les capacités d'Aspose.PDF à enrichir le contenu PDF avec des éléments graphiques dynamiques.
---

## Ajouter un objet cercle

Comme les graphiques à barres, les graphiques circulaires peuvent être utilisés pour afficher des données dans plusieurs catégories distinctes. Cependant, contrairement aux graphiques à barres, les graphiques circulaires ne peuvent être utilisés que lorsque vous disposez de données pour toutes les catégories qui composent l’ensemble. Jetons donc un œil à l'ajout d'un objet [Circle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/circle/) avec Aspose.PDF pour Python .NET.

Cet exemple illustre comment dessiner programatiquement un cercle dans un document PDF en utilisant Aspose.PDF pour Python via .NET. En exploitant le module de dessin, les développeurs peuvent créer des éléments graphiques complexes avec un contrôle précis de leur apparence et de leur positionnement. Cette capacité est essentielle pour les applications qui nécessitent la génération dynamique de contenu graphique au sein de PDFs, comme les diagrammes techniques, les graphiques ou les illustrations personnalisées.

Suivez les étapes ci-dessous :

1. Créez une instance de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Créez un [objet Drawing](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) avec certaines dimensions.
1. Définissez la [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) pour l'objet Drawing.
1. Ajoutez l'objet [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) à la collection de paragraphes de la page.
1. Enregistrez notre fichier PDF.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 200)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create a circle with the specified coordinates and radius
    circle = drawing.Circle(100, 100, 40)

    # Set the circle's color
    circle.graph_info = drawing.GraphInfo()
    circle.graph_info.color = ap.Color.green_yellow

    # Add the circle to the graph shapes
    graph.shapes.add(circle)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

Notre cercle dessiné ressemblera à ceci :

![Drawing Circle](drawing_circle.png)

## Créer un objet cercle rempli

Cet exemple montre comment ajouter un objet Circle qui est rempli de couleur.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 200)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create a filled circle
    circle = drawing.Circle(100, 100, 40)
    circle.graph_info = drawing.GraphInfo()
    circle.graph_info.color = ap.Color.green_yellow
    circle.graph_info.fill_color = ap.Color.green
    circle.text = ap.text.TextFragment("Circle")

    # Add the circle to the graph shapes
    graph.shapes.add(circle)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

Voyons le résultat de l'ajout d'un cercle rempli :

![Filled Circle](filled_circle.png)


