---
title: Linienformen zu PDF in Python hinzufügen
linktitle: Linie hinzufügen
type: docs
weight: 40
url: /de/python-net/add-line/
description: Erfahren Sie, wie Sie Linienformen und formatierte Linien in PDF-Dateien mit Python zeichnen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Linienformen in PDF-Dateien mit Python zeichnen
Abstract: Dieser Artikel zeigt, wie man Linienformen zu PDF-Dokumenten mit Aspose.PDF for Python via .NET hinzufügt. Er behandelt das Erstellen einfacher Linien, das Konfigurieren von gestrichelten Linienstilen und das Zeichnen von Linien über eine Seite.
---

## Linienobjekt hinzufügen

Aspose.PDF for Python via .NET ermöglicht das Hinzufügen [Linie](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) Formen zu PDF-Seiten mithilfe der [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) Klasse. Sie können die Linienfarbe, das Strichmuster und die Platzierung steuern.

Befolgen Sie die nachstehenden Schritte:

1. Erstellen [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Instanz.
1. Erstelle ein Graph-Objekt
1. Hinzufügen [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) Objekt zur Absatzsammlung der Seite.
1. Erstelle und konfiguriere die Linie
1. Füge das [Linie](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) zum Graph
1. Speichern Sie unsere PDF-Datei.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def add_line(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    line = drawing.Line([100, 100, 200, 100])
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1
    graph.shapes.add(line)

    document.save(outfile)
```

![Linie hinzufügen](add_line.png)

## Wie man eine gepunktete gestrichelte Linie zu Ihrem PDF-Dokument hinzufügt

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_dotted_dashed_line(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    line = drawing.Line([100, 100, 200, 100])
    line.graph_info.color = ap.Color.red
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1
    graph.shapes.add(line)

    document.save(outfile)
```

Ergebnis beim Hinzufügen einer gepunkteten gestrichelten Linie:

![Gestrichelte Linie](dash_line.png)

## Linie über die Seite zeichnen

Sie können auch Linien über die Seite zeichnen, um ein Kreuz zu bilden.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def draw_line_across_page(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    page.page_info.margin.left = 0
    page.page_info.margin.right = 0
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0

    graph = drawing.Graph(page.page_info.width, page.page_info.height)
    line = drawing.Line([page.rect.llx, 0, page.page_info.width, page.rect.ury])
    graph.shapes.add(line)
    line2 = drawing.Line([0, page.rect.ury, page.page_info.width, page.rect.llx])
    graph.shapes.add(line2)
    page.paragraphs.add(graph)

    document.save(outfile)
```

![Linie zeichnen](draw_line.png)

## Verwandte Graph-Themen

- [Arbeiten mit PDF-Graphen in Python](/pdf/de/python-net/working-with-graphs/)
- [Kurvenformen zum PDF in Python hinzufügen](/pdf/de/python-net/add-curve/)
- [Fügen Sie Rechteckformen zum PDF in Python hinzu.](/pdf/de/python-net/add-rectangle/)
- [Formgrenzen in PDF-Grafiken mit Python prüfen](/pdf/de/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)
