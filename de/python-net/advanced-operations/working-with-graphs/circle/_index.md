---
title: Kreisformen zu PDF in Python hinzufügen
linktitle: Kreis hinzufügen
type: docs
weight: 20
url: /de/python-net/add-circle/
description: Erfahren Sie, wie Sie Kreisformen in PDF-Dateien in Python zeichnen und ausfüllen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Zeichnen Sie Kreisformen in PDF-Dateien mit Python
Abstract: Dieser Artikel zeigt, wie man Kreisformen zu PDF-Dokumenten mit Aspose.PDF for Python via .NET hinzufügt. Er behandelt das Erstellen von umrandeten Kreisen, das Füllen von Kreisen mit Farbe und das Platzieren von Text in Kreisobjekten.
---

## Kreisobjekt hinzufügen

Aspose.PDF for Python via .NET ermöglicht das Hinzufügen [Kreis](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/circle/) Formen zu PDF‑Seiten durch die [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) Klasse. Verwenden Sie Kreise für Diagramme, Anmerkungen und einfache visuelle Elemente.

Befolgen Sie die nachstehenden Schritte:

1. Erstellen [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Instanz.
1. Erstellen [Graphobjekt](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) mit bestimmten Abmessungen.
1. Setzen [Rand](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) für das Graph-Objekt.
1. Hinzufügen [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) Objekt zur Absatzsammlung der Seite.
1. Speichern Sie unsere PDF-Datei.

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

Unser gezeichneter Kreis wird so aussehen:

![Kreis zeichnen](drawing_circle.png)

## Gefülltes Kreisobjekt erstellen

Dieses Beispiel zeigt, wie man einen Kreis hinzufügt und ihn mit Farbe füllt.

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

Ergebnis des Hinzufügens eines gefüllten Kreises:

![Gefüllter Kreis](filled_circle.png)

## Verwandte Graph-Themen

- [Arbeiten mit PDF-Graphen in Python](/pdf/de/python-net/working-with-graphs/)
- [Bogenformen zu PDF in Python hinzufügen](/pdf/de/python-net/add-arc/)
- [Fügen Sie Ellipsenformen zum PDF in Python hinzu.](/pdf/de/python-net/add-ellipse/)
- [Fügen Sie Rechteckformen zum PDF in Python hinzu.](/pdf/de/python-net/add-rectangle/)