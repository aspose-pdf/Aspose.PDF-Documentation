---
title: Abrufen, Aktualisieren und Erweitern von PDF-Lesezeichen in Python
linktitle: Abrufen, Aktualisieren und Erweitern eines Lesezeichens
type: docs
weight: 20
url: /de/python-net/get-update-and-expand-bookmark/
description: Erfahren Sie, wie Sie Lesezeichen in PDF-Dokumenten mit Python abrufen, aktualisieren und erweitern.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man Lesezeichen in PDF mit Python verwendet
Abstract: Dieser Artikel bietet eine umfassende Anleitung zur Verwaltung von Lesezeichen innerhalb eines PDF-Dokuments mithilfe der Aspose.PDF-Bibliothek in Python. Er beginnt mit einer Erklärung, wie Lesezeichen aus einer PDF-Datei über die `OutlineCollection` abgerufen werden, die alle Lesezeichen enthält, und geht auf den Zugriff auf Lesezeichenattribute über die `OutlineItemCollection` ein. Der Artikel beschreibt anschließend den Vorgang, die mit einem Lesezeichen verbundene Seitenzahl mithilfe des `PdfBookmarkEditor` zu bestimmen. Weiterhin erklärt er, wie hierarchische Lesezeichenstrukturen behandelt werden, indem Kindlesezeichen innerhalb jedes `OutlineItemCollection` abgerufen werden. Er behandelt außerdem das Aktualisieren von Lesezeichen‑Eigenschaften, zeigt, wie Lesezeichenattribute geändert und Änderungen in einer PDF gespeichert werden können. Abschließend geht der Artikel auf die Anforderung ein, Lesezeichen beim Anzeigen eines Dokuments zu erweitern, und zeigt, wie der Öffnungsstatus jedes Lesezeichens gesetzt wird, damit sie standardmäßig erweitert sind. Code‑Snippets begleiten jeden Abschnitt und liefern praktische Beispiele für die Umsetzung dieser Funktionalitäten.
---

## Lesezeichen abrufen

Der [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Objekts [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) Die Sammlung enthält alle Lesezeichen einer PDF-Datei. Dieser Artikel erklärt, wie man Lesezeichen aus einer PDF-Datei erhält und wie man herausfindet, auf welcher Seite sich ein bestimmtes Lesezeichen befindet.

Um die Lesezeichen zu erhalten, iteriere durch die [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) Sammlung und rufe jedes Lesezeichen in der OutlineItemCollection ab. Der [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) bietet Zugriff auf alle Attribute des Lesezeichens. Der folgende Codeausschnitt zeigt, wie Sie Lesezeichen aus der PDF-Datei erhalten.

```python
from os import path
import sys
import aspose.pdf as ap

def get_bookmarks(input_pdf):
    document = ap.Document(input_pdf)
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```

## Abrufen der Seitenzahl eines Lesezeichens

Nachdem Sie ein Lesezeichen hinzugefügt haben, können Sie herausfinden, auf welcher Seite es sich befindet, indem Sie die dem Bookmark-Objekt zugehörige Ziel‑PageNumber ermitteln.

```python
from os import path
import sys
import aspose.pdf as ap

def get_bookmark_page_number(input_pdf):
    # Create PdfBookmarkEditor
    bookmark_editor = ap.facades.PdfBookmarkEditor()
    # Open PDF file
    bookmark_editor.bind_pdf(input_pdf)
    # Extract bookmarks
    bookmarks = bookmark_editor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_separator = ""
        for i in range(bookmark.level):
            str_level_separator += "----"

        print(str_level_separator, "Title:", bookmark.title)
        print(str_level_separator, "Page Number:", bookmark.page_number)
        print(str_level_separator, "Page Action:", bookmark.action)
```

## Untergeordnete Lesezeichen aus einem PDF‑Dokument abrufen

Lesezeichen können in einer hierarchischen Struktur mit übergeordneten und untergeordneten Elementen organisiert werden. Um alle Lesezeichen zu erhalten, durchlaufen Sie die Outlines‑Sammlungen des Document‑Objekts. Um jedoch auch untergeordnete Lesezeichen zu erhalten, durchlaufen Sie außerdem alle Lesezeichen in jedem [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) Objekt, das in der ersten Schleife erhalten wurde. Die folgenden Code‑Snippets zeigen, wie man untergeordnete Lesezeichen aus einem PDF‑Dokument erhält.

```python
from os import path
import sys
import aspose.pdf as ap

def get_child_bookmarks(input_pdf):
    document = ap.Document(input_pdf)
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
        count = len(outline_item)
        if count > 0:
            print("Child Bookmarks")
            # There are child bookmarks then loop through that as well
            for j in range(len(outline_item)):
                child_outline_item = outline_item[j + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## Lesezeichen in einem PDF-Dokument aktualisieren

Um ein Lesezeichen in einer PDF-Datei zu aktualisieren, holen Sie zunächst das entsprechende Lesezeichen aus der OutlineColletion collection des Document-Objekts, indem Sie den Index des Lesezeichens angeben. Sobald Sie das Lesezeichen in [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) Objekt, können Sie seine Eigenschaften aktualisieren und anschließend die aktualisierte PDF-Datei mit der Save-Methode speichern. Die folgenden Code‑Snippets zeigen, wie Lesezeichen in einem PDF-Dokument aktualisiert werden.

```python
from os import path
import sys
import aspose.pdf as ap

def update_bookmarks(input_pdf, output_pdf):
    # Open document
    document = ap.Document(input_pdf)

    # Get a bookmark object
    outline = document.outlines[1]

    # Get child bookmark object
    child_outline = outline[1]
    child_outline.title = "Updated Outline"
    child_outline.italic = True
    child_outline.bold = True

    # Save output
    document.save(output_pdf)
```

## Erweiterte Lesezeichen beim Betrachten des Dokuments

Lesezeichen werden im Document-Objekt des [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) Sammlung, selbst im [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) Sammlung. Allerdings können wir die Anforderung haben, dass beim Betrachten der PDF‑Datei alle Lesezeichen erweitert werden.

Um diese Anforderung zu erfüllen, können wir den Öffnungsstatus für jedes Outline-/Lesezeichen-Element auf Open setzen. Das folgende Code‑Snippet zeigt, wie man den Öffnungsstatus jedes Lesezeichens in einem PDF‑Dokument als erweitert festlegt.

```python
from os import path
import sys
import aspose.pdf as ap

def expanded_bookmarks(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.page_mode = ap.PageMode.USE_OUTLINES
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        item.open = True
    document.save(output_pdf)
```

## Verwandte Lesezeichen-Themen

- [Arbeiten mit PDF-Lesezeichen in Python](/pdf/de/python-net/bookmarks/)
- [PDF-Lesezeichen in Python hinzufügen und löschen](/pdf/de/python-net/add-and-delete-bookmark/)
- [Navigation und Interaktion in PDF mit Python](/pdf/de/python-net/navigation-and-interaction/)

