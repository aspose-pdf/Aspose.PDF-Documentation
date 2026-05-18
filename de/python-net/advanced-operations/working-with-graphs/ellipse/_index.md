---
title: Ellipseformen zu PDF in Python hinzufügen
linktitle: Ellipse hinzufügen
type: docs
weight: 60
url: /de/python-net/add-ellipse/
description: Erfahren Sie, wie Sie Ellipsenformen in PDF-Dateien mit Python zeichnen, füllen und beschriften.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ellipseformen in PDF-Dateien mit Python zeichnen
Abstract: Dieser Artikel zeigt, wie man Ellipsenformen zu PDF-Dokumenten mit Aspose.PDF for Python via .NET hinzufügt. Er behandelt umrandete Ellipsen, gefüllte Ellipsen und das Hinzufügen von Text innerhalb von Ellipsenobjekten.
---

## Ellipse-Objekt hinzufügen

Aspose.PDF for Python via .NET ermöglicht das Hinzufügen [Ellipse](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) Formen zu PDF-Seiten mit dem [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) Klasse. Sie können Ellipsenumrisse zeichnen, Füllfarben anwenden und Text in Ellipsenobjekten platzieren.

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

![Ellipse hinzufügen](ellipse.png)

## Gefülltes Ellipsenobjekt erstellen

Der folgende Codeabschnitt zeigt, wie man ein [Ellipse](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) Objekt, das mit Farbe gefüllt ist.

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

![Gefüllte Ellipse](fill_ellipse.png)

## Text innerhalb der Ellipse hinzufügen

Aspose.PDF for Python via .NET ermöglicht es Ihnen außerdem, Text innerhalb von Shape-Objekten zu platzieren. Das folgende Beispiel fügt Text zu Ellipsenformen hinzu.

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

![Text innerhalb der Ellipse](text_ellipse.png)

## Verwandte Graph-Themen

- [Arbeiten mit PDF-Graphen in Python](/pdf/de/python-net/working-with-graphs/)
- [Kreisformen zum PDF in Python hinzufügen](/pdf/de/python-net/add-circle/)
- [Kurvenformen zum PDF in Python hinzufügen](/pdf/de/python-net/add-curve/)
- [Fügen Sie Rechteckformen zum PDF in Python hinzu.](/pdf/de/python-net/add-rectangle/)
