---
title: Ajouter des formes de cercle au PDF en Python
linktitle: Ajouter un cercle
type: docs
weight: 20
url: /fr/python-net/add-circle/
description: Apprenez comment dessiner et remplir des formes de cercle dans des fichiers PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dessiner des formes de cercle dans des fichiers PDF en utilisant Python
Abstract: Cet article montre comment ajouter des formes de cercle aux documents PDF avec Aspose.PDF for Python via .NET. Il couvre la création de cercles à contour, le remplissage de cercles avec de la couleur et l'insertion de texte à l'intérieur des objets cercle.
---

## Ajouter un objet Cercle

Aspose.PDF for Python via .NET vous permet d'ajouter [Circle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/circle/) formes vers les pages PDF via le [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) classe. Utilisez des cercles pour les diagrammes, les annotations et les éléments visuels simples.

Suivez les étapes ci-dessous:

1. Créer [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instance.
1. Créer [Objet Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) avec certaines dimensions.
1. Définir [bordure](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) pour l'objet Graph.
1. Ajouter [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) objet à la collection paragraphs de la page.
1. Enregistrez notre fichier PDF.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_circle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    circle = drawing.Circle(100, 100, 40)
    circle.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(circle)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Notre cercle dessiné aura cette apparence :

![Dessiner un cercle](drawing_circle.png)

## Créer un objet cercle rempli

Cet exemple montre comment ajouter un cercle et le remplir de couleur.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_circle_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    circle = drawing.Circle(100, 100, 40)
    circle.graph_info.color = ap.Color.green_yellow
    circle.graph_info.fill_color = ap.Color.green
    circle.text = ap.text.TextFragment("Circle")
    graph.shapes.add(circle)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Résultat de l'ajout d'un cercle rempli :

![Cercle rempli](filled_circle.png)

## Sujets liés aux graphiques

- [Travailler avec les graphes PDF en Python](/pdf/fr/python-net/working-with-graphs/)
- [Ajouter des formes d'arc au PDF en Python](/pdf/fr/python-net/add-arc/)
- [Ajouter des formes elliptiques au PDF en Python](/pdf/fr/python-net/add-ellipse/)
- [Ajouter des formes rectangulaires au PDF en Python](/pdf/fr/python-net/add-rectangle/)