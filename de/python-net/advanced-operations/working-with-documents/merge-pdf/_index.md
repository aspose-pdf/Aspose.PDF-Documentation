---
title: PDF-Dateien in Python zusammenführen
linktitle: PDF-Dateien zusammenführen
type: docs
weight: 50
url: /de/python-net/merge-pdf-documents/
description: Erfahren Sie, wie Sie mehrere PDF‑Dateien in einem einzigen Dokument mit Python zusammenführen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF‑Seiten mit Python kombinieren
Abstract: Dieser Artikel behandelt das häufige Bedürfnis, mehrere PDF-Dateien zu einem einzigen Dokument zusammenzuführen, ein Vorgang, der für die Organisation und Optimierung von Speicherung und Freigabe von PDF-Inhalten wertvoll ist. Er untersucht die Verwendung von Aspose.PDF for Python via .NET, um PDF-Dateien effizient zu kombinieren, und weist darauf hin, dass das Zusammenführen von PDFs in Python ohne Drittanbieterbibliotheken eine Herausforderung darstellen kann. Der Artikel bietet eine Schritt-für-Schritt-Anleitung zum Verketten von PDF-Dateien - Erstellung eines neuen Dokuments, Zusammenführen der Dateien und Speichern des zusammengeführten Dokuments. Ein Code‑Snippet demonstriert die Implementierung mit Aspose.PDF und hebt die Fähigkeit der Bibliothek hervor, den Zusammenführungsprozess zu vereinfachen. Zusätzlich wird der Aspose.PDF Merger vorgestellt, ein Online‑Tool zum Zusammenführen von PDFs, das es Benutzern ermöglicht, die Funktionalität in einer webbasierten Umgebung zu erkunden.
---

## Mehrere PDFs in Python zu einer einzigen PDF zusammenführen oder kombinieren

Das Zusammenführen von PDF-Dateien ist bei Benutzern eine sehr beliebte Anfrage. Dies kann nützlich sein, wenn Sie mehrere PDF-Dateien haben, die Sie gemeinsam als ein Dokument teilen oder speichern möchten.

Das Zusammenführen von PDF-Dateien kann Ihnen dabei helfen, Ihre Dokumente zu organisieren, Speicherplatz auf Ihrem PC freizugeben und mehrere PDF-Dateien für andere zu teilen, indem Sie sie zu einem Dokument zusammenfassen.

Das Zusammenführen von PDFs in Python via .NET ist keine unkomplizierte Aufgabe, wenn man keine Drittanbieterbibliothek verwendet.
Dieser Artikel zeigt, wie man mehrere PDF-Dateien zu einem einzigen PDF-Dokument zusammenführt, indem man Aspose.PDF for Python via .NET verwendet. 

## PDF-Dateien mit Python und DOM zusammenführen

Um zwei PDF-Dateien zu verketten:

1. Ein neues Dokument erstellen.
1. PDF-Dateien zusammenführen
1. Speichern Sie das zusammengeführte Dokument

Mehrere PDF-Dokumente zu einer einzigen Datei kombinieren:

```python
import sys
import aspose.pdf as ap
from os import path


def merge_two_documents(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    document1.pages.add(document2.pages)
    document1.save(outfile)
```

## Einen Seitenbereich von einer PDF an eine andere anhängen

Kopieren und Anhängen eines bestimmten Seitenbereichs von einem Quell‑PDF‑Dokument zu einem Ziel‑PDF‑Dokument mit Aspose.PDF für Python.

1. Öffnen Sie die PDF-Dateien mit der Document-Klasse.
1. Überprüfen Sie, ob das Quell-Dokument Seiten hat.
1. Validieren Sie den Seitenbereich.
1. Überspringen Sie den Vorgang, wenn die Startseite größer als die Endseite ist.
1. Durchlaufen Sie den Seitenbereich.
1. Seiten an das Zieldokument anhängen.

```python
import sys
import aspose.pdf as ap
from os import path


def _append_page_range(source_document, destination_document, start_page, end_page):
    total_pages = len(source_document.pages)
    if total_pages == 0:
        return

    start = max(1, start_page)
    end = min(end_page, total_pages)
    if start > end:
        return

    for page_number in range(start, end + 1):
        destination_document.pages.add(source_document.pages[page_number])
```

## Mehrere PDF-Dokumente zu einem zusammenführen

Dieses Code‑Snippet erklärt, wie man mehrere PDF‑Dateien zu einem einzigen Dokument zusammenführt:

1. Erstellen Sie ein leeres Ausgabe-Document.
1. Durchlaufen Sie die Eingabedateien.
1. Laden Sie jedes Quellendokument.
1. Seitenbereich bestimmen.
1. Seiten an das Ausgabedokument anhängen.
1. Wiederholen Sie dies für alle Dokumente.
1. Speichern Sie die zusammengefügte PDF.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_multiple_documents(input_files, outfile):
    output_document = ap.Document()

    for input_file in input_files:
        source_document = ap.Document(input_file)
        _append_page_range(
            source_document, output_document, 1, len(source_document.pages)
        )

    output_document.save(outfile)
```

## Ausgewählte Seitenbereiche aus mehreren PDFs zusammenführen

1. Laden Sie die Quell-PDF-Dokumente.
1. Erstellen Sie ein Ausgabedokument.
1. Definieren Sie Seitenbereiche für jedes Dokument.
1. Seiten aus dem ersten Dokument anhängen.
1. Seiten aus dem zweiten Dokument anhängen.
1. Seiten in gewünschter Reihenfolge kombinieren.
1. Speichern Sie die zusammengefügte PDF.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_selected_page_ranges(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    output_document = ap.Document()

    _append_page_range(document1, output_document, 1, 2)
    _append_page_range(document2, output_document, 2, 3)

    output_document.save(outfile)
```

