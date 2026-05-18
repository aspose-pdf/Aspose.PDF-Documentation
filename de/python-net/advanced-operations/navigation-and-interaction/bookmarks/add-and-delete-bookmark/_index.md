---
title: PDF-Lesezeichen in Python hinzufügen und löschen
linktitle: Ein Lesezeichen hinzufügen und löschen
type: docs
weight: 10
url: /de/python-net/add-and-delete-bookmark/
description: Erfahren Sie, wie Sie Lesezeichen in PDF-Dokumenten mit Python hinzufügen und löschen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man Lesezeichen mit Python hinzufügt und entfernt
Abstract: Dieser Artikel bietet umfassende Anweisungen zur Verwaltung von Lesezeichen in PDF-Dokumenten mithilfe der Aspose.PDF-Bibliothek für Python. Er erläutert die Prozesse zum Hinzufügen, Ändern und Löschen von Lesezeichen in einem PDF. Der Artikel beginnt mit einer Anleitung zum Hinzufügen eines Lesezeichens, indem ein `OutlineItemCollection`-Objekt erstellt und der `OutlineCollection` des Dokuments hinzugefügt wird. Er enthält Codebeispiele, die die Erstellung und das Hinzufügen sowohl von übergeordneten als auch von untergeordneten Lesezeichen demonstrieren und dabei eine hierarchische Beziehung hervorheben. Zusätzlich behandelt der Artikel Methoden zum Löschen aller Lesezeichen oder eines bestimmten Lesezeichens anhand des Titels. Jeder Abschnitt enthält Python-Code‑Snippets, die die Vorgänge veranschaulichen, sodass die Leser die beschriebenen Funktionalitäten in ihren PDF‑Manipulationsaufgaben leicht umsetzen können.
---

## Ein Lesezeichen zu einem PDF-Dokument hinzufügen

Lesezeichen werden im Document-Objekt des [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) Sammlung, selbst im [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) Sammlung.

Um ein Lesezeichen zu einer PDF hinzuzufügen:

1. Öffnen Sie ein PDF-Dokument mit [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Objekt.
1. Erstellen Sie ein Lesezeichen und definieren Sie dessen Eigenschaften.
1. Fügen Sie das [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) Sammlung zur Outlines collection.

Das folgende Code‑Snippet zeigt, wie Sie ein Lesezeichen in einem PDF‑Dokument hinzufügen.

```python
import aspose.pdf as ap
import sys
from os import path

def add_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Create a bookmark object
    pdf_outline = ap.OutlineItemCollection(document.outlines)
    pdf_outline.title = "Test Outline"
    pdf_outline.italic = True
    pdf_outline.bold = True

    # Set the destination page number
    pdf_outline.action = ap.annotations.GoToAction(document.pages[1])

    # Add bookmark to the document's outline collection
    outlines = document.outlines
    outlines.append(pdf_outline)

    # Save PDF document
    document.save(outfile)
```

## Ein untergeordnetes Lesezeichen zum PDF-Dokument hinzufügen

Lesezeichen können verschachtelt werden, wodurch eine hierarchische Beziehung zwischen übergeordneten und untergeordneten Lesezeichen angezeigt wird. Dieser Artikel erklärt, wie man ein untergeordnetes Lesezeichen, also ein Lesezeichen der zweiten Ebene, zu einem PDF hinzufügt.

Um ein untergeordnetes Lesezeichen zu einer PDF-Datei hinzuzufügen, fügen Sie zuerst ein übergeordnetes Lesezeichen hinzu:

1. Öffnen Sie ein Dokument.
1. Fügen Sie ein Lesezeichen zum [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), die seine Eigenschaften definiert.
1. Fügen Sie die OutlineItemCollection dem Document-Objekt hinzu [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) Sammlung.

Das untergeordnete Lesezeichen wird genau wie das übergeordnete Lesezeichen erstellt, wie oben erklärt, aber dem Outlines collection des übergeordneten Lesezeichens hinzugefügt

Die folgenden Code‑Snippets zeigen, wie man ein untergeordnetes Lesezeichen zu einem PDF‑Dokument hinzufügt

```python
import aspose.pdf as ap
import sys
from os import path

def add_child_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Create a parent bookmark object
    pdf_outline = ap.OutlineItemCollection(document.outlines)
    pdf_outline.title = "Parent Outline"
    pdf_outline.italic = True
    pdf_outline.bold = True

    # Create a child bookmark object
    pdf_child_outline = ap.OutlineItemCollection(document.outlines)
    pdf_child_outline.title = "Child Outline"
    pdf_child_outline.italic = True
    pdf_child_outline.bold = True

    # Add child bookmark to parent bookmark's collection
    pdf_outline.append(pdf_child_outline)

    # Add parent bookmark to the document's outline collection
    document.outlines.append(pdf_outline)

    # Save PDF document
    document.save(outfile)
```

## Alle Lesezeichen aus einem PDF-Dokument löschen

Alle Lesezeichen in einem PDF werden im [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) Sammlung. Dieser Artikel erklärt, wie man alle Lesezeichen aus einer PDF-Datei löscht.

Um alle Lesezeichen aus einer PDF-Datei zu löschen:

1. Rufen Sie die [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) Delete-Methode der Sammlung.
1. Speichern Sie die modifizierte Datei mit dem [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Objekts [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) Methode.

Die folgenden Code‑Snippets zeigen, wie man alle Lesezeichen aus einem PDF‑Dokument löscht.

```python
import aspose.pdf as ap
import sys
from os import path

def delete_bookmarks(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Delete all bookmarks in the PDF document
    document.outlines.delete()

    # Save PDF document
    document.save(outfile)
```

## Ein bestimmtes Lesezeichen aus einem PDF-Dokument löschen

Um ein bestimmtes Lesezeichen aus einer PDF-Datei zu löschen:

1. Übergeben Sie den Titel des Lesezeichens als Parameter an die [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) Delete-Methode der Sammlung.
1. Speichern Sie dann die aktualisierte Datei mit der Save‑Methode des Document‑Objekts.

Der [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Klasse’ liefert die [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) Sammlung. Die [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) Methode entfernt jedes Lesezeichen mit dem an die Methode übergebenen Titel.

Die folgenden Code‑Snippets zeigen, wie man ein bestimmtes Lesezeichen aus dem PDF‑Dokument löscht.

```python
import aspose.pdf as ap
import sys
from os import path

def delete_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Delete a specific bookmark by title.
    # Note: If multiple bookmarks have the same title, only the first matching bookmark will be deleted.
    document.outlines.delete("Child Outline")

    # Save PDF document
    document.save(outfile)
```

## Verwandte Lesezeichen-Themen

- [Arbeiten mit PDF-Lesezeichen in Python](/pdf/de/python-net/bookmarks/)
- [Abrufen, Aktualisieren und Erweitern von PDF-Lesezeichen in Python](/pdf/de/python-net/get-update-and-expand-bookmark/)
- [Navigation und Interaktion in PDF mit Python](/pdf/de/python-net/navigation-and-interaction/)

