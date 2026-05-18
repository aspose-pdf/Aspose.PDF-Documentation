---
title: Rechteckformen zu PDF in Python hinzufügen
linktitle: Rechteck hinzufügen
type: docs
weight: 50
url: /de/python-net/add-rectangle/
description: Erfahren Sie, wie Sie Rechteckformen in PDF-Dateien mit Python zeichnen und füllen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Zeichnen Sie Rechteckformen in PDF-Dateien mit Python
Abstract: Dieser Artikel zeigt, wie man Rechteckformen zu PDF-Dokumenten mit Aspose.PDF for Python via .NET hinzufügt. Er behandelt umrandete Rechtecke, solide und Verlauf‑Füllungen, Alpha‑Transparenz und die Z‑Order‑Steuerung.
---

## Rectangle-Objekt hinzufügen

Aspose.PDF for Python via .NET ermöglicht das Hinzufügen [Rechteck](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) Formen zu PDF‑Seiten durch die [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) class. Sie können umrandete Rechtecke zeichnen und solide, Verlauf‑ oder transparente Füllungen anwenden.

Befolgen Sie die nachstehenden Schritte:

1. Erstellen Sie ein neues PDF [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Hinzufügen [Seite](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) zur pages collection der PDF-Datei.
1. Hinzufügen [Textfragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) zur Absatzsammlung der Seiteninstanz.
1. Erstellen [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) Instanz.
1. Rand festlegen für [Graphobjekt](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/).
1. Hinzufügen [Rechteck](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) Objekt zur Formen­sammlung des Graph-Objekts.
1. Füge das Graph-Objekt zur Absatzsammlung der Seiteninstanz hinzu.
1. Hinzufügen [Textfragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) zur Absatzsammlung der Seiteninstanz.
1. Und speichere deine PDF-Datei

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

![Rechteck erstellen](create_rectangle.png)

## Gefülltes Rechteckobjekt erstellen

Aspose.PDF for Python via .NET bietet ebenfalls die Funktion, ein Rechteckobjekt mit einer bestimmten Farbe zu füllen.

Der folgende Codeabschnitt zeigt, wie man ein [Rechteck](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) Objekt, das mit Farbe gefüllt ist.

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

Ergebnis des Rechtecks, das mit einer Vollfarbe gefüllt ist:

![Gefülltes Rechteck](fill_rectangle.png)

## Zeichnung mit Farbverlauf hinzufügen

Aspose.PDF for Python via .NET unterstützt die Funktion, Grafikobjekte zu PDF-Dokumenten hinzuzufügen, und manchmal ist es erforderlich, Grafikobjekte mit Farbverlauf zu füllen.

Der folgende Codeabschnitt zeigt, wie man ein [Rechteck](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) Objekt, das mit Farbverlauf gefüllt ist.

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

![Gradient Rechteck](gradient.png)

## Rechteck mit Alpha-Farbkanal erstellen

Aspose.PDF for Python via .NET unterstützt ebenfalls Transparenz durch einen Alpha-Farbkanal.

Der folgende Codeabschnitt zeigt, wie man ein [Rechteck](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) Objekt mit Alpha-Werten.

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

![Rechteck Alpha-Kanal-Farbe](rectangle_color.png)

## Steuern der Z-Reihenfolge von Formen

Aspose.PDF for .NET unterstützt die Funktion, Grafikobjekte (z. B. Diagramm, Linie, Rechteck usw.) zu PDF-Dokumenten hinzuzufügen. Beim Hinzufügen von mehr als einer Instanz desselben Objekts in einer PDF-Datei können wir deren Darstellung steuern, indem wir die Z-Reihenfolge angeben. Die Z-Reihenfolge wird auch verwendet, wenn wir Objekte übereinander rendern müssen.

Der folgende Codeabschnitt zeigt die Schritte zum Rendern [Rechteck](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) Objekte übereinander.

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

![Steuerung der Z-Reihenfolge](control.png)

## Verwandte Graph-Themen

- [Arbeiten mit PDF-Graphen in Python](/pdf/de/python-net/working-with-graphs/)
- [Formgrenzen in PDF-Grafiken mit Python prüfen](/pdf/de/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)
- [Linienformen zum PDF in Python hinzufügen](/pdf/de/python-net/add-line/)
- [Fügen Sie Ellipsenformen zum PDF in Python hinzu.](/pdf/de/python-net/add-ellipse/)