---
title: Formannotationen via Python
linktitle: Form‑Annotationen
type: docs
weight: 20
url: /de/python-net/shape-annotations/
description: Erfahren Sie, wie Sie Linien-, Quadrat-, Kreis-, Polygon- und Polylinien-Annotationen in PDF-Dokumenten hinzufügen, überprüfen und löschen, indem Sie Aspose.PDF for Python via .NET verwenden.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Arbeiten Sie mit geometrischen PDF-Anmerkungen in Python.
Abstract: Dieser Artikel erklärt, wie man Form‑Anmerkungen in PDF‑Dokumenten mit Aspose.PDF for Python via .NET erstellt, liest und entfernt. Er behandelt Linien‑, Quadrat‑, Kreis‑, Polygon‑ und Polylinien‑Anmerkungen, wobei jeder Arbeitsablauf in kleine Schritte unterteilt ist und vollständige Code‑Beispiele enthält.
---

Dieser Artikel zeigt, wie man mit Form‑Annotationen in PDF‑Dokumenten mithilfe von Aspose.PDF for Python via .NET arbeitet.

Das Beispielskript demonstriert mehrere geometriebasierte Anmerkungs-Workflows:

- Linienanmerkungen
- Quadratanmerkungen
- Kreisannotationen
- Polygon-Annotationen
- Polylinien-Anmerkungen

## Linienannotation 

### Linienannotation hinzufügen 

Dieses Beispiel fügt der ersten Seite eine Linienannotation hinzu und konfiguriert Pfeilstile, Linienbreite und ein Popup‑Fenster.

#### Öffnen Sie das Quell-PDF

```python
document = ap.Document(infile)
```

#### Erstellen und konfigurieren Sie die Linienannotation

```python
line_annotation = ap.annotations.LineAnnotation(
    document.pages[1],
    ap.Rectangle(550, 93, 562, 439, True),
    ap.Point(556, 99),
    ap.Point(556, 443),
)

line_annotation.title = "John Smith"
line_annotation.color = ap.Color.red
line_annotation.width = 3
line_annotation.starting_style = ap.annotations.LineEnding.OPEN_ARROW
line_annotation.ending_style = ap.annotations.LineEnding.OPEN_ARROW
```

#### Anhängen Sie das Popup und speichern Sie die PDF

```python
popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 124, 1021, 266, True),
)
line_annotation.popup = popup

document.pages[1].annotations.append(line_annotation)
document.save(outfile)
```

#### Vollständiges Beispiel

```python
def line_annotation_add(infile, outfile):
    document = ap.Document(infile)

    line_annotation = ap.annotations.LineAnnotation(
        document.pages[1],
        ap.Rectangle(550, 93, 562, 439, True),
        ap.Point(556, 99),
        ap.Point(556, 443),
    )

    line_annotation.title = "John Smith"
    line_annotation.color = ap.Color.red
    line_annotation.width = 3
    line_annotation.starting_style = ap.annotations.LineEnding.OPEN_ARROW
    line_annotation.ending_style = ap.annotations.LineEnding.OPEN_ARROW

    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 124, 1021, 266, True),
    )
    line_annotation.popup = popup

    document.pages[1].annotations.append(line_annotation)
    document.save(outfile)
```

### Linienannotation abrufen 

Um Linienanmerkungen zu prüfen, filtern Sie die Anmerkungssammlung auf der ersten Seite und casten jedes Ergebnis zu `LineAnnotation` so können Sie seine Start- und Endpunkte lesen.

#### Laden Sie das PDF und sammeln Sie Zeilenanmerkungen

```python
document = ap.Document(infile)

line_annotation = [
    cast(ap.annotations.LineAnnotation, annotation)
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.LINE
]
```

#### Geben Sie die Linienkoordinaten aus

```python
for annotation in line_annotation:
    print(
        f"[{annotation.starting.x},{annotation.starting.y}]"
        f"-[{annotation.ending.x},{annotation.ending.y}]"
    )
```

#### Vollständiges Beispiel

```python
def line_annotations_get(infile, outfile):
    document = ap.Document(infile)

    line_annotation = [
        cast(ap.annotations.LineAnnotation, annotation)
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    for annotation in line_annotation:
        print(
            f"[{annotation.starting.x},{annotation.starting.y}]"
            f"-[{annotation.ending.x},{annotation.ending.y}]"
        )
```

