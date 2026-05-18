---
title: Suche und extrahiere PDF-Text in Python
linktitle: Suche und Text abrufen
type: docs
weight: 60
url: /de/python-net/search-and-get-text-from-pdf/
description: Erfahren Sie, wie Sie Text in PDF-Dokumenten mit Python suchen, prüfen und extrahieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Durchsuchen Sie PDF-Text und prüfen Sie extrahierte Fragmente mit Python.
Abstract: Dieser Artikel erklärt, wie man Text aus PDF-Dokumenten mit Aspose.PDF for Python via .NET sucht und extrahiert. Er behandelt `TextAbsorber` und `TextFragmentAbsorber`, einschließlich regionbasierter Extraktion, seitenspezifischer Suchen, Phrasenerkennung und Prüfung von Textposition und Schriftarteigenschaften.
---

## Text aus PDF suchen

Suchen und extrahieren Sie Text aus einem definierten rechteckigen Bereich in einem PDF-Dokument mit `TextAbsorber` Klasse. Sie verwendet den reinen Textformatierungsmodus für saubere, nicht formatierte Ausgaben, was nützlich ist, um Inhalte aus strukturierten Bereichen wie Kopfzeilen, Fußzeilen oder Tabellenbereichen zu extrahieren. Durch Kombination `TextExtractionOptions` und `TextSearchOptions` Mit rechteckigen Einschränkungen können Sie steuern, wo und wie Text extrahiert wird.

Verwenden Sie diese Seite, wenn Sie den PDF-Textinhalt prüfen, Text zur Analyse extrahieren oder die Positionen und Formatierungen übereinstimmender Textfragmente überprüfen müssen.

1. Laden Sie die PDF-Datei mit 'ap.Document'.
1. Text-Extraktionsoptionen konfigurieren.
1. Definieren Sie den Suchbereich mit Rechteckbeschränkungen.
1. Erstellen und konfigurieren Sie TextAbsorber.
1. Alle Seiten im Dokument verarbeiten.
1. Abrufen und Anzeigen des extrahierten Textes.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search(input_file_path):
    # Open PDF document
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Process all pages
    document.pages.accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## Text von einer bestimmten PDF-Seite suchen

Suchen und extrahieren Sie Text von einer bestimmten Seite und Region in einer PDF mithilfe von Aspose.PDF’s TextAbsorber. Es richtet sich an Seite 2 des Dokuments und extrahiert ausschließlich den Text, der sich innerhalb eines definierten rechteckigen Bereichs befindet.
Durch die Kombination von TextExtractionOptions (zur Steuerung der Formatierung) und TextSearchOptions (zur Einschränkung des Bereichs) können Sie eine präzise, seitenbezogene Textextraktion effizient durchführen.

1. Laden Sie das PDF Document.
1. Text-Extraktionsoptionen einrichten.
1. Beschränken Sie die Textextraktion auf ein bestimmtes rechteckiges Gebiet auf der Seite.
1. Erstellen und konfigurieren Sie TextAbsorber.
1. Eine bestimmte Seite verarbeiten.
1. Abrufen und Anzeigen des extrahierten Textes.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search_page(input_file_path):
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Only page 2
    document.pages[2].accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## Analysieren und detaillierte Textfragment‑Eigenschaften aus einer PDF extrahieren

Im Gegensatz zu TextAbsorber, das Rohtext extrahiert, bietet TextFragmentAbsorber detaillierte, niedrigstufige Informationen zu jedem Textfragment — wie dessen Position, Schriftattribute, Farbe und Einbettungsdetails.

1. Laden Sie das PDF Document.
1. Initialisieren Sie TextFragmentAbsorber.
1. Alle Seiten im Dokument verarbeiten.
1. Durchlaufen Sie extrahierte Textfragmente.
1. Grundlegende Textinformationen ausgeben.
1. Schriftart und Formatierungsdetails drucken.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    document.pages.accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
        print("XIndent:", fragment.position.x_indent)
        print("YIndent:", fragment.position.y_indent)
        print("Font - Name:", fragment.text_state.font.font_name)
        print("Font - IsAccessible:", fragment.text_state.font.is_accessible)
        print("Font - IsEmbedded:", fragment.text_state.font.is_embedded)
        print("Font - IsSubset:", fragment.text_state.font.is_subset)
        print("Font Size:", fragment.text_state.font_size)
        print("Foreground Color:", fragment.text_state.foreground_color)
