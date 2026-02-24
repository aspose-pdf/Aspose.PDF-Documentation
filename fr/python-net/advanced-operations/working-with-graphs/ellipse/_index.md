---
title: Ajouter un objet Ellipse au fichier PDF
linktitle: Ajouter une ellipse
type: docs
weight: 60
url: /fr/python-net/add-ellipse/
description: Cet article explique comment créer un objet Ellipse dans votre PDF en utilisant Aspose.PDF pour Python via .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajout d'un objet Ellipse au PDF avec Python
Abstract: L'article fournit un guide complet sur l'utilisation d'Aspose.PDF pour Python via .NET afin d'ajouter et de personnaliser des objets Ellipse dans des documents PDF. Il explique le processus de création et de manipulation des ellipses, y compris la définition de leurs dimensions, couleurs et positionnement, en utilisant le module de dessin. Il montre comment tracer des ellipses sur une page PDF, démontrant la capacité de contrôler leur apparence et leur position. L'exemple comprend la définition des propriétés de bordure et l'ajout de plusieurs ellipses à un graphique. Il illustre comment remplir les ellipses avec des couleurs spécifiques, en proposant un exemple où deux ellipses sont remplies de couleurs différentes et ajoutées à un document PDF. Il explique comment insérer du texte à l'intérieur des objets Ellipse en utilisant la propriété texte de l'objet Graph. L'exemple fourni montre comment définir les propriétés de police et ajouter du texte à
---

## Ajouter un objet Ellipse

Aspose.PDF pour Python via .NET permet d'ajouter des objets [Ellipse](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) aux documents PDF. Il offre également la fonctionnalité de remplir un objet ellipse avec une certaine couleur.

Cet exemple illustre comment tracer et personnaliser programmétiquement des ellipses dans un document PDF en utilisant Aspose.PDF pour Python via .NET. En exploitant le module de dessin, les développeurs peuvent créer des éléments graphiques complexes avec un contrôle précis de leur apparence et de leur positionnement. Cette capacité est essentielle pour les applications qui nécessitent la génération dynamique de contenu graphique dans les PDF, tels que les diagrammes techniques, les graphiques ou les illustrations personnalisées.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add a page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create first ellipse with specified coordinates and radii
    ellipse1 = drawing.Ellipse(150, 100, 120, 60)
    ellipse1.graph_info.color = ap.Color.green_yellow
    ellipse1.text = ap.TextFragment("Ellipse")

    # Add first ellipse to graph
    graph.shapes.add(ellipse1)

    # Create second ellipse with different dimensions and color
    ellipse2 = drawing.Ellipse(50, 50, 18, 300)
    ellipse2.graph_info.color = ap.Color.dark_red

    # Add second ellipse to graph
    graph.shapes.add(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)

```

![Ajouter une ellipse](ellipse.png)

## Créer un objet Ellipse rempli

Le fragment de code suivant montre comment ajouter un objet [Ellipse](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) rempli de couleur.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add a page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create first ellipse and set its fill color
    ellipse1 = drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow

    # Add first ellipse to graph
    graph.shapes.add(ellipse1)

    # Create second ellipse and set its fill color
    ellipse2 = drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red

    # Add second ellipse to graph
    graph.shapes.add(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

![Ellipse remplie](fill_ellipse.png)

## Ajouter du texte à l'intérieur de l'Ellipse

Aspose.PDF pour Python via .NET permet d'ajouter du texte à l'intérieur de l'objet Graph. La propriété texte de l'objet Graph offre la possibilité de définir le texte de l'objet Graph. Le fragment de code suivant montre comment ajouter du texte à l'intérieur d'un objet Ellipse.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    text_fragment = ap.text.TextFragment("Ellipse")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Helvetica")
    text_fragment.text_state.font_size = 24

    ellipse1 = ap.drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    ellipse1.text = text_fragment
    graph.shapes.append(ellipse1)

    ellipse2 = ap.drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    ellipse2.text = text_fragment
    graph.shapes.append(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF file
    document.save(path_outfile)
```

![Texte à l'intérieur de l'Ellipse](text_ellipse.png)