### Zeilenannotation löschen 

Dieser Workflow entfernt alle Linienanmerkungen von der ersten Seite und speichert das aktualisierte PDF.

#### Zeilenannotationen zum Entfernen finden

```python
document = ap.Document(infile)
page = document.pages[1]

line_annotations = [
    annotation
    for annotation in page.annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.LINE
]
```

#### Löschen Sie die Anmerkungen und speichern Sie das PDF

```python
for annotation in line_annotations:
    page.annotations.delete(annotation)

document.save(outfile)
```

#### Vollständiges Beispiel

```python
def line_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    line_annotations = [
        annotation
        for annotation in page.annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    for annotation in line_annotations:
        page.annotations.delete(annotation)

    document.save(outfile)
```


## Quadrat- und Kreis-Anmerkungen

### Quadratische Anmerkung hinzufügen 

Quadratische Anmerkungen sind nützlich, um rechteckige Bereiche in einem Dokument zu markieren. Dieses Beispiel erstellt eine quadratische Anmerkung mit Rand-, Füll‑ und Transparenzeinstellungen.

#### Öffnen Sie das PDF und erstellen Sie die Quadratannotation

```python
document = ap.Document(infile)

square_annotation = ap.annotations.SquareAnnotation(
    document.pages[1],
    ap.Rectangle(60, 600, 250, 450, True),
)
square_annotation.title = "John Smith"
square_annotation.color = ap.Color.blue
square_annotation.interior_color = ap.Color.blue_violet
square_annotation.opacity = 0.25
```

#### Fügen Sie die Anmerkung hinzu und speichern Sie das PDF

```python
document.pages[1].annotations.append(square_annotation)
document.save(outfile)
```

#### Vollständiges Beispiel

```python
def square_annotation_add(infile, outfile):
    document = ap.Document(infile)

    square_annotation = ap.annotations.SquareAnnotation(
        document.pages[1],
        ap.Rectangle(60, 600, 250, 450, True),
    )
    square_annotation.title = "John Smith"
    square_annotation.color = ap.Color.blue
    square_annotation.interior_color = ap.Color.blue_violet
    square_annotation.opacity = 0.25

    document.pages[1].annotations.append(square_annotation)
    document.save(outfile)
```

### Quadrat‑Annotation abrufen 

Um quadratische Anmerkungen zu prüfen, filtern Sie die Anmerkungen der ersten Seite nach dem `SQUARE` Tippen und drucken Sie jedes Rechteck.

#### Laden Sie das Dokument und sammeln Sie quadratische Anmerkungen

```python
document = ap.Document(infile)
square_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
]
```

#### Drucken Sie die Anmerkungsrechtecke

```python
for annotation in square_annotations:
    print(annotation.rect)
```

#### Vollständiges Beispiel

```python
def square_annotation_get(infile, outfile):
    document = ap.Document(infile)
    square_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
    ]

    for annotation in square_annotations:
        print(annotation.rect)
```

### Quadratische Anmerkung löschen 

Dieser Workflow entfernt alle quadratischen Anmerkungen von der ersten Seite und speichert das Dokument.

#### Quadrat-Anmerkungen finden und löschen

```python
document = ap.Document(infile)
square_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
]

for annotation in square_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Vollständiges Beispiel

```python
def square_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    square_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
    ]

    for annotation in square_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

### Kreis-Anmerkung hinzufügen 

Kreis-Anmerkungen kennzeichnen abgerundete Bereiche in einem PDF. Dieses Beispiel fügt eine Kreis-Anmerkung mit Füllfarbe, Transparenz und einer Popup-Anmerkung hinzu.

#### Öffnen Sie das PDF und erstellen Sie die Kreisannotation

```python
document = ap.Document(infile)

circle_annotation = ap.annotations.CircleAnnotation(
    document.pages[1],
    ap.Rectangle(270, 160, 483, 383, True),
)
circle_annotation.title = "John Smith"
circle_annotation.color = ap.Color.red
circle_annotation.interior_color = ap.Color.misty_rose
circle_annotation.opacity = 0.5
```

