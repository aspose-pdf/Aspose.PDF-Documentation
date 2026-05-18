---
title: Textbasierte Anmerkungen mit Python
linktitle: Textanmerkungen
type: docs
weight: 10
url: /de/python-net/text-based-Annotations/
description: Erfahren Sie, wie Sie Freitext‑, Hervorhebungs‑, Unterstreichungs‑, Wellenlinien‑ und Durchstreichungs‑Anmerkungen in PDF‑Dokumenten hinzufügen, prüfen und löschen können, indem Sie Aspose.PDF for Python via .NET verwenden.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Arbeiten Sie mit Text‑ und Textauszeichnungs‑PDF‑Anmerkungen in Python.
Abstract: Dieser Artikel erklärt, wie man textbasierte Anmerkungen in PDF‑Dokumenten mit Aspose.PDF for Python via .NET erstellt, liest und entfernt. Er behandelt Freitext‑Anmerkungen und Textauszeichnungs‑Anmerkungen wie Hervorhebung, Unterstreichung, wellige Unterstreichung und Durchstreichung, einschließlich fortgeschrittener Unterstreichungs‑Workflows wie Flattening, Quad‑Points und das Extrahieren markierten Textes.
---

Dieser Artikel zeigt, wie man mit textbasierten Anmerkungen in PDF-Dokumenten mithilfe von Aspose.PDF for Python via .NET arbeitet.

Das Beispielskript demonstriert mehrere Textanmerkungs‑Workflows:

- Freitext-Anmerkungen
- Markierungsanmerkungen
- Unterstreichungsannotationen
- wellige Anmerkungen
- Durchgestrichene Anmerkungen

## Freitext-Anmerkungen

### Freitext-Anmerkungen hinzufügen 

Freitext-Annotationen ermöglichen es Ihnen, sichtbare Textkommentare direkt auf einer PDF-Seite zu platzieren. Dieses Beispiel fügt der ersten Seite eine einfache Freitext-Annotation hinzu.

#### Öffnen Sie das Quell-PDF

```python
document = ap.Document(infile)
```

#### Erstelle und konfiguriere die Freitextannotation

```python
free_text_annotation = ap.annotations.FreeTextAnnotation(
    document.pages[1],
    ap.Rectangle(299, 713, 308, 720, True),
    ap.annotations.DefaultAppearance(),
)
free_text_annotation.title = "Aspose User"
free_text_annotation.color = ap.Color.light_green
```

#### Fügen Sie die Anmerkung hinzu und speichern Sie das PDF

```python
document.pages[1].annotations.append(free_text_annotation)
document.save(outfile)
```

#### Vollständiges Beispiel

```python
def free_text_annotation_add(infile, outfile):
    document = ap.Document(infile)

    free_text_annotation = ap.annotations.FreeTextAnnotation(
        document.pages[1],
        ap.Rectangle(299, 713, 308, 720, True),
        ap.annotations.DefaultAppearance(),
    )
    free_text_annotation.title = "Aspose User"
    free_text_annotation.color = ap.Color.light_green

    document.pages[1].annotations.append(free_text_annotation)
    document.save(outfile)
```

### Freitext‑Anmerkungen abrufen 

Um Freitext-Annotationen zu prüfen, filtern Sie die Annotationen der ersten Seite nach dem `FREE_TEXT` Tippen und drucken Sie jedes Annotationsrechteck.

#### Laden Sie das Dokument und sammeln Sie Freitext-Annotationen

```python
document = ap.Document(infile)
free_text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
]
```

#### Drucken Sie die Anmerkungsrechtecke

```python
for annotation in free_text_annotations:
    print(annotation.rect)
```

#### Vollständiges Beispiel

```python
def free_text_annotation_get(infile, outfile):
    document = ap.Document(infile)
    free_text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
    ]

    for annotation in free_text_annotations:
        print(annotation.rect)
```

### Freitext-Anmerkungen löschen 

Dieser Workflow entfernt alle Freitext-Anmerkungen von der ersten Seite und speichert das aktualisierte PDF.

#### Freitext-Anmerkungen finden und löschen

```python
document = ap.Document(infile)
free_text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
]

for annotation in free_text_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Vollständiges Beispiel

```python
def free_text_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    free_text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
    ]

    for annotation in free_text_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


