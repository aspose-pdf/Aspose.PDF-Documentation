---
title: Ajouter des formes de courbe au PDF en Python
linktitle: Ajouter une courbe
type: docs
weight: 30
url: /fr/python-net/add-curve/
description: Apprenez comment tracer et remplir des formes de courbe dans des fichiers PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tracer des formes de courbe dans des fichiers PDF à l'aide de Python
Abstract: Cet article montre comment ajouter des formes de courbe aux documents PDF avec Aspose.PDF for Python via .NET. Il couvre la création de courbes décrites, le remplissage d'objets de courbe et le rendu de chemins de courbe personnalisés dans un conteneur Graph.
---

## Ajouter un objet Courbe

Aspose.PDF for Python via .NET vous permet d'ajouter [Curve](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/) formes vers les pages PDF via le [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) classe.

Cet article montre comment créer des courbes à la fois tracées et remplies.

Suivez les étapes ci-dessous:

1. Créer [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instance.
1. Créer [Objet Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) avec certaines dimensions.
1. Définir [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) pour l'objet Graph.
1. Ajouter [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) objet à la collection paragraphs de la page.
1. Enregistrez notre fichier PDF.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_curve(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(curve1)

    page.paragraphs.add(graph)
    document.save(outfile)
```

L'image suivante montre le résultat exécuté avec notre extrait de code:

![Dessin de la courbe](drawing_curve.png)

## Créer un objet de courbe remplie

Cet exemple montre comment ajouter un objet Curve qui est rempli de couleur.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def add_curve_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(curve1)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Résultat de l'ajout d'une courbe remplie :

![Courbe remplie](filled_curve.png)

## Sujets liés aux graphiques

- [Travailler avec les graphes PDF en Python](/pdf/fr/python-net/working-with-graphs/)
- [Ajouter des formes d'arc au PDF en Python](/pdf/fr/python-net/add-arc/)
- [Ajouter des formes de ligne au PDF en Python](/pdf/fr/python-net/add-line/)
- [Ajouter des formes elliptiques au PDF en Python](/pdf/fr/python-net/add-ellipse/)