---
title: Ajouter un objet Arc au fichier PDF
linktitle: Ajouter un Arc
type: docs
weight: 10
url: /fr/python-net/add-arc/
description: Cet article explique comment créer un objet arc dans votre PDF en utilisant Aspose.PDF pour Python via .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajout d'un objet Arc au PDF avec Python
Abstract: L'article fournit un guide détaillé sur la manière d'ajouter et de personnaliser des objets arc dans les documents PDF en utilisant Aspose.PDF pour Python via .NET. Il met en évidence la capacité de la bibliothèque à incorporer des éléments graphiques tels que des arcs, essentiels pour les applications nécessitant une génération dynamique de contenu PDF, comme les diagrammes techniques et les illustrations personnalisées. L'article comprend des instructions étape par étape et des extraits de code montrant comment créer une instance de `Document`, configurer un objet `Drawing` avec des dimensions et des propriétés de bordure spécifiées, et ajouter des objets `Graph` et `Arc` à une page PDF. De plus, il couvre le processus de remplissage des objets arc avec de la couleur, démontrant comment définir les propriétés de remplissage pour les arcs et les lignes, et finalement enregistrer le document PDF. Les exemples fournis servent de guide pratique pour les développeurs souhaitant exploiter Aspose.PDF pour des manipulations graphiques précises dans les fichiers PDF.
---

## Ajouter un objet Arc

Aspose.PDF pour Python via .NET prend en charge la fonctionnalité d'ajout d'objets graphiques (par exemple graphique, ligne, rectangle, etc.) aux documents PDF. Il offre également la fonctionnalité de remplissage d'un objet arc avec une certaine couleur.

Cet exemple illustre comment tracer programmétiquement des arcs dans un document PDF en utilisant Aspose.PDF pour Python via .NET. En tirant parti du module de dessin, les développeurs peuvent créer des éléments graphiques complexes, tels que des arcs, avec un contrôle précis de leur apparence et de leur positionnement. Cette capacité est essentielle pour les applications qui nécessitent une génération dynamique de contenu graphique dans les PDF, comme les diagrammes techniques, les graphiques ou les illustrations personnalisées.

Suivez les étapes ci-dessous :

1. Créez une instance de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Créez un [objet Drawing](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) avec certaines dimensions.
1. Définissez la [bordure](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) pour l'objet Drawing.
1. Ajoutez l'objet [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) à la collection de paragraphes de la page.
1. Enregistrez notre fichier PDF.

L'extrait de code suivant montre comment ajouter un objet [Arc](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/).

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create arcs and set their properties
    arc1 = drawing.Arc(100, 100, 95, 0, 90)
    arc1.graph_info = drawing.GraphInfo()
    arc1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(arc1)

    arc2 = drawing.Arc(100, 100, 90, 70, 180)
    arc2.graph_info = drawing.GraphInfo()
    arc2.graph_info.color = ap.Color.dark_blue
    graph.shapes.add(arc2)

    arc3 = drawing.Arc(100, 100, 85, 120, 210)
    arc3.graph_info = drawing.GraphInfo()
    arc3.graph_info.color = ap.Color.red
    graph.shapes.add(arc3)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

## Créer un objet Arc rempli

L'exemple suivant montre comment ajouter un objet Arc rempli de couleur et de dimensions spécifiques.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create an arc and set fill color
    arc = drawing.Arc(100, 100, 95, 0, 90)
    arc.graph_info = drawing.GraphInfo()
    arc.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(arc)

    # Create a line and set fill color
    line = drawing.Line([195, 100, 100, 100, 100, 195])
    line.graph_info = drawing.GraphInfo()
    line.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(line)

    # Add Graph object to the paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

Voyons le résultat de l'ajout d'un Arc rempli :

![Filled Arc](filled_arc.png)

