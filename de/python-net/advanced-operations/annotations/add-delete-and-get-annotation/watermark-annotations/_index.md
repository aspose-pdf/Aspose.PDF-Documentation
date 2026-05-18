---
title: Wasserzeichen-Annotationen mit Python
linktitle: Wasserzeichen-Annotationen
type: docs
weight: 70
url: /de/python-net/watermark-annotations/
description: Erfahren Sie, wie Sie Wasserzeichen-Annotationen in PDF-Dokumenten hinzufügen, prüfen und löschen können, indem Sie Aspose.PDF for Python via .NET verwenden.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Arbeiten Sie mit Wasserzeichen-Anmerkungen in PDF-Dateien mithilfe von Python.
Abstract: Dieser Artikel erklärt, wie man Wasserzeichen-Anmerkungen in PDF-Dokumenten mithilfe von Aspose.PDF for Python via .NET erstellt, liest und entfernt. Er behandelt das Hinzufügen einer Text-Wasserzeichen-Anmerkung mit benutzerdefiniertem Textzustand und Opazität, das Überprüfen vorhandener Wasserzeichen-Anmerkungen und das Löschen von Wasserzeichen-Anmerkungen von einer PDF-Seite.
---

Dieser Artikel zeigt, wie man mit Wasserzeichen-Anmerkungen in PDF-Dokumenten mithilfe von Aspose.PDF for Python via .NET arbeitet.

Das Beispielskript demonstriert drei gängige Arbeitsabläufe:

- eine Wasserzeichen-Annotation hinzufügen
- Wasserzeichen-Anmerkungsrechtecke abrufen
- Wasserzeichen-Annotationen löschen

## Wasserzeichen-Anmerkung hinzufügen

Dieses Beispiel fügt eine Wasserzeichen-Annotation zur ersten Seite eines PDF-Dokuments hinzu. Das Wasserzeichen verwendet einen Textzustand, um die Schriftarteinstellungen zu steuern, und wendet eine benutzerdefinierte Deckkraft für ein halbtransparentes Erscheinungsbild an.

### Öffnen Sie das PDF und holen Sie die Zielseite

```python
document = ap.Document(infile)
page = document.pages[1]
```

### Erstelle die Wasserzeichen-Annotation

Definieren Sie das Annotationsrechteck und fügen Sie es der Annotationssammlung der Seite hinzu.

```python
watermark_annotation = ap.annotations.WatermarkAnnotation(
    page,
    ap.Rectangle(100, 100, 400, 200, True),
)

page.annotations.append(watermark_annotation)
```

### Textaussehen konfigurieren

Erstelle ein `TextState` Objekt zur Steuerung von Textfarbe, Schriftgröße und Schriftfamilie.

```python
text_state = ap.text.TextState()
text_state.foreground_color = ap.Color.blue
text_state.font_size = 25
text_state.font = ap.text.FontRepository.find_font("Arial")
```

### Deckkraft und Wasserzeichentext festlegen

Das Beispiel verwendet 50% Deckkraft und schreibt drei Textzeilen in die Wasserzeichenannotation.

```python
watermark_annotation.opacity = 0.5
watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)
```

### PDF speichern

```python
document.save(outfile)
```

### Vollständiges Beispiel

```python
def watermark_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    watermark_annotation = ap.annotations.WatermarkAnnotation(
        page,
        ap.Rectangle(100, 100, 400, 200, True),
    )

    page.annotations.append(watermark_annotation)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 25
    text_state.font = ap.text.FontRepository.find_font("Arial")

    watermark_annotation.opacity = 0.5
    watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)

    document.save(outfile)
```

## Wasserzeichen-Anmerkung abrufen

Um vorhandene Wasserzeichen-Anmerkungen zu inspizieren, filtern Sie die Anmerkungen der ersten Seite nach dem `WATERMARK` Tippen und drucken Sie deren Rechtecke.

### Laden Sie das Dokument und sammeln Sie Wasserzeichen-Annotationen

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### Drucken Sie die Anmerkungsrechtecke

```python
for watermark_annotation in watermark_annotations:
    print(watermark_annotation.rect)
```

### Vollständiges Beispiel

```python
def watermark_get(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        print(watermark_annotation.rect)
```

## Wasserzeichen-Anmerkung löschen

Dieser Workflow entfernt alle Wasserzeichen-Anmerkungen von der ersten Seite und speichert das aktualisierte PDF.

### Wasserzeichen-Annotationen zum Entfernen finden

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### Löschen Sie die Anmerkungen und speichern Sie das PDF

```python
for watermark_annotation in watermark_annotations:
    document.pages[1].annotations.delete(watermark_annotation)

document.save(outfile)
```

### Vollständiges Beispiel

```python
def watermark_delete(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        document.pages[1].annotations.delete(watermark_annotation)

    document.save(outfile)
```

## Verwandte Themen

- [Import und Export von Anmerkungen](/python-net/import-export-annotations/)
- [Interaktive Anmerkungen](/python-net/interactive-annotations/)
- [Markup-Anmerkungen](/python-net/markup-annotations/)
- [Medien-Anmerkungen](/python-net/media-annotations/)
- [Sicherheitsanmerkungen](/python-net/security-annotations/)
- [Form‑Annotationen](/python-net/shape-annotations/)
- [Textbasierte Anmerkungen](/python-net/text-based-Annotations/)
