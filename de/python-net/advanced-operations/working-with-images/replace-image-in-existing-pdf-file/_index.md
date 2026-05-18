---
title: Bild in vorhandener PDF-Datei mit Python ersetzen
linktitle: Bild ersetzen
type: docs
weight: 70
url: /de/python-net/replace-image-in-existing-pdf-file/
description: Erfahren Sie, wie Sie eingebettete Bilder in vorhandenen PDF-Dateien mit Python ersetzen.
lastmod: "2026-05-18"
TechArticle: true
AlternativeHeadline: Bilder in vorhandenen PDF-Dateien mit Python ersetzen
Abstract: Dieser Artikel zeigt, wie man Bilder in PDF-Dokumenten mit Aspose.PDF for Python via .NET ersetzt. Er behandelt das Ersetzen eines Bildes über den Ressourcen‑Index sowie das Ersetzen eines bestimmten gefundenen Bildes mit ImagePlacementAbsorber.
---

## Ein Bild in PDF ersetzen

Verwenden Sie diese Seite, wenn Sie Logos, Diagramme oder andere eingebettete Grafiken in einem PDF aktualisieren müssen, ohne das Dokumentlayout neu zu erstellen.

1. Laden Sie das Quell-PDF mit `ap.Document(infile)`.
1. Öffnen Sie das Ersatzbild als binären Stream.
1. Ersetzen Sie eine Bildressource anhand des Index auf einer Seite.
1. Speichere das aktualisierte PDF.

```python
import aspose.pdf as ap
from io import FileIO


def replace_image(infile, image_file, outfile):
    document = ap.Document(infile)

    with FileIO(image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(outfile)
```

## Ein bestimmtes Bild ersetzen.

Dieses Beispiel ersetzt eine bestimmte Bildplatzierung, die gefunden wurde von `ImagePlacementAbsorber`.

1. Laden Sie das Quell‑PDF.
1. Erstellen `ImagePlacementAbsorber` und sammle Bildplatzierungen auf der Seite.
1. Überprüfe, ob Bildplatzierungen auf der Seite existieren.
1. Ersetze die ausgewählte Platzierung durch einen neuen Bild-Stream.
1. Speichere das aktualisierte PDF.

```python
import aspose.pdf as ap
from io import FileIO


def replace_image_with_absorber(infile, image_file, outfile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(outfile)
```

## Verwandte Bildthemen

- [Arbeiten mit Bildern in PDF mit Python](/pdf/de/python-net/working-with-images/)
- [Bilder aus PDF-Dateien löschen](/pdf/de/python-net/delete-images-from-pdf-file/)
- [Bilder aus PDF-Dateien extrahieren](/pdf/de/python-net/extract-images-from-pdf-file/)
- [Bilder zu bestehenden PDF-Dateien hinzufügen](/pdf/de/python-net/add-image-to-existing-pdf-file/)
