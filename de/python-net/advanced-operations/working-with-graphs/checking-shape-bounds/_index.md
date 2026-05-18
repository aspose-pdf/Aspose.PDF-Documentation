---
title: Formgrenzen in PDF‑Diagrammen mit Python prüfen
linktitle: Formgrenzen prüfen
type: docs
weight: 70
url: /de/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Erfahren Sie, wie Sie Formgrenzen in PDF‑Diagrammsammlungen mit Python validieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validieren Sie Diagrammformgrenzen in PDF‑Dateien mit Python
Abstract: Dieser Artikel zeigt, wie Sie Formgrenzen in Graph‑Sammlungen mit Aspose.PDF für Python via .NET validieren. Er behandelt die Konfiguration von BoundsCheckMode, das Erkennen von Formen außerhalb des zulässigen Bereichs und das sichere Behandeln von Ausnahmen bei Grenzen.
---

## Formgrenzen in einem Diagramm prüfen

Wenn Sie Formen zu einer [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/), können Sie die Begrenzungsvalidierung aktivieren, um sicherzustellen, dass jede Form innerhalb des Diagrammbereichs passt.

Verwenden [BoundsCheckMode](https://reference.aspose.com/pdf/python-net/aspose.pdf/boundscheckmode/) um das Verhalten zu definieren, wenn eine Form außerhalb des Bereichs liegt. In diesem Beispiel, `THROW_EXCEPTION_IF_DOES_NOT_FIT` wird verwendet, um eine Ausnahme auszulösen.

Befolgen Sie die nachstehenden Schritte:

1. Erstellen Sie ein neues PDF [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Hinzufügen [Seite](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Erstelle ein [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) und fügen Sie es der Seite hinzu.
1. Erstelle ein [Rechteck](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) die außerhalb der Diagrammgrenzen reicht.
1. Grenzüberprüfungsmodus festlegen auf `THROW_EXCEPTION_IF_DOES_NOT_FIT`.
1. Fügen Sie das Rechteck hinzu und behandeln Sie die Ausnahme.
1. Speichern Sie das Dokument.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def check_shape_bounds(outfile: str):
    document = ap.Document()
    page = document.pages.add()

    graph = drawing.Graph(100, 100)
    graph.top = 10
    graph.left = 15
    graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(-1, 0, 50, 50)
    rect.graph_info.fill_color = ap.Color.tomato

    try:
        graph.shapes.update_bounds_check_mode(
            ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT
        )
        graph.shapes.add(rect)
    except Exception as e:
        print(e)

    document.save(outfile)
```

## Hinweise

- Verwenden `THROW_EXCEPTION_IF_DOES_NOT_FIT` wenn eine strenge Layout-Validierung erforderlich ist.
- Für ein permissives Verhalten wählen Sie ein anderes `BoundsCheckMode` Option basierend auf Ihren Layout-Anforderungen.

## Verwandte Graph-Themen

- [Arbeiten mit PDF-Graphen in Python](/pdf/de/python-net/working-with-graphs/)
- [Fügen Sie Rechteckformen zum PDF in Python hinzu.](/pdf/de/python-net/add-rectangle/)
- [Linienformen zum PDF in Python hinzufügen](/pdf/de/python-net/add-line/)
- [Fügen Sie Ellipsenformen zum PDF in Python hinzu.](/pdf/de/python-net/add-ellipse/)
