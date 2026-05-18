---
title: PDF-Dokumente in Python formatieren
linktitle: PDF-Dokument formatieren
type: docs
weight: 11
url: /de/python-net/formatting-pdf-document/
description: Erfahren Sie, wie Sie PDF-Dokumente formatieren, Schriftarten einbetten, Viewer‑Einstellungen steuern und Anzeigeoptionen in Python anpassen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Dokumente mit Python formatieren
Abstract: Der Artikel bietet eine umfassende Anleitung zum Manipulieren und Formatieren von PDF‑Dokumenten mit der Aspose.PDF‑Bibliothek in Python. Er behandelt verschiedene Aspekte der PDF‑Anpassung, einschließlich der Festlegung von Dokumenten‑Fenster‑ und Seitenanzeige­eigenschaften wie dem Zentrieren des Fensters, der Lesrichtung und dem Ausblenden von UI‑Elementen. Der Artikel erklärt, wie man diese Eigenschaften programmgesteuert mit der `Document`‑Klasse abruft und festlegt. Zusätzlich behandelt er das Font‑Management und beschreibt, wie Standard‑Type‑1‑Fonts und andere Fonts in PDFs eingebettet werden können, um die Portabilität des Dokuments und die visuelle Konsistenz über Systeme hinweg sicherzustellen. Er hebt außerdem Techniken hervor, um einen Standard‑Font‑Namen festzulegen, alle Fonts aus einem PDF abzurufen und das Einbetten von Fonts mithilfe von `FontSubsetStrategy` zu optimieren. Weitergehend erläutert der Artikel die Anpassung des Zoom‑Faktors von PDF‑Dokumenten mit der `GoToAction`‑Klasse und die Konfiguration von Druckdialog‑Voreinstellungen, einschließlich Duplex‑Druckoptionen. Code‑Snippets begleiten jeden Abschnitt und liefern praktische Beispiele zur Implementierung dieser Funktionen.
---

Dieses Handbuch ist nützlich, wenn Sie das Verhalten des PDF-Viewers, das Einbetten von Schriftarten, die Standard-Anzeigeneinstellungen oder die Druckeinstellungen in mit Python erstellten Dokumenten steuern müssen.

## PDF-Dokument formatieren

### Dokumentfenster- und Seitenanzeigeeigenschaften abrufen

Dieses Thema hilft Ihnen zu verstehen, wie Sie Eigenschaften des Dokumentfensters, der Viewer-Anwendung und der Anzeige von Seiten abrufen. Um diese Eigenschaften festzulegen:

