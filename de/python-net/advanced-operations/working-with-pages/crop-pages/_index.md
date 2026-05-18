---
title: PDF-Seiten in Python zuschneiden
linktitle: Zuschneiden von PDF-Seiten
type: docs
weight: 70
url: /de/python-net/crop-pages/
description: Erfahren Sie, wie Sie PDF-Seiten zuschneiden und die Crop‑, Trim‑, Bleed‑ und Media‑Boxen in Python anpassen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man Seiten‑Eigenschaften in PDF mit Python abruft und ändert
Abstract: Der Artikel gibt einen Überblick darüber, wie man Seiten‑Eigenschaften in einem PDF‑Dokument mit Aspose.PDF for Python abruft und ändert. Er beschreibt mehrere Seiten‑Eigenschaften, darunter die media box, bleed box, trim box, art box und crop box, und erklärt deren Rolle bei der Definition der Abmessungen und Grenzen einer PDF‑Seite für Druck‑ und Anzeigezwecke. Die media box stellt die größte Seitengröße dar, während die bleed box sicherstellt, dass die Tinte über den Seitenrand hinausgeht, um das Beschneiden zu ermöglichen. Die trim box markiert die endgültige Dokumentgröße nach dem Beschneiden, und die art box umschließt den eigentlichen Seiteninhalt. Die crop box definiert den sichtbaren Bereich in Adobe Acrobat. Der Artikel enthält ein Python‑Code‑Snippet, das demonstriert, wie man für eine bestimmte Seite in einem PDF‑Dokument eine neue crop box sowie weitere Boxen festlegt. Visuelle Beispiele zeigen das Aussehen der Seite vor und nach dem Anwenden des Zuschnitts und veranschaulichen die praktische Anwendung der Änderung dieser Eigenschaften.
---

## Seiten‑Eigenschaften abrufen

Jede Seite in einer PDF-Datei hat eine Reihe von Eigenschaften, wie Breite, Höhe, bleed-, crop- und trimbox. Aspose.PDF for Python ermöglicht den Zugriff auf diese Eigenschaften.

Verwenden Sie diese Seite, wenn Sie den sichtbaren Seitenbereich reduzieren, Dateien für Druck-Workflows vorbereiten oder die Geometrie der Seitenkästen in PDF-Dokumenten prüfen müssen.

- **media_box**: Die Media-Box ist die größte Seitenbox. Sie entspricht der Seitengröße (z. B. A4, A5, US Letter usw.), die ausgewählt wurde, als das Dokument zu PostScript oder PDF gedruckt wurde. Mit anderen Worten bestimmt die Media-Box die physische Größe des Mediums, auf dem das PDF‑Dokument angezeigt oder gedruckt wird.
- **bleed_box**: Wenn das Dokument Bleed hat, enthält das PDF ebenfalls eine Bleed-Box. Bleed ist die Menge an Farbe (oder Grafik), die über den Rand einer Seite hinausgeht. Sie wird verwendet, um sicherzustellen, dass beim Drucken und Zuschneiden des Dokuments (\u0022trimmed\u0022) die Tinte bis zum Seitenrand reicht. Selbst wenn die Seite fehlerhaft zugeschnitten wird – leicht von den Schnittmarken abgezogen – erscheinen keine weißen Ränder auf der Seite.
- **trim_box**: Die Trim-Box gibt die endgültige Größe eines Dokuments nach dem Drucken und Zuschneiden an.
- **art_box**: Die Art-Box ist das Rechteck, das um den tatsächlichen Inhalt der Seiten in Ihren Dokumenten gezeichnet wird. Diese Seitenbox wird verwendet, wenn PDF-Dokumente in andere Anwendungen importiert werden.
- **crop_box**: Die Crop-Box ist die "Seiten"-Größe, in der Ihr PDF-Dokument in Adobe Acrobat angezeigt wird. In der Normalansicht werden nur die Inhalte der Crop-Box in Adobe Acrobat angezeigt. Für detaillierte Beschreibungen dieser Eigenschaften lesen Sie die Adobe.Pdf-Spezifikation, insbesondere 10.10.1 Page Boundaries.

Beschneiden Sie das erste [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) eines PDF zu einem bestimmten rechteckigen Bereich unter Verwendung von Aspose.PDF for Python. Die Funktion passt mehrere Page-Boxen an—`crop_box`, `trim_box`, `art_box`, und `bleed_box`—um konsistente visuelle Ergebnisse zu gewährleisten. Zuschneiden kann nützlich sein, um unerwünschte Ränder zu entfernen oder sich auf einen bestimmten Bereich einer Seite zu konzentrieren.

1. Lade das PDF als [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (verwenden `ap.Document()`).
1. Definieren Sie das Beschneidungs‑Rechteck mit [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) mit den gewünschten Koordinaten (in Punkten).
1. Setze das [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)'s `crop_box`, `trim_box`, `art_box`, und `bleed_box` zum definierten Rechteck.
1. Speichern Sie das modifizierte [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) zu einer neuen Ausgabedatei.

```python
import sys
import aspose.pdf as ap
from os import path

def crop_page(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_file_name)
```

In diesem Beispiel haben wir eine Beispieldatei verwendet [hier](crop_page.pdf). Zunächst sieht unsere Seite wie in Abbildung 1 gezeigt aus.
![Abbildung 1. Beschnittene Seite](crop_page.png)

Nach der Änderung sieht die Seite wie Abbildung 2 aus.
![Abbildung 2. Beschnittene Seite](crop_page2.png)

## PDF‑Seite basierend auf dem Inhalt des ersten Bildes zuschneiden

Beschneiden Sie das erste [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) dynamisch basierend auf den Grenzen des ersten auf der Seite gefundenen Bildes. Durch die Verwendung [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/), das Skript identifiziert das erste Bild und passt die Seite an `crop_box` um die Abmessungen des Bildes anzupassen. Dieser Ansatz ist nützlich, wenn Sie sich auf spezifische visuelle Inhalte konzentrieren möchten, anstatt vordefinierte Koordinaten zu verwenden.

1. Lade das PDF als [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Bilder auf der ersten Seite finden mit [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/).
1. Überprüfen, ob Bilder vorhanden sind:
    - Wenn gefunden, setze das [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) `crop_box` um dem ersten Bild zu entsprechen [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
    - Wenn nicht, belassen Sie die Seite unverändert und benachrichtigen Sie den Benutzer.
1. Speichern Sie das modifizierte [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) zur angegebenen Ausgabedatei.

```python
import sys
import aspose.pdf as ap
from os import path

def crop_page_by_content(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Find first image on first page using ImagePlacementAbsorber
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        first_image = absorber.image_placements[1]
        document.pages[1].crop_box = first_image.rectangle
    else:
        print("No images found on the first page")
    document.save(output_file_name)
```

## Verwandte Seitenthemen

- [Arbeiten Sie mit PDF-Seiten in Python](/pdf/de/python-net/working-with-pages/)
- [PDF-Seitengröße in Python ändern](/pdf/de/python-net/change-page-size/)
- [PDF‑Seiteneigenschaften in Python abrufen und festlegen](/pdf/de/python-net/get-and-set-page-properties/)
- [PDF‑Seiten in Python drehen](/pdf/de/python-net/rotate-pages/)