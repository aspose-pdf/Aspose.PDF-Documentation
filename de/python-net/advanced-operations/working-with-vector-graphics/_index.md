---
title: Arbeiten mit Vektorgrafiken in Python
linktitle: Arbeiten mit Vektorgrafiken
type: docs
weight: 100
url: /de/python-net/working-with-vector-graphics/
description: Erfahren Sie, wie Sie Vektorgrafiken zwischen PDF‑Seiten mit GraphicsAbsorber in Python extrahieren, verschieben, entfernen und kopieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Verwenden Sie GraphicsAbsorber, um PDF‑Vektorgrafiken in Python zu untersuchen und zu bearbeiten.
Abstract: Dieser Artikel erklärt, wie man mit Vektorgrafiken in Aspose.PDF for Python via .NET unter Verwendung der Klasse GraphicsAbsorber arbeitet. Erfahren Sie, wie Sie Vektorelemente aus PDF‑Seiten extrahieren, sie verschieben oder entfernen und Grafiken zwischen Seiten mit niedriger Ebene Steuerung in Python‑Workflows kopieren.
---

[Aspose.PDF for Python via .NET](/pdf/de/python-net/) stellt bereit [GrafikAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) Klasse zum Zugreifen und Manipulieren von Vektorgrafiken, die bereits in einer PDF-Seite vorhanden sind. Rufen Sie sie auf `visit` Methode auf jeder Seite, um Pfade, Formen und andere grafische Operatoren zu extrahieren, dann diese Elemente nach Bedarf zu verschieben, zu entfernen oder zu kopieren.

Verwenden Sie diese Seite, wenn Sie Vektorgrafikelemente, die in ein bestehendes PDF eingebettet sind, untersuchen oder ändern müssen, anstatt neue Formen von Grund auf zu zeichnen.

## Grafiken extrahieren

Extraktion ist der Ausgangspunkt für alle Vektorgrafikaufgaben. `GraphicsAbsorber` liest den Inhaltsstream einer Seite und gibt jedes grafische Element mit seiner Seitenreferenz, Position und den rohen Operatoren aus.

1. Öffnen Sie das PDF-Dokument.
1. Erstelle ein [GrafikAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) Instanz.
1. Anruf `visit` auf der Zielseite ausfüllen `elements`.
1. Durchlaufen `elements` um die Position und die Operatorzählungen zu prüfen.

```python
import aspose.pdf as ap
import sys
from os import path

def using_graphics_absorber(infile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")
```

`GraphicsAbsorber` ist Teil von `aspose.pdf.vector` Namespace und ist speziell dafür ausgelegt, mit Vektorgrafiken in PDF-Inhaltsströmen zu interagieren.

## Bewegte Grafiken

Nach der Extraktion setzen Sie ein neues `position` bei jedem Element, um es auf derselben Seite zu verschieben. Verpacken Sie die Updates in `suppress_update` / `resume_update` Aufrufe, um Schreibvorgänge des Content-Streams zu bündeln, in einer einzigen Operation und redundante Neuzeichnungen zu vermeiden.

