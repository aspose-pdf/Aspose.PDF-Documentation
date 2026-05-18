---
title: Bild zu PDF mit Python hinzufügen
linktitle: Bild hinzufügen
type: docs
weight: 10
url: /de/python-net/add-image-to-existing-pdf-file/
description: Erfahren Sie, wie Sie Bilder zu vorhandenen PDF-Dateien in Python hinzufügen.
lastmod: "2026-05-18"
TechArticle: true
AlternativeHeadline: Bilder zu bestehenden PDF-Dateien mit Python hinzufügen
Abstract: Dieser Artikel zeigt, wie man mit Aspose.PDF for Python via .NET Bilder zu PDF-Dokumenten hinzufügt. Er behandelt das Hinzufügen eines Bildes bei festen Koordinaten, das Platzieren von Bildern mit Low-Level-Operatoren, das Zuweisen von Alternativtext für Barrierefreiheit und das Einbetten von Bildern mit Flate‑Kompression.
---

## Bild in einer bestehenden PDF-Datei hinzufügen

Dieses Beispiel zeigt, wie man mit Aspose.PDF for Python via .NET ein Bild an einer festen Position auf einer bestehenden PDF‑Seite platziert.

Verwenden Sie diese Beispiele von dieser Seite, wenn Sie Logos, Fotos oder andere Grafiken bei festen Koordinaten in einem bestehenden PDF‑Layout platzieren müssen.

1. Laden Sie ein vorhandenes PDF mit `ap.Document(infile)`.
1. Wählen Sie die Zielseite (`document.pages[1]` für die erste Seite).
1. Anruf `page.add_image()` mit:
    - Der Pfad zur Bilddatei.
    - A `Rectangle` Festlegen von Platzierungskoordinaten.
1. Speichere das aktualisierte PDF.

```python
import aspose.pdf as ap


def add_image(infile, image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))
    document.save(outfile)
```

## Ein Bild mit Operatoren hinzufügen

Dieser Ansatz fügt ein Bild mit Low-Level-PDF-Operatoren anstelle von High-Level-Operatoren hinzu. `add_image()` Helfer.

1. Neu erstellen `Document` und füge eine Seite hinzu.
1. Füge das Bild zu den Seitenressourcen hinzu (`page.resources.images`).
1. Erstelle Transformationsoperatoren (`GSave`, `ConcatenateMatrix`, `Do`, `GRestore`).
1. Fügen Sie Operatoren zu den Seiteninhalten hinzu.
1. Speichern Sie das resultierende PDF.

```python
import aspose.pdf as ap
from io import FileIO


def add_image_using_operators(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream)

    rectangle = ap.Rectangle(0, 0, page.media_box.width, page.media_box.height, True)

    operators = [
        ap.operators.GSave(),
        ap.operators.ConcatenateMatrix(
            ap.Matrix(
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            )
        ),
        ap.operators.Do(image_id),
        ap.operators.GRestore(),
    ]

    page.contents.add(operators)
    document.save(outfile)
```

## Bild mit Alternativtext hinzufügen

Dieses Beispiel fügt ein Bild hinzu und weist einen Alternativtext zur Barrierefreiheit zu.

1. Neu erstellen `Document` und füge eine Seite hinzu.
1. Fügen Sie das Bild zur Seite hinzu `page.add_image()`.
1. Bildressourcen abrufen von `page.resources.images`.
1. Alt-Text festlegen mit `try_set_alternative_text()`.
1. Speichern Sie das resultierende PDF.

```python
import aspose.pdf as ap


def add_image_set_alternative_text(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)

    page.add_image(image_file, ap.Rectangle(0, 0, 842, 595, True))
    resources_images = page.resources.images
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text("Alternative text for image", page)

    if result:
        print("Alternative text has been added successfully")

    document.save(outfile)
```

## Fügen Sie ein Bild zu einem PDF mit Flate-Kompression hinzu

Dieses Beispiel bettet ein Bild ein `ImageFilterType.FLATE` Kompression.

1. Neu erstellen `Document` und füge eine Seite hinzu.
1. Fügen Sie das Bild zu den Seitenressourcen mit Flate-Kompression hinzu.
1. Verwenden Sie Matrixoperatoren, um das Bild zu platzieren und zu zeichnen.
1. Speichern Sie das Dokument.

```python
import aspose.pdf as ap
from io import FileIO


def add_image_to_pdf_with_flate_compression(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream, ap.ImageFilterType.FLATE)

    rectangle = ap.Rectangle(0, 0, 600, 600, True)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.lly,
    )

    page.contents.add([ap.operators.GSave()])
    page.contents.add([ap.operators.ConcatenateMatrix(matrix)])
    page.contents.add([ap.operators.Do(image_id)])
    page.contents.add([ap.operators.GRestore()])

    document.save(outfile)
```

## Verwandte Bildthemen

- [Arbeiten mit Bildern in PDF mit Python](/pdf/de/python-net/working-with-images/)
- [Bilder in vorhandenen PDF-Dateien ersetzen](/pdf/de/python-net/replace-image-in-existing-pdf-file/)
- [Bilder aus PDF-Dateien löschen](/pdf/de/python-net/delete-images-from-pdf-file/)
- [Bilder aus PDF-Dateien extrahieren](/pdf/de/python-net/extract-images-from-pdf-file/)
