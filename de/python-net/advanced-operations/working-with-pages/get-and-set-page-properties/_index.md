---
title: Abrufen und Festlegen von PDF-Seiteneigenschaften in Python
linktitle: Abrufen und Festlegen von Seiteneigenschaften
type: docs
weight: 90
url: /de/python-net/get-and-set-page-properties/
description: Erfahren Sie, wie Sie PDF‑Seiteneigenschaften wie Größe, Anzahl und Farbinformationen in Python prüfen und aktualisieren können.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man Seiteneigenschaften mit Python abruft und festlegt
Abstract: Dieser Artikel behandelt die Möglichkeiten von Aspose.PDF for Python via .NET und konzentriert sich auf das Lesen und Setzen von Seiteneigenschaften in PDF-Dateien mit Python. Der Artikel deckt verschiedene Funktionalitäten ab, einschließlich der Ermittlung der Seitenanzahl in einem PDF, dem Zugriff auf und der Änderung von Seiteneigenschaften sowie der Handhabung von Farbinformationen. Um die Anzahl der Seiten zu erhalten, werden die `Document`‑Klasse und die `PageCollection`‑Auflistung verwendet, wobei Code‑Snippets zeigen, wie man die Seitenzahl abruft, sogar ohne das Dokument zu speichern. Der Artikel erklärt verschiedene Seiteneigenschaften wie MediaBox, BleedBox, TrimBox, ArtBox und CropBox und liefert Codebeispiele zum Zugriff auf diese Eigenschaften. Zusätzlich wird beschrieben, wie man eine bestimmte Seite aus einem PDF extrahiert und als separates Dokument speichert sowie den Farbtyp jeder Seite ermittelt. Die Beispiele werden durchgehend in Python umgesetzt und veranschaulichen praktische Anwendungsfälle dieser Funktionen.
---

Aspose.PDF for Python via .NET ermöglicht Ihnen das Lesen und Festlegen von Eigenschaften von Seiten in einer PDF-Datei in Ihren Python-Anwendungen. Dieser Abschnitt zeigt, wie Sie die Anzahl der Seiten in einer PDF-Datei ermitteln, Informationen zu PDF-Seiteneigenschaften wie Farbe abrufen und Seiteneigenschaften festlegen. Die Beispiele verwenden die [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) und [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) APIs und sind in Python geschrieben.

Verwenden Sie dieses Handbuch, wenn Sie Seiten-Metadaten untersuchen, Seitenzahlen bestimmen oder seitenbezogene Eigenschaften im Rahmen von Dokumentenanalysen oder Normalisierungsaufgaben aktualisieren müssen.

## Anzahl der Seiten in einer PDF-Datei ermitteln

Beim Arbeiten mit Dokumenten möchte man häufig wissen, wie viele Seiten sie enthalten. Mit Aspose.PDF dauert das nicht mehr als zwei Codezeilen.

Um die Seitenzahl einer PDF-Datei zu erhalten:

