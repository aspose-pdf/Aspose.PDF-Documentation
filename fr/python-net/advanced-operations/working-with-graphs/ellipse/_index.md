---
title: Ajouter des formes d'ellipse au PDF en Python
linktitle: Ajouter une ellipse
type: docs
weight: 60
url: /fr/python-net/add-ellipse/
description: Apprenez à dessiner, remplir et étiqueter des formes d'ellipse dans les fichiers PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dessiner des formes d'ellipse dans des fichiers PDF en utilisant Python
Abstract: Cet article montre comment ajouter des formes d'ellipse aux documents PDF avec Aspose.PDF for Python via .NET. Il couvre les ellipses avec contour, les ellipses remplies et l'ajout de texte à l'intérieur des objets ellipse.
---

## Ajouter l'objet Ellipse

Aspose.PDF for Python via .NET vous permet d'ajouter [Ellipse](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) formes aux pages PDF avec le [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) classe. Vous pouvez dessiner des contours d'ellipse, appliquer des couleurs de remplissage et placer du texte à l'intérieur des objets ellipse.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_ellipse(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    ellipse1 = drawing.Ellipse(150, 100, 120, 60)
    ellipse1.graph_info.color = ap.Color.green_yellow
    ellipse1.text = ap.text.TextFragment("Ellipse")
    graph.shapes.add(ellipse1)

    ellipse2 = drawing.Ellipse(50, 50, 18, 300)
    ellipse2.graph_info.color = ap.Color.dark_red
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![Ajouter une ellipse](ellipse.png)

## Créer un objet ellipse rempli

Le fragment de code suivant montre comment ajouter un [Ellipse](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) objet rempli de couleur.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def create_ellipse_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    ellipse1 = drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(ellipse1)

    ellipse2 = drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![Ellipse remplie](fill_ellipse.png)

## Ajouter du texte à l'intérieur de l'ellipse

Aspose.PDF for Python via .NET vous permet également d'insérer du texte dans les objets de forme. L'exemple suivant ajoute du texte aux formes ellipse.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_text_inside_ellipse(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    text_fragment = ap.text.TextFragment("Ellipse")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Helvetica")
    text_fragment.text_state.font_size = 24

    ellipse1 = ap.drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    ellipse1.text = text_fragment
    graph.shapes.add(ellipse1)

    ellipse2 = ap.drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    ellipse2.text = text_fragment
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![Texte à l'intérieur de l'Ellipse](text_ellipse.png)

## Sujets liés aux graphiques

- [Travailler avec les graphes PDF en Python](/pdf/fr/python-net/working-with-graphs/)
- [Ajouter des formes de cercle au PDF en Python](/pdf/fr/python-net/add-circle/)
- [Ajouter des formes de courbe au PDF en Python](/pdf/fr/python-net/add-curve/)
- [Ajouter des formes rectangulaires au PDF en Python](/pdf/fr/python-net/add-rectangle/)