Öffnen Sie die PDF-Datei mit dem [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Klasse. Jetzt können Sie die Eigenschaften des Document-Objekts festlegen, wie zum Beispiel

- CenterWindow – Zentriert das Dokumentenfenster auf dem Bildschirm. Standard: false.
- Richtung – Lesereihenfolge. Dies bestimmt, wie Seiten angeordnet werden, wenn sie nebeneinander angezeigt werden. Standard: von links nach rechts.
- DisplayDocTitle – Zeigt den Dokumenttitel in der Titelleiste des Dokumentfensters an. Standard: false (der Titel wird angezeigt).
- HideMenuBar – Ausblenden oder Anzeigen der Menüleiste des Dokumentfensters. Standard: false (Menüleiste wird angezeigt).
- HideToolBar – Ausblenden oder Anzeigen der Symbolleiste des Dokumentfensters. Standard: false (Symbolleiste wird angezeigt).
- HideWindowUI – Versteckt oder zeigt Dokumentfenster-Elemente wie Bildlaufleisten an. Standard: false (UI-Elemente werden angezeigt).
- NonFullScreenPageMode – Wie das Dokument angezeigt wird, wenn es nicht im Vollbildmodus dargestellt wird.
- PageLayout – Das Seitenlayout.
- PageMode – Wie das Dokument beim ersten Öffnen angezeigt wird. Die Optionen sind Miniaturansichten anzeigen, Vollbild, Anlagen-Panel anzeigen.

Das folgende Code‑Snippet zeigt Ihnen, wie Sie die Eigenschaften mithilfe von erhalten [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Klasse.

```python
import aspose.pdf as ap


def get_document_window(input_pdf, output_pdf):
    """Print document window metadata for inspection."""
    document = ap.Document(input_pdf)

    print("CenterWindow:", document.center_window)
    print("Direction:", document.direction)
    print("DisplayDocTitle:", document.display_doc_title)
    print("FitWindow:", document.fit_window)
    print("HideMenuBar:", document.hide_menubar)
    print("HideToolBar:", document.hide_tool_bar)
    print("HideWindowUI:", document.hide_window_ui)
    print("NonFullScreenPageMode:", document.non_full_screen_page_mode)
    print("PageLayout:", document.page_layout)
    print("PageMode:", document.page_mode)
```

### Dokumentenfenster- und Seitenanzeigeeigenschaften festlegen

Dieses Thema erklärt, wie die Eigenschaften des Dokumentfensters, der Viewer-Anwendung und der Seitenanzeige festgelegt werden. Um diese verschiedenen Eigenschaften festzulegen:

1. Öffnen Sie die PDF-Datei mit dem [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Klasse.
1. Setzen Sie die Eigenschaften des Document-Objekts.
1. Speichern Sie die aktualisierte PDF-Datei mit der Save-Methode.

Verfügbare Eigenschaften sind:

- Fenster zentrieren
- Richtung
- Dokumenttitel anzeigen
- Fenster anpassen
- Menüleiste ausblenden
- Symbolleiste ausblenden
- Fenster‑UI ausblenden
- NichtVollbildSeitenmodus
- Seitenlayout
- Seitenmodus

Jeder wird verwendet und im nachstehenden Code beschrieben. Der folgende - Codeausschnitt zeigt dir, wie du die Eigenschaften mit dem [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Klasse.

```python
import aspose.pdf as ap


def set_document_window(input_pdf, output_pdf):
    """Set document window properties and save the result."""
    document = ap.Document(input_pdf)

    document.center_window = True
    document.direction = ap.Direction.R2L
    document.display_doc_title = True
    document.fit_window = True
    document.hide_menubar = True
    document.hide_tool_bar = True
    document.hide_window_ui = True
    document.non_full_screen_page_mode = ap.PageMode.USE_OC
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT
    document.page_mode = ap.PageMode.USE_THUMBS

    document.save(output_pdf)
```

### Einbetten von Standard‑Type‑1‑Schriften

Einige PDF-Dokumente enthalten Schriftarten aus einem speziellen Adobe-Schriftarten-Set. Schriftarten aus diesem Set werden “Standard Type 1 Fonts” genannt. Dieses Set umfasst 14 Schriftarten, und das Einbetten dieser Art von Schriftarten erfordert die Verwendung spezieller Flags, d. h. [Standard‑Schriften einbetten](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). Folgendes ist das Code‑Snippet, das verwendet werden kann, um ein Dokument mit allen eingebetteten Schriften zu erhalten, einschließlich Standard‑Typ‑1‑Schriften:

```python
import aspose.pdf as ap


def embedded_fonts(input_pdf, output_pdf):
    """Ensure fonts in an existing PDF are embedded."""
    document = ap.Document(input_pdf)
    document.embed_standard_fonts = True

    for page in document.pages:
        if page.resources.fonts:
            for page_font in page.resources.fonts:
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### Einbetten von Schriftarten beim Erstellen von PDF

Wenn Sie eine andere Schriftart als die von Adobe Reader unterstützten 14 Kernschriftarten verwenden müssen, müssen Sie die Schriftartbeschreibung beim Erzeugen der PDF-Datei einbetten. Wenn Schriftinformationen nicht eingebettet sind, übernimmt Adobe Reader sie vom Betriebssystem, sofern sie dort installiert ist, oder es erzeugt eine Ersatzschriftart gemäß dem Schriftartdescriptor im PDF.

>Bitte beachten Sie, dass die eingebettete Schriftart auf dem Host‑Computer installiert sein muss, d. h. im Falle des folgenden Codes ist die Schriftart ‘Univers Condensed’ über das System installiert.

Wir verwenden die Eigenschaft 'is_embedded', um die Schriftinformationen in die PDF-Datei einzubetten. Das Setzen des Wertes dieser Eigenschaft auf 'True' bettet die vollständige Schriftdatei in das PDF ein, wobei bekannt ist, dass dies die PDF-Dateigröße erhöht. Im Folgenden finden Sie den Codeausschnitt, der verwendet werden kann, um die Schriftinformationen in das PDF einzubetten.

```python
import aspose.pdf as ap


def embedded_fonts_in_new_document(input_pdf, output_pdf):
    """Embed fonts while generating a document from scratch."""
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    text_state = ap.text.TextState()
    text_state.font = ap.text.FontRepository.find_font("Arial")
    text_state.font.is_embedded = True
    segment.text_state = text_state
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    document.save(output_pdf)
```

### Standard‑Schriftartnamen beim Speichern von PDF festlegen

Wenn ein PDF‑Dokument Schriften enthält, die im Dokument selbst und auf dem Gerät nicht verfügbar sind, ersetzt die API diese Schriften durch die Standardschrift. Ist die Schrift verfügbar (auf dem Gerät installiert oder im Dokument eingebettet), sollte das ausgegebene PDF dieselbe Schrift haben (sie sollte nicht durch die Standardschrift ersetzt werden). Der Wert der Standardschrift sollte den Namen der Schrift enthalten (nicht den Pfad zu den Schriftdateien). Wir haben eine Funktion implementiert, mit der der Standardschriftname beim Speichern eines Dokuments als PDF festgelegt werden kann. Der folgende Code‑Abschnitt kann verwendet werden, um die Standardschrift festzulegen:

```python
import aspose.pdf as ap


def set_default_font(input_pdf, output_pdf):
    """Assign a fallback font when saving a PDF."""
    document = ap.Document(input_pdf)

    save_options = ap.PdfSaveOptions()
    save_options.default_font_name = "Arial"
    document.save(output_pdf, save_options)
```

### Alle Fonts aus PDF-Dokument abrufen

Falls Sie alle Schriften aus einem PDF-Dokument abrufen möchten, können Sie verwenden [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) Methode bereitgestellt in [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Klasse. Bitte prüfen Sie den folgenden Codeabschnitt, um alle Schriften aus einem bestehenden PDF-Dokument zu erhalten:

```python
import aspose.pdf as ap


def get_all_fonts(input_pdf, output_pdf):
    """Print all fonts referenced by a document."""
    document = ap.Document(input_pdf)
    for font in document.font_utilities.get_all_fonts():
        print(font.font_name)
```

### Verbessern Sie die Schriftarteinbettung mit FontSubsetStrategy

Der folgende Codeausschnitt zeigt, wie man setzt [FontSubsetStrategie](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) verwendet [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) Eigenschaft:

```python
import aspose.pdf as ap


def improve_fonts_embedding(input_pdf, output_pdf):
    """Apply different font subset strategies to reduce file size."""
    document = ap.Document(input_pdf)

    document.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    document.font_utilities.subset_fonts(
        ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY
    )

    document.save(output_pdf)
```

### Zoom-Faktor der PDF-Datei abrufen und setzen

Manchmal möchte man bestimmen, welcher aktuelle Zoomfaktor eines PDF-Dokuments vorliegt. Mit Aspose.Pdf kann man den aktuellen Wert herausfinden und auch einen festlegen.

Der [GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) Die Klassen‑Eigenschaft Destination ermöglicht es Ihnen, den Zoomwert einer PDF‑Datei abzurufen. Ebenso kann sie verwendet werden, um den Zoomfaktor einer Datei festzulegen.

#### Zoomfaktor festlegen

Der folgende Codeausschnitt zeigt, wie man den Zoomfaktor einer PDF-Datei einstellt.

```python
import aspose.pdf as ap


def set_zoom_factor(input_pdf, output_pdf):
    """Set an initial zoom level via document open action."""
    document = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(
        ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5)
    )
    document.open_action = action
    document.save(output_pdf)
```

#### Zoomfaktor abrufen

Der folgende Codeabschnitt zeigt, wie man den Zoomfaktor einer PDF-Datei ermittelt.

```python
import aspose.pdf as ap


def get_zoom_factor(input_pdf, output_pdf):
    """Print the zoom level configured in the document open action."""
    document = ap.Document(input_pdf)

    action = document.open_action
    if action and action.destination:
        print("Zoom:", action.destination.zoom)
    else:
        print("Zoom: not set")
```

## Verwandte Dokumentthemen

- [Arbeiten mit PDF-Dokumenten in Python](/pdf/de/python-net/working-with-documents/)
- [Erstelle PDF-Dateien in Python](/pdf/de/python-net/create-pdf-document/)
- [PDF‑Dokumente in Python manipulieren](/pdf/de/python-net/manipulate-pdf-document/)
- [PDF‑Dateien in Python optimieren](/pdf/de/python-net/optimize-pdf/)
