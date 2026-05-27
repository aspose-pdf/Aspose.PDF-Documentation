---
title: Ajouter des formes rectangulaires à un PDF en Python
linktitle: Ajouter un rectangle
type: docs
weight: 50
url: /fr/python-net/add-rectangle/
description: Apprenez comment dessiner et remplir des formes rectangulaires dans des fichiers PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dessiner des formes rectangulaires dans des fichiers PDF en utilisant Python
Abstract: Cet article montre comment ajouter des formes rectangulaires aux documents PDF avec Aspose.PDF for Python via .NET. Il couvre les rectangles tracés, les remplissages pleins et dégradés, la transparence alpha et le contrôle de l'ordre Z.
---

## Ajouter l'objet Rectangle

Aspose.PDF for Python via .NET vous permet d'ajouter [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) formes vers les pages PDF via le [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) classe. Vous pouvez dessiner des rectangles bordés et appliquer des remplissages pleins, dégradés ou transparents.

Suivez les étapes ci-dessous:

1. Créer un nouveau PDF [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Ajouter [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) à la collection de pages du fichier PDF.
1. Ajouter [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) vers la collection de paragraphes de l'instance de page.
1. Créer [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) instance.
1. Définir la bordure pour [Objet Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/).
1. Ajouter [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) objet vers la collection de formes de l'objet Graph.
1. Ajouter l'objet graphique à la collection de paragraphes de l'instance de page.
1. Ajouter [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) vers la collection de paragraphes de l'instance de page.
1. Et enregistrez votre fichier PDF

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_rectangle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("Rectangle")
    page.paragraphs.add(text_fragment)

    graph = drawing.Graph(400, 300)
    page.paragraphs.add(graph)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    rect = drawing.Rectangle(20, 20, 350, 250)
    graph.shapes.add(rect)
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

![Créer un rectangle](create_rectangle.png)

## Créer un objet rectangle rempli

Aspose.PDF for Python via .NET offre également la fonction de remplir l'objet rectangle avec une certaine couleur.

Le fragment de code suivant montre comment ajouter un [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) objet rempli de couleur.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def create_rectangle_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(100, 100, 200, 120)
    rect.graph_info.fill_color = ap.Color.red
    graph.shapes.add(rect)

    document.save(outfile)
```

Résultat du rectangle rempli avec une couleur unie :

![Rectangle rempli](fill_rectangle.png)

## Ajouter un dessin avec remplissage en dégradé

Aspose.PDF for Python via .NET prend en charge la fonctionnalité d'ajouter des objets graphiques aux documents PDF et il est parfois nécessaire de remplir ces objets graphiques avec une couleur en dégradé.

Le fragment de code suivant montre comment ajouter un [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) objet rempli avec une couleur en dégradé.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_drawing_with_gradient_fill(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(0, 0, 300, 300)
    gradient_color = ap.Color()
    gradient_settings = drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    gradient_settings.start = ap.Point(0, 0)
    gradient_settings.end = ap.Point(350, 350)
    gradient_color.pattern_color_space = gradient_settings
    rect.graph_info.fill_color = gradient_color
    graph.shapes.add(rect)

    document.save(outfile)
```

![Rectangle dégradé](gradient.png)

## Créer un rectangle avec un canal de couleur alpha

Aspose.PDF for Python via .NET prend également en charge la transparence via un canal de couleur alpha.

Le fragment de code suivant montre comment ajouter un [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) objet avec des valeurs alpha.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def create_rectangle_with_alpha_color_channel(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(100, 100, 200, 120)
    rect.graph_info.fill_color = ap.Color.from_argb(128, 244, 180, 0)
    graph.shapes.add(rect)

    rect1 = drawing.Rectangle(200, 150, 200, 100)
    rect1.graph_info.fill_color = ap.Color.from_argb(160, 120, 0, 120)
    graph.shapes.add(rect1)

    document.save(outfile)
```

![Couleur du canal Alpha du rectangle](rectangle_color.png)

## Contrôler l'ordre Z des formes

Aspose.PDF for .NET prend en charge la fonctionnalité d’ajout d’objets graphiques (par exemple graphique, ligne, rectangle, etc.) aux documents PDF. Lors de l’ajout de plusieurs instances du même objet dans un fichier PDF, nous pouvons contrôler leur rendu en spécifiant l’ordre Z. L’ordre Z est également utilisé lorsque nous devons rendre les objets les uns sur les autres.

Le fragment de code suivant montre les étapes pour rendre [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) objets les uns sur les autres.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def _add_rectangle_to_page(
    page: ap.Page,
    x: float,
    y: float,
    width: float,
    height: float,
    color: ap.Color,
    zindex: int,
):
    graph = drawing.Graph(width, height)
    graph.is_change_position = False
    graph.left = x
    graph.top = y
    rect = drawing.Rectangle(0, 0, width, height)
    rect.graph_info.fill_color = color
    rect.graph_info.color = color
    graph.shapes.add(rect)
    graph.z_index = zindex
    page.paragraphs.add(graph)


def control_z_order_of_rectangle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(375, 300)
    page.page_info.margin.left = 0
    page.page_info.margin.top = 0

    _add_rectangle_to_page(page, 50, 40, 60, 40, ap.Color.red, 2)
    _add_rectangle_to_page(page, 20, 20, 30, 30, ap.Color.blue, 1)
    _add_rectangle_to_page(page, 40, 40, 60, 30, ap.Color.green, 0)

    document.save(outfile)
```

![Contrôle de l'ordre Z](control.png)

## Sujets liés aux graphiques

- [Travailler avec les graphes PDF en Python](/pdf/fr/python-net/working-with-graphs/)
- [Vérifier les limites de forme dans les graphiques PDF avec Python](/pdf/fr/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)
- [Ajouter des formes de ligne au PDF en Python](/pdf/fr/python-net/add-line/)
- [Ajouter des formes elliptiques au PDF en Python](/pdf/fr/python-net/add-ellipse/)