1. Öffnen Sie das PDF-Dokument.
1. Erstelle ein `GraphicsAbsorber` und rufen `visit` auf der Zielseite.
1. Anruf `suppress_update` um das Schreiben von Content-Streams zu pausieren.
1. Aktualisieren Sie `position` von jedem Element.
1. Anruf `resume_update` alle Änderungen auf einmal committen.
1. Speichern Sie das geänderte Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def move_graphics(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                position = element.position
                element.position = ap.Point(position.x + 150, position.y - 10)
            graphics_absorber.resume_update()
        document.save(outfile)
```

## Grafiken entfernen

Um bestimmte Vektorelemente von einer Seite zu löschen, filtern Sie nach Position oder Begrenzungsrechteck und entfernen Sie sie anschließend. Aspose.PDF for Python bietet zwei Ansätze, je nachdem, ob Sie Elemente inline entfernen oder zuerst sammeln möchten.

### Methode 1: Inline mit Rechteckgrenze entfernen

Dieser Ansatz prüft die Position jedes Elements gegen ein Rechteck und ruft `element.remove()` direkt innerhalb der Schleife. Verwenden Sie es, wenn Sie knappen Code wollen und das entfernte Set anschließend nicht inspizieren müssen.

1. Öffnen Sie das PDF-Dokument.
1. Erstelle ein `GraphicsAbsorber` und rufen `visit` auf der Zielseite.
1. Definieren Sie das Ziel [Rechteck](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
1. Anruf `suppress_update` um das Schreiben von Content-Streams zu pausieren.
1. Iterieren `elements`, anrufend `remove()` bei jedem Element, dessen Position innerhalb des Rechtecks liegt.
1. Anruf `resume_update` die Löschungen festschreiben.
1. Speichern Sie das geänderte Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    element.remove()
            graphics_absorber.resume_update()
        document.save(outfile)
```

### Methode 2: Elemente zuerst sammeln, dann löschen

Dieser Ansatz sammelt passende Elemente in ein [GraphicElementCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicelementcollection/) und übergibt die Sammlung an `page.delete_graphics`. Verwenden Sie es, wenn Sie überprüfen oder protokollieren müssen, was entfernt wird, bevor Sie die Löschung durchführen.

1. Öffnen Sie das PDF-Dokument.
1. Erstelle ein `GraphicsAbsorber` und rufen `visit` auf der Zielseite.
1. Definieren Sie das Zielrechteck.
1. Iterieren `elements` und füge passende Elemente zu einem `GraphicElementCollection`.
1. Anruf `page.contents.suppress_update` um das Schreiben von Content-Streams zu pausieren.
1. Anruf `page.delete_graphics` mit der Sammlung.
1. Anruf `page.contents.resume_update` die Löschungen festschreiben.
1. Speichern Sie das geänderte Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.visit(page)
            removed_elements_collection = ap.vector.GraphicElementCollection()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    removed_elements_collection.add(element)
            page.contents.suppress_update()
            page.delete_graphics(removed_elements_collection)
            page.contents.resume_update()
        document.save(outfile)
```

## Grafiken zu einer anderen Seite hinzufügen

Vektor-Elemente, die von einer Seite extrahiert wurden, können auf jeder anderen Seite desselben Dokuments platziert werden. Zwei Methoden stehen zur Verfügung: einzelne Elemente hinzufügen oder die gesamte Sammlung in einem einzigen Aufruf übergeben.

### Methode 1: Elemente einzeln hinzufügen

Verwenden Sie diese Methode, wenn Sie pro Element Kontrolle benötigen, etwa beim Filtern oder Transformieren einzelner Elemente, bevor Sie sie auf der Zielseite platzieren.

1. Öffnen Sie das PDF-Dokument.
1. Erstelle ein `GraphicsAbsorber` und rufen `visit` auf der Quellseite.
1. Fügen Sie dem Dokument eine neue Zielseite hinzu.
1. Anruf `page_2.contents.suppress_update` um das Schreiben von Content-Streams zu pausieren.
1. Anruf `element.add_on_page(page_2)` für jedes Element.
1. Anruf `page_2.contents.resume_update` Alle Ergänzungen committen.
1. Speichern Sie das geänderte Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            for element in graphics_absorber.elements:
                element.add_on_page(page_2)
            page_2.contents.resume_update()
        document.save(outfile)
```

### Methode 2: Die gesamte Sammlung auf einmal hinzufügen

Verwenden Sie diese Methode, wenn Sie alle extrahierten Elemente in einem einzigen Vorgang auf eine Seite kopieren möchten, ohne manuell zu iterieren.

1. Öffnen Sie das PDF-Dokument.
1. Erstelle ein `GraphicsAbsorber` und rufen `visit` auf der Quellseite.
1. Fügen Sie dem Dokument eine neue Zielseite hinzu.
1. Anruf `page_2.contents.suppress_update` um das Schreiben von Content-Streams zu pausieren.
1. Anruf `page_2.add_graphics` mit dem vollen `elements` Sammlung.
1. Anruf `page_2.contents.resume_update` Alle Ergänzungen committen.
1. Speichern Sie das geänderte Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            page_2.add_graphics(graphics_absorber.elements, None)
            page_2.contents.resume_update()
        document.save(outfile)
```

## Verwandte Themen

- [Erweiterte PDF-Operationen in Python](/pdf/de/python-net/advanced-operations/)
- [Arbeiten mit PDF-Graphen in Python](/pdf/de/python-net/working-with-graphs/)
- [Arbeiten Sie mit PDF-Operatoren in Python](/pdf/de/python-net/working-with-operators/)
- [Arbeiten Sie mit PDF-Seiten in Python](/pdf/de/python-net/working-with-pages/)
