---
title: Seitenzahlen zu PDF in Python hinzufügen
linktitle: Seitenzahl hinzufügen
type: docs
weight: 30
url: /de/python-net/add-page-number/
description: Erfahren Sie, wie Sie Seitenzahlstempel zu PDF-Dokumenten in Python hinzufügen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man mit Python Seitenzahlen zu PDF hinzufügt
Abstract: Dieser Artikel erörtert die Bedeutung des Hinzufügens von Seitenzahlen zu Dokumenten für eine einfachere Navigation und stellt die Aspose.PDF for Python via .NET-Bibliothek als Werkzeug zum Erreichen dessen in PDF-Dateien vor. Die Bibliothek verwendet die Klasse PageNumberStamp, die Eigenschaften zur Anpassung des Seitenzahlstempels bietet, einschließlich Format, Rändern, Ausrichtungen und Startnummer. Der Vorgang beinhaltet das Erstellen eines Document-Objekts und eines PageNumberStamp-Objekts, das Konfigurieren der gewünschten Eigenschaften und das Anwenden des Stempels auf die PDF-Seiten mittels der Methode add_stamp(). Der Artikel liefert ein Python-Codebeispiel, das zeigt, wie Seitenzahlstempel mit anpassbaren Schriftattribute eingerichtet und angewendet werden.
---

Alle Dokumente müssen Seitenzahlen enthalten. Die Seitenzahl erleichtert dem Leser die Auffindung verschiedener Teile des Dokuments.

**Aspose.PDF for Python via .NET** ermöglicht das Hinzufügen von Seitenzahlen mit [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

## Hinzufügen eines PageNumberStamp zu einem PDF

Dynamische Seitenzahlstempel zu einem PDF hinzufügen [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) mit Aspose.PDF for Python. Der [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) Objekt ermöglicht es Ihnen, automatisch die aktuelle Seitenzahl zusammen mit der Gesamtzahl der Seiten anzuzeigen. Das Beispiel zeigt, wie man einen Seitenzahlenstempel erstellt, dessen Aussehen (Schriftart, Größe, Stil, Farbe, Ausrichtung und Ränder) unter Verwendung von [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/), und wenden Sie es auf ein bestimmtes [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) im PDF über die [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) Methode. Ausrichtungswerte stammen aus dem [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) Enum und Farbe/Schriftart/Stil sind verfügbar über [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) und [`FontStyles`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontstyles/) (Schriften entdeckt über [`FontRepository.find_font()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontrepository/#methods)). Diese Funktion ist nützlich, um professionelle, nummerierte Dokumente zu erstellen und die Seitennummerierung in PDF-Workflows zu automatisieren.

1. Öffnen Sie das PDF-Dokument.
1. Erstelle einen Seitenzahlenstempel.
1. Lege Stempel‑Eigenschaften fest.
1. Passe den Textstil an.
1. Wende den Stempel auf eine Seite an.
1. Speichere das bearbeitete PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_num_stamp(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.format = "Page # of " + str(len(document.pages))
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 1
    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    document.pages[1].add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## Römische Seitenzahlen zu einem PDF hinzufügen

Fügen Sie Seitenzahlen im römischen Zahlenformat zu allen Seiten eines PDF-Dokuments hinzu. Die Seitenzahlen werden als Stempel mit Hilfe von [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/), mit anpassbarer Schriftart, Größe, Stil, Farbe und Ausrichtung. Verwenden Sie das [`NumberingStyle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/) enum, um römische Zahlen oder andere Nummerierungsschemata zu wählen. Die Nummerierung kann auch bei einem beliebigen angegebenen Wert beginnen.

1. Öffnen Sie das PDF-Dokument.
1. Erstelle einen Seitenzahlenstempel.
1. Stempel-Eigenschaften konfigurieren.
1. Textaufbau festlegen.
1. Den Stempel auf alle Seiten anwenden.
1. Speichere das bearbeitete PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_num_stamp_roman(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 42
    page_number_stamp.numbering_style = ap.NumberingStyle.NUMERALS_ROMAN_UPPERCASE

    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    for page in document.pages:
        page.add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## Live‑Beispiel

[PDF-Seitenzahlen hinzufügen](https://products.aspose.app/pdf/page-number) ist eine kostenlose Online-Webanwendung, die es Ihnen ermöglicht zu untersuchen, wie die Funktion zum Hinzufügen von Seitenzahlen funktioniert.

[![Wie man Seitenzahlen in PDF mit Python hinzufügt](page_number.png)](https://products.aspose.app/pdf/page-number)

## Verwandte Stempel-Themen

- [PDF-Seiten in Python stempeln](/pdf/de/python-net/stamping/)
- [Seitenstempel zu PDF in Python hinzufügen](/pdf/de/python-net/page-stamps-in-the-pdf-file/)
- [Bildstempel zu PDF in Python hinzufügen](/pdf/de/python-net/image-stamps-in-pdf-page/)
- [Textstempel zu PDF in Python hinzufügen](/pdf/de/python-net/text-stamps-in-the-pdf-file/)