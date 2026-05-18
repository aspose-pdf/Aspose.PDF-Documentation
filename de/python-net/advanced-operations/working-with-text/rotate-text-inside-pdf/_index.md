---
title: PDF-Text in Python drehen
linktitle: Text im PDF drehen
type: docs
weight: 50
url: /de/python-net/rotate-text-inside-pdf/
description: Erfahren Sie, wie Sie Textfragmente und Absätze in PDF-Dokumenten mit Python drehen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Textfragmente und Absätze in PDF-Dokumenten mit Python drehen.
Abstract: Dieser Artikel erklärt, wie man Text in PDF-Dokumenten mit Aspose.PDF for Python via .NET rotiert. Er zeigt, wie man die `rotation`-Eigenschaft von `TextFragment` festlegt, rotierten Inhalt mit `TextBuilder` und `TextParagraph` erstellt und rotierten Text direkt zu Seitenabsätzen für verschiedene Layout‑Szenarien hinzufügt.
---

Drehen Sie Textfragmente in einem PDF-Dokument mithilfe von Aspose.PDF for Python via .NET. Diese Seite zeigt, wie man die Position und Drehung von Text durch Verwendung steuert. `TextFragment`, `TextState`, und `TextBuilder`. Durch Anpassen der Rotationswinkel können Sie Layouts wie diagonale Kopfzeilen, vertikale Beschriftungen und gedrehte Anmerkungen erstellen.

## Textfragmente mit TextBuilder in PDF rotieren

Erstellt eine PDF-Datei namens `rotated_fragments.pdf` enthält drei Textfragmente, die horizontal ausgerichtet sind:

- Der erste Text ist nicht gedreht
- Der zweite ist um 45° gedreht
- Der dritte ist um 90° gedreht

