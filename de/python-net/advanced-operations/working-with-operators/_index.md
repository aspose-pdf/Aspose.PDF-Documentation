---
title: Arbeiten mit PDF-Operatoren in Python
linktitle: Arbeiten mit Operatoren
type: docs
weight: 90
url: /de/python-net/working-with-operators/
description: Erfahren Sie, wie Sie Low-Level-PDF-Operatoren in Python für präzise Content-Stream-Manipulation und Grafiksteuerung verwenden.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Verwenden Sie Low-Level-PDF-Operatoren für die Steuerung des Content-Streams in Python
Abstract: Dieser Artikel erklärt, wie man mit Low-Level-PDF-Operatoren in Aspose.PDF for Python via .NET arbeitet. Erfahren Sie, wie Sie Inhaltsströme direkt manipulieren, Grafiken präzise mit Operatorklassen positionieren und gezeichnete Objekte aus PDF-Seiten in Python-Workflows entfernen.
---

## Einführung in die PDF-Operatoren und deren Verwendung

Ein Operator ist ein PDF‑Schlüsselwort, das eine auszuführende Aktion spezifiziert, z. B. das Malen einer grafischen Form auf der Seite. Ein Operator‑Schlüsselwort unterscheidet sich von einem benannten Objekt durch das Fehlen eines initialen Schrägstrich‑Zeichens (2Fh). Operatoren sind nur innerhalb des Inhaltsstroms bedeutungsvoll.

