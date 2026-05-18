---
title: Verwenden Sie FloatingBox für PDF-Layout in Python
linktitle: FloatingBox verwenden
type: docs
weight: 30
url: /de/python-net/floating-box/
description: Erfahren Sie, wie Sie FloatingBox für die Textanordnung, mehrspaltigen Inhalt und präzise Positionierung in PDF-Dokumenten mit Python verwenden.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Erstellen und positionieren Sie formatierte FloatingBox-Container in PDF mit Python.
Abstract: Dieser Artikel erklärt, wie man FloatingBox in Aspose.PDF for Python via .NET verwendet. Erfahren Sie, wie Sie Text und andere Inhalte in stilisierten schwebenden Containern platzieren, das Layout, Rahmen, Ausrichtung und das Clipping steuern und strukturiertere PDF‑Seiten‑Designs in Python erstellen.
---

## Grundlegende Verwendung von FloatingBox

Der [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) Klasse ist ein Container zum Platzieren von Text und anderem Inhalt auf einer PDF‑Seite. Sie gibt Ihnen eine stärkere Kontrolle über Layout, Ränder und Stilierung als reguläre Textabsätze. Wenn der Inhalt die Boxgröße überschreitet, wird das Abschneiden‑Verhalten durch die Boxeinstellungen gesteuert.

Verwenden Sie diese Seite, wenn Sie strukturierte Textcontainer, mehrspaltige Layouts und präzise Positionierung in PDF-Dokumenten mit Aspose.PDF for Python via .NET benötigen.

