---
title: PDF-Dateien in Python aufteilen
linktitle: PDF-Dateien aufteilen
type: docs
weight: 60
url: /de/python-net/split-pdf-document/
description: Erfahren Sie, wie Sie PDF‑Seiten in separate PDF‑Dateien mit Python aufteilen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aufteilen von PDF‑Seiten mit Python
Abstract: Der Artikel beschreibt den Vorgang, PDF‑Seiten mit Python in einzelne Dateien zu splitten, und hebt den Nutzen einer solchen Funktion für die Verwaltung großer PDF‑Dokumente hervor. Er verweist auf den Aspose.PDF Splitter, ein Online‑Tool, das die PDF‑Split‑Funktionalität demonstriert. Der Artikel liefert eine detaillierte Methode, um dies in Python‑Anwendungen zu erreichen, indem man über die Seiten eines PDF‑Dokuments mittels der `Document`‑Objekt‑`PageCollection` iteriert. Für jede Seite wird ein neues `Document`‑Objekt erstellt, die Seite wird hinzugefügt und die neue PDF‑Datei wird mit der `save()`‑Methode gespeichert. Ein begleitendes Python‑Code‑Snippet illustriert diesen Vorgang und zeigt die notwendigen Schritte, um ein PDF‑Dokument in separate Dateien zu splitten, indem man über seine Seiten iteriert und jede als einzelne PDF speichert.
---

Das Aufteilen von PDF-Seiten kann eine nützliche Funktion für diejenigen sein, die eine große Datei in einzelne Seiten oder Seitengruppen aufteilen möchten.

Verwenden Sie diesen Workflow, wenn Sie große PDFs in Einzelseiten‑Dateien oder kleinere Dokumentensätze für die Verteilung, Überprüfung oder nachgelagerte Verarbeitung aufteilen müssen.

## Live‑Beispiel

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) ist eine kostenlose Online-Webanwendung, die es Ihnen ermöglicht zu untersuchen, wie die Präsentationsaufteilungsfunktion funktioniert.

