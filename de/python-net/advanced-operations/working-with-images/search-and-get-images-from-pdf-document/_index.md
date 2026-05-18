---
title: Bilder in PDF abrufen und suchen
linktitle: Bilder abrufen und suchen
type: docs
weight: 40
url: /de/python-net/search-and-get-images-from-pdf-document/
description: Erfahren Sie, wie Sie in Python nach Bildern in PDF-Dokumenten suchen und diese untersuchen.
lastmod: "2026-05-18"
TechArticle: true
AlternativeHeadline: Suchen und untersuchen Sie Bilder in PDF-Dateien mit Python
Abstract: Dieser Artikel zeigt, wie man nach Bildern in PDF-Dokumenten sucht und diese mit Aspose.PDF for Python via .NET inspiziert. Er behandelt die Verwendung von ImagePlacementAbsorber, um die Bildplatzierung, Größe, Auflösung und den Alternativtext zu analysieren.
---

## Bildplatzierungseigenschaften in einer PDF-Seite prüfen

Dieses Beispiel demonstriert, wie man die Eigenschaften aller Bilder auf einer bestimmten PDF-Seite mithilfe von Aspose.PDF for Python via .NET analysiert und anzeigt.

Verwenden Sie diese Seite, wenn Sie die Bildplatzierung prüfen, die Bildauflösung inspizieren oder eingebettete Bildobjekte über PDF-Seiten hinweg identifizieren müssen.

1. Erstelle einen 'ImagePlacementAbsorber', um alle Bilder auf der Seite zu sammeln.
1. Rufe 'document.pages[1].accept(absorber)' auf, um die Bildplatzierungen auf der ersten Seite zu analysieren.
1. Iteriere durch 'absorber.image_placements' und zeige die wichtigsten Eigenschaften jedes Bildes an:
    - Breite und Höhe (Punkte).
    - Untere linke X (LLX) und untere linke Y (LLY) Koordinaten.
    - Horizontale (X) und vertikale (Y) Auflösung (DPI).

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_params(infile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))
```

## Extrahieren und Zählen von Bildtypen in einer PDF

Diese Funktion analysiert alle Bilder auf der ersten Seite einer PDF und zählt, wie viele Graustufen- und RGB-Bilder vorhanden sind.

1. Erstelle einen 'ImagePlacementAbsorber', um alle Bilder auf der Seite zu sammeln.
1. Initialisieren Sie Zähler für Graustufen- und RGB-Bilder.
1. Rufen Sie 'document.pages[1].accept(absorber)' auf, um Bildplatzierungen zu analysieren.
1. Geben Sie die Gesamtzahl der gefundenen Bilder aus.
1. Iterieren Sie über jedes Bild in 'absorber.image_placements':
    - Ermitteln Sie den Bildfarbtyp mit 'image_placement.image.get_color_type()'.
    - Erhöhen Sie den entsprechenden Zähler (grayscaled oder rgb).
    - Drucken Sie für jedes Bild eine Meldung, die angibt, ob es Graustufen- oder RGB ist.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_types_from_pdf(infile):
    """
    Extract and count image types (grayscale/RGB) with resolution analysis.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_image_types_from_pdf("sample_extr.pdf")

    Note:
        Prints total images count, color type for each image, and resolution info.
    """

    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()

    # Counters for grayscale and RGB images
    grayscaled = 0
    rgb = 0

    document.pages[1].accept(absorber)

    print("--------------------------------")
    print("Total Images = " + str(len(absorber.image_placements)))

    image_counter = 1

    for image_placement in absorber.image_placements:
        # Determine the color type of the image
        colorType = image_placement.image.get_color_type()
        if colorType == ap.ColorType.GRAYSCALE:
            grayscaled += 1
            print(f"Image {image_counter} is Grayscale...")
        elif colorType == ap.ColorType.RGB:
            rgb += 1
            print(f"Image {image_counter} is RGB...")
        image_counter += 1

    print("--------------------------------")
    print("Grayscale Images = " + str(grayscaled))
    print("RGB Images = " + str(rgb))
```

## Detaillierte Bildinformationen aus einem PDF extrahieren