#### Anhängen Sie das Popup und speichern Sie die PDF

```python
circle_annotation.popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 316, 1021, 459, True),
)

document.pages[1].annotations.append(circle_annotation)
document.save(outfile)
```

#### Vollständiges Beispiel

```python
def circle_annotation_add(infile, outfile):
    document = ap.Document(infile)

    circle_annotation = ap.annotations.CircleAnnotation(
        document.pages[1],
        ap.Rectangle(270, 160, 483, 383, True),
    )
    circle_annotation.title = "John Smith"
    circle_annotation.color = ap.Color.red
    circle_annotation.interior_color = ap.Color.misty_rose
    circle_annotation.opacity = 0.5
    circle_annotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 316, 1021, 459, True),
    )

    document.pages[1].annotations.append(circle_annotation)
    document.save(outfile)
```

### Kreisannotation abrufen 

Um Kreis-Anmerkungen zu untersuchen, filtern Sie die Seitenanmerkungen nach dem `CIRCLE` Tippen und drucken Sie deren Rechtecke.

#### Laden Sie das Dokument und sammeln Sie Kreisanmerkungen

```python
document = ap.Document(infile)
circle_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
]
```

#### Drucken Sie die Anmerkungsrechtecke

```python
for annotation in circle_annotations:
    print(annotation.rect)
```

#### Vollständiges Beispiel

```python
def circle_annotation_get(infile, outfile):
    document = ap.Document(infile)
    circle_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
    ]

    for annotation in circle_annotations:
        print(annotation.rect)
```

### Kreisannotation löschen 

Dieser Workflow entfernt alle Kreisanmerkungen von der ersten Seite und speichert das Ausgabe-PDF.

#### Kreisanmerkungen finden und löschen

```python
document = ap.Document(infile)
circle_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
]

for annotation in circle_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Vollständiges Beispiel

```python
def circle_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    circle_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
    ]

    for annotation in circle_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


## Polygon‑ und Polyline‑Annotationen

### Polygon-Annotation hinzufügen 

Polygon-Anmerkungen definieren eine geschlossene Multi-Punkt-Form. Dieses Beispiel erstellt eine Polygon-Anmerkung aus einem Rechteck und einer Liste von Punkten.

#### Öffnen Sie das PDF und erstellen Sie die Polygon‑Anmerkung

```python
document = ap.Document(infile)

polygon_annotation = ap.annotations.PolygonAnnotation(
    document.pages[1],
    ap.Rectangle(200, 300, 400, 400, True),
    [
        ap.Point(200, 300),
        ap.Point(220, 300),
        ap.Point(250, 330),
        ap.Point(300, 304),
        ap.Point(300, 400),
    ],
)
polygon_annotation.title = "John Smith"
polygon_annotation.color = ap.Color.blue
polygon_annotation.interior_color = ap.Color.blue_violet
polygon_annotation.opacity = 0.25
```

#### Fügen Sie die Anmerkung hinzu und speichern Sie das PDF

```python
document.pages[1].annotations.append(polygon_annotation)
document.save(outfile)
```

#### Vollständiges Beispiel

```python
def polygon_annotation_add(infile, outfile):
    document = ap.Document(infile)

    polygon_annotation = ap.annotations.PolygonAnnotation(
        document.pages[1],
        ap.Rectangle(200, 300, 400, 400, True),
        [
            ap.Point(200, 300),
            ap.Point(220, 300),
            ap.Point(250, 330),
            ap.Point(300, 304),
            ap.Point(300, 400),
        ],
    )
    polygon_annotation.title = "John Smith"
    polygon_annotation.color = ap.Color.blue
    polygon_annotation.interior_color = ap.Color.blue_violet
    polygon_annotation.opacity = 0.25

    document.pages[1].annotations.append(polygon_annotation)
    document.save(outfile)
```

### Polygon-Annotation abrufen 

Um Polygon-Anmerkungen zu inspizieren, filtern Sie die Anmerkungen der ersten Seite nach dem `POLYGON` Tippen und drucken Sie jedes Annotationsrechteck.

#### Laden Sie das Dokument und sammeln Sie Polygon-Anmerkungen

