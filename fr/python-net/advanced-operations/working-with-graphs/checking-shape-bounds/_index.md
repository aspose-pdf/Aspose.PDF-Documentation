---
title: Vérifier les limites des formes dans la collection Shapes avec Python
type: docs
weight: 70
url: /fr/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Apprenez à vérifier les limites d'une forme lorsqu'elle est insérée dans la collection Shapes afin de vous assurer qu'elle s'adapte à son conteneur parent.
lastmod: "2025-05-14"
draft: false
TechArticle: true
AlternativeHeadline: Guide sur la vérification des limites des formes dans Shapes
Abstract: Cet article propose un guide complet sur l'utilisation de la fonction de vérification des limites dans la collection Shapes, en particulier dans les documents PDF avec Python. Cette fonction est essentielle pour garantir que les éléments graphiques, tels que les formes, s'adaptent correctement à leurs conteneurs parents. Elle peut être configurée pour lever une exception si le composant dépasse les limites du conteneur, assurant ainsi une gestion des erreurs robuste. Le guide explique comment créer un nouveau document PDF, ajouter une page et établir un élément graphique (une forme rectangulaire) au sein d'un objet Graph. Des instructions détaillées sont fournies pour instancier un `Document`, ajouter une `Page` et créer un objet `Graph`. Il décrit la mise en place d'une forme `Rectangle` et la configuration du `BoundsCheckMode` à `THROW_EXCEPTION_IF_DOES_NOT_FIT`, ce qui garantit qu'une exception est levée si la forme ne tient pas dans les dimensions spécifiées du graphique. Le processus est illustré avec un exemple de code Python utilisant la bibliothèque Aspose.PDF, mettant en évidence la mise en œuvre pratique de ces fonctionnalités.
---

Cet article fournit un guide détaillé sur l'utilisation de la fonction de vérification des limites dans la collection Shapes. Cette fonction garantit que les éléments s'adaptent à leur conteneur parent et peut être configurée pour lever une exception si le composant ne tient pas.

1. Créez un nouveau PDF [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Ajoutez une page
1. Créez un [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/)
1. Créez une forme Rectangle
1. Mode de vérification des limites
1. Ajoutez le [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) au Graph

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create a Graph object with specified dimensions
    graph = ap.drawing.Graph(100, 100)
    graph.top = 10
    graph.left = 15
    graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
    page.paragraphs.add(graph)

    # Create a shape object(for example, Rectangle) with specified dimensions
    rect = drawing.Rectangle(-1, 0, 50, 50)
    rect.graph_info.fill_color = ap.Color.tomato

    # Set the BoundsCheck mode to THROW_EXCEPTION_IF_DOES_NOT_FIT
    graph.shapes.update_bounds_check_mode(ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT)

    # Add the rectangle to the graph
    graph.shapes.add(rect)
```            