Ein Inhaltsstrom ist ein PDF‑Stromobjekt, dessen Daten aus Anweisungen bestehen, die die grafischen Elemente beschreiben, die auf einer Seite gemalt werden sollen. Weitere Details zu PDF‑Operatoren finden Sie im [PDF-Spezifikation](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

Verwenden Sie diese Seite, wenn Sie in Python direkte Kontrolle über PDF-Inhaltsströme benötigen, z. B. um Grafiken an genauen Koordinaten zu platzieren, Änderungen des Grafikzustands zu kapseln oder bestimmte Zeichenoperatoren von einer Seite zu entfernen.

## Bilder mit Operatorklassen hinzufügen

Verwenden Sie Low-Level-Operatorklassen, wenn Sie Bildinhalte sehr präzise in einem PDF-Seitenstrom platzieren müssen, ohne sich auf höhere Layout-Abstraktionen zu verlassen.

Diese Methode bietet eine feinkörnige Kontrolle über die Bildplatzierung innerhalb eines PDF, indem sie den Inhaltsstrom direkt mit niedrigstufigen Grafikoperatoren manipuliert. Sie ist besonders nützlich, wenn eine präzise Positionierung und Transformation von Bildern erforderlich ist, zum Beispiel:

- Hinzufügen von Wasserzeichen oder Logos an bestimmten Stellen.
- Überlagern von Bildern auf vorhandenen Inhalt mit exakt ausgerichteter Positionierung.
- Implementieren benutzerdefinierter Layouts, die mit höheren Abstraktionsebenen nicht realisierbar sind.

Durch die Verwendung von Operatoren wie GSave, ConcatenateMatrix, Do und GRestore können Entwickler sicherstellen, dass Bilder exakt und ohne unbeabsichtigte Nebenwirkungen auf anderen Seiteninhalten gerendert werden.

- Der [GSave](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/gsave/) operator speichert den aktuellen grafischen Zustand des PDFs.
- Der [ConcatenateMatrix](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/concatenatematrix/) Der (concatenate matrix)-Operator wird verwendet, um zu definieren, wie ein Bild auf der PDF-Seite platziert werden soll.
- Der [Do](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/do/) Der Operator zeichnet das Bild auf der Seite.
- Der [GRestore](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/grestore/) Operator stellt den Grafikzustand wieder her.

Um ein Bild in eine PDF-Datei hinzuzufügen:

1. PDF-Dokument öffnen
1. Bildplatzierungskoordinaten definieren
1. Zugriff auf die Zielseite
1. Bild in einen Stream laden
1. Aktuellen Grafikzustand speichern
1. Ein Rechteck und eine Transformationsmatrix erstellen
1. Transformationsmatrix anwenden
1. Bild zeichnen
1. Vorherigen Grafikstatus wiederherstellen
1. Modifiziertes PDF-Dokument speichern

Der folgende Codeausschnitt zeigt, wie man PDF-Operatoren verwendet:

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_using_pdf_operators(infile, imagefile, outfile):
    with ap.Document(infile) as document:
        lower_left_x = 100
        lower_left_y = 100
        upper_right_x = 200
        upper_right_y = 200

        page = document.pages[1]

        with open(imagefile, "rb") as image_stream:
            page.resources.images.add(image_stream)

        page.contents.append(ap.operators.GSave())

        rectangle = ap.Rectangle(
            lower_left_x, lower_left_y, upper_right_x, upper_right_y, True
        )
        matrix = ap.Matrix(
            [
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            ]
        )

        page.contents.append(ap.operators.ConcatenateMatrix(matrix))

        x_image = page.resources.images[len(page.resources.images)]

        page.contents.append(ap.operators.Do(x_image.name))

        page.contents.append(ap.operators.GRestore())

        document.save(outfile)
```

## Zeichne XForm auf Seite mit Operatoren

Dieses Beispiel nutzte die Leistungsfähigkeit von XForms und Grafikoperatoren, um grafische Inhalte innerhalb einer PDF effizient wiederzuverwenden. Durch das Kapseln des Bildes in einem XForm kann es mehrfach gezeichnet werden, ohne die Bilddaten zu duplizieren, was zu kleineren Dateigrößen und verbesserter Leistung führt. Dieser Ansatz ist besonders vorteilhaft, wenn:

- das gleiche Bild oder die gleiche Grafik mehrfach in einem Dokument erscheinen muss.

- eine präzise Kontrolle über die Platzierung und Transformation von Grafiken erforderlich ist.

- die Optimierung der PDF hinsichtlich Leistung und Größe Priorität hat.

Durch die Verwaltung des Grafikstatus mit GSave und GRestore und die Verwendung von Transformationsmatrizen mit ConcatenateMatrix stellt diese Technik sicher, dass jede Grafik korrekt und unabhängig gerendert wird.

```python
import sys
import aspose.pdf as ap
from os import path

def draw_xform_on_page(infile, imagefile, outfile):
    with ap.Document(infile) as document:
        page_contents = document.pages[1].contents

        page_contents.insert(1, ap.operators.GSave())
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GSave())

        form = ap.XForm.create_new_form(document.pages[1], document)
        document.pages[1].resources.forms.append(form)

        form.contents.append(ap.operators.GSave())
        form.contents.append(ap.operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0))

        with open(imagefile, "rb") as image_stream:
            form.resources.images.add(image_stream)

        x_image = form.resources.images[len(form.resources.images)]
        form.contents.append(ap.operators.Do(x_image.name))
        form.contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 500)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 300)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GRestore())

        document.save(outfile)
```

## Grafikobjekte mit Operatorklassen entfernen

Der folgende Codeausschnitt zeigt, wie Grafiken entfernt werden. Bitte beachten Sie, dass, wenn die PDF-Datei Textbeschriftungen für die Grafiken enthält, diese bei Verwendung dieses Ansatzes in der PDF-Datei verbleiben können. Suchen Sie daher nach den Grafikoperatoren für eine alternative Methode, solche Bilder zu löschen.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_graphics_objects(infile, outfile):
    with ap.Document(infile) as document:
        page = document.pages[1]
        # Collect operators to remove in single pass
        # Operator codes: S=Stroke, h=ClosePathStroke, f=Fill'
        graphics_operators = {"S", "h", "f"}
        operators_to_remove = [
            op for op in page.contents if str(op) in graphics_operators
        ]

        page.contents.delete(operators_to_remove)
        document.save(outfile)
```

## Verwandte Themen

- [Erweiterte PDF-Operationen in Python](/pdf/de/python-net/advanced-operations/)
- [Arbeiten Sie mit PDF-Seiten in Python](/pdf/de/python-net/working-with-pages/)
- [Arbeiten mit Bildern in PDF mit Python](/pdf/de/python-net/working-with-images/)
- [Arbeiten mit PDF-Graphen in Python](/pdf/de/python-net/working-with-graphs/)
