---
title: Text im PDF mit Python ersetzen
linktitle: Text im PDF ersetzen
type: docs
weight: 40
url: /de/python-net/replace-text-in-pdf/
description: Erfahren Sie, wie Sie Text in PDF-Dokumenten mit Python ersetzen, neu anordnen und entfernen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Ersetzen, Entfernen und Anpassen von Textinhalten in PDFs mit Python
Abstract: Dieser Artikel behandelt praktische Workflows zum Ersetzen von Text in PDF-Dokumenten mithilfe von Aspose.PDF for Python via .NET. Er umfasst das Ersetzen von Text über mehrere Seiten hinweg, die Beschränkung des Ersetzens auf bestimmte Regionen, die Anpassung des Textlayouts während des Ersetzens, die Arbeit mit regex‑basierten Übereinstimmungen, das Ersetzen von Schriftarten und das Entfernen von Textinhalten bei Bedarf.
---

Diese Beispiele zeigen, wie man **Text in einem bestehenden PDF ändern oder entfernen**.

Verwenden Sie diese Seite, wenn Sie Textwerte aktualisieren, unerwünschte Inhalte entfernen oder Text‑Ersetzungsregeln für PDF‑Seiten anwenden müssen.

## Vorhandenen Text ersetzen

### Text in allen Seiten des PDF-Dokuments ersetzen

{{% alert color="primary" %}}

