---
title: Sicherheitsanmerkungen mit Python
linktitle: Sicherheitsanmerkungen
type: docs
weight: 75
url: /de/python-net/security-annotations/
description: Erfahren Sie, wie Sie Text für die Schwärzung markieren, Schwärzungsanmerkungen anwenden und Bildbereiche in PDF-Dateien mit Aspose.PDF for Python via .NET schwärzen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Vertrauliche PDF-Inhalte in Python mit Sicherheitsanmerkungen schwärzen.
Abstract: Dieses Dokument erklärt, wie man mit Sicherheitsanmerkungen in PDF-Dokumenten unter Verwendung von Aspose.PDF for Python via .NET arbeitet. Es behandelt das Markieren von übereinstimmendem Text mit Schwärzungsanmerkungen, das dauerhafte Anwenden von Schwärzungen und das Schwärzen ausgewählter Bildbereiche basierend auf erkannten Bildplatzierungsrechtecken.
---

Dieser Artikel zeigt, wie man Sicherheitsanmerkungen in PDF-Dokumenten mit Aspose.PDF for Python via .NET verwendet.

Das Beispielskript demonstriert drei gängige Redaktions‑Workflows:

- Markieren Sie Textfragmente mit Redaktionsanmerkungen
- bestehende Redaktionsanmerkungen dauerhaft anwenden
- einen erkannten Bildbereich auf einer Seite zensieren

## Textredaktion markieren

Dieser Workflow sucht im Dokument nach passendem Text und setzt Redaktionsanmerkungen über jede Übereinstimmung. Er entfernt den Inhalt noch nicht; er markiert den Text lediglich für eine spätere Redaktion.

### Öffnen Sie das PDF und suchen Sie nach dem Zieltext

Erstelle ein `TextFragmentAbsorber` für den Suchbegriff und aktivieren Sie die regulären Textsuchoptionen, bevor Sie alle Seiten durchsuchen.

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

text_search_options = ap.text.TextSearchOptions(True)
text_fragment_absorber.text_search_options = text_search_options
document.pages.accept(text_fragment_absorber)
```

### Erstellen Sie Redaktionsanmerkungen für jede Übereinstimmung

Für jedes gefundene Textfragment erstelle ein `RedactionAnnotation` Verwenden Sie das Fragmentrechteck und konfigurieren Sie dessen visuelle Darstellung.

```python
for text_fragment in text_fragment_absorber.text_fragments:
    page = text_fragment.page
    annotation_rectangle = text_fragment.rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(
        page, annotation_rectangle
    )
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True
    page.annotations.add(redaction_annotation, True)
```

### Speichern Sie das markierte PDF

```python
document.save(outfile)
```

### Vollständiges Beispiel

```python
def mark_text_redaction(infile, outfile, search_term):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

    text_search_options = ap.text.TextSearchOptions(True)
    text_fragment_absorber.text_search_options = text_search_options
    document.pages.accept(text_fragment_absorber)

    for text_fragment in text_fragment_absorber.text_fragments:
        page = text_fragment.page
        annotation_rectangle = text_fragment.rectangle
        redaction_annotation = ap.annotations.RedactionAnnotation(
            page, annotation_rectangle
        )
        redaction_annotation.fill_color = ap.Color.gray
        redaction_annotation.border_color = ap.Color.red
        redaction_annotation.color = ap.Color.white
        redaction_annotation.overlay_text = "REDACTED"
        redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
        redaction_annotation.repeat = True
        page.annotations.add(redaction_annotation, True)

    document.save(outfile)
```



## Redaktion anwenden

Nachdem Redaktionsanmerkungen hinzugefügt wurden, wendet dieser Workflow sie dauerhaft auf der ersten Seite an. Sobald sie angewendet wurden, wird der Originalinhalt aus der Dokumentausgabe entfernt.

### Laden Sie das PDF und sammeln Sie Redaktionsanmerkungen

```python
document = ap.Document(infile)
redaction_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
]
```

### Wenden Sie jede Redaktionsanmerkung an

Das Beispiel prüft, dass jede Anmerkung als ein `RedactionAnnotation` vor dem Aufruf `redact()`.

```python
for redaction_annotation in redaction_annotations:
    if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
        cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()
```

### Speichern Sie das geschwärzte PDF

```python
document.save(outfile)
```

### Vollständiges Beispiel

```python
def apply_redaction(infile, outfile):
    document = ap.Document(infile)
    redaction_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
    ]

    for redaction_annotation in redaction_annotations:
        if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
            cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()

    document.save(outfile)
```



## Redaktionsbereich

Dieses Beispiel redigiert einen erkannten Bildbereich anstelle von Text. Es scannt die Seite nach Bildplatzierungen, wählt ein Platzierungsrechteck aus und fügt über diesem Bereich eine Redaktionsanmerkung hinzu.

### Öffnen Sie das PDF und erkennen Sie Bildplatzierungen

Verwenden `ImagePlacementAbsorber` um Bildpositionen auf der ersten Seite zu finden.

```python
document = ap.Document(infile)

image_placement_absorber = ap.ImagePlacementAbsorber()
page = document.pages[1]
page.accept(image_placement_absorber)
```

### Erstellen Sie eine Redaktionsanmerkung für den ausgewählten Bildbereich

Das Beispiel verwendet die drittentdeckte Bildplatzierung und wendet dieselbe Redaktionsformatierung an, die im Text-Markierungsbeispiel verwendet wurde.

```python
target_rect = image_placement_absorber.image_placements[2].rectangle
redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
redaction_annotation.fill_color = ap.Color.gray
redaction_annotation.border_color = ap.Color.red
redaction_annotation.color = ap.Color.white
redaction_annotation.overlay_text = "REDACTED"
redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
redaction_annotation.repeat = True
```

### Fügen Sie die Anmerkung hinzu und speichern Sie das PDF

```python
page.annotations.add(redaction_annotation, True)
document.save(outfile)
```

### Vollständiges Beispiel

```python
def redact_area(infile, outfile):
    document = ap.Document(infile)

    image_placement_absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(image_placement_absorber)

    target_rect = image_placement_absorber.image_placements[2].rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True

    page.annotations.add(redaction_annotation, True)
    document.save(outfile)
```

## Verwandte Themen

- [Import und Export von Anmerkungen](/python-net/import-export-annotations/)
- [Interaktive Anmerkungen](/python-net/interactive-annotations/)
- [Markup-Anmerkungen](/python-net/markup-annotations/)
- [Medien-Anmerkungen](/python-net/media-annotations/)
- [Form‑Annotationen](/python-net/shape-annotations/)
- [Textbasierte Anmerkungen](/python-net/text-based-Annotations/)
- [Wasserzeichen-Annotationen](/python-net/watermark-annotations/)
