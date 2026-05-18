---
title: Arc-Formen zu PDF in Python hinzufügen
linktitle: Arc hinzufügen
type: docs
weight: 10
url: /de/python-net/add-arc/
description: Erfahren Sie, wie Sie Arc-Formen in PDF-Dateien mit Python zeichnen und füllen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Arc-Formen in PDF-Dateien mit Python zeichnen
Abstract: Dieser Artikel zeigt, wie man Arc-Formen zu PDF-Dokumenten mit Aspose.PDF for Python via .NET hinzufügt. Er behandelt das Erstellen von umrissenen Arc-Formen, das Zeichnen von gefüllten Arc-Segmenten und das Hinzufügen dieser zu einem Graph-Container.
---

## Arc-Objekt hinzufügen

Aspose.PDF for Python via .NET ermöglicht das Hinzufügen [Bogen](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) Formen zu PDF-Seiten mithilfe der [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) Klasse. Sie können umrissene Bögen und gefüllte Bogenabschnitte für Diagramme und technische Illustrationen zeichnen.

Befolgen Sie die nachstehenden Schritte:

1. Erstellen [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Instanz.
1. Erstellen [Graphobjekt](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) mit bestimmten Abmessungen.
1. Setzen [Rand](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) für das Graph-Objekt.
1. Erstellen Sie ein entsprechendes Bogen-Objekt.
1. Fügen Sie dieses Objekt zur Shapes-Sammlung im Graph-Objekt hinzu.
1. Hinzufügen [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) Objekt zur Absatzsammlung der Seite.
1. Speichern Sie unsere PDF-Datei.

Der folgende Codeabschnitt zeigt, wie man ein [Bogen](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) Objekt.

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

## Gefülltes Bogen-Objekt erstellen

Dieses Beispiel zeigt, wie man ein mit Farbe gefülltes Bogensegment hinzufügt.

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

Ergebnis des Hinzufügens eines gefüllten Bogens:

![Gefüllter Bogen](filled_arc.png)

## Verwandte Graph-Themen

- [Arbeiten mit PDF-Graphen in Python](/pdf/de/python-net/working-with-graphs/)
- [Kreisformen zum PDF in Python hinzufügen](/pdf/de/python-net/add-circle/)
- [Kurvenformen zum PDF in Python hinzufügen](/pdf/de/python-net/add-curve/)
- [Linienformen zum PDF in Python hinzufügen](/pdf/de/python-net/add-line/)