## Text-Markup-Annotationen

### Hervorhebungsannotationen

#### Textmarkierung hinzufügen

Highlight-Anmerkungen betonen Teile des Dokuments, ohne den zugrunde liegenden Inhalt zu ändern. Dieses Beispiel fügt eine Highlight-Anmerkung zur ersten Seite hinzu.

```python
document = ap.Document(infile)

highlight_annotation = ap.annotations.HighlightAnnotation(
    document.pages[1],
    ap.Rectangle(300, 750, 320, 770, True),
)

document.pages[1].annotations.append(highlight_annotation)
document.save(outfile)
```

```python
def text_highlight_annotation_add(infile, outfile):
    document = ap.Document(infile)

    highlight_annotation = ap.annotations.HighlightAnnotation(
        document.pages[1],
        ap.Rectangle(300, 750, 320, 770, True),
    )

    document.pages[1].annotations.append(highlight_annotation)
    document.save(outfile)
```

#### Text-Highlight erhalten

Um Hervorhebungsannotationen zu untersuchen, filtern Sie die Seitenannotationen nach dem `HIGHLIGHT` Tippen und drucken Sie deren Rechtecke.

```python
document = ap.Document(infile)
highlight_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
]

for annotation in highlight_annotations:
    print(annotation.rect)
```

```python
def text_highlight_annotation_get(infile, outfile):
    document = ap.Document(infile)
    highlight_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
    ]

    for annotation in highlight_annotations:
        print(annotation.rect)
```

#### Textmarkierung löschen

Dieser Workflow entfernt alle Highlight-Annotationen von der ersten Seite und speichert das Ausgabe-PDF.

```python
document = ap.Document(infile)
highlight_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
]

for annotation in highlight_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_highlight_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    highlight_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
    ]

    for annotation in highlight_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


### Unterstreichungs-Anmerkungen

#### Textunterstreichungs‑Anmerkungen hinzufügen

Unterstreichungs-Annotationen markieren Text mit einer sichtbaren Unterstreichung. Dieses Beispiel fügt eine grundlegende Unterstreichungs-Annotation hinzu und legt deren Metadaten und Farbe fest.

```python
document = ap.Document(infile)

underline_annotation = ap.annotations.UnderlineAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
)
underline_annotation.title = "Aspose User"
underline_annotation.subject = "Inserted Underline 1"
underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
underline_annotation.color = ap.Color.blue

document.pages[1].annotations.append(underline_annotation)
document.save(outfile)
```

```python
def text_underline_annotation_add(infile, outfile):
    document = ap.Document(infile)

    underline_annotation = ap.annotations.UnderlineAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline 1"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(underline_annotation)
    document.save(outfile)
```

#### Textunterstreichungs-Anmerkungen hinzufügen und flachlegen 

Wenn Sie möchten, dass die Unterstreichung Teil des Seiteninhalts wird, anstatt eine interaktive Anmerkung zu bleiben, können Sie sie nach dem Hinzufügen flachlegen.

```python
document = ap.Document(infile)

underline_annotation = ap.annotations.UnderlineAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
)
underline_annotation.title = "Aspose User"
underline_annotation.subject = "Inserted Underline to Flatten"
underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
underline_annotation.color = ap.Color.blue

document.pages[1].annotations.append(underline_annotation)
underline_annotation.flatten()

document.save(outfile)
```

```python
def text_underline_flatten_add(infile, outfile):
    document = ap.Document(infile)

    underline_annotation = ap.annotations.UnderlineAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline to Flatten"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(underline_annotation)
    underline_annotation.flatten()

    document.save(outfile)
```

#### Textunterstreichungs‑Anmerkungen mit Quad‑Punkten hinzufügen

Quad-Punkte ermöglichen es Ihnen, den exakt markierten Bereich für die Unterstreichungsannotation zu definieren. Dies ist nützlich, wenn Sie mehr Kontrolle benötigen als ein einfaches Rechteck.

```python
document = ap.Document(infile)
rect = ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)

