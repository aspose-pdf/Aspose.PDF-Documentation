---
title: Interaktive Anmerkungen mit Python
linktitle: Interaktive Anmerkungen
type: docs
weight: 60
url: /de/python-net/interactive-annotations/
description: Erfahren Sie, wie Sie Link‑Annotationen hinzufügen, lesen und löschen und wie Sie Navigations‑ und Druckschaltflächen in PDF‑Dokumenten mithilfe von Aspose.PDF for Python via .NET erstellen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Arbeiten Sie mit interaktiven PDF‑Annotationen und Schaltflächen in Python.
Abstract: Dieser Artikel erklärt, wie man mit interaktiven Anmerkungen in PDF-Dateien unter Verwendung von Aspose.PDF for Python via .NET arbeitet. Er behandelt das Hinzufügen von Link-Anmerkungen, das Auslesen vorhandener Link‑Bereiche, das Löschen von Link-Anmerkungen, das Erstellen von Seiten‑Navigationsschaltflächen und das Hinzufügen einer Druckschaltfläche zu einem PDF-Dokument.
---

Dieser Artikel zeigt, wie man mit interaktiven Anmerkungen in PDF-Dokumenten unter Verwendung von Aspose.PDF für Python via .NET arbeitet.

Das Beispielskript demonstriert mehrere gängige Workflows:

- Fügen Sie eine Linkannotation zu bestehendem Text hinzu
- Link-Anmerkungsrechtecke von einer Seite abrufen
- Link-Annotationen löschen
- Navigationsschaltflächen erstellen
- Erstelle einen Druck-Button

## Link-Annotation

### Link-Annotation hinzufügen

Dieses Beispiel durchsucht die erste Seite nach dem Textfragment `"file"` und platziert eine anklickbare Link-Annotation über dem entsprechenden Textbereich. Wenn der Benutzer die Annotation anklickt, öffnet das PDF die angegebene Webadresse.

#### Laden Sie das Dokument und finden Sie den Zieltext

Erstelle ein `Document` Objekt und verwenden `TextFragmentAbsorber` nach dem Text suchen, der interaktiv wird.

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

document.pages[1].accept(text_fragment_absorber)
phone_number_fragment = text_fragment_absorber.text_fragments[1]
```

#### Erstelle die Link-Annotation

Erstelle ein `LinkAnnotation` Verwenden Sie das Rechteck des übereinstimmenden Textfragmentes und weisen Sie ihm eine URI‑Aktion zu.

```python
link_annotation = ap.annotations.LinkAnnotation(
    document.pages[1], phone_number_fragment.rectangle
)
link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")
```

#### Fügen Sie die Anmerkung hinzu und speichern Sie das PDF

Fügen Sie die Anmerkung zur Seite hinzu und speichern Sie die aktualisierte Datei.

```python
document.pages[1].annotations.append(link_annotation)
document.save(outfile)
```

#### Vollständiges Beispiel

```python
def link_add(infile, outfile):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

    document.pages[1].accept(text_fragment_absorber)
    phone_number_fragment = text_fragment_absorber.text_fragments[1]

    link_annotation = ap.annotations.LinkAnnotation(
        document.pages[1], phone_number_fragment.rectangle
    )
    link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")

    document.pages[1].annotations.append(link_annotation)
    document.save(outfile)
```

### Link-Annotation abrufen

Um vorhandene interaktive Links zu prüfen, filtern Sie die Annotationen‑Sammlung auf der ersten Seite und behalten nur Elemente, deren Typ ist `LINK`. Das Beispiel gibt dann das Rechteck für jede passende Anmerkung aus.

#### Laden Sie das PDF und sammeln Sie Link-Annotationen

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### Lese die Anmerkungsrechtecke

Durchlaufen Sie die gefilterten Anmerkungen und geben Sie die Koordinaten jedes Linkbereichs aus.

```python
for link_annotation in link_annotations:
    print(link_annotation.rect)