```

## Suche nach einer spezifischen Textphrase auf einer einzelnen PDF-Seite

Suchen Sie nach einer bestimmten Textphrase innerhalb einer Seite eines PDF-Dokuments mithilfe von TextFragmentAbsorber. Im Gegensatz zur Suche im gesamten Dokument beschränkt dieser Ansatz die Suche auf nur eine Seite, was die Bestätigung des Vorhandenseins und der Position von Text in gezielten Bereichen wie Kopfzeilen, Fußzeilen oder bestimmten Inhaltsabschnitten effizienter macht.

1. Laden Sie das PDF Document.
1. Initialisieren Sie TextFragmentAbsorber mit Suchausdruck.
1. Absorber auf bestimmte Seite anwenden.
1. Durch gefundene Fragmente iterieren.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_page(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale")
    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Sequenzielle seitenweise Textsuche mit kumulativen Ergebnissen

Durchsuchen Sie Text schrittweise über mehrere Seiten eines PDF-Dokuments mithilfe von Aspose.PDF’s TextFragmentAbsorber.
Im Gegensatz zu einer einseitigen oder dokumentweiten Suche ermöglicht dieser Ansatz, Seiten nacheinander zu verarbeiten, Ergebnisse schrittweise zu sammeln und Textfragmente mit seitenspezifischem Kontext zu analysieren. Diese Methode ist ideal für große Dokumente oder progressive Verarbeitungsabläufe.

1. Laden Sie das PDF Document.
1. Initialisieren Sie TextFragmentAbsorber und setzen Sie den Suchbegriff.
1. Verarbeite die erste Seite. Suche nur Seite 1. Gibt Text, Seitennummer und Position aus. Liefere isolierte, seitenbezogene Ergebnisse für Klarheit.
1. Verarbeite die nächste Seite sequenziell. Gehe zu Seite 2 und fahre optional mit dem Rest des Dokuments fort. Der 'absorber.visit()' stellt sicher, dass die Ergebnisse aller besuchten Seiten angesammelt werden. Gibt die kumulativen Suchergebnisse aus und zeigt sowohl den Text als auch den Ort an.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_sequential_search(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.phrase = "whale"

    # First page
    document.pages[1].accept(absorber)
    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)

    print("--")

    # Continue to next page
    document.pages[2].accept(absorber)
    absorber.visit(document)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)
```

## Gezielte Phrasensuche in einem rechteckigen Bereich

Suchen Sie nach einer bestimmten Phrase in einer PDF, wobei die Suche auf einen bestimmten rechteckigen Bereich einer einzelnen Seite eingeschränkt wird.
Durch die Kombination von Phrasensuche mit räumlichen Einschränkungen können Sie Inhalte genau in festgelegten Bereichen finden, ohne die gesamte Seite oder das gesamte Dokument zu durchsuchen. Dies ist besonders nützlich für Formulare, Kopfzeilen, Fußzeilen oder strukturierte Berichte, bei denen Inhalte an vorhersehbaren Positionen erscheinen.