1. Öffnen Sie die PDF-Datei mit dem [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Klasse.
1. Verwenden Sie dann die [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) collection's Count property (from the Document object), um die Gesamtanzahl der Seiten im Dokument zu erhalten.

Das folgende Code‑Snippet zeigt, wie man die Anzahl der Seiten einer PDF‑Datei ermittelt.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_count(input_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Get page count
    print("Page Count:", str(len(document.pages)))
```

### Seitenanzahl ohne Speichern des Dokuments ermitteln

Manchmal erzeugen wir PDF-Dateien spontan und während der PDF-Erstellung kann es vorkommen, dass wir die Anforderung (z. B. das Erstellen eines Inhaltsverzeichnisses usw.) haben, die Seitenanzahl einer PDF-Datei zu erhalten, ohne die Datei im System oder Stream zu speichern. Um dieser Anforderung gerecht zu werden, gibt es eine Methode [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) Wurde in der Document‑Klasse eingeführt. Bitte schauen Sie sich das folgende Code‑Snippet an, das die Schritte zum Ermitteln der Seitenzahl ohne das Dokument zu speichern, zeigt.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_count_without_saving(input_file_name):
    # Instantiate Document instance
    document = ap.Document()
    # Add page to pages collection of PDF file
    page = document.pages.add()
    # Create loop instance
    for _ in range(0, 300):
        # Add TextFragment to paragraphs collection of page object
        page.paragraphs.add(ap.text.TextFragment("Pages count test"))
    # Process the paragraphs in PDF file to get accurate page count
    document.process_paragraphs()
    # Print number of pages in document
    print("Number of pages in document =", str(len(document.pages)))
```

## Seiten‑Eigenschaften abrufen

Jede Seite in einer PDF‑Datei hat mehrere Eigenschaften, wie z. B. Breite, Höhe, bleed‑, crop‑ und trimbox. Aspose.PDF ermöglicht den Zugriff auf diese Eigenschaften.

### Verstehen von Seiteneigenschaften: Der Unterschied zwischen Artbox, BleedBox, CropBox, MediaBox, TrimBox und Rect‑Eigenschaft

- **Media box**: Die Media box ist die größte Seitenbox. Sie entspricht der Seitengröße (z. B. A4, A5, US Letter usw.), die beim Drucken des Dokuments in PostScript oder PDF ausgewählt wurde. Mit anderen Worten bestimmt die Media box die physische Größe des Mediums, auf dem das PDF‑Dokument angezeigt oder gedruckt wird.
- **Bleed box**: Wenn das Dokument Beschnitt (bleed) hat, wird die PDF ebenfalls eine Bleed‑Box enthalten. Bleed ist die Menge an Farbe (oder Grafik), die über den Rand einer Seite hinausgeht. Es wird verwendet, um sicherzustellen, dass beim Drucken und Zuschneiden des Dokuments („trimmed“), die Tinte bis zum Rand der Seite reicht. Selbst wenn die Seite falsch zugeschnitten wird – leicht von den Schnittmarken ab – entstehen keine weißen Ränder auf der Seite.
- **Trim box**: Die Trim‑Box gibt die endgültige Größe eines Dokuments nach dem Drucken und Zuschneiden an.
- **Art box**: Die Art‑Box ist die um den eigentlichen Inhalt der Seiten in Ihren Dokumenten gezeichnete Box. Diese Seitenbox wird beim Importieren von PDF‑Dokumenten in andere Anwendungen verwendet.
- **Crop box**: Die Crop-Box ist die „Seite“-Größe, bei der Ihr PDF‑Dokument in Adobe Acrobat angezeigt wird. In der Normalansicht werden nur die Inhalte der Crop‑Box in Adobe Acrobat angezeigt.
  Für detaillierte Beschreibungen dieser Eigenschaften lesen Sie die Adobe.Pdf‑Spezifikation, insbesondere 10.10.1 Seitenbegrenzungen.
-- **Page.Rect**: die Schnittmenge (gewöhnlich sichtbares Rechteck) von MediaBox und DropBox (`Page.rect`). Siehe die [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) Typ für Rechteckeigenschaften. Das Bild unten veranschaulicht diese Eigenschaften.

Für weitere Details besuchen Sie bitte [diese Seite](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Zugriff auf Seiteneigenschaften

Der [Seite](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) Klasse stellt alle Eigenschaften bereit, die sich auf eine bestimmte PDF-Seite beziehen. Alle Seiten der PDF-Dateien sind im ... des [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objekts [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) Sammlung.

Von dort aus ist es möglich, auf einzelne zuzugreifen `Page` Objekte mithilfe ihres Indexes oder indem man die Sammlung durchläuft, um alle Seiten zu erhalten. Sobald eine einzelne Seite aufgerufen wird, können wir ihre Eigenschaften abrufen. Das folgende Code‑Snippet zeigt, wie man Seiten­eigenschaften (die `Page` API).

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_properties(input_file_name):
    # Open document
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Get page properties
    boxes = {
        "ArtBox": page.art_box,
        "BleedBox": page.bleed_box,
        "CropBox": page.crop_box,
        "MediaBox": page.media_box,
        "TrimBox": page.trim_box,
        "Rect": page.rect,
    }

    # Print box properties
    for box_name, box in boxes.items():
        print(
            f"{box_name} : Height={box.height},Width={box.width},LLX={box.llx},LLY={box.lly},URX={box.urx},URY={box.ury}"
        )

    # Print other page properties
    print(f"Page Number : {page.number}")
    print(f"Rotate : {page.rotate}")
```

## Seitenfarbe bestimmen

Der [Seite](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) Die Klasse stellt die Eigenschaften bereit, die sich auf eine bestimmte Seite in einem PDF-Dokument beziehen, einschließlich des Farbtyps – RGB, Schwarzweiß, Graustufen oder undefiniert – den die Seite verwendet.

Alle Seiten der PDF-Dateien sind enthalten von dem [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) Sammlung. Die [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) Die Eigenschaft gibt die Farbe der Elemente auf der Seite an. Um die Farbinformation für eine bestimmte PDF-Seite abzurufen oder zu bestimmen, verwenden Sie die [Seite](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) objekts [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) Eigenschaft.

Das folgende Code-Snippet zeigt, wie man einzelne Seiten einer PDF-Datei durchläuft, um Farbinformationen zu erhalten.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_color_type(input_file_name):
    # Open source PDF file
    document = ap.Document(input_file_name)
    # Iterate through all the page of PDF file
    for page_number in range(1, len(document.pages) + 1):
        # Get the color type information for particular PDF page
        page_color_type = document.pages[page_number].color_type
        color_type_map = {
            ap.ColorType.BLACK_AND_WHITE: "Black and white",
            ap.ColorType.GRAYSCALE: "Gray Scale",
            ap.ColorType.RGB: "RGB",
            ap.ColorType.UNDEFINED: "undefined",
        }
        color_description = color_type_map.get(page_color_type, "unknown")
        print(f"Page # {page_number} is {color_description}.")
```

## Verwandte Seitenthemen

- [Arbeiten Sie mit PDF-Seiten in Python](/pdf/de/python-net/working-with-pages/)
- [PDF-Seitengröße in Python ändern](/pdf/de/python-net/change-page-size/)
- [PDF‑Seiten in Python zuschneiden](/pdf/de/python-net/crop-pages/)
- [PDF‑Seiten in Python drehen](/pdf/de/python-net/rotate-pages/)