```

#### Vollständiges Beispiel

```python
def link_get(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        print(link_annotation.rect)
```

### Link-Annotation löschen

Dieser Workflow entfernt alle Link-Anmerkungen von der ersten Seite und speichert das bereinigte PDF als neue Datei.

#### Finde die Link-Annotationen zum Entfernen

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### Löschen Sie jede Linkannotation

```python
for link_annotation in link_annotations:
    document.pages[1].annotations.delete(link_annotation)
```

#### Speichern Sie das aktualisierte Dokument

```python
document.save(outfile)
```

#### Vollständiges Beispiel

```python
def link_delete(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        document.pages[1].annotations.delete(link_annotation)

    document.save(outfile)
```

## Widget-Annotation

### Navigationsschaltfläche hinzufügen

Navigationsschaltflächen sind in mehrseitigen PDFs nützlich, wenn Sie möchten, dass Leser zwischen den Seiten wechseln, ohne die Viewer-Oberfläche zu verwenden. Dieses Beispiel fügt hinzu `Previous Page` und `Next Page` Schaltflächen zu jeder Seite.

#### Button-Einstellungen definieren

Speichern Sie die Schaltflächenbeschriftungen, Positionen und vordefinierten Aktionen in einer einfachen Konfigurationsliste.

```python
button_config = [
    ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
    ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
]
```

#### Laden Sie das PDF und stellen Sie sicher, dass mehrere Seiten vorhanden sind

Das Beispiel öffnet das Quell‑Dokument und fügt eine weitere Seite hinzu, damit die Navigationsaktionen mindestens zwei Seiten zur Verfügung haben.

```python
document = ap.Document(infile)
document.pages.add()
```

#### Erstelle die Schaltflächen auf jeder Seite

Für jede Seite, erstelle ein `ButtonField`, setzen Sie seinen Text und seine Farben, weisen Sie eine vordefinierte Navigationsaktion zu und fügen Sie es dem Formular hinzu.

```python
for page in document.pages:
    for name, x_pos, action in button_config:
        rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
        button = ap.forms.ButtonField(page, rect)
        button.partial_name = name
        button.value = name
        button.characteristics.border = ap.Color.red.to_rgb()
        button.characteristics.background = ap.Color.orange.to_rgb()
        button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
        document.form.add(button)
```

#### Ergebnis speichern

```python
document.save(outfile)
```

#### Vollständiges Beispiel

```python
def navigation_buttons_add(infile, outfile):
    button_config = [
        ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
        ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
    ]

    document = ap.Document(infile)
    document.pages.add()

    for page in document.pages:
        for name, x_pos, action in button_config:
            rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ap.forms.ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
            document.form.add(button)

    document.save(outfile)
```

### Druckschaltfläche hinzufügen

Dieses Beispiel erstellt ein neues einseitiges PDF und platziert einen Druck‑Button nahe dem oberen Rand der Seite. Das Klicken des Buttons löst die vordefinierte Druckaktion in einem kompatiblen PDF‑Betrachter aus.

#### Erstelle ein neues PDF und füge eine Seite hinzu

```python
document = ap.Document()
page = document.pages.add()
```

#### Erstelle und konfiguriere die Schaltfläche

Definieren Sie das Schaltflächenrechteck, erstellen Sie das `ButtonField`, setzen Sie seine Beschriftung und fügen Sie die Druckaktion hinzu.

```python
rect = ap.Rectangle(72, 748, 164, 768, True)

print_button = ap.forms.ButtonField(page, rect)
print_button.alternate_name = "Print current document"
print_button.color = ap.Color.black
print_button.partial_name = "printBtn1"
print_button.value = "Print Document"
print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
    ap.annotations.PredefinedAction.FILE_PRINT
)
```

#### Rand- und Hintergrundstile festlegen

Das Beispiel definiert einen durchgezogenen Rand und wendet benutzerdefinierte Farben an, um die Schaltfläche im Dokument sichtbar zu machen.

```python
border = ap.annotations.Border(print_button)
border.style = ap.annotations.BorderStyle.SOLID
border.width = 2
print_button.border = border

print_button.characteristics.border = ap.Color.blue.to_rgb()
print_button.characteristics.background = ap.Color.light_blue.to_rgb()
```

#### Fügen Sie die Schaltfläche hinzu und speichern Sie das PDF

```python
document.form.add(print_button)
document.save(outfile)
```

#### Vollständiges Beispiel

```python
def print_button_add(infile, outfile):
    document = ap.Document()
    page = document.pages.add()

    rect = ap.Rectangle(72, 748, 164, 768, True)

    print_button = ap.forms.ButtonField(page, rect)
    print_button.alternate_name = "Print current document"
    print_button.color = ap.Color.black
    print_button.partial_name = "printBtn1"
    print_button.value = "Print Document"
    print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
        ap.annotations.PredefinedAction.FILE_PRINT
    )

    border = ap.annotations.Border(print_button)
    border.style = ap.annotations.BorderStyle.SOLID
    border.width = 2
    print_button.border = border

    print_button.characteristics.border = ap.Color.blue.to_rgb()
    print_button.characteristics.background = ap.Color.light_blue.to_rgb()

    document.form.add(print_button)
    document.save(outfile)
```

## Verwandte Themen

- [Import und Export von Anmerkungen](/python-net/import-export-annotations/)
- [Markup-Anmerkungen](/python-net/markup-annotations/)
- [Medien-Anmerkungen](/python-net/media-annotations/)
- [Sicherheitsanmerkungen](/python-net/security-annotations/)
- [Form‑Annotationen](/python-net/shape-annotations/)
- [Textbasierte Anmerkungen](/python-net/text-based-Annotations/)
- [Wasserzeichen-Annotationen](/python-net/watermark-annotations/)