1. Laden Sie das PDF Document.
1. Initialisieren Sie TextFragmentAbsorber mit Phrase und rechteckigen Einschränkungen
1. Wenden Sie den Absorber auf Seite 2 an. Beschränkt die Verarbeitung auf Seite 2, wodurch unnötige Berechnungen reduziert werden. Stellt sicher, dass die Suche seitenbezogen ist.
1. Iteriere durch gefundene Fragmente und drucke sie

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_phrase(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Textmustersuche in PDF mit regulären Ausdrücken

Suchen Sie nach Textmustern in einer PDF mithilfe regulärer Ausdrücke. Durch das Aktivieren des Regex‑Modus im TextFragmentAbsorber können Sie komplexe Muster wie Zahlen, Datumsangaben, Preise, Koordinaten oder benutzerdefinierte Textformate finden. Die Funktion begrenzt die Suche auf eine bestimmte Seite, was sie für die gezielte Extraktion strukturierter Daten effizient macht.

1. Laden Sie das PDF Document.
1. Initialisieren Sie TextFragmentAbsorber mit einem Regex-Muster.
1. Wenden Sie den Absorber auf Seite 2 an. Beschränkt die Suche auf Seite 2 für Effizienz und Präzision. Nur der Text auf dieser Seite wird analysiert.
1. Durchlauf gefundener Fragmente. Druckt passende Textfragmente und deren Koordinaten. Liefert präzise Standortinformationen für extrahierte Muster.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_regex(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        r"\d+\.\d+", ap.text.TextSearchOptions(is_regular_expression_used=True)
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Textübereinstimmungen in PDF in Hyperlinks umwandeln mit TextFragmentAbsorber

Suchen Sie nach bestimmten Textphrasen in einem PDF und konvertieren Sie sie in anklickbare Hyperlinks. Mit TextFragmentAbsorber und regex‑Mustern werden Zielwörter gefunden und visuelle Formatierungen (Farbe und Unterstreichung) sowie interaktive Links angewendet.

1. Laden Sie das PDF Document.
1. Initialisieren Sie TextFragmentAbsorber mit einem Regex-Muster.
1. Wenden Sie Absorber auf Seite 1 an.
1. Stil und Hyperlinks zu Übereinstimmungen hinzufügen.
1. Geändertes PDF speichern.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_add_hyperlink(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale|elephant")
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.underline = True
        fragment.hyperlink = ap.WebHyperlink(
            f"https://en.wikipedia.org/wiki/{fragment.text}"
        )

    output = input_file_path.replace("in.pdf", "out.pdf")
    document.save(output)
```

## Suchen und Identifizieren von formatiertem Text in PDF mit TextFragmentAbsorber

Suchen Sie nach Textfragmenten in einem PDF basierend auf deren Formatierungseigenschaften anstatt auf dem Inhalt. Mit TextFragmentAbsorber werden Texte mit bestimmten Stilmerkmalen, wie zum Beispiel fettem Text, identifiziert.

1. Laden Sie das PDF Document.
1. Initialisieren Sie TextFragmentAbsorber.
1. Wenden Sie Absorber auf Seite 1 an.
1. Textfragmente basierend auf Formatierung prüfen. Prüft den Font-Stil auf Fettdruck.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_styled_text(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.font_style == ap.text.FontStyles.BOLD:
            print(f"Bold: {fragment.text}")
        if fragment.text_state.invisible:
            print(f"Invisible: {fragment.text}")
```

## Visuelle Textmarkierung in PDF-Seiten

Diese Funktion kombiniert Texterkennung und Rendering zu einem einzigen Workflow. Sie extrahiert nicht nur Text, sondern visualisiert ihn auch, indem sie Fragmente, Segmente und Zeichen mit farblich gekennzeichneten Rechtecken auf PNG-Bildern jeder Seite hervorhebt.

Unser Beispiel führt eine erweiterte Textvisualisierung in einem PDF durch, indem es:

- Suche nach allen sichtbaren Textfragmenten mit regulären Ausdrücken
- Rendern jeder PDF-Seite in ein hochauflösendes PNG-Bild
- Zeichnen farbiger Rechtecke um Textfragmente, Textsegmente und einzelne Zeichen

1. Ausgabe-Bildauflösung festlegen. Jede PDF‑Seite wird in ein 150 DPI‑PNG‑Bild konvertiert.
1. Öffnen Sie das PDF und initialisieren Sie den TextAbsorber.
1. Jede Seite verarbeiten. Den Absorber auf jede Seite anwenden. Alle erkannten Textfragmente und ihre geometrischen Positionen sammeln.
1. Seite in PNG-Stream konvertieren.
1. Grafikobjekt zum Zeichnen vorbereiten.
1. Koordinatentransformation anwenden. PDF-Koordinaten in Bildpixel umwandeln.
1. Rechtecke für Textelemente zeichnen.
1. Speichern Sie das Ergebnis.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_highlight(infile):
    resolution = 150
    png_device = ap.devices.PngDevice(ap.devices.Resolution(resolution, resolution))

    # Open PDF document
    document = ap.Document(infile)
    absorber = ap.text.TextFragmentAbsorber(r"[\S]+")
    absorber.text_search_options.is_regular_expression_used = True

    for page in document.pages:
        page.accept(absorber)
        stream = io.BytesIO()
        png_device.process(page, stream)
        with drawing.Bitmap.from_stream(stream) as bmp:
            with drawing.Graphics.from_image(bmp) as gr:
                scale = resolution / 72
                gr.transform = drawing.drawing2d.Matrix(
                    float(scale),
                    float(0),
                    float(0),
                    float(-scale),
                    float(0),
                    float(bmp.height),
                )
                text_fragment_collection = absorber.text_fragments
                # Loop through the fragments
                for text_fragment in text_fragment_collection:
                    gr.draw_rectangle(
                        drawing.Pens.yellow,
                        float(text_fragment.position.x_indent),
                        float(text_fragment.position.y_indent),
                        float(text_fragment.rectangle.width),
                        float(text_fragment.rectangle.height),
                    )
                    for seg_num in range(1, len(text_fragment.segments) + 1):
                        segment = text_fragment.segments[seg_num]
                        for char_num in range(1, len(segment.characters) + 1):
                            character_info = segment.characters[char_num]
                            rect = page.get_page_rect(True)
                            print(
                                f"TextFragment = {text_fragment.text}"
                                + f" Page URY = {rect.ury}"
                                + f" TextFragment URY = {text_fragment.rectangle.ury}"
                            )
                            gr.draw_rectangle(
                                drawing.Pens.black,
                                float(character_info.rectangle.llx),
                                float(character_info.rectangle.lly),
                                float(character_info.rectangle.width),
                                float(character_info.rectangle.height),
                            )
                        gr.draw_rectangle(
                            drawing.Pens.green,
                            float(segment.rectangle.llx),
                            float(segment.rectangle.lly),
                            float(segment.rectangle.width),
                            float(segment.rectangle.height),
                        )

                # Save result
                bmp.save(
                    infile.replace("_in.pdf", str(page.number) + "_out.png"),
                    drawing.imaging.ImageFormat.png,
                )
```

## Verwandte Textthemen

- [Arbeiten Sie mit Text in PDF mit Python](/pdf/de/python-net/working-with-text/)
- [Text in PDF über Python ersetzen](/pdf/de/python-net/replace-text-in-pdf/)
- [Tooltips zum PDF-Text in Python hinzufügen](/pdf/de/python-net/pdf-tooltip/)
- [Text zum PDF hinzufügen](/pdf/de/python-net/add-text-to-pdf-file/)