Sie können versuchen, den Text im Dokument mit Aspose.PDF zu finden und zu ersetzen und die Ergebnisse online hier abzurufen. [Link](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Text ersetzen ist eine häufige Anforderung beim Aktualisieren oder Korrigieren von Inhalten in bestehenden PDF-Dokumenten — zum Beispiel beim Ändern von Produktnamen, Korrigieren von Tippfehlern oder Aktualisieren von Terminologie über mehrere Seiten hinweg.

Aspose.PDF for Python via .NET bietet eine leistungsstarke und effiziente Methode zum programmgesteuerten Suchen und Ersetzen von Text über die [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) Klasse.

Dieses Beispiel demonstriert, wie man alle Vorkommen einer bestimmten Phrase (in diesem Fall "Black cat") findet und sie durch eine neue Phrase ("White dog") im gesamten PDF-Dokument ersetzt.

1. Geben Sie Such- und Ersetzungssätze an. Legen Sie den Text fest, den Sie finden möchten, und den Text, durch den er ersetzt werden soll.
1. Laden Sie das PDF Document.
1. Erstellen Sie einen Text Absorber. Ein TextFragmentAbsorber wird mit dem Suchbegriff initialisiert. Er durchsucht das Dokument nach allen Vorkommen des angegebenen Begriffs.
1. Wenden Sie den Absorber auf alle Seiten an. Dies iteriert über alle Seiten und sammelt Textfragmente, die der Phrase entsprechen.
1. Ersetzen Sie jedes gefundene Fragment. Jede Instanz von "Black cat" sollte zu "White dog" geändert werden.
1. Speichern Sie das aktualisierte PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_on_all_pages(infile, outfile):
    search_phrase = "PDF"
    replace_phrase = "pdf"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Text in einem bestimmten Seitenbereich ersetzen

Manchmal müssen Sie Text nur innerhalb eines bestimmten Bereichs einer PDF-Seite ersetzen, anstatt das gesamte Dokument zu durchsuchen — zum Beispiel, um eine Kopfzeile, Fußzeile oder eine Tabellenzelle an einer bekannten Position zu aktualisieren.

Die Aspose.PDF for Python via .NET Bibliothek ermöglicht diese Funktionalität, indem sie die [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) in Verbindung mit regionsbasiertem Textsuchen.

Dieses Beispiel demonstriert, wie man alle Vorkommen einer Zielphrase innerhalb eines definierten rechteckigen Bereichs auf einer bestimmten Seite findet und ersetzt.

1. Geben Sie Such- und Ersetzungsphrasen an.
1. Laden Sie das PDF Document.
1. Erstelle einen Text Absorber zum Suchen. Initialisiere einen TextFragmentAbsorber, um den gewünschten Text zu finden.
1. Beschränken Sie den Suchbereich. Das Rechteck gibt die x- und y-Koordinatenbegrenzungen auf der Seite an.
1. Wenden Sie den Absorber auf einer bestimmten Seite an. Dies führt die Suche aus und sammelt passende Textfragmente im angegebenen Bereich.
1. Ersetzen Sie den gefundenen Text. Jedes Vorkommen von 'doc' im definierten Bereich wird zu 'DOC'.
1. Speichern Sie das aktualisierte PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_in_particular_page_region(infile, outfile):
    search_phrase = "doc"
    replace_phrase = "DOC"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        absorber.text_search_options.limit_to_page_bounds = True
        absorber.text_search_options.rectangle = ap.Rectangle(300, 442, 500, 742, True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Größe ändern und Text verschieben, ohne die Schriftgröße zu verändern

Beim Ersetzen von Text in einem PDF möchte man manchmal den neuen Text in einem bestimmten Bereich anpassen oder neu positionieren, ohne die Schriftgröße zu ändern.
Aspose.PDF for Python via .NET bietet Optionen zur Anpassung des Textlayouts und des Zeilenabstands, während die ursprüngliche Schriftgröße unverändert bleibt.

1. Laden Sie das PDF Document.
1. Sammeln Sie alle Textfragmente auf der Seite mithilfe eines 'TextFragmentAbsorber'.
1. Wählen Sie das Fragment zum Modifizieren aus.
1. Verschieben und die Größe des Textrechtecks ändern.
1. Textabstand anpassen. Aktivieren Sie die Abstandsanpassung, um den Text in das geänderte Rechteck einzupassen.
1. Ersetzen Sie den Fragmenttext.
1. Speichern Sie das aktualisierte PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_shift_without_changing_font_size(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = fragment.rectangle
        rect.llx += 50
        rect.urx -= 50
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Größe ändern und Absatz in PDF verschieben

Wenn Sie mit PDFs arbeiten, müssen Sie manchmal einen Absatz ersetzen oder erweitern, während er visuell mit dem Seitenlayout ausgerichtet bleibt. Aspose.PDF ermöglicht es Ihnen, das Begrenzungsrechteck des Absatzes zu ändern und den Abstand anzupassen, um neuen Text einzupassen, und das alles, ohne die Font size zu ändern.

1. Laden Sie das PDF Document.
1. Verwenden Sie 'TextFragmentAbsorber', um alle Textfragmente auf der Seite zu sammeln.
1. Wählen Sie das Fragment zum Modifizieren aus.
1. Größe ändern und den Absatz verschieben. Verwenden Sie die Media-Box der Seite, um die Grenzen zu bestimmen und das Rechteck anzupassen.
1. Abstand anpassen. Dies ändert den Abstand zwischen Wörtern/Buchstaben, anstatt die Schriftgröße zu ändern.
1. Ersetzen Sie den Fragmenttext.
1. Speichern Sie das bearbeitete PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_shift_paragraph(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = document.pages[1].media_box
        rect.llx += 20
        rect.urx -= 20
        rect.ury -= 20
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Text ersetzen und Schrift automatisch erweitern, um den Zielbereich zu füllen

Ersetzen Sie Text in einer PDF, während die Schriftart automatisch verkleinert und vergrößert wird, um einen bestimmten rechteckigen Bereich auszufüllen. Mit der Aspose.PDF for Python via .NET-Bibliothek passt der Code die Schriftgröße und den Abstand dynamisch an, sodass der neue Textinhalt perfekt in ein definiertes Begrenzungsfeld passt — ohne manuelle Schriftberechnungen.

1. Laden Sie das PDF.
1. TextFragment erfassen.
1. Wählen Sie ein bestimmtes Fragment aus.
1. Zielrechteck definieren.
1. Optionen zur Textanpassung aktivieren.
1. Text ersetzen.
1. Speichern Sie das Document.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_expand_font(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = ap.Rectangle(100, 300, 512, 692, True)
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SCALE_TO_FILL
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Text ersetzen und in ein Rechteck einpassen

Ersetzen Sie Text in einem PDF-Dokument und stellen Sie sicher, dass der neue Inhalt innerhalb des rechteckigen Bereichs des Originaltextes bleibt, indem bei Bedarf die Schriftgröße automatisch reduziert wird.

Mit der Aspose.PDF for Python via .NET-Bibliothek passt diese Funktion sowohl das Textlayout als auch die Fontgröße dynamisch an, wobei die Document-Struktur erhalten bleibt und ein Überlauf verhindert wird.

1. Erstellen Sie ein TextFragmentAbsorber-Objekt, um alle Textfragmente von der ersten Seite zu extrahieren.
1. Zugriff auf ein bestimmtes Textfragment.
1. Ersetzenbereich festlegen.
1. Konfigurieren Sie die Textanpassungsoptionen. Legen Sie zwei wichtige Ersetzungsoptionen fest:
    - Schriftgrößenanpassung - 'SHRINK_TO_FIT' reduziert automatisch die Schriftgröße, wenn der neue Text zu lang ist.
    - Abstandsanpassung - 'ADJUST_SPACE_WIDTH' hält den Abstand proportional.
1. Ersetzen Sie den Text.
1. Speichern Sie das bearbeitete PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_fit_text_into_rectangle(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = fragment.rectangle
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SHRINK_TO_FIT
        )
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Platzhaltertext automatisch ersetzen und PDF-Layout neu anordnen

Platzhaltertext in einem PDF (z. B. Vorlagen oder Formulare) durch tatsächliche Daten wie Namen oder Firmeninformationen ersetzen.
Es passt das Seitenlayout automatisch an, um neuen Text einzufügen, während es benutzerdefinierte Formatierungen (Schriftart, Farbe, Größe) anwendet.

1. Importieren und Laden Sie das PDF.
1. Erstelle einen TextAbsorber für den Platzhalter.
1. Wenden Sie den Absorber auf alle Seiten an.
1. Durch gefundene Textfragmente iterieren.
1. Benutzerdefinierte Textformatierung anwenden.
1. Speichern Sie das aktualisierte Dokument.

```python
import sys
import aspose.pdf as ap
from os import path

def automatically_rearrange_page_contents(input_file, output_file):
    document = ap.Document(input_file)

    absorber = ap.text.TextFragmentAbsorber("[Long_placeholder_Long_placeholder]")
    document.pages.accept(absorber)

    for text_fragment in absorber.text_fragments:
        # text_fragment.text = "John Smith"
        text_fragment.text = "John Smith, South Development Studio"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Calibri")
        text_fragment.text_state.font_size = 12
        text_fragment.text_state.foreground_color = ap.Color.navy

    # Save PDF document
    document.save(output_file)
```

### Text basierend auf einem regulären Ausdruck ersetzen

Bei der Arbeit mit PDF-Dokumenten müssen Sie möglicherweise Text ersetzen, der einem Muster folgt, anstatt einer konkreten Phrase – zum Beispiel Telefonnummern, Codes oder datumsähnliche Formate.

Aspose.PDF for Python via .NET ermöglicht es Ihnen, solche Ersetzungen mithilfe regulärer Ausdrücke (Regex) mit der TextFragmentAbsorber-Klasse durchzuführen.

Dieses Beispiel zeigt, wie man Textmuster findet (in diesem Fall jeder Text, der dem Format ####-#### entspricht, z. B. 1234-5678) und sie durch einen formatierten String 'ABC1-2XZY' ersetzt. Es zeigt außerdem, wie man die Schriftart, Farbe und Größe des ersetzten Textes anpassen kann.

Das folgende Code‑Snippet zeigt Ihnen, wie Sie Text anhand eines regulären Ausdrucks ersetzen.

1. Laden Sie das PDF Document.
1. Erstellen Sie einen regexbasierten TextAbsorber. Initialisieren Sie den TextFragmentAbsorber mit einem regulären Ausdrucksmuster.
1. Aktiviere den regulären Ausdrucksmodus. Der Parameter 'True' aktiviert den Suchmodus für reguläre Ausdrücke.
1. Wenden Sie den Absorber auf eine Seite an. Dies durchsucht die Seite nach allen Textfragmenten, die dem definierten Regex-Muster entsprechen.
1. Ersetzen Sie jede Übereinstimmung durch neuen Text und wenden Sie benutzerdefiniertes Styling an.
1. Speichern Sie das modifizierte Dokument.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_based_on_regex(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(r"\d{4}-\d{4}")
        absorber.text_search_options = ap.text.TextSearchOptions(True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = "ABC1-2XZY"
            fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
            fragment.text_state.font_size = 12
            fragment.text_state.foreground_color = ap.Color.blue
            fragment.text_state.background_color = ap.Color.light_green

        document.save(outfile)
```

## Schriftarten ersetzen oder ungenutzte Schriftarten entfernen

### Schriften in einer vorhandenen PDF-Datei ersetzen

Gelegentlich müssen Sie Schriftarten in einem PDF standardisieren oder aktualisieren – zum Beispiel, indem Sie eine veraltete oder proprietäre Schriftart durch eine zugänglichere ersetzen. Die Aspose.PDF for Python via .NET Bibliothek ermöglicht es Ihnen, Schriftarten programmgesteuert zu erkennen und zu ersetzen, wodurch eine konsistente Typografie und Dokumentkompatibilität sichergestellt wird.

Dieses Beispiel zeigt, wie man alle Vorkommen einer bestimmten Schriftart (z. B. 'Arial-BoldMT') durch eine andere Schriftart (z. B. 'Verdana') in einem PDF-Dokument ersetzt.

Das folgende Code‑Snippet zeigt, wie man die Schriftart in einem PDF‑Dokument ersetzt:

1. Öffnen Sie das PDF-Dokument.
1. Initialisieren Sie einen TextFragmentAbsorber.
1. Verwenden Sie den Absorber, um Textfragmente von jeder Seite im Document zu extrahieren.
1. Schriftarten identifizieren und ersetzen. Das Skript prüft, ob die aktuelle Schriftart eines Fragments ‘Arial-BoldMT’ ist. Falls ja, ersetzt es sie durch die ‘Verdana’-Schriftart mithilfe der FontRepository.find_font()-Methode.
1. Speichern Sie das modifizierte Dokument.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_fonts(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

### Unbenutzte Schriftarten entfernen

Im Laufe der Zeit können sich in PDF-Dokumenten ungenutzte oder eingebettete Schriftarten ansammeln, die die Dateigröße erhöhen und die Verarbeitung verlangsamen. Diese ungenutzten Schriftarten bleiben oft selbst nach Textänderungen oder -austauschen erhalten, insbesondere bei der Arbeit mit großen oder komplexen PDFs.

Die Aspose.PDF for Python via .NET Bibliothek bietet einen effizienten Weg, solche redundanten Schriftarten mithilfe der TextEditOptions-Klasse zu entfernen. Dies optimiert nicht nur Ihr Dokument, sondern stellt auch sicher, dass nur die tatsächlich im sichtbaren Text verwendeten Schriftarten verwendet werden.

Die Methode 'remove_unused_fonts()' ist eine einfache, aber leistungsstarke Möglichkeit, PDF-Dateien zu optimieren, indem überflüssige Schriftartdaten entfernt werden.

Dieses Beispiel zeigt, wie man:

- Ein PDF nach ungenutzten Schriftarten durchsuchen.
- Entfernen Sie sie sicher.
- Ordnen Sie aktive Textfragmente einer einheitlichen Schriftart zu (z. B. Times New Roman).

1. Öffnen Sie das PDF-Dokument.
1. Konfigurieren Sie die Optionen für die Textbearbeitung. Dies weist die Engine an, alle eingebetteten Fonts zu entfernen, die derzeit im sichtbaren Text nicht verwendet werden.
1. Erstellen Sie einen TextAbsorber mit Optionen. Ein TextFragmentAbsorber extrahiert Textfragmente aus dem Dokument zur Bearbeitung.
1. Weisen Sie eine Standard Font zu. Sobald der Absorber alle Fragmente gesammelt hat, iterieren Sie durch sie und wenden eine konsistente Font an.
1. Speichern Sie das bereinigte PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_unused_fonts(input_file, output_file):
    # Open PDF document
    document = ap.Document(input_file)

    # Initialize text edit options to remove unused fonts
    options = ap.text.TextEditOptions(
        ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS
    )

    # Create a TextFragmentAbsorber with the specified options
    absorber = ap.text.TextFragmentAbsorber(options)
    document.pages.accept(absorber)

    # Iterate through all TextFragments
    for text_fragment in absorber.text_fragments:
        text_fragment.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )

    # Save the updated PDF document
    document.save(output_file)
```

## Alle Texte entfernen

### Text aus PDF entfernen

Entfernen Sie allen Textinhalt aus einer PDF-Datei, während Bilder, Formen und Layoutstrukturen erhalten bleiben.
Durch die Nutzung von TextFragmentAbsorber scannt der Code effizient das gesamte Document und löscht jedes gefundene TextFragment auf jeder Page.

1. Laden Sie das PDF Document.
1. Ein TextFragmentAbsorber‑Objekt wird erstellt, um Textfragmente im PDF zu erkennen und zu verarbeiten.
1. Alle Textinhalte entfernen. Die Methode 'absorber.remove_all_text()' entfernt jedes Textelement aus dem geladenen Dokument, wobei nicht‑textuelle Komponenten unverändert bleiben.
1. Speichern Sie das aktualisierte Dokument.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber1(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document)
        document.save(outfile)
```

### Entfernen Sie allen Text von einer bestimmten Seite

Entfernen Sie den gesamten Text von einer einzelnen Seite eines PDF-Dokuments mithilfe der TextFragmentAbsorber-Klasse in Aspose.PDF.
Im Gegensatz zur vollständigen Dokumentenlöschung führt diese Methode eine Textbereinigung auf Seitenebene durch und löscht den Text nur von der ausgewählten Seite, während alle anderen Seiten unverändert bleiben.

1. Laden Sie die PDF-Datei.
1. Erstellen Sie eine TextFragmentAbsorber-Instanz.
1. Entfernen Sie den gesamten Text von der ersten Seite.
1. Speichern Sie das bearbeitete PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber2(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

### Entfernen Sie allen Text aus einem bestimmten Bereich auf der PDF-Seite

Entfernen Sie allen Text aus einem bestimmten rechteckigen Bereich auf einer Seite mithilfe von Aspose.PDF’s TextFragmentAbsorber.
Anstatt eine ganze Seite zu löschen, führt diese Methode eine gezielte Textentfernung durch, die eine präzise Kontrolle darüber ermöglicht, welcher Teil der Seite betroffen ist.

1. Laden Sie das PDF Document.
1. Erstelle einen TextFragmentAbsorber.
1. Definieren Sie den Zielbereich (Rechteck).
1. Text aus dem angegebenen Bereich entfernen.
1. Den Rest des Dokuments beibehalten.
1. Speichern Sie das bearbeitete PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber3(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(
            document.pages[1], ap.Rectangle(10, 200, 120, 600, True)
        )
        document.save(outfile)
```

### Entfernen Sie allen versteckten Text aus einem PDF-Dokument

Entfernen Sie allen Text aus einem bestimmten rechteckigen Bereich auf einer Seite mithilfe von Aspose.PDF’s TextFragmentAbsorber.
Anstatt eine ganze Seite zu löschen, führt diese Methode eine gezielte Textentfernung durch, die eine präzise Kontrolle darüber ermöglicht, welcher Teil der Seite betroffen ist.

1. Laden Sie das PDF Document.
1. Erstelle einen TextFragmentAbsorber.
1. Definieren Sie den Zielbereich (Rechteck).
1. Text aus dem angegebenen Bereich entfernen.
1. Den Rest des Dokuments beibehalten.
1. Speichern Sie das bearbeitete PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_hidden_text(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(
            ap.text.TextReplaceOptions.ReplaceAdjustment.NONE
        )
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(outfile)
```

## Verwandte Textthemen

- [Arbeiten Sie mit Text in PDF mit Python](/pdf/de/python-net/working-with-text/)
- [Text zum PDF hinzufügen](/pdf/de/python-net/add-text-to-pdf-file/)
- [PDF-Text in Python suchen und extrahieren](/pdf/de/python-net/search-and-get-text-from-pdf/)
- [PDF-Text formatieren in Python](/pdf/de/python-net/text-formatting-inside-pdf/)
