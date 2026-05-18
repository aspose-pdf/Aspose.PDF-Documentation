---
title: Markup-Anmerkungen mit Python
linktitle: Markup-Anmerkungen
type: docs
weight: 30
url: /de/python-net/markup-annotations/
description: Erfahren Sie, wie Sie Text-, Caret- und Ersetzungs‑Anmerkungen in PDF‑Dokumenten hinzufügen, lesen und löschen können, indem Sie Aspose.PDF for Python via .NET verwenden.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Arbeiten Sie mit Markup‑Anmerkungen in PDF‑Dateien mit Python.
Abstract: Dieser Artikel erklärt, wie man Markup-Annotationen in PDF-Dokumenten mit Aspose.PDF for Python via .NET erstellt, prüft und entfernt. Er behandelt Textannotationen, Caret-Annotationen und Ersetzungsannotationen, wobei jeder Arbeitsablauf in kleine Schritte und Codebeispiele unterteilt ist.
---

Dieser Artikel zeigt, wie man mit Markup-Annotationen in PDF-Dokumenten mithilfe von Aspose.PDF for Python via .NET arbeitet.

Das Beispielskript demonstriert drei gängige Anmerkungs‑Workflows:

- Textanmerkungen für Notizstil‑Kommentare
- Caret-Anmerkungen für Einfügemarken
- Annotations für Text-Ersetzungs-Markup ersetzen

## Textanmerkungen

### Textanmerkungen hinzufügen

Dieses Beispiel erstellt eine Textannotation auf der ersten Seite und verknüpft sie mit einem Popup-Fenster. Textannotationen sind nützlich für Kommentare im Stil von Haftnotizen in Überprüfungsabläufen.

#### Öffnen Sie das Quell-PDF

```python
document = ap.Document(infile)
```

#### Erstellen und konfigurieren Sie die Textannotation

Definieren Sie das Annotationsrechteck und legen Sie dessen Titel, Betreff, Inhalt, Anzeige‑Flags, Farbe und Symbol fest.

```python
text_annotation = ap.annotations.TextAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 613.664, 428.708, 680.769, True),
)
text_annotation.title = "Aspose User"
text_annotation.subject = "Sticky Note"
text_annotation.contents = (
    "This is a text annotation added by Aspose.PDF for Python via .NET"
)
text_annotation.flags = ap.annotations.AnnotationFlags.PRINT
text_annotation.color = ap.Color.blue
text_annotation.icon = ap.annotations.TextIcon.HELP
```

#### Erstelle die Popup-Annotation

Erstellen Sie ein Popup-Fenster und verbinden Sie es mit der Textanmerkung.

```python
popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(428.708, 613.664, 528.708, 713.664, True),
)
popup.open = True

text_annotation.popup = popup
```

#### Fügen Sie die Annotation hinzu und speichern Sie das PDF

```python
document.pages[1].annotations.add(text_annotation, consider_rotation=False)
document.save(outfile)
```

#### Vollständiges Beispiel

```python
def text_annotation_add(infile, outfile):
    document = ap.Document(infile)

    text_annotation = ap.annotations.TextAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 613.664, 428.708, 680.769, True),
    )
    text_annotation.title = "Aspose User"
    text_annotation.subject = "Sticky Note"
    text_annotation.contents = (
        "This is a text annotation added by Aspose.PDF for Python via .NET"
    )
    text_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    text_annotation.color = ap.Color.blue
    text_annotation.icon = ap.annotations.TextIcon.HELP

    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(428.708, 613.664, 528.708, 713.664, True),
    )
    popup.open = True

    text_annotation.popup = popup

    document.pages[1].annotations.add(text_annotation, consider_rotation=False)
    document.save(outfile)
```

### Textanmerkungen abrufen

Um vorhandene Textannotation zu inspizieren, filtern Sie die Annotationssammlung auf der ersten Seite und behalten nur Elemente, deren Typ ist `TEXT`.

#### Laden Sie das Dokument und sammeln Sie Textanmerkungen

```python
document = ap.Document(infile)
text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
]
```

#### Drucken Sie die Anmerkungsrechtecke

```python
for annotation in text_annotations:
    print(annotation.rect)
```

#### Vollständiges Beispiel

```python
def text_annotation_get(infile, outfile):
    document = ap.Document(infile)
    text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
    ]

    for annotation in text_annotations:
        print(annotation.rect)
```

