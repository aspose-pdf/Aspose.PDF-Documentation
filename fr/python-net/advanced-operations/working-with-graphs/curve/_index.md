---
title: Ajouter un objet de courbe au fichier PDF
linktitle: Ajouter une courbe
type: docs
weight: 30
url: /fr/python-net/add-curve/
description: Cet article explique comment créer un objet courbe dans votre PDF à l'aide d'Aspose.PDF pour Python via .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajout d'un objet Courbe au PDF avec Python
Abstract: L'article aborde la mise en œuvre des courbes graphiques dans les documents PDF à l'aide de la bibliothèque Aspose.PDF pour Python via .NET. Il présente le concept de courbe graphique, qui est une union de droites projectives, et détaille le processus de création de courbes de Bézier simples et remplies de manière programmatique. L'article fournit des instructions étape par étape et des extraits de code pour dessiner des courbes dans un PDF, mettant en évidence la manipulation des éléments graphiques à l'aide du module de dessin d'Aspose.PDF. Le processus comprend la création d'une instance `Document`, la définition d'un objet `Drawing` avec des dimensions spécifiées, la définition des bordures, et l'ajout d'un objet `Graph` à une page PDF. Les résultats visuels de ces exemples de code sont illustrés par des images montrant les courbes obtenues. L'article explore également la création d'objets de courbes remplies, démontrant comment définir les couleurs de remplissage des courbes, ce qui est crucial pour générer du contenu graphique dynamique tel que des diagrammes techniques, des graphiques ou des illustrations personnalisées dans les PDF.
---

## Ajouter un objet Courbe

Un graphique [Courbe](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/) est une union connectée de droites projectives, chaque droite rencontrant trois autres en points doubles ordinaires.

Dans cet article, nous examinerons simplement les courbes graphiques, et les courbes remplies, que vous pouvez créer dans votre document PDF.

Cet exemple illustre comment dessiner une courbe de Bézier de manière programmatique dans un document PDF à l'aide d'Aspose.PDF pour Python via .NET. En exploitant le module de dessin, les développeurs peuvent créer des éléments graphiques complexes avec un contrôle précis de leur apparence et de leur positionnement. Cette capacité est essentielle pour les applications nécessitant la génération dynamique de contenu graphique dans les PDF, comme les diagrammes techniques, les graphiques ou les illustrations personnalisées.

Suivez les étapes ci-dessous :

1. Créez une instance [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Créez un [objet Drawing](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) avec certaines dimensions.
1. Définissez la [bordure](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) de l'objet Drawing.
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

    # Create a curve and set its properties
    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info = drawing.GraphInfo()
    curve1.graph_info.color = ap.Color.green_yellow

    # Add the curve to the graph shapes
    graph.shapes.add(curve1)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

L'image suivante montre le résultat obtenu avec notre extrait de code :

![Courbe de dessin](drawing_curve.png)

## Créer un objet Courbe remplie

Cet exemple montre comment ajouter un objet Courbe rempli de couleur.

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

    # Create a curve and set fill color
    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info = drawing.GraphInfo()
    curve1.graph_info.fill_color = ap.Color.green_yellow

    # Add the curve to the graph shapes
    graph.shapes.add(curve1)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

Regardez le résultat de l'ajout d'une Courbe remplie :

![Courbe remplie](filled_curve.png)

