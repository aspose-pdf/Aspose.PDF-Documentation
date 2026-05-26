---
title: Ajouter des formes d'arc au PDF en Python
linktitle: Ajouter un arc
type: docs
weight: 10
url: /fr/python-net/add-arc/
description: Apprenez comment tracer et remplir des formes d'arc dans des fichiers PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dessiner des formes d'arc dans des fichiers PDF à l'aide de Python
Abstract: Cet article montre comment ajouter des formes d'arc aux documents PDF avec Aspose.PDF for Python via .NET. Il couvre la création d'arcs contournés, le tracé de segments d'arc remplis, et leur ajout à un conteneur Graph.
---

## Ajouter l'objet Arc

Aspose.PDF for Python via .NET vous permet d'ajouter [Arc](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) des formes aux pages PDF en utilisant le [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) classe. Vous pouvez dessiner des arcs contournés et des segments d'arc remplis pour les diagrammes et les illustrations techniques.

Suivez les étapes ci-dessous:

1. Créer [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instance.
1. Créer [Objet Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) avec certaines dimensions.
1. Définir [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) pour l'objet Graph.
1. Créer un objet d'arc correspondant.
1. Ajouter cet objet à la collection Shapes dans l'objet graph.
1. Ajouter [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) objet à la collection paragraphs de la page.
1. Enregistrez notre fichier PDF.

Le fragment de code suivant montre comment ajouter un [Arc](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) objet.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_arc(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    arc1 = drawing.Arc(100, 100, 95, 0, 90)
    arc1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(arc1)

    arc2 = drawing.Arc(100, 100, 90, 70, 180)
    arc2.graph_info.color = ap.Color.dark_blue
    graph.shapes.add(arc2)

    arc3 = drawing.Arc(100, 100, 85, 120, 210)
    arc3.graph_info.color = ap.Color.red
    graph.shapes.add(arc3)

    page.paragraphs.add(graph)
    document.save(outfile)
```

## Créer un objet d'arc rempli

Cet exemple montre comment ajouter un segment d'arc rempli de couleur.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_arc_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    arc = drawing.Arc(100, 100, 95, 0, 90)

    arc.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(arc)

    line = drawing.Line([195, 100, 100, 100, 100, 195])
    line.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(line)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Résultat de l'ajout d'un arc rempli :

![Arc rempli](filled_arc.png)

## Sujets liés aux graphiques

- [Travailler avec les graphes PDF en Python](/pdf/fr/python-net/working-with-graphs/)
- [Ajouter des formes de cercle au PDF en Python](/pdf/fr/python-net/add-circle/)
- [Ajouter des formes de courbe au PDF en Python](/pdf/fr/python-net/add-curve/)
- [Ajouter des formes de ligne au PDF en Python](/pdf/fr/python-net/add-line/)