## Ein PDF an einer bestimmten Position in ein anderes einfügen

1. Laden Sie die Basis und fügen Sie Dokumente ein.
1. Erstellen Sie ein Ausgabedokument.
1. Bestimmen Sie die Gesamtseitenzahl im Basisdokument.
1. Validieren Sie den Einfügeindex.
1. Seiten vor dem Einfügepunkt anhängen.
1. Alle Seiten aus dem einzufügenden Dokument anhängen.
1. Hängen Sie die verbleibenden Seiten aus dem Basisdokument an.
1. Speichern Sie das resultierende PDF.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_insert_document_at_position(infile1, infile2, insert_after_page, outfile):
    base_document = ap.Document(infile1)
    insert_document = ap.Document(infile2)
    output_document = ap.Document()

    base_total_pages = len(base_document.pages)
    insert_index = max(0, min(insert_after_page, base_total_pages))

    _append_page_range(base_document, output_document, 1, insert_index)
    _append_page_range(insert_document, output_document, 1, len(insert_document.pages))
    _append_page_range(
        base_document, output_document, insert_index + 1, base_total_pages
    )

    output_document.save(outfile)
```

## PDFs durch abwechselnde Seiten zusammenführen

Dieses Beispiel demonstriert, wie man zwei PDF-Dokumente durch abwechselndes Einfügen ihrer Seiten mit Aspose.PDF for Python zusammenführt.

1. Laden Sie die Eingabe‑PDF‑Dokumente.
1. Erstellen Sie ein Ausgabedokument.
1. Ermitteln Sie die Anzahl der Seiten in jedem Dokument.
1. Berechnen Sie die maximale Seitenzahl.
1. Iterieren Sie durch Seitenzahlen.
1. Seiten abwechselnd anhängen.
1. Ungleiche Seitenzahlen verarbeiten.
1. Speichern Sie die zusammengefügte PDF.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_alternating_pages(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    output_document = ap.Document()

    document1_pages = len(document1.pages)
    document2_pages = len(document2.pages)
    max_pages = max(document1_pages, document2_pages)

    for page_number in range(1, max_pages + 1):
        if page_number <= document1_pages:
            output_document.pages.add(document1.pages[page_number])
        if page_number <= document2_pages:
            output_document.pages.add(document2.pages[page_number])

    output_document.save(outfile)
```

## PDFs mit Abschnittstrennzeichen und Lesezeichen zusammenführen

Mehrere PDF-Dokumente zu einer einzigen Datei mit strukturierten Abschnitten und Navigations-Lesezeichen zusammenführen, dabei Aspose.PDF for Python verwenden.

1. Erstellen Sie ein Ausgabedokument.
1. Durchlaufen Sie die Eingabedateien.
1. Laden Sie das Quelldokument.
1. Füge eine Trennseite hinzu.
1. Erstelle ein Abschnitts-Lesezeichen.
1. Quellendokumentseiten anhängen.
1. Verfolgen Sie die erste Inhaltsseite.
1. Ein verschachteltes Inhalts-Lesezeichen hinzufügen (optional).
1. Wiederholen Sie dies für alle Dokumente.
1. Speichern Sie die zusammengefügte PDF.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_with_section_separators_and_bookmarks(input_files, outfile):
    output_document = ap.Document()

    for section_index, input_file in enumerate(input_files, start=1):
        source_document = ap.Document(input_file)
        source_page_count = len(source_document.pages)

        separator_page = output_document.pages.add()
        separator_page.paragraphs.add(
            ap.text.TextFragment(
                f"Section {section_index}: {path.basename(input_file)}"
            )
        )

        section_bookmark = ap.OutlineItemCollection(output_document.outlines)
        section_bookmark.title = f"Section {section_index}"
        section_bookmark.action = ap.annotations.GoToAction(separator_page)
        output_document.outlines.append(section_bookmark)

        first_content_page_number = len(output_document.pages) + 1
        _append_page_range(source_document, output_document, 1, source_page_count)

        if source_page_count > 0 and first_content_page_number <= len(
            output_document.pages
        ):
            content_bookmark = ap.OutlineItemCollection(output_document.outlines)
            content_bookmark.title = f"Section {section_index} Content"
            content_bookmark.action = ap.annotations.GoToAction(
                output_document.pages[first_content_page_number]
            )
            section_bookmark.append(content_bookmark)

    output_document.save(outfile)
```

## Live‑Beispiel

[Aspose.PDF-Merger](https://products.aspose.app/pdf/merger) ist eine kostenlose Online-Webanwendung, die es ermöglicht, zu untersuchen, wie die Präsentationszusammenführungsfunktion funktioniert.

[![Aspose.PDF-Merger](merger.png)](https://products.aspose.app/pdf/merger)

## Verwandte Dokumentthemen

- [Arbeiten mit PDF-Dokumenten in Python](/pdf/de/python-net/working-with-documents/)
- [PDF-Dateien in Python teilen](/pdf/de/python-net/split-document/)
- [PDF‑Dateien in Python optimieren](/pdf/de/python-net/optimize-pdf/)
- [PDF‑Dokumente in Python manipulieren](/pdf/de/python-net/manipulate-pdf-document/)