[![Aspose PDF aufteilen](splitter.png)](https://products.aspose.app/pdf/splitter)

Dieses Thema zeigt, wie Sie PDF-Seiten in einzelne PDF-Dateien in Ihren Python-Anwendungen aufteilen können. Um PDF-Seiten mit Python in einseitige PDF-Dateien aufzuteilen, können Sie die folgenden Schritte ausführen:

1. Durchlaufen Sie die Seiten des PDF-Dokuments durch die [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objekts [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) Sammlung
1. Für jede Iteration erstellen Sie ein neues Document-Objekt und fügen das Einzelne hinzu. [Seite](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) Objekt in das leere Dokument
1. Speichern Sie das neue PDF mit [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) Methode

## PDF in mehrere Dateien aufteilen oder separate PDFs in Python

Das folgende Python-Code‑Snippet zeigt Ihnen, wie Sie PDF‑Seiten in einzelne PDF‑Dateien aufteilen.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents(infile, outdir):
    document = ap.Document(infile)
    for page_num in range(1, len(document.pages) + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num}.pdf"))
```

## Eine PDF in zwei gleiche Teile aufteilen

1. Laden Sie das PDF-Dokument.
1. Bestimmen Sie die Gesamtzahl der Seiten.
1. Berechnen Sie den Mittelpunkt.
1. Erstelle das erste Ausgabedokument.
1. Entfernen Sie die Seiten der zweiten Hälfte aus dem ersten Dokument.
1. Speichern Sie den ersten Teil.
1. Erstelle das zweite Ausgabedokument.
1. Entfernen Sie die erste Hälfte der Seiten aus dem zweiten Dokument.
1. Speichern Sie den zweiten Teil.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_two_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    mid_point = total_pages // 2

    # First part
    with ap.Document(infile) as first_document:
        first_part_range = range(mid_point + 1, total_pages + 1)
        first_document.pages.delete(first_part_range)
        first_document.save(path.join(outdir, "Part_1.pdf"))

    # Second part
    with ap.Document(infile) as second_document:
        second_part_range = range(1, mid_point + 1)
        second_document.pages.delete(second_part_range)
        second_document.save(path.join(outdir, "Part_2.pdf"))
```

## PDF in mehrere Dateien aufteilen, alle N Seiten

PDF-Dokument in mehrere kleinere Dateien aufteilen, basierend auf einer festen Seitenanzahl, unter Verwendung von Aspose.PDF for Python.

1. Laden Sie das PDF-Dokument.
1. Bestimmen Sie die Gesamtzahl der Seiten.
1. Definieren Sie Seiten pro Teil.
1. Durchlaufen Sie das Dokument in Abschnitten.
1. Berechnen Sie den Seitenbereich für jeden Teil.
1. Erstellen Sie ein neues Dokument für jeden Teil.
1. Seiten in das neue Dokument kopieren.
1. Speichern Sie das geteilte Dokument.
1. Wiederholen, bis alle Seiten verarbeitet sind.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_every_n_pages(infile, outdir, pages_per_part=3):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    part_index = 1
    for start_page in range(1, total_pages + 1, pages_per_part):
        end_page = min(start_page + pages_per_part - 1, total_pages)

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(
                path.join(outdir, f"Every_{pages_per_part}_Part_{part_index}.pdf")
            )

        part_index += 1
```

## PDF nach benutzerdefinierten Seitenbereichen teilen

Teilen Sie ein PDF-Dokument in mehrere Dateien basierend auf benutzerdefinierten Seitenbereichen mit Aspose.PDF für Python.

1. Laden Sie das PDF-Dokument.
1. Bestimmen Sie die Gesamtzahl der Seiten.
1. Erstellen Sie eine Liste von Tupeln, die (start_page, end_page)-Bereiche darstellen.
1. Durchlaufen Sie definierte Bereiche.
1. Validieren Sie die Startseite.
1. Passen Sie die Endseite an.
1. Validieren Sie den effektiven Bereich.
1. Erstelle ein neues Dokument für jeden Bereich.
1. Seiten in das neue Dokument kopieren.
1. Speichern Sie jedes geteilte Document.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_by_page_ranges(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    # Define ranges as (start_page, end_page). Use None to indicate last page.
    ranges = [(1, 3), (4, 6), (7, None)]

    for index, (start_page, end_page) in enumerate(ranges, start=1):
        if start_page > total_pages:
            continue

        effective_end = total_pages if end_page is None else min(end_page, total_pages)
        if start_page > effective_end:
            continue

        with ap.Document() as range_document:
            for page_num in range(start_page, effective_end + 1):
                range_document.pages.add(document.pages[page_num])
            range_document.save(
                path.join(outdir, f"Range_{index}_{start_page}_to_{effective_end}.pdf")
            )
```

## PDF in die erste Seite und die restlichen Seiten aufteilen

Trennen Sie die erste Seite eines PDF-Dokuments vom Rest der Seiten mithilfe von Aspose.PDF für Python.

1. Laden Sie das PDF-Dokument.
1. Bestimmen Sie die Gesamtzahl der Seiten.
1. Überprüfen Sie, ob das Dokument leer ist.
1. Erstellen Sie ein Dokument für die erste Seite.
1. Füge die erste Seite hinzu.
1. Speichern Sie das Dokument der ersten Seite.
1. Überprüfen Sie, ob weitere Seiten vorhanden sind.
1. Erstellen Sie ein Dokument für die restlichen Seiten.
1. Kopiere verbleibende Seiten.
1. Speichern Sie das verbleibende Seiten‑Dokument.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_first_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as first_page_document:
        first_page_document.pages.add(document.pages[1])
        first_page_document.save(path.join(outdir, "First_Page.pdf"))

    if total_pages == 1:
        return

    with ap.Document() as remaining_pages_document:
        for page_num in range(2, total_pages + 1):
            remaining_pages_document.pages.add(document.pages[page_num])
        remaining_pages_document.save(path.join(outdir, "Remaining_Pages.pdf"))
```

## Ein PDF in die letzte Seite und die vorherigen Seiten aufteilen

Extrahieren Sie die letzte Seite eines PDF-Dokuments und trennen Sie sie von den übrigen Seiten mithilfe von Aspose.PDF für Python.

1. Laden Sie das PDF-Dokument.
1. Bestimmen Sie die Gesamtzahl der Seiten.
1. Überprüfen Sie, ob das Dokument leer ist.
1. Erstelle ein Dokument für die letzte Seite.
1. Fügen Sie die letzte Seite hinzu.
1. Speichern Sie das Dokument der letzten Seite.
1. Auf einseitige Dokumente prüfen.
1. Entfernen Sie die letzte Seite aus dem ursprünglichen Dokument.
1. Speichern Sie die übrigen Seiten.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_last_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as last_page_document:
        last_page_document.pages.add(document.pages[total_pages])
        last_page_document.save(path.join(outdir, "Last_Page.pdf"))

    if total_pages == 1:
        return

    document.pages.delete(total_pages)  # Remove last page from original document
    document.save(path.join(outdir, "Previous_Pages.pdf"))
```

## Ein PDF in drei Teile aufteilen

Teilen Sie ein PDF-Dokument mit Aspose.PDF for Python in drei separate Teile.

1. Laden Sie das PDF-Dokument.
1. Bestimmen Sie die Gesamtzahl der Seiten.
1. Überprüfen Sie, ob das Dokument leer ist.
1. Teilgröße berechnen.
1. Durchlaufe drei Teile.
1. Bestimmen Sie den Seitenbereich für jeden Teil.
1. Validieren Sie den Seitenbereich.
1. Erstellen Sie ein neues Dokument für jeden Teil.
1. Kopieren Sie Seiten in das Teil-Dokument.
1. Jeden Teil speichern.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_three_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    part_size = max(1, (total_pages + 2) // 3)

    for part_index in range(3):
        start_page = part_index * part_size + 1
        end_page = min((part_index + 1) * part_size, total_pages)

        if start_page > total_pages:
            break

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(path.join(outdir, f"Three_Parts_{part_index + 1}.pdf"))
```

## Benutzerdefinierter PDF‑Seiten­splitter

Ein PDF-Dokument in mehrere Dateien aufteilen, basierend auf benutzerdefinierten Seitengruppen, mit Aspose.PDF for Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_custom_page_groups(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    groups = [
        [1, 2, 5],
        [3, 4, 6, 7],
    ]

    for group_index, group in enumerate(groups, start=1):
        valid_pages = [page_num for page_num in group if 1 <= page_num <= total_pages]
        if not valid_pages:
            continue

        with ap.Document() as group_document:
            for page_num in valid_pages:
                group_document.pages.add(document.pages[page_num])
            group_document.save(path.join(outdir, f"Custom_Group_{group_index}.pdf"))
```

## PDF in einzelne Seiten aufteilen mit stabilen Dateinamen

Teilen Sie ein PDF-Dokument in einzelne Seiten und speichern Sie diese mit stabilen Dateinamen mithilfe von Aspose.PDF for Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_with_stable_filenames(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    for page_num in range(1, total_pages + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num:03d}.pdf"))
```

## PDF in ungerade und gerade Seiten aufteilen

Teilen Sie ein PDF-Dokument in zwei separate Dateien, die ungerade bzw. gerade Seiten enthalten, mithilfe von Aspose.PDF for Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_odd_even_pages(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Odd pages document
    with ap.Document(infile) as document:
        with ap.Document() as odd_document:
            for page_num in range(1, total_pages + 1, 2):
                odd_document.pages.add(document.pages[page_num])
            odd_document.save(path.join(outdir, "Odd_Pages.pdf"))

        with ap.Document() as even_document:
            for page_num in range(2, total_pages + 1, 2):
                even_document.pages.add(document.pages[page_num])
            even_document.save(path.join(outdir, "Even_Pages.pdf"))
```

## Verwandte Dokumentthemen

- [Arbeiten mit PDF-Dokumenten in Python](/pdf/de/python-net/working-with-documents/)
- [PDF-Dateien in Python zusammenführen](/pdf/de/python-net/merge-pdf-documents/)
- [PDF‑Dateien in Python optimieren](/pdf/de/python-net/optimize-pdf/)
- [PDF‑Dokumente in Python manipulieren](/pdf/de/python-net/manipulate-pdf-document/)