Diese Funktion analysiert alle Bilder auf der ersten Seite eines PDFs und berechnet deren skalierte Abmessungen sowie die effektive Auflösung basierend auf den Grafiktransformationen der Seite.

1. PDF laden und Variablen initialisieren
1. Bildressourcen sammeln
1. Seiteninhaltsoperatoren verarbeiten:
    - 'GSave' - schiebe das aktuelle CTM auf den Stapel.
    - 'GRestore' - den letzten CTM vom Stapel entfernen.
    - 'ConcatenateMatrix' - das aktuelle CTM aktualisieren, indem man es mit der Matrix des Operators multipliziert.
1. Gib den Bildnamen, die skalierten Abmessungen und die berechnete Auflösung aus.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_information_from_pdf(infile):
    with ap.Document(infile) as document:
        default_resolution = 72
        graphics_state = []

        image_names = list(document.pages[1].resources.images.names)

        graphics_state.append(
            drawing.drawing2d.Matrix(
                float(1), float(0), float(0), float(1), float(0), float(0)
            )
        )

        for op in document.pages[1].contents:
            if is_assignable(op, ap.operators.GSave):
                graphics_state.append(
                    cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone()
                )

            elif is_assignable(op, ap.operators.GRestore):
                graphics_state.pop()

            elif is_assignable(op, ap.operators.ConcatenateMatrix):
                op_cm = cast(ap.operators.ConcatenateMatrix, op)
                cm = drawing.drawing2d.Matrix(
                    float(op_cm.matrix.a),
                    float(op_cm.matrix.b),
                    float(op_cm.matrix.c),
                    float(op_cm.matrix.d),
                    float(op_cm.matrix.e),
                    float(op_cm.matrix.f),
                )

                graphics_state[-1].multiply(cm)
                continue

            elif is_assignable(op, ap.operators.Do):
                op_do = cast(ap.operators.Do, op)
                if op_do.name in image_names:
                    last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                    index = image_names.index(op_do.name) + 1
                    image = document.pages[1].resources.images[index]

                    scaled_width = math.sqrt(
                        last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2
                    )
                    scaled_height = math.sqrt(
                        last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2
                    )

                    original_width = image.width
                    original_height = image.height

                    res_horizontal = (
                        original_width * default_resolution / scaled_width
                    )
                    res_vertical = (
                        original_height * default_resolution / scaled_height
                    )

                    info = (
                        f"{infile} image {op_do.name} "
                        f"({scaled_width:.2f}:{scaled_height:.2f}): "
                        f"res {res_horizontal:.2f} x {res_vertical:.2f}\n"
                    )
                    print(info.rstrip())
```

## Alternativtext aus Bildern in einer PDF extrahieren

Diese Funktion ruft den alternativen Text (Alt-Text) aller Bilder auf der ersten Seite eines PDFs ab, was für Barrierefreiheit und PDF/UA‑Konformitätsprüfungen nützlich ist.

1. Laden Sie das PDF-Dokument mit 'ap.Document()'.
1. Erstelle einen 'ImagePlacementAbsorber', um alle Bilder auf der Seite zu sammeln.
1. Akzeptieren Sie den Absorber auf der ersten Seite (page.accept(absorber)).
1. Iterieren Sie über jedes Bild in 'absorber.image_placements':
    - Gib den Namen des Bildes in der Ressourcensammlung der Seite aus (get_name_in_collection()).
    - Rufen Sie den alternativen Text mit 'get_alternative_text(page)' ab.
    - Drucken Sie die erste Zeile des Alt-Texts.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_alt_text(infile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: " + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])
```

## Verwandte Bildthemen

- [Arbeiten mit Bildern in PDF mit Python](/pdf/de/python-net/working-with-images/)
- [Bilder aus PDF-Dateien extrahieren](/pdf/de/python-net/extract-images-from-pdf-file/)
- [Bilder in vorhandenen PDF-Dateien ersetzen](/pdf/de/python-net/replace-image-in-existing-pdf-file/)
- [Bilder zu bestehenden PDF-Dateien hinzufügen](/pdf/de/python-net/add-image-to-existing-pdf-file/)