1. Erstellen Sie ein neues PDF-Dokument.
1. Fügen Sie eine neue Seite ein, um den gedrehten Text zu hosten.
1. Erstelle das erste TextFragment (keine Drehung).
1. Erstelle das zweite TextFragment (45° Drehung).
1. Erstelle das dritte TextFragment (90° Drehung).
1. Textfragmente hinzufügen mit `TextBuilder`.
1. Speichern Sie das Dokument.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_1(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        text_fragment_3.text_state.rotation = 90
        # create TextBuilder object
        builder = ap.text.TextBuilder(page)
        # Append the text fragment to the PDF page
        builder.append_text(text_fragment_1)
        builder.append_text(text_fragment_2)
        builder.append_text(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Einzelne Textfragmente innerhalb eines Absatzes im PDF drehen

Drehen Sie einzelne Textfragmente innerhalb eines Absatzes. Es wird gezeigt, wie ein mehrzeiliger Absatz (TextParagraph) erstellt wird, der mehrere Fragmente (TextFragment) enthält, von denen jedes einen eigenen Drehwinkel hat. Diese Technik ist nützlich, um visuell ansprechende Dokumente zu erstellen, die horizontal und diagonal orientierten Text kombinieren — zum Beispiel stilisierte Überschriften, Diagramme oder annotierte Beschriftungen.

Erstellt ein PDF mit dem Namen `rotated_paragraph_fragments.pdf` enthält einen Absatz mit drei Textzeilen, bei denen jede Zeile unterschiedlich gedreht ist:

- die erste Zeile ist um 45° gedreht
- die zweite Zeile bleibt horizontal (0°)
- die dritte Zeile ist um -45° gedreht

1. Erstellen Sie ein neues PDF-Dokument.
1. Füge eine leere Seite hinzu, wo der gedrehte Text erscheint.
1. Erstelle ein `TextParagraph`.
1. Erstelle und konfiguriere das erste Textfragment (+45° Drehung).
1. Erstelle das zweite Textfragment (keine Drehung).
1. Erstelle das dritte Textfragment (-45° Drehung).
1. Textfragmente an den Absatz anhängen.
1. Fügen Sie den Absatz zur Seite hinzu, indem Sie `TextBuilder`.
1. Speichern Sie das Dokument.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_2(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        paragraph = ap.text.TextParagraph()
        paragraph.position = ap.text.Position(200, 600)
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_3.text_state.rotation = -45
        # Append the text fragments to the paragraph
        paragraph.append_line(text_fragment_1)
        paragraph.append_line(text_fragment_2)
        paragraph.append_line(text_fragment_3)
        # Create TextBuilder object
        text_builder = ap.text.TextBuilder(page)
        # Append the text paragraph to the PDF page
        text_builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## Text mit Seitenabsätzen im PDF drehen

Dieser Abschnitt demonstriert eine vereinfachte Methode zum Drehen von Text innerhalb eines PDF mithilfe von Aspose.PDF for Python via .NET.
Im Gegensatz zu niedrigeren Ansätzen mit `TextBuilder` oder `TextParagraph`, diese Methode fügt gedrehte Textfragmente direkt zur Absatzsammlung der Seite hinzu (`page.paragraphs`). Es ist ideal, wenn Sie eine einfache Textrotation benötigen, aber keine präzise Positionierung oder Absatzstrukturierung benötigen.

Erzeugt eine Datei mit dem Namen `simple_rotated_text.pdf` enthält:

- ein Haupt‑Horizontal‑Textfragment mit 0° Rotation
- 315° gedrehter Fragment
- 270° gedrehter Fragment

1. Ein neues PDF-Dokument initialisieren.
1. Erstellen Sie eine Seite, auf der der gedrehte Text platziert wird.
1. Erstelle das erste TextFragment (keine Drehung).
1. Erstellen Sie das zweite Textfragment (315° Drehung).
1. Erstelle das dritte Textfragment (270° Drehung).
1. Fügen Sie Textfragmente direkt zu Seitenabsätzen hinzu.
1. Speichern Sie das PDF-Dokument.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_3(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Gesamte Absätze in einem PDF drehen

Dieses Beispiel demonstriert eine erweiterte Textdrehung auf Absatzebene in einem PDF. Im Gegensatz zur Fragment‑Ebene‑Drehung (bei der jedes Textstück einzeln gedreht wird), rotiert diese Methode ganze Absätze als einheitliche Blöcke in unterschiedlichen Winkeln.
Jeder Absatz enthält mehrere formatierte Textfragmente, und der gesamte Absatz wird um bestimmte Winkel gedreht — was komplexe, konsistente Layout-Transformationen ermöglicht.
Dies ist ideal für künstlerische Layouts, Wasserzeichen oder designintensive PDFs, bei denen ganze Textabschnitte in verschiedene Richtungen ausgerichtet werden müssen.

Erstellt `rotated_paragraphs.pdf`, enthält vier vollständig gestaltete und gedrehte Absätze:

- jede um einen eindeutigen Winkel gedreht (45°, 135°, 225° und 315°)
- jeder Absatz hat drei Zeilen Text mit farbigen Hintergründen, Unterstreichungen und einheitlichem Stil

1. Erstellen Sie ein neues PDF-Dokument.
1. Fügen Sie eine leere Seite hinzu, um die gedrehten Absätze zu halten.
1. Iterieren, um mehrere Absätze zu erstellen.
1. Erstelle und positioniere den Absatz.
1. Erstelle Textfragmente mit Formatierung.
1. Textformatierung anwenden.
1. Fügen Sie Textfragmente zum Absatz hinzu.
1. Fügen Sie den Absatz mithilfe der Seite hinzu `TextBuilder`.
1. Wiederholen Sie dies für alle vier Drehungen.
1. Speichern Sie das PDF-Dokument.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_4(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        for i in range(4):
            paragraph = ap.text.TextParagraph()
            paragraph.position = ap.text.Position(200, 600)
            # Specify rotation
            paragraph.rotation = i * 90 + 45
            # Create text fragment
            text_fragment_1 = ap.text.TextFragment("Paragraph Text")
            # Create text fragment
            text_fragment_1.text_state.font_size = 12
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_3.text_state.background_color = ap.Color.light_gray
            text_fragment_3.text_state.foreground_color = ap.Color.blue
            text_fragment_3.text_state.underline = True
            paragraph.append_line(text_fragment_1)
            paragraph.append_line(text_fragment_2)
            paragraph.append_line(text_fragment_3)
            # Create TextBuilder object
            builder = ap.text.TextBuilder(page)
            # Append the text fragment to the PDF page
            builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## Verwandte Textthemen

- [Arbeiten Sie mit Text in PDF mit Python](/pdf/de/python-net/working-with-text/)
- [Text zum PDF hinzufügen](/pdf/de/python-net/add-text-to-pdf-file/)
- [PDF-Text formatieren in Python](/pdf/de/python-net/text-formatting-inside-pdf/)
- [Text in PDF mit Python ersetzen](/pdf/de/python-net/replace-text-in-pdf/)