### Textanmerkungen löschen

Dieser Workflow entfernt alle Textanmerkungen von der ersten Seite und speichert das modifizierte PDF.

#### Textanmerkungen zum Entfernen finden

```python
document = ap.Document(infile)
text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
]
```

#### Löschen Sie die Anmerkungen und speichern Sie die Datei

```python
for annotation in text_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Vollständiges Beispiel

```python
def text_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
    ]

    for annotation in text_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## Caret-Annotationen

### Caret-Anmerkungen hinzufügen

Caret-Annotationen werden verwendet, um Einfügepositionen in Überprüfungsszenarien zu kennzeichnen. Dieses Beispiel fügt eine Caret-Annotation mit einer angehängten Popup-Notiz hinzu.

#### Öffnen Sie das Dokument und rufen Sie die Zielseite ab

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Caret-Annotation erstellen und konfigurieren

```python
caret_annotation = ap.annotations.CaretAnnotation(
    page, ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
)
caret_annotation.title = "Aspose User"
caret_annotation.subject = "Inserted text 1"
caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
caret_annotation.color = ap.Color.blue
```

#### Fügen Sie das Popup hinzu und speichern Sie das Dokument

```python
caret_annotation.popup = ap.annotations.PopupAnnotation(
    page, ap.Rectangle(310, 713, 410, 730, True)
)
page.annotations.append(caret_annotation)

document.save(outfile)
```

#### Vollständiges Beispiel

```python
def caret_annotations_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotation = ap.annotations.CaretAnnotation(
        page, ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    caret_annotation.title = "Aspose User"
    caret_annotation.subject = "Inserted text 1"
    caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation.color = ap.Color.blue
    caret_annotation.popup = ap.annotations.PopupAnnotation(
        page, ap.Rectangle(310, 713, 410, 730, True)
    )
    page.annotations.append(caret_annotation)

    document.save(outfile)
```

### Caret-Anmerkungen abrufen

Um Caret-Anmerkungen zu prüfen, iterieren Sie durch die Seitenanmerkungen und filtern Sie nach dem `CARET` Annotationstyp.

#### Laden Sie das Dokument und die Seite

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Drucke Caret-Anmerkungsrechtecke

```python
for annot in page.annotations:
    if annot.annotation_type == ap.annotations.AnnotationType.CARET:
        print(annot.rect)
```

#### Vollständiges Beispiel

```python
def caret_annotations_get(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.CARET:
            print(annot.rect)
```

### Caret-Anmerkungen löschen

Dieser Workflow sammelt zunächst Caret-Annotationen, löscht sie einzeln und speichert anschließend die aktualisierte Datei.

#### Laden Sie das Dokument und sammeln Sie Caret-Annotationen

```python
document = ap.Document(infile)
page = document.pages[1]

caret_annotations = [
    annot
    for annot in page.annotations
    if annot.annotation_type == ap.annotations.AnnotationType.CARET
]
```

#### Löschen Sie die Anmerkungen und speichern Sie das Dokument

```python
for annot in caret_annotations:
    page.annotations.delete(annot)

document.save(outfile)
```

#### Vollständiges Beispiel

```python
def caret_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotations = [
        annot
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.CARET
    ]

    for annot in caret_annotations:
        page.annotations.delete(annot)

    document.save(outfile)
```

## Annotationen ersetzen

### Anmerkungen hinzufügen / ersetzen

Ersetzen-Anmerkungen kombinieren eine Caret-Anmerkung und eine gruppierte Durchstreichungs-Anmerkung. Dieses Muster kennzeichnet Text, der ersetzt werden soll, und verknüpft die Ersetzungsnotiz mit dem durchgestrichenen Inhalt.

#### Öffnen Sie das Dokument und holen Sie die Seite

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Erstellen Sie die Caret-Annotation für Ersetzungstext

```python
caret_annotation = ap.annotations.CaretAnnotation(
    page, ap.Rectangle(361.246, 727.908, 370.081, 735.107, True)
)
caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
caret_annotation.subject = "Inserted text 2"
caret_annotation.title = "Aspose User"
caret_annotation.color = ap.Color.blue
caret_annotation.popup = ap.annotations.PopupAnnotation(
    page, ap.Rectangle(310, 713, 410, 730, True)
)
```

#### Erstellen Sie die gruppierte Durchstreichungsannotation