1. Neu erstellen [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Hinzufügen [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) zum Dokument.
1. Erstelle ein [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/).
1. Setzen Sie den Rand der Box mit [`BorderInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) und [`BorderSide`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderside/).
1. Wiederholung der Steuerelementbox mit dem [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) Eigenschaft.
1. Textinhalt hinzufügen mit [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/).
1. Füge das `FloatingBox` zu dem [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Speichern Sie das endgültige PDF‑Dokument mit [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import aspose.pdf as ap

def create_and_add_floating_box(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.border = ap.BorderInfo(ap.BorderSide.ALL, 1.5, ap.Color.dark_green)
        box.is_need_repeating = False
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        box.paragraphs.add(ap.text.TextFragment(phrase))
        # Add box
        page.paragraphs.add(box)
        document.save(outfile)
```

Im obigen Beispiel ist die `FloatingBox` wird mit einer Breite von 400 pt und einer Höhe von 30 pt erstellt.
Der Text überschreitet absichtlich die verfügbare Höhe, sodass ein Teil davon abgeschnitten wird.

![Bild 1](image01.png)

Der [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) Eigenschaft mit einem Wert von `False` Begrenzt das Rendern von Text auf einer einzelnen Seite.

Wenn Sie diese Eigenschaft auf `True`, der Text fließt zu nachfolgenden Seiten an derselben Position um.

![Bild 2](image02.png)

## Erweiterte FloatingBox-Funktionen

### Mehrspaltenunterstützung

#### Mehrspaltiges Layout (einfacher Fall)

`FloatingBox` unterstützt ein mehrspaltiges Layout. Um ein solches Layout zu erstellen, müssen Sie die Werte des [`ColumnInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/columninfo/) Eigenschaften.

* `column_widths` ist eine Zeichenkette, die die Breite jeder Spalte in Punkten definiert.
* `column_spacing` ist eine Zeichenkette, die die Lückenbreite zwischen Spalten definiert.
* `column_count` ist die Anzahl der Spalten.

```python
import sys
import aspose.pdf as ap
from os import path

def multi_column_layout(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Set margin settings
        page.page_info.margin = ap.MarginInfo(36, 18, 36, 18)
        column_count = 3
        spacing = 10
        width = (
            page.page_info.width
            - page.page_info.margin.left
            - page.page_info.margin.right
            - (column_count - 1) * spacing
        )
        column_width = width / 3
        # Create FloatingBox
        box = ap.FloatingBox()
        box.is_need_repeating = True
        box.column_info.column_widths = f"{column_width} {column_width} {column_width}"
        box.column_info.column_spacing = f"{spacing}"
        box.column_info.column_count = 3
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        paragraphs = [
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
        ]
        for paragraph in paragraphs:
            box.paragraphs.add(ap.text.TextFragment(paragraph))
        # Add a box to a page
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

Das Beispiel erzeugt Beispielabsätze und platziert sie über drei Spalten. Der Inhalt wird auf zusätzlichen Seiten fortgesetzt, bis alle Absätze gerendert sind.

#### Mehrspaltiges Layout mit erzwungenem Spaltenbeginn

Dieses Beispiel verwendet dieselbe mehrspaltige Anordnung, zwingt jedoch jeden hinzugefügten Absatz, in einer neuen Spalte zu beginnen. Um dies zu tun, setzen Sie `is_first_paragraph_in_column = True` bei jedem `TextFragment` bevor es dem hinzugefügt wird `FloatingBox`.

```python
import sys
import aspose.pdf as ap
from os import path

def multi_column_layout_2(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Set margin settings
        page.page_info.margin = ap.MarginInfo(36, 18, 36, 18)
        column_count = 3
        spacing = 10
        width = (
            page.page_info.width
            - page.page_info.margin.left
            - page.page_info.margin.right
            - (column_count - 1) * spacing
        )
        column_width = width / 3
        # Create FloatingBox
        box = ap.FloatingBox()
        box.is_need_repeating = True
        box.column_info.column_widths = f"{column_width} {column_width} {column_width}"
        box.column_info.column_spacing = f"{spacing}"
        box.column_info.column_count = 3
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        paragraphs = [
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
        ]
        for paragraph in paragraphs:
            text = ap.text.TextFragment(paragraph)
            text.is_first_paragraph_in_column = True
            box.paragraphs.add(text)
        # Add a box to a page
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

### Hintergrundunterstützung

Wenden Sie eine Hintergrundfarbe auf ein `FloatingBox` in einem PDF-Dokument mit Aspose.PDF for Python via .NET.
Durch Zuweisen eines [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) zu `background_color`, Sie können Inhalte für Überschriften, Hervorhebungen oder formatierte Abschnitte hervorheben.

Dieses Code‑Snippet zeigt, wie man ein einfaches hellgrünes Textfeld mit Beispielinhalt erstellt.

```python
import sys
import aspose.pdf as ap
from os import path

def background_support(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.background_color = ap.Color.light_green
        box.is_need_repeating = False
        box.paragraphs.add(ap.text.TextFragment("text example"))
        # Add box
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

### Positionierungsunterstützung

Die Position von einem `FloatingBox` auf der Seite wird gesteuert von `positioning_mode`, `left`, und `top`.
Wenn `positioning_mode` ist:

* [`ParagraphPositioningMode.DEFAULT`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/) (Standard)

Der Standort hängt von zuvor hinzugefügten Elementen ab. Das Hinzufügen eines neuen Absatzes beeinflusst den Fluss nachfolgender Elemente. Wenn [`left`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) oder [`top`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) sind ungleich Null, sie werden ebenfalls angewendet.

* [`ParagraphPositioningMode.ABSOLUTE`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/)

Der Ort wird festgelegt durch `left` und `top`; es hängt nicht von vorherigen Elementen ab und beeinflusst den Ablauf späterer nicht.

```python
import sys
import aspose.pdf as ap
from os import path

def offset_support(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.top = 45
        box.left = 15
        box.positioning_mode = ap.ParagraphPositioningMode.ABSOLUTE
        box.border = ap.BorderInfo(ap.BorderSide.ALL, 1.5, ap.Color.dark_green)
        box.paragraphs.add(ap.text.TextFragment("text example 1"))
        page.paragraphs.add(ap.text.TextFragment("text example 2"))
        # Add the box to the page
        page.paragraphs.add(box)
        page.paragraphs.add(ap.text.TextFragment("text example 3"))
        document.save(outfile)
```

### Schwebende Boxen mit vertikaler und horizontaler Ausrichtung im PDF ausrichten

Ausrichten `FloatingBox` Elemente auf einer PDF-Seite verwenden [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) und [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) in Aspose.PDF for Python via .NET. Das hilft Ihnen, schwebende Container an oberen, mittleren oder unteren Positionen für Seitenlayouts, Kopf-/Fußzeilenblöcke oder Randnotizen zu platzieren.

1. Erstellen Sie ein neues PDF-Dokument.
1. Fügen Sie dem Dokument eine Seite hinzu.
1. Füge das Erste hinzu `FloatingBox` mit Ausrichtung unten rechts.
1. Füge das zweite hinzu `FloatingBox` mit zentriert-rechter Ausrichtung.
1. Füge das Dritte hinzu `FloatingBox` mit rechts-oben-Ausrichtung.
1. Speichern Sie das Dokument.

```python
import sys
import aspose.pdf as ap
from os import path

def align_text_to_float(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()

        # Create float box
        float_box = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box.vertical_alignment = ap.VerticalAlignment.BOTTOM
        float_box.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box.paragraphs.add(ap.text.TextFragment("FloatingBox_bottom"))
        float_box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box)

        # Create float box
        float_box_2 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_2.vertical_alignment = ap.VerticalAlignment.CENTER
        float_box_2.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_2.paragraphs.add(ap.text.TextFragment("FloatingBox_center"))
        float_box_2.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_2)

        # Create float box
        float_box_3 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_3.vertical_alignment = ap.VerticalAlignment.TOP
        float_box_3.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_3.paragraphs.add(ap.text.TextFragment("FloatingBox_top"))
        float_box_3.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_3)

        # Save the document
        document.save(outfile)
```

## Verwandte Textthemen

* [Arbeiten Sie mit Text in PDF mit Python](/pdf/de/python-net/working-with-text/)
* [Text zum PDF hinzufügen](/pdf/de/python-net/add-text-to-pdf-file/)
* [PDF-Text formatieren in Python](/pdf/de/python-net/text-formatting-inside-pdf/)
* [Tooltips zum PDF-Text in Python hinzufügen](/pdf/de/python-net/pdf-tooltip/)
