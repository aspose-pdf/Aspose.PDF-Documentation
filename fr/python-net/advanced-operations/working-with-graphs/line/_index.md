---
title: Ajouter des formes de ligne au PDF en Python
linktitle: Ajouter une ligne
type: docs
weight: 40
url: /fr/python-net/add-line/
description: Apprenez comment dessiner des formes de ligne et des lignes stylisées dans des fichiers PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dessiner des formes de ligne dans des fichiers PDF en utilisant Python
Abstract: Cet article montre comment ajouter des formes de ligne aux documents PDF avec Aspose.PDF for Python via .NET. Il couvre la création de lignes de base, la configuration de styles de ligne en pointillés et le tracé de lignes à travers une page.
---

## Ajouter l'objet Line

Aspose.PDF for Python via .NET vous permet d'ajouter [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) des formes aux pages PDF en utilisant le [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) classe. Vous pouvez contrôler la couleur de la ligne, le motif du tiret et le placement.

Suivez les étapes ci-dessous:

1. Créer [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instance.
1. Créer un objet de graphe
1. Ajouter [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) objet à la collection paragraphs de la page.
1. Créer et configurer la ligne
1. Ajouter le [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) au graphe
1. Enregistrez notre fichier PDF.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def add_line(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    line = drawing.Line([100, 100, 200, 100])
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1
    graph.shapes.add(line)

    document.save(outfile)
```

![Ajouter une ligne](add_line.png)

## Comment ajouter une ligne pointillée et tiretée à votre document PDF

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_dotted_dashed_line(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    line = drawing.Line([100, 100, 200, 100])
    line.graph_info.color = ap.Color.red
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1
    graph.shapes.add(line)

    document.save(outfile)
```

Résultat de l'ajout d'une ligne pointillée tiretée:

![Ligne tiretée](dash_line.png)

## Dessiner une ligne à travers la page

Vous pouvez également dessiner des lignes à travers la page pour former une croix.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def draw_line_across_page(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    page.page_info.margin.left = 0
    page.page_info.margin.right = 0
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0

    graph = drawing.Graph(page.page_info.width, page.page_info.height)
    line = drawing.Line([page.rect.llx, 0, page.page_info.width, page.rect.ury])
    graph.shapes.add(line)
    line2 = drawing.Line([0, page.rect.ury, page.page_info.width, page.rect.llx])
    graph.shapes.add(line2)
    page.paragraphs.add(graph)

    document.save(outfile)
```

![Dessiner une ligne](draw_line.png)

## Sujets liés aux graphiques

- [Travailler avec les graphes PDF en Python](/pdf/fr/python-net/working-with-graphs/)
- [Ajouter des formes de courbe au PDF en Python](/pdf/fr/python-net/add-curve/)
- [Ajouter des formes rectangulaires au PDF en Python](/pdf/fr/python-net/add-rectangle/)
- [Vérifier les limites de forme dans les graphiques PDF avec Python](/pdf/fr/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)