Definieren Sie den Durchstreichbereich, weisen Sie Quad-Punkte zu und verknüpfen Sie ihn mit der Caret-Annotation durch `in_reply_to` und `reply_type`.

```python
strikeout_annotation = ap.annotations.StrikeOutAnnotation(
    page, ap.Rectangle(318.407, 727.826, 368.916, 740.098, True)
)
strikeout_annotation.color = ap.Color.blue
strikeout_annotation.quad_points = [
    ap.Point(321.66, 739.416),
    ap.Point(365.664, 739.416),
    ap.Point(321.66, 728.508),
    ap.Point(365.664, 728.508),
]
strikeout_annotation.subject = "Cross-out"
strikeout_annotation.in_reply_to = caret_annotation
strikeout_annotation.reply_type = ap.annotations.ReplyType.GROUP
``` 

#### Fügen Sie beide Anmerkungen hinzu und speichern Sie das PDF

```python
page.annotations.append(caret_annotation)
page.annotations.append(strikeout_annotation)

document.save(outfile)
```

#### Vollständiges Beispiel

```python
def replace_annotations_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotation = ap.annotations.CaretAnnotation(
        page, ap.Rectangle(361.246, 727.908, 370.081, 735.107, True)
    )
    caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation.subject = "Inserted text 2"
    caret_annotation.title = "Aspose User"
    caret_annotation.color = ap.Color.blue
    caret_annotation.popup = ap.annotations.PopupAnnotation(
        page, ap.Rectangle(310, 713, 410, 730, True)
    )

    strikeout_annotation = ap.annotations.StrikeOutAnnotation(
        page, ap.Rectangle(318.407, 727.826, 368.916, 740.098, True)
    )
    strikeout_annotation.color = ap.Color.blue
    strikeout_annotation.quad_points = [
        ap.Point(321.66, 739.416),
        ap.Point(365.664, 739.416),
        ap.Point(321.66, 728.508),
        ap.Point(365.664, 728.508),
    ]
    strikeout_annotation.subject = "Cross-out"
    strikeout_annotation.in_reply_to = caret_annotation
    strikeout_annotation.reply_type = ap.annotations.ReplyType.GROUP

    page.annotations.append(caret_annotation)
    page.annotations.append(strikeout_annotation)

    document.save(outfile)
```

### Ersetzen‑Anmerkungen abrufen

Um Ersetzungsanmerkungen zu identifizieren, finden Sie Durchstreichungsanmerkungen, die als Antworten auf eine andere Anmerkung gruppiert sind. Das Beispiel wandelt jede Durchstreichungsanmerkung, bevor es die Beziehungsfelder prüft, um.

#### Laden Sie das Dokument und iterieren Sie durch die Anmerkungen

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Gruppierte Durchstreichungs-Anmerkungen filtern

```python
for annot in page.annotations:
    if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT:
        sa = cast(ap.annotations.StrikeOutAnnotation, annot)
        if (
            sa.in_reply_to is not None
            and sa.reply_type == ap.annotations.ReplyType.GROUP
        ):
            print(f"Replace annotation rect: {sa.rect}")
```

#### Vollständiges Beispiel

```python
def replace_annotations_get(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT:
            sa = cast(ap.annotations.StrikeOutAnnotation, annot)
            if (
                sa.in_reply_to is not None
                and sa.reply_type == ap.annotations.ReplyType.GROUP
            ):
                print(f"Replace annotation rect: {sa.rect}")
```

### Löschen Ersetzen Annotationen

Dieser Arbeitsablauf sammelt Durchstreichungs‑Anmerkungen, die für Ersetzungs‑Markup verwendet werden, entfernt sie von der Seite und speichert das ausgegebene PDF.

#### Laden Sie das Dokument und sammeln Sie Ersetzungsanmerkungen

```python
document = ap.Document(infile)
page = document.pages[1]

replace_annotations = [
    cast(ap.annotations.StrikeOutAnnotation, annot)
    for annot in page.annotations
    if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
]
```

#### Löschen Sie die Anmerkungen und speichern Sie das Dokument

```python
for annot in replace_annotations:
    page.annotations.delete(annot)

document.save(outfile)
```

#### Vollständiges Beispiel

```python
def replace_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    replace_annotations = [
        cast(ap.annotations.StrikeOutAnnotation, annot)
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annot in replace_annotations:
        page.annotations.delete(annot)

    document.save(outfile)
```