underline_annotation = ap.annotations.UnderlineAnnotation(document.pages[1], rect)
underline_annotation.title = "Aspose User"
underline_annotation.subject = "Inserted Underline with Quad Points"
underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
underline_annotation.color = ap.Color.blue
underline_annotation.quad_points = [
    ap.Point(rect.llx, rect.lly),
    ap.Point(rect.urx, rect.lly),
    ap.Point(rect.urx, rect.ury),
    ap.Point(rect.llx, rect.ury),
]

document.pages[1].annotations.append(underline_annotation)
document.save(outfile)
```

```python
def text_underline_with_quad_points_add(infile, outfile):
    document = ap.Document(infile)
    rect = ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)

    underline_annotation = ap.annotations.UnderlineAnnotation(document.pages[1], rect)
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline with Quad Points"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue
    underline_annotation.quad_points = [
        ap.Point(rect.llx, rect.lly),
        ap.Point(rect.urx, rect.lly),
        ap.Point(rect.urx, rect.ury),
        ap.Point(rect.llx, rect.ury),
    ]

    document.pages[1].annotations.append(underline_annotation)
    document.save(outfile)
```

#### Textunterstreichungs-Annotationen löschen

Dieser Workflow entfernt alle Unterstreichungsanmerkungen von der ersten Seite und speichert das aktualisierte Dokument.

```python
document = ap.Document(infile)
underline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_underline_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

#### Textunterstreichungs-Annotationen nach Titel löschen

Dieser Workflow zeigt, wie man Unterstreichungs‑Annotationen selektiv löscht, nachdem man ihren Titel überprüft hat.

```python
document = ap.Document(infile)

underline_annotations = [
    cast(ap.annotations.UnderlineAnnotation, annotation)
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    if annotation.title.startswith("a"):
        document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_underline_by_title_delete(infile, outfile):
    document = ap.Document(infile)

    underline_annotations = [
        cast(ap.annotations.UnderlineAnnotation, annotation)
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        if annotation.title.startswith("a"):
            document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

#### Textunterstreichungsannotationen abrufen

Um Unterstreichungs-Anmerkungen zu untersuchen, filtern Sie die Anmerkungen der ersten Seite nach dem `UNDERLINE` Tippen und drucken Sie jedes Rechteck.

```python
document = ap.Document(infile)
underline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    print(annotation.rect)
```

```python
def text_underline_annotation_get(infile, outfile):
    document = ap.Document(infile)
    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        print(annotation.rect)
```

#### Text Unterstreichungsannotation markierten Text abrufen

Dieser Workflow konvertiert jede Unterstreichungsannotation in ein `UnderlineAnnotation` Objekt und extrahiert den markierten Text.

```python
document = ap.Document(infile)

underline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    ua = cast(ap.annotations.UnderlineAnnotation, annotation)
    print(f"Marked text: {ua.get_marked_text()}")
```

```python
def text_underline_marked_text_get(infile, outfile):
    document = ap.Document(infile)

    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        ua = cast(ap.annotations.UnderlineAnnotation, annotation)
        print(f"Marked text: {ua.get_marked_text()}")
```

#### Textunterstreichungs‑Anmerkungen markierte Fragmente abrufen

Wenn Sie jedes markierte Fragment einzeln benötigen, können Sie durch die zurückgegebene Sammlung iterieren. `get_marked_text_fragments()`.

```python
document = ap.Document(infile)

underline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    ua = cast(ap.annotations.UnderlineAnnotation, annotation)
    for fragment in ua.get_marked_text_fragments():
        print(f"Fragment text: {fragment.text}")
```

```python
def text_underline_marked_fragments_get(infile, outfile):
    document = ap.Document(infile)

    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        ua = cast(ap.annotations.UnderlineAnnotation, annotation)
        for fragment in ua.get_marked_text_fragments():
            print(f"Fragment text: {fragment.text}")
```


### Wellenlinien-Anmerkungen

#### Squiggly-Anmerkungen hinzufügen

Wellenlinien-Anmerkungen werden häufig verwendet, um Rechtschreib-, Grammatik- oder Aufmerksamkeitsbereiche im Text zu kennzeichnen. Dieses Beispiel fügt der ersten Seite eine Wellenlinien-Anmerkung hinzu.

```python
document = ap.Document(infile)
page = document.pages[1]