```python
document = ap.Document(infile)
polygon_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
]
```

#### Drucken Sie die Anmerkungsrechtecke

```python
for annotation in polygon_annotations:
    print(annotation.rect)
```

#### Vollständiges Beispiel

```python
def polygon_annotation_get(infile, outfile):
    document = ap.Document(infile)
    polygon_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
    ]

    for annotation in polygon_annotations:
        print(annotation.rect)
```

### Polygon-Annotation löschen 

Dieser Workflow entfernt alle Polygon-Annotationen von der ersten Seite und speichert das aktualisierte PDF.

#### Polygon-Annotationen finden und löschen

```python
document = ap.Document(infile)
polygon_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
]

for annotation in polygon_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Vollständiges Beispiel

```python
def polygon_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    polygon_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
    ]

    for annotation in polygon_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

### PolyLine-Annotation hinzufügen 

Polyline-Anmerkungen definieren einen offenen Pfad durch mehrere Punkte. Dieses Beispiel erstellt eine Polyline-Annotation mit einer Popup-Notiz.

#### Öffnen Sie das PDF und erstellen Sie die Polylinien-Annotation

```python
document = ap.Document(infile)

polyline_annotation = ap.annotations.PolylineAnnotation(
    document.pages[1],
    ap.Rectangle(270, 193, 571, 383, True),
    [
        ap.Point(545, 150),
        ap.Point(545, 190),
        ap.Point(667, 190),
        ap.Point(667, 110),
        ap.Point(626, 111),
    ],
)
polyline_annotation.title = "John Smith"
polyline_annotation.color = ap.Color.red
```

#### Anhängen Sie das Popup und speichern Sie die PDF

```python
polyline_annotation.popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 196, 1021, 338, True),
)

document.pages[1].annotations.append(polyline_annotation)
document.save(outfile)
```

#### Vollständiges Beispiel

```python
def polyline_annotation_add(infile, outfile):
    document = ap.Document(infile)

    polyline_annotation = ap.annotations.PolylineAnnotation(
        document.pages[1],
        ap.Rectangle(270, 193, 571, 383, True),
        [
            ap.Point(545, 150),
            ap.Point(545, 190),
            ap.Point(667, 190),
            ap.Point(667, 110),
            ap.Point(626, 111),
        ],
    )
    polyline_annotation.title = "John Smith"
    polyline_annotation.color = ap.Color.red
    polyline_annotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 196, 1021, 338, True),
    )

    document.pages[1].annotations.append(polyline_annotation)
    document.save(outfile)
```

### PolyLine-Annotation abrufen 

Um Polyline-Anmerkungen zu inspizieren, filtern Sie die Seitenanmerkungen nach dem `POLY_LINE` Tippen und drucken Sie deren Rechtecke.

#### Laden Sie das Dokument und sammeln Sie Polylinien-Annotationen

```python
document = ap.Document(infile)
polyline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
]
```

#### Drucken Sie die Anmerkungsrechtecke

```python
for annotation in polyline_annotations:
    print(annotation.rect)
```

#### Vollständiges Beispiel

```python
def polyline_annotation_get(infile, outfile):
    document = ap.Document(infile)
    polyline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
    ]

    for annotation in polyline_annotations:
        print(annotation.rect)
```

### PolyLine-Annotation löschen 

Dieser Workflow entfernt alle Polylinien‑Anmerkungen von der ersten Seite und speichert das Ergebnis‑PDF.

#### Polyline-Anmerkungen finden und löschen

```python
document = ap.Document(infile)
polyline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
]

for annotation in polyline_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Vollständiges Beispiel

```python
def polyline_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    polyline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
    ]

    for annotation in polyline_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## Verwandte Themen

- [Import und Export von Anmerkungen](/python-net/import-export-annotations/)
- [Interaktive Anmerkungen](/python-net/interactive-annotations/)
- [Markup-Anmerkungen](/python-net/markup-annotations/)
- [Medien-Anmerkungen](/python-net/media-annotations/)
- [Sicherheitsanmerkungen](/python-net/security-annotations/)
- [Textbasierte Anmerkungen](/python-net/text-based-Annotations/)
- [Wasserzeichen-Annotationen](/python-net/watermark-annotations/)
