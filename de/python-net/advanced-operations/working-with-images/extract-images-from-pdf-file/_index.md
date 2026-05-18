---
title: Bilder aus PDF-Datei mit Python extrahieren
linktitle: Bilder extrahieren
type: docs
weight: 30
url: /de/python-net/extract-images-from-pdf-file/
description: Erfahren Sie, wie Sie eingebettete Bilder aus PDF-Dateien mit Python extrahieren.
lastmod: "2026-05-18"
TechArticle: true
AlternativeHeadline: Bilder aus PDF-Dateien mit Python extrahieren
Abstract: Dieser Artikel zeigt, wie man Bilder aus PDF-Dokumenten mit Aspose.PDF for Python via .NET extrahiert. Er behandelt das Extrahieren eines einzelnen eingebetteten Bildes und den Export von Bildern, die sich in einem bestimmten rechteckigen Bereich auf einer Seite befinden.
---

Verwenden Sie diese Seite, wenn Sie eingebettete Grafiken wiederverwenden, Bildressourcen archivieren oder Bildinhalte außerhalb des PDFs verarbeiten müssen.

1. Laden Sie das Quell-PDF mit `ap.Document(infile)`.
1. Wählen Sie die Zielseite und den Bildressourcen-Index aus.
1. Speichern Sie das Bildobjekt in einen Ausgabestream.

```python
import aspose.pdf as ap
from io import FileIO


def extract_image(infile, outfile):
    document = ap.Document(infile)
    x_image = document.pages[1].resources.images[1]
    with FileIO(outfile, "wb") as output_image:
        x_image.save(output_image)
```

## Bilder aus einem bestimmten Bereich in PDF extrahieren

Dieses Beispiel extrahiert Bilder, die sich innerhalb eines angegebenen rechteckigen Bereichs auf einer PDF‑Seite befinden, und speichert sie als separate Dateien.

1. Laden Sie das Quell‑PDF.
1. Erstellen `ImagePlacementAbsorber` und akzeptiere es auf der Zielseite.
1. Definieren Sie das Zielrechteck.
1. Iterieren Sie über die Bildplatzierungen und prüfen Sie, ob die Begrenzungen jedes Bildes in den Bereich passen.
1. Speichern Sie passende Bilder in Ausgabedateien.

```python
import aspose.pdf as ap
from io import FileIO


def extract_image_from_specific_region(infile, outfile):
    document = ap.Document(infile)
    rectangle = ap.Rectangle(0, 0, 590, 590, True)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(image_placement.rectangle.llx, image_placement.rectangle.lly)
        point2 = ap.Point(image_placement.rectangle.urx, image_placement.rectangle.ury)

        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(outfile.replace("index", str(index)), "wb") as output_image:
                image_placement.image.save(output_image)
            index += 1
```

## Verwandte Bildthemen

- [Arbeiten mit Bildern in PDF mit Python](/pdf/de/python-net/working-with-images/)
- [Bilder in vorhandenen PDF-Dateien ersetzen](/pdf/de/python-net/replace-image-in-existing-pdf-file/)
- [Bilder aus PDF-Dateien löschen](/pdf/de/python-net/delete-images-from-pdf-file/)
- [Bilder zu bestehenden PDF-Dateien hinzufügen](/pdf/de/python-net/add-image-to-existing-pdf-file/)