squiggly_annotation = ap.annotations.SquigglyAnnotation(
    page,
    ap.Rectangle(67, 317, 261, 459, True),
)
squiggly_annotation.title = "John Smith"
squiggly_annotation.color = ap.Color.blue

page.annotations.append(squiggly_annotation)
document.save(outfile)
```

```python
def text_squiggly_annotation_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    squiggly_annotation = ap.annotations.SquigglyAnnotation(
        page,
        ap.Rectangle(67, 317, 261, 459, True),
    )
    squiggly_annotation.title = "John Smith"
    squiggly_annotation.color = ap.Color.blue

    page.annotations.append(squiggly_annotation)
    document.save(outfile)
```

#### Squiggly-Annotationen abrufen

Um Squiggly-Anmerkungen zu prüfen, filtern Sie die Seitenanmerkungen nach dem `SQUIGGLY` Tippen und drucken Sie deren Rechtecke.

```python
document = ap.Document(infile)
squiggly_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
]

for annotation in squiggly_annotations:
    print(annotation.rect)
```

```python
def text_squiggly_annotation_get(infile, outfile):
    document = ap.Document(infile)
    squiggly_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
    ]

    for annotation in squiggly_annotations:
        print(annotation.rect)
```

#### Zickzack-Anmerkungen löschen

Dieser Workflow entfernt alle welligen Anmerkungen von der ersten Seite und speichert das Ergebnis.

```python
document = ap.Document(infile)
squiggly_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
]

for annotation in squiggly_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_squiggly_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    squiggly_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
    ]

    for annotation in squiggly_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


### Durchgestrichene Anmerkungen

#### Textdurchstreichungs-Annotationen hinzufügen

Durchstreichungs-Anmerkungen markieren Text, der als entfernt oder durchgestrichen behandelt werden soll. Dieses Beispiel fügt eine Durchstreichungs-Anmerkung hinzu und legt deren Metadaten und Farbe fest.

```python
document = ap.Document(infile)

strikeout_annotation = ap.annotations.StrikeOutAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
)
strikeout_annotation.title = "Aspose User"
strikeout_annotation.subject = "Inserted text 1"
strikeout_annotation.flags = ap.annotations.AnnotationFlags.PRINT
strikeout_annotation.color = ap.Color.blue

document.pages[1].annotations.append(strikeout_annotation)
document.save(outfile)
```

```python
def text_strikeout_annotation_add(infile, outfile):
    document = ap.Document(infile)

    strikeout_annotation = ap.annotations.StrikeOutAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    strikeout_annotation.title = "Aspose User"
    strikeout_annotation.subject = "Inserted text 1"
    strikeout_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    strikeout_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(strikeout_annotation)
    document.save(outfile)
```

#### Textdurchstreichungs‑Anmerkungen abrufen

Um Durchstreichungs‑Annotationen zu untersuchen, filtern Sie die Seiten‑Annotationen nach dem `STRIKE_OUT` Tippen und drucken Sie deren Rechtecke.

```python
document = ap.Document(infile)
strikeout_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
]

for annotation in strikeout_annotations:
    print(annotation.rect)
```

```python
def text_strikeout_annotation_get(infile, outfile):
    document = ap.Document(infile)
    strikeout_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annotation in strikeout_annotations:
        print(annotation.rect)
```

#### Textdurchstreichungs-Anmerkungen löschen

Dieser Workflow entfernt alle Durchstreichungs‑Anmerkungen von der ersten Seite und speichert das aktualisierte Document.

```python
document = ap.Document(infile)
strikeout_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
]

for annotation in strikeout_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_strikeout_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    strikeout_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annotation in strikeout_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## Verwandte Themen

- [Import und Export von Anmerkungen](/python-net/import-export-annotations/)
- [Interaktive Anmerkungen](/python-net/interactive-annotations/)
- [Markup-Anmerkungen](/python-net/markup-annotations/)
- [Medien-Anmerkungen](/python-net/media-annotations/)
- [Sicherheitsanmerkungen](/python-net/security-annotations/)
- [Form‑Annotationen](/python-net/shape-annotations/)
- [Wasserzeichen-Annotationen](/python-net/watermark-annotations/)
