---
title: Kurvenformen zu PDF in Python hinzufügen
linktitle: Kurve hinzufügen
type: docs
weight: 30
url: /de/python-net/add-curve/
description: Erfahren Sie, wie Sie Kurvenformen in PDF-Dateien in Python zeichnen und füllen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Kurvenformen in PDF-Dateien mit Python zeichnen
Abstract: Dieser Artikel zeigt, wie man Kurvenformen zu PDF-Dokumenten mit Aspose.PDF for Python via .NET hinzufügt. Er behandelt das Erstellen von umrandeten Kurven, das Füllen von Kurvenobjekten und das Rendern benutzerdefinierter Kurvenpfade in einem Graph-Container.
---

## Kurvenobjekt hinzufügen

Aspose.PDF for Python via .NET ermöglicht das Hinzufügen [Kurve](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/) Formen zu PDF‑Seiten durch die [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) Klasse.

Dieser Artikel zeigt, wie man sowohl umrandete als auch gefüllte Kurven erstellt.

Befolgen Sie die nachstehenden Schritte:

1. Erstellen [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Instanz.
1. Erstellen [Graphobjekt](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) mit bestimmten Abmessungen.
1. Setzen [Rand](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) für das Graph-Objekt.
1. Hinzufügen [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) Objekt zur Absatzsammlung der Seite.
1. Speichern Sie unsere PDF-Datei.

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

Das folgende Bild zeigt das Ergebnis, das mit unserem Code-Snippet ausgeführt wurde:

![Kurve zeichnen](drawing_curve.png)

## Gefülltes Kurvenobjekt erstellen

Dieses Beispiel zeigt, wie man ein Kurvenobjekt hinzufügt, das mit Farbe gefüllt ist.

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

Ergebnis des Hinzufügens einer gefüllten Kurve:

![Gefüllte Kurve](filled_curve.png)

## Verwandte Graph-Themen

- [Arbeiten mit PDF-Graphen in Python](/pdf/de/python-net/working-with-graphs/)
- [Bogenformen zu PDF in Python hinzufügen](/pdf/de/python-net/add-arc/)
- [Linienformen zum PDF in Python hinzufügen](/pdf/de/python-net/add-line/)
- [Fügen Sie Ellipsenformen zum PDF in Python hinzu.](/pdf/de/python-net/add-ellipse/)