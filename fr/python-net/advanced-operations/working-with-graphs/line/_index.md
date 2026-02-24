---
title: Ajouter un objet Ligne au fichier PDF
linktitle: Ajouter une ligne
type: docs
weight: 40
url: /fr/python-net/add-line/
description: Cet article explique comment créer un objet ligne dans votre PDF en utilisant Aspose.PDF pour Python via .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajout d'un objet ligne au PDF avec Python
Abstract: L'article explique comment ajouter des objets ligne à un document PDF en utilisant Aspose.PDF pour Python via .NET. Il décrit le processus de création d'une instance `Document` et d'ajout d'un objet `Graph` au PDF. L'article fournit des étapes détaillées pour créer et configurer un objet `Line`, y compris la spécification de son motif de tirets et de sa couleur. Il inclut des extraits de code montrant comment ajouter une ligne simple, une ligne pointillée tiretée, et comment tracer des lignes à travers une page pour former un motif en croix. Chaque section est accompagnée d'une représentation visuelle du PDF résultant. Ce guide sert de ressource pratique aux développeurs souhaitant enrichir leurs documents PDF avec des éléments graphiques en utilisant Aspose.PDF.
---

## Ajouter un objet Ligne

Aspose.PDF pour Python via .NET prend en charge la fonction d'ajout d'objets graphiques (par exemple graphique, ligne, rectangle, etc.) aux documents PDF. Vous bénéficiez également de la possibilité d'ajouter l'objet [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) où vous pouvez spécifier le motif de tirets, la couleur et d'autres formats pour l'élément Ligne.

Suivez les étapes ci-dessous :

1. Créez une instance [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Créez un objet Graph
1. Ajoutez l'objet [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) à la collection de paragraphes de la page.
1. Créez et configurez la Ligne
1. Ajoutez le [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) au Graph
1. Enregistrez notre fichier PDF.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(100, 400)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance
    line = drawing.Line([100, 100, 200, 100])

    # Specify fill color for Graph object
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(line)

    # Save PDF file
    document.save(path_outfile)
```

![Ajouter une ligne](add_line.png)

## Comment ajouter une ligne pointillée tiretée à votre document PDF

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(100, 400)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance
    line = drawing.Line([100, 100, 200, 100])

    # Set color for Line object
    line.graph_info.color = ap.Color.red

    # Specify fill color for Graph object
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(line)

    # Save PDF file
    document.save(path_outfile)
```

Vérifions le résultat :

![Ligne pointillée](dash_line.png)

## Dessiner une ligne à travers la page

Nous pouvons également utiliser l'objet ligne pour dessiner une croix allant du coin inférieur gauche au coin supérieur droit et du coin supérieur gauche au coin inférieur droit.

Veuillez consulter le fragment de code suivant pour répondre à cette exigence.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Set page margin on all sides as 0
    page.page_info.margin.left = 0
    page.page_info.margin.right = 0
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0

    # Create Graph object with Width and Height equal to page dimensions
    graph = drawing.Graph(page.page_info.width, page.page_info.height)

    # Create first line object starting from Lower-Left to Top-Right corner of page
    line = drawing.Line([page.rect.llx, 0, page.page_info.width, page.rect.ury])

    # Add line to shape collection of Graph object
    graph.shapes.append(line)

    # Draw line from Top-Left corner of page to Bottom-Right corner of page
    line2 = drawing.Line([0, page.rect.ury, page.page_info.width, page.rect.llx])

    # Add line to shape collection of Graph object
    graph.shapes.append(line2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF file
    document.save(path_outfile)
```

![Dessin de ligne](draw